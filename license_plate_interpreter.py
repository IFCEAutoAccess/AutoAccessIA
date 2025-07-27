import cv2
import numpy as np
import tensorflow as tf

img = cv2.imread("val-1-_jpg.rf.cfbce5fd20cc7f879288dcf366c42582_placa0.jpg", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESHOLD_BINARY_INV)
binary = cv2.medianBlur(binary, 3)

contours, _ = cv2.find

