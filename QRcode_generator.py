# Import QR-code module.
import pyqrcode

print('Create your personal QR code')

# seek user input...
msg = input('Please type in your message: ')

code = pyqrcode.create(msg)
code.png('QRCODE.png', scale=5)

print('Here is your QR-code!')
