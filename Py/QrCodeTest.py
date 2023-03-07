import cv2
import numpy as np
from pyzbar.pyzbar import decode

#Imagem
#img = cv2.imread("qrcode.png")

#Video
video = cv2.VideoCapture(0)

#Definindo altura e largura:
video.set(3, 640)
video.set(4, 480)

while True:
    sucess, qrcode = video.read()
    for barcode in decode(qrcode):
        myData = barcode.data.decode("utf-8")
        print(myData)
        pontos = np.array([barcode.polygon], np.int32)
        pontos = pontos.reshape((-1, 1, 2))
        cv2.polylines(qrcode, [pontos], True, (255, 0, 0), 5)

    cv2.imshow("Janela", qrcode)
    cv2.waitKey(1)
