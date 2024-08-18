import pyqrcode
qr = pyqrcode.create("https://akhileshdasari.github.io/testsite/")
qr.png("qr.png")