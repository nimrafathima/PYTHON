import qrcode

img_qrcode = qrcode.make("https://dnathanael19.github.io/CARTAO_RESPOSTAS/")
img_qrcode.save("qrcode.png")