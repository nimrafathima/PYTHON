import cv2
import numpy 
from pyzbar.pyzbar import decode

img = cv2.imread("qrcode.png")
print(decode(img))