import cv2
import numpy as np
from pyzbar.pyzbar import decode

#Imagem
#img = cv2.imread("qrcode.png")

#Video
video = cv2.VideoCapture(0)

#Definindo altura e largura:
video.set(3, 700)
video.set(4, 500)

while True:
    sucess, ler = video.read()
    for barcode in decode(ler):
        myData = barcode.data.decode("utf-8")
        print(myData)
        pontos = np.array([barcode.polygon], np.int64)
        pontos = pontos.reshape((-1, 1, 2))
        cv2.polylines(ler, [pontos], True, (255, 0, 0), 2)
        pontos2 = barcode.rect
        cv2.putText(ler, myData, (pontos2[0], pontos2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                                     0.9, (255, 0, 0), 2)

    cv2.imshow("Janela", ler)
    cv2.waitKey(1)

