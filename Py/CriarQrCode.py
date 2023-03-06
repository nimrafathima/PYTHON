import qrcode

img_qrcode = qrcode.make("https://dnathanael19.github.io/cartao-respostas/")
img_qrcode.save("qrcode.png")