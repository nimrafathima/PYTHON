from barcode import Code128
from barcode.writer import ImageWriter

lista_alunos = {"Diego Cavalcante": "20211321000", "Rayssa Damacieira":"20211321001"}

for percorre in lista_alunos:
    codigo = lista_alunos[percorre]
    cod = Code128(codigo, writer=ImageWriter())
    cod.save(f"barcod_{percorre}")