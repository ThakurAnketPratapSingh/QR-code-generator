import qrcode
img=qrcode.make(input('what should the QR code contain ? \n'))
img.save('anket.png')
img.show('anket.png')
