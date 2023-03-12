# Importar as libs
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Detectar camera
video = cv2.VideoCapture(0)

# Tamanho da camera
video.set(3,640) #Largura
video.set(4, 480) #Altura

# Enquanto o loop for verdade
while True:

    # Salvar a imagem capturada na camera
    sucesso, img=video.read()

    # Detectar os qr/barcode na img
    for barcode in decode(img):

        # Decodifica qr/barcode
        mydata=barcode.data.decode('utf-8')

        # Mostrar o codigo
        print(mydata)

        # Coordenadas do qr/barcode
        pts = np.array([barcode.polygon], np.int32)

        # Modificar o arranjo de pts
        pts = pts.reshape((-1, 1, 2))

        # Criar retangulo para qr/barcode
        cv2.polylines(img, # Imagem
                      [pts], # Coordenadas
                      True, # O polígono está fechado
                      (0, 0, 255), # Cor do polígono
                      5) # Espessura do polígono

        # Criar um retangulo para o texto
        pts2=barcode.rect

        # Criar texto
        cv2.putText(img, # Imagem
                    mydata, # Texto que vai aparecer
                    (pts2[0], pts2[1]), # Coordenadas
                    cv2.FONT_HERSHEY_SIMPLEX, # Tipo de letra
                    0.9, # Tamanho da fonte
                    (0, 0, 255), # Cor da letra
                    3) # Espessura da letra

    # Mostrar a camera
    cv2.imshow('Janela', img)

    # Para a camera não fechar
    cv2.waitKey(1)