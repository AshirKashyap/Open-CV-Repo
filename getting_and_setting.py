from __future__ import print_function
import argparse
import cv2

object = argparse.ArgumentParser()
object.add_argument("--image", required = True,
help = "Pathway to location of the image :)")
arguments = vars(object.parse_args())

picture = cv2.imread(arguments["image"])
cv2.imshow("Image", picture)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", picture)

(b, g, r) = picture[200,200]
print("Pixel at (400,400): red = {} green= {} blue = {}".format(r, g, b))

picture[200, 200] = (120, 230, 20)

(b, g, r) = picture[200,200]
print("Pixel at (0,0): red = {} green= {} blue = {}".format(r, g, b))


bigRectangle = picture[0:200, 0:200]
cv2.imshow("rectangle", bigRectangle)

picture[0:200, 0:200] = (120, 230, 20)

cv2.imshow("radicalRedRectangle", picture)
cv2.waitKey(0)
