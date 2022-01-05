# Import pyzbar module
from pyzbar.pyzbar import decode
from PIL import Image

print('Scan your QR-code')


# Opening the images
img = Image.open('QRCODE.svg')

# Decoding the image
d = decode(img)

# Printing the image
print(d[0].data.decode())
