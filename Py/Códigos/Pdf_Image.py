#Importar lib
import cv2
from pdf2image import convert_from_path

images = convert_from_path("CartãoResposta.pdf", dpi=200 ,poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

if type(images) == list:
    for img in images:
        img.save('cartao.png', "PNG")
        print(type(img))

        open = cv2.imread('cartao.png')
        cv2.imshow('janela', open)
        cv2.waitKey(0)