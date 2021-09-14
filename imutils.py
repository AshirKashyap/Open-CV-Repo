import numpy as n
import cv2

def translate(picture, x, y):
    matrix = n.float32([[1, 0, x], [0, 1, y]])
    shift = cv2.warpAffine(picture, matrix, (picture.shape[1], picture.shape[0]))

    return shift

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dimensions = None
    (h, w,) = image.shape[:2]

    if width is None and height is None:
        return Image

    if width is None:
        ratio = height / float(h)
        dimensions = (int(w * ratio), height)

    else:
        ratio = width / float(w)
        dimensions = (width, int(h * ratio))

    resizedImage = cv2.resize(image, dimensions, interpolation = inter)

    return resizedImage

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    Matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, Matrix, (w, h))


    return rotated
