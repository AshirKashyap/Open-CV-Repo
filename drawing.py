import numpy as n
import cv2

canvas = n.zeros((500, 500, 3), dtype = "uint8")

blue = (255, 0, 0)
red = (0, 0, 255)
cv2.line(canvas, (0, 0), (500, 500), blue)
cv2.line(canvas, (0, 500), (500, 0), red, 15)
cv2.imshow("Cool Blue Line and Radical Red Line", canvas)
cv2.waitKey(0)

green= (0, 255, 0)
cv2.rectangle(canvas, (20, 20), (370, 380), green, -1)
cv2.imshow("Great Green Rectangle", canvas)
cv2.waitKey(0)

yellow = (0, 255, 255)
cv2.circle(canvas, (250, 250), 50, yellow, -1)
cv2.imshow("Yellow Circle", canvas)
cv2.waitKey(0)

canvas = n.zeros((500, 500, 3), dtype = "uint8")

(xCoor, yCoor) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for radius in range(0, 200, 25):
    cv2.circle(canvas, (xCoor, yCoor), radius, white)

cv2.imshow("White Circles", canvas)
cv2.waitKey(0)

for numCircles in range(0, 500):
    radius = n.random.randint(5, 300)
    color = n.random.randint(0, 256, size = (3,)).tolist()
    coordinates = n.random.randint(0, 300, size = (2,))

    cv2.circle(canvas, tuple(coordinates), radius, color, -1)

cv2.imshow("Lot Kool Circles", canvas)
cv2.waitKey(0)
