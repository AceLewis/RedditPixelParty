import re
import math

from PIL import Image
from bs4 import BeautifulSoup


def hex_to_rgb(value):
    "Convert hex to RGB"
    return tuple(int(value[i:i + 2], 16) for i in range(1, 7, 2))


def distance(colour_1, colour_2):
    "Find the 'distance' between two colours"
    (r1, g1, b1) = colour_1
    (r2, g2, b2) = colour_2
    return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)


def find_closest(point, colour_dict):
    "Find the closest colour in the dictionary"
    colors = list(colour_dict.keys())
    closest_colors = sorted(colors, key=lambda color: distance(color, point))
    closest_color = closest_colors[0]
    return colour_dict[closest_color]


def sub_function(match_object):
    "Substitution function for minimizing text"
    m_g = match_object.groups()
    return '[{}{}](//{})'.format(m_g[0], m_g[2], m_g[1])

# Can't scrape Reddit as has anti-scrape stuff to stop bots
# can possibly could bypass but easy enough to visit and just
# and save the HTML.

# HTML saved to file of https://www.reddit.com/r/PixelParty/wiki/colors
with open('colours.html', 'r') as content_file:
    colours_html = content_file.read()

# Create soup
soup = BeautifulSoup(colours_html, 'html.parser')
# Find table
colour_table = soup.find("table")
rows = colour_table.find("tbody").find_all("tr")
# Create colour dictionary
colour_dict = {}
# Get all colours from the table on the page
for row in rows:
    cells = row.find_all("td")
    name = cells[0].get_text()
    hex_code = cells[1].get_text()
    if hex_code == 'transparent':
        continue
    colour_code = hex_to_rgb(hex_code)
    colour_dict[colour_code] = name

# load image
im = Image.open(image_to_load)
im = im.convert("RGB")
# Start string with thing to make the pixels small
string = '''
#####s
#####s
#####s
#####s
#####s
####s'''.strip()

# For each pixel append to end of string, a .join method may be slightly faster
# but this method is easier and faster for this quick and dirty code
for x in range(image_size[0]):
    for y in range(image_size[0]):
        string += r'[..](//{})'.format(find_closest(im.getpixel((y, x)), colour_dict))
    string += '\n\n'

# Minimize the output
while True:
    a = re.sub(r'\[(\.*)\]\(\/\/([a-zA-Z]*)\)\[(\.*)]\(\/\/\2\)', sub_function, string)
    if a == string:
        break
    else:
        string = a

# Save to output
with open("Output.txt", "w") as text_file:
    text_file.write(string[:-2])

print('The string is {} characters long'.format(len(string[:-2])))

if len(string[:-2]) > 40000:
    print('This is too big to post to Reddit')
else:
    print('You have {} characters to spare'.format(40000 - len(string[:-2])))
