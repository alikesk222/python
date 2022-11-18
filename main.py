""""
kütüphaneleri yüklemek için terminalde

pip install Pillow
pip install qrcode
"""



import qrcode

data = "" #tırnak içine qr kod içine yüklemek istediğiniz içeriği ekleyin.

Image = qrcode.make(data)

Image.save("QRcode.png")