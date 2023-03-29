import cv2
from pdf2image import convert_from_path

def read_qrcode(filename):
    #Lê a img
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, qrcode = detect.detectAndDecode(img)
        return value, points, qrcode
    #Se der erro ele roda except
    except:
        '''pdf = convert_from_path(filename, dpi=200 ,poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

        if type(pdf) == list:
            for png in pdf:
                png.save('cartao.png', "PNG")
                read_qrcode('cartao.png')'''


def draw_qrcode(filename, pts):
    points_list = pts.tolist()
    pt1 = map(int, points_list[0][0])
    pt2 = map(int, points_list[0][2])
    img = cv2.imread(filename)
    retangulo = cv2.rectangle(img, tuple(pt1), tuple(pt2), (0, 0, 255), 2)
    cv2.imshow('janela', retangulo)
    cv2.waitKey(0)

def show_qrcode(qrcode):
    '''cv2.namedWindow("qr", 0)
    cv2.imshow("qr", qrcode)'''
    cv2.waitKey(0)

if __name__ == '__main__':
    path = 'CartãoResposta.pdf'
    value, points, qrcode = read_qrcode(path)
    draw_qrcode(path, points)
    #show_qrcode(qrcode)
