# Reddit Pixel Party

This is a Python script to automatically create the text used for pixel art on [/r/PixelParty/](https://www.reddit.com/r/PixelParty/) from input images.

It works in 3 steps, quantizing the colours to the colours available for use on [/r/PixelParty/](https://www.reddit.com/r/PixelParty/), then converting the pixel values to a string one by one and finally just minimizing the string allowing for larger images to be used.

The recommended image size for input into this script is 64 by 64 pixels however larger images can be used if colours are repeated throughout the image e.g a cartoon image.

Example output, to see the output you must be on a desktop version of Reddit (not mobile) and must have not disabled subreddit themes then you can visit [here for an image of jack sparrow](https://www.reddit.com/r/PixelParty/comments/62q0d0/captain_jack_sparrow_image_test/).
