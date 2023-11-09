from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

root = Tk()
filename = ""


def placeIMG(image):
    global newimg, getimg
    canvas.delete("all")
    getimg = Image.open(image)
    resized_image = getimg.resize((240, 240), Image.LANCZOS)
    newimg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=newimg)

def openfile():
    global filename
    filename = filedialog.askopenfilename(
        title="Select a QR Code",
        filetypes=(
            ("image files", "*.png *.jpg *.jpeg *.ico *.gif"),
            ("all files", "*.*"),
        ),
        initialdir=".",
    )
    if filename != "":
        placeIMG(filename)

def decode_function():
    global filename
    if filename != "":
        try:
            result = decode(Image.open(filename))
            input_T.delete("1.0", END)
            input_T.insert(END, result[0][0].decode("utf-8"))
        except:
            input_T.delete("1.0", END)
            input_T.insert(END, "Invalid QR Code!")
    else:
        input_T.delete("1.0", END)
        input_T.insert(END, "Please Select a QR Code to generate text")


title_L = Label(root, text="QR Code Decoder!")
title_L.config(font=("Segoe UI", 14))
title_L.place(x=10, y=10)

copy_L = Label(root, text="©M.TALAL MAJEED - 2023")
copy_L.config(font=("Segoe UI", 12))
copy_L.place(x=10, y=370)

input_L = Label(root, text="Please Select a QR Code to generate text:")
input_L.config(font=("Segoe UI", 12))
input_L.place(x=10, y=50)

select_B = Button(root, text="Select")
select_B.config(font=("Segoe UI", 12))
select_B.place(x=15, y=90, width=170)
select_B.config(command=openfile)

input_T = Text(root)
input_T.config(font=("Segoe UI", 12))
input_T.place(x=15, y=150, height=107, width=360)


decode_B = Button(root, text="Decode")
decode_B.config(command=decode_function)
decode_B.config(font=("Segoe UI", 12))
decode_B.place(x=205, y=90, width=170)

canvas = Canvas(root, width=240, height=240)
canvas.place(x=400, y=15)
canvas.config(bg="white")

canvas.create_text(
    120, 120, text="QR Code will appear here", font=("Segoe UI", 12), fill="black"
)


root.title("QR Code Decoder")
root.geometry("660x400")
root.resizable(False, False)
root.mainloop()
