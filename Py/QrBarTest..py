import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("qrcode.png")
code = decode(img)
print(code)