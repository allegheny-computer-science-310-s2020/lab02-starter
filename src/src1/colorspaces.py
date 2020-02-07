# USAGE
# python colorspaces.py --image images/beach.png
# docker run --rm -v $(pwd)/src1:/root opencv python colorspaces.py --image images/beach.png

# Import the necessary packages
import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and show it
image = cv2.imread(args["image"])
cv2.imwrite("images/colors/Original.png", image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/colors/Gray.png", gray)

# Convert the image to the HSV (Hue, Saturation, Value)
# color spaces
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite("images/colors/HSV.png", hsv)

# Convert the image to the L*a*b* color spaces
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imwrite("images/colors/L*a*b*.png", lab)
#cv2.waitKey(0)
