import qrcode as qr

url = input("Enter the URL: ")

qr = qr.QRCode(version=3, box_size=20, border=1, error_correction=qr.constants.ERROR_CORRECT_H)

qr.add_data(url)

qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white")

filename = input("Enter the file name: ")

img.save(filename + ".png")

