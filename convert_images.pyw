# Convert PNG files to ICO
# v1.0 - August 2nd 2022 -- Initial version
# v1.1 - August 9th 2024 -- Adding convertWebp function

import subprocess
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image
import os.path

principal = Tk()
principal.title("Image conversion")


miFrame = Frame(principal, width=950, height=950)
miFrame.pack()
contra = Entry(miFrame, show=" ")
rutain = Entry(miFrame)


def abrirf():
    rutain.delete(0, END)
    origen = filedialog.askopenfilename(title="Buscar", filetypes=[("png files", "*.png"), ("jpg files", "*.jpg"),
                                                                   ("webp files", "*.webp")], initialdir="/")
    rutain.insert(1, origen)


def fuera():
    rr = messagebox.askquestion("Saliendo", "¿Deseas salir de la aplicación?")
    if rr == "yes":
        principal.destroy()


def ayD():
    messagebox.showinfo("Ayuda",
                        "1. Elige archivo PNG, JPG o WEBp\n2. Convierte el archivo a ICO o PNG/JPG")


def version():
    messagebox.showinfo("Versión", "PNG to ICO \nWEBP to PNG/JPG\n\n\tversion: 1.1")


def convertImage():
    '''

    :param imagec: PNG or JPG filename
    :return: None
    '''
    imagec = rutain.get()
    img = Image.open(imagec)
    icon_sizes = [(16,16), (24, 24), (32, 32), (48, 48), (64,64), (128, 128), (256, 256)]

    for SIZEIM in icon_sizes:
        img.save(imagec.split(".")[0] + "_" + str(SIZEIM[0]) + '.ico', sizes=[SIZEIM])

    subprocess.Popen('explorer ' + os.path.dirname(imagec.replace("/", "\\")))

def convertWebp():
    '''
    Converts WEBP images into PNG/JPG
    :return: None
    :rtype:
    '''
    webp = rutain.get()
    imgw = Image.open(webp)

    for format_ima in [ "jpeg", "png" ]:
        imgw.save(webp.split(".")[0] + "." + format_ima, format_ima)

    subprocess.Popen('explorer ' + os.path.dirname(webp.replace("/", "\\")))


Button(miFrame, text="Buscar Archivo", command=abrirf, height= 1, width=25, padx=15, pady=25).pack()
Button(miFrame, text="Convertir a ICO", command=convertImage, height= 1, width=25, padx=15, pady=25).pack()
Button(miFrame, text="Convertir de Webp a PNG/JPG", command=convertWebp, height= 1, width=25, padx=15, pady=25).pack()
Button(miFrame, text="Salir", command=fuera, height= 1, width=25, padx=15, pady=25).pack()

barraMenu = Menu(principal)
principal.config(menu=barraMenu)

cierraM = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=cierraM)
cierraM.add_command(label="Uso", command=ayD)
cierraM.add_command(label="Version", command=version)
cierraM.add_command(label="Salir", command=fuera)

principal.mainloop()

# if __name__ == '__main__':
#     convertImage()