from barcode import Code39
from barcode.writer import ImageWriter

lista_alunos = {"Diego Cavalcante": "20211321000339", "Rayssa Damacieira":"20211321000018"}

for percorre in lista_alunos:
    codigo = lista_alunos[percorre]
    cod = Code39(codigo, writer=ImageWriter())
    cod.save(f"barcod_{percorre}")