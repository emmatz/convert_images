from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QLabel, QMenuBar, QMenu, QLineEdit, QDialog
)
from PIL import Image
import subprocess
import os
import sys
import platform

class ImageConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Conversion")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Selecciona una imagen:")
        layout.addWidget(self.label)

        self.file_path = QLineEdit(self)
        layout.addWidget(self.file_path)

        self.btn_browse = QPushButton("Buscar Archivo", self)
        self.btn_browse.clicked.connect(self.abrirf)
        layout.addWidget(self.btn_browse)

        self.btn_convert_ico = QPushButton("Convertir a ICO", self)
        self.btn_convert_ico.clicked.connect(self.convertImage)
        layout.addWidget(self.btn_convert_ico)

        self.btn_convert_webp = QPushButton("Convertir de Webp a PNG/JPG", self)
        self.btn_convert_webp.clicked.connect(self.convertWebp)
        layout.addWidget(self.btn_convert_webp)

        self.btn_resize = QPushButton("Redimensionar Imagen", self)
        self.btn_resize.clicked.connect(self.abrirVentanaRedimensionar)
        layout.addWidget(self.btn_resize)

        self.btn_exit = QPushButton("Salir", self)
        self.btn_exit.clicked.connect(self.cerrarApp)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)

        # Menú
        self.menu_bar = QMenuBar(self)
        menu_ayuda = QMenu("Ayuda", self)
        menu_ayuda.addAction("Uso", self.ayD)
        menu_ayuda.addAction("Versión", self.version)
        menu_ayuda.addAction("Salir", self.cerrarApp)
        self.menu_bar.addMenu(menu_ayuda)

    def abrirf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Buscar", "/", "Imágenes (*.png *.jpg *.webp)")
        if file_name:
            self.file_path.setText(file_name)

    def cerrarApp(self):
        respuesta = QMessageBox.question(self, "Saliendo", "¿Deseas salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            QApplication.instance().quit()

    def ayD(self):
        QMessageBox.information(self, "Ayuda", "1. Elige un archivo PNG, JPG o WEBP\n2. Convierte el archivo a ICO o PNG/JPG")

    def version(self):
        QMessageBox.information(self, "Versión", "PNG to ICO \nWEBP to PNG/JPG\n\n\tversion: 1.3git ")

    def convertImage(self):
        imagec = self.file_path.text()
        if not imagec:
            QMessageBox.warning(self, "Error", "Por favor, selecciona una imagen")
            return

        img = Image.open(imagec)
        icon_sizes = [(16,16), (24, 24), (32, 32), (48, 48), (64,64), (128, 128), (256, 256)]

        for size in icon_sizes:
            img.save(f"{imagec.split('.')[0]}_{size[0]}.ico", sizes=[size])

        QMessageBox.information(self, "Éxito", "Conversión a ICO completada")
        AbrirImagen(imagec).openp()

    def convertWebp(self):
        webp = self.file_path.text()
        if not webp:
            QMessageBox.warning(self, "Error", "Por favor, selecciona una imagen")
            return

        imgw = Image.open(webp)
        for format_ima in ["jpeg", "png"]:
            imgw.save(f"{webp.split('.')[0]}.{format_ima}", format_ima)

        QMessageBox.information(self, "Éxito", "Conversión de WEBP a PNG/JPG completada")
        AbrirImagen(webp).openp()

    def abrirVentanaRedimensionar(self):
        dialog = RedimensionarImagen(self)
        dialog.exec()

class RedimensionarImagen(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Redimensionar Imagen")

        layout = QVBoxLayout()

        self.label_width = QLabel("Ancho:")
        layout.addWidget(self.label_width)
        self.entry_width = QLineEdit(self)
        layout.addWidget(self.entry_width)

        self.label_height = QLabel("Alto:")
        layout.addWidget(self.label_height)
        self.entry_height = QLineEdit(self)
        layout.addWidget(self.entry_height)

        self.btn_resize = QPushButton("Redimensionar", self)
        self.btn_resize.clicked.connect(self.resizeImage)
        layout.addWidget(self.btn_resize)

        self.btn_reset = QPushButton("Restablecer Valores", self)
        self.btn_reset.clicked.connect(self.resetearValores)
        layout.addWidget(self.btn_reset)

        self.setLayout(layout)

    def resizeImage(self):
        parent = self.parent()
        old_imagec = parent.file_path.text()

        if not old_imagec:
            QMessageBox.warning(self, "Error", "Selecciona una imagen antes de redimensionar.")
            return

        try:
            old_image = Image.open(old_imagec)
            new_W = int(self.entry_width.text())
            new_H = int(self.entry_height.text())

            new_image = old_image.resize((new_W, new_H))
            new_image.save(f"{old_imagec.split('.')[0]}_new_size.{old_imagec.split('.')[1]}")
            
            QMessageBox.information(self, "Éxito", "Imagen redimensionada correctamente")
            AbrirImagen(old_imagec).openp()
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingresa valores válidos para el ancho y alto.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error desconocido: {str(e)}")

    def resetearValores(self):
        self.entry_width.clear()
        self.entry_width.setText("0")
        self.entry_height.clear()
        self.entry_height.setText("0")

class AbrirImagen():
    def __init__(self, imgagep):
        self.imgagep = imgagep

    def openp(self):
        os_view = {"Windows": "explorer", "Linux": "xdg-open", "Darwin": "open"}
        subprocess.Popen([os_view.get(platform.system()), os.path.normpath(os.path.dirname(self.imgagep))])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ImageConverterApp()
    ventana.show()
    sys.exit(app.exec())

