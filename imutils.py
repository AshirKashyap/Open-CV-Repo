import numpy as n
import cv2

def translate(picture, x, y):
    matrix = n.float32([[1, 0, x], [0, 1, y]])
    shift = cv2.warpAffine(picture, matrix, (picture.shape[1], picture.shape[0]))

    return shift
