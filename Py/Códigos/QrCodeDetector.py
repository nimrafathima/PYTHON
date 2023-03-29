import cv2
from pyzbar.pyzbar import decode


img =  cv2.imread('cartao_resposta.png')
detectar = decode(img)

for i in detectar:
    print(i.data.decode('utf-8'))

cv2.imshow('Janela', img)
cv2.waitKey(0)

