from tkinter import *
import qrcode
from PIL import Image, ImageTk

root = Tk()

def placeIMG():
    global newimg, getimg
    canvas.delete("all")
    getimg = Image.open("qrcode.png")
    resized_image = getimg.resize((240, 240), Image.LANCZOS)
    newimg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=newimg)


def generate():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qrdata = input_T.get("1.0", END)
    qrdata = qrdata[:-1] if qrdata.endswith("\n") else qrdata
    qr.add_data(qrdata)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    placeIMG()


title_L = Label(root, text="QR Code Generator!")
title_L.config(font=("Segoe UI", 14))
title_L.place(x=10, y=10)

copy_L = Label(root, text="©M.TALAL MAJEED - 2023")
copy_L.config(font=("Segoe UI", 12))
copy_L.place(x=10, y=370)

input_L = Label(root, text="Please Enter Some text below to generate a QR Code:")
input_L.config(font=("Segoe UI", 12))
input_L.place(x=10, y=50)

input_T = Text(root)
input_T.config(font=("Segoe UI", 12))
input_T.place(x=15, y=100, height=100, width=360)

generate_B = Button(root, text="Generate")
generate_B.config(command=generate)
generate_B.config(font=("Segoe UI", 12))
generate_B.place(x=15, y=220, width=170)

canvas = Canvas(root, width=240, height=240)
canvas.place(x=400, y=15)
canvas.config(bg="white")

canvas.create_text(
    120, 120, text="QR Code will appear here", font=("Segoe UI", 12), fill="black"
)

root.title("QR Code Generator")
root.geometry("660x400")
root.resizable(False, False)
root.mainloop()
