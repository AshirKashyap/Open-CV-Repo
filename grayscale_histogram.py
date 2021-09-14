from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required = True,
help = "Pathway to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("grayscale hist")
plt.xlabel("Bins")
plt.ylabel("# pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
