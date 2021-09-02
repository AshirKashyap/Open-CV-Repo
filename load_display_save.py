from __future__ import print_function
import argparse
import cv2

object = argparse.ArgumentParser()
object.add_argument("-picture", "--image", required = True,
help = "Pathway to location of the image")
arguments = vars(object.parse_args())

picture = cv2.imread(arguments["image"])
print("height: {} pixels".format(picture.shape[0]))
print("width {} pixels".format(picture.shape[1]))
print("channels: {}".format(picture.shape[2]))

cv2.imshow("Image", picture)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", picture)
