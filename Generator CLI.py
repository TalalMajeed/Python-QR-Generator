import qrcode

data = input("Please Enter Some Data: ")

def create_qrcode(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')

create_qrcode(data)
