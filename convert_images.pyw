# Convert PNG files to ICO
# v1.0 - August 2nd 2022 -- Initial version
# v1.1 - August 9th 2024 -- Adding convertWebp function
# v1.2 - March  3rd 2025 -- Adding resizeImage function
# v2.0 - March  5th 2025 -- Change to Qt for GUI. Major update. Qt designer used to build GUI
# v2.1 - March  6th 2025 -- Changing default directory to open.

from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsPixmapItem,
                               QGraphicsScene, QWidget)
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt
from interfaces.mainWin import Ui_MainWindow
from interfaces.redimensionar import Ui_rediForm
from PIL import Image
from pathlib import Path
import platform
import subprocess
import sys

class OpenFileExplorer():
    def __init__(self, file_path):
        self.file_path = file_path

    def openDirectory(self):
        os_view = {"Windows": "explorer", "Linux": "xdg-open", "Darwin": "open"}
        path = Path(self.file_path).resolve()
        directory = path.parent
        subprocess.Popen([os_view.get(platform.system()), str(directory)])


class RediWindow(QWidget, Ui_rediForm):
    def __init__(self, path_image=None):
        super().__init__()
        self.setupUi(self)
        self.pushSalir.clicked.connect(self.close)
        self.pushRedi.clicked.connect(self.new_size)
        self.pushReset.clicked.connect(self.reset_original_values)

        self.path_image = path_image
        self.original_width = 0
        self.original_height = 0

        if path_image:
            self.set_image_dimensions()

    def set_image_dimensions(self):
        try:
            img = Image.open(self.path_image)
            self.original_width, self.original_height = img.size  # Guarda valores originales

            self.spinBoxAncho.setValue(self.original_width)
            self.spinBoxAlto.setValue(self.original_height)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def new_size(self):
        """Redimensiona la imagen según los valores de los spinBox."""
        try:
            new_width = self.spinBoxAncho.value()
            new_height = self.spinBoxAlto.value()

            # Verifica si los valores cambiaron
            if new_width == self.original_width and new_height == self.original_height:
                QMessageBox.information(self, "Sin cambios", "Las dimensiones son iguales a la original.")
                return

            img = Image.open(self.path_image)
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)

            new_path = f"{Path(self.path_image).parent}/{Path(self.path_image).stem}_resized{Path(self.path_image).suffix}"
            resized_img.save(new_path)

            QMessageBox.information(self, "Éxito", f"Imagen redimensionada")
            explorer = OpenFileExplorer(new_path)
            explorer.openDirectory()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al redimensionar la imagen: {e}")

    def reset_original_values(self):
        """Restaura los valores originales de los spinBox."""
        self.spinBoxAncho.setValue(self.original_width)
        self.spinBoxAlto.setValue(self.original_height)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Crear la escena para el QGraphicsView
        self.scene = QGraphicsScene(self)  # Crea la escena
        self.graphicsView.setScene(self.scene)  # Establece la escena al QGraphicsView
        # Conectar el evento de texto cambiado en el QLineEdit al método que actualizará la imagen
        self.lineEdit.textChanged.connect(self.update_image)

        self.pushBuscar.clicked.connect(self.abrirf)
        self.pushIco.clicked.connect(self.convertToIco)
        self.pushWebp.clicked.connect(self.convertWebp)
        self.pushRed.clicked.connect(self.resizeImage)
        self.pushSalir.clicked.connect(self.close)

    def error(self):
        try:
            text = self.lineEdit.text()

            if text.strip() == "":
                QMessageBox.critical(self, "Error", "No hay imagen a procesar.")
                return None

            if Path(text).is_file():
                return text
            else:
                QMessageBox.warning(self, "Error", "El archivo no existe o no se especificó correctamente.")
                return None

        except Exception as e:
            QMessageBox.warning(self, "Error", "Hubo un problema al procesar el archivo.")
            return None

    def abrirf(self):
        # Obtén el archivo seleccionado
        # file_name, _ = QFileDialog.getOpenFileName(self, caption="Buscar", dir="/", filter="*.png *.jpg *.webp *.jpeg")
        file_name, _ = QFileDialog.getOpenFileName(self, caption="Buscar",
                                                   dir=str(Path.home()/'Pictures' if Path.home()/'Pictures' else Path.home()),
                                                   filter="*.png *.jpg *.webp *.jpeg")
        if file_name:
            # Actualiza el QLineEdit con la ruta seleccionada
            self.lineEdit.setText(file_name)

    def openNewImage(self, img):
        '''
        Opens directory where the image was stored.
        :param img: Absolute path
        :type img:  str
        :return: None
        :rtype: None
        '''
        explorer = OpenFileExplorer(img)
        explorer.openDirectory()
        return None

    def update_image(self):
        # Obtener el path de la imagen desde el QLineEdit
        image_path = self.lineEdit.text()

        # Si el campo está vacío, limpiamos la escena
        if not image_path:
            self.scene.clear()
            return

        # Crear un QPixmap a partir del path de la imagen
        pixmap = QPixmap(image_path)

        # Verificar si la imagen se cargó correctamente
        if not pixmap.isNull():
            # Obtener el tamaño del QGraphicsView
            view_width = self.graphicsView.width()
            view_height = self.graphicsView.height()

            # Escalar la imagen al tamaño del QGraphicsView sin modificar la imagen original
            scaled_pixmap = pixmap.scaled(view_width, view_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Crear un QGraphicsPixmapItem y agregarlo a la escena
            pixmap_item = QGraphicsPixmapItem(scaled_pixmap)

            # Crear un QGraphicsPixmapItem y agregarlo a la escena ==== tamano normal
            # pixmap_item = QGraphicsPixmapItem(pixmap)

            # Limpiar la escena y agregar el nuevo item
            self.scene.clear()
            self.scene.addItem(pixmap_item)

            # Ajustar la vista para que la imagen se vea bien
            # self.view.setRenderHint(QPainter.Antialiasing)
            # self.view.setRenderHint(QPainter.SmoothPixmapTransform)
            self.graphicsView.setRenderHint(QPainter.Antialiasing)
            self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        else:
            # Si la imagen no se carga correctamente, limpiar la escena
            self.scene.clear()
            # QMessageBox.warning(self, "Error", "No se pudo cargar la imagen.")

    def convertToIco(self):
        try:
            imagec = self.error()
            if not imagec:
                return

            img = Image.open(imagec)
            icon_sizes = [(16,16), (24, 24), (32, 32), (48, 48), (64,64), (128, 128), (256, 256)]

            for size in icon_sizes:
                img.save(f"{Path(imagec).parent / Path(imagec).stem}_{size[0]}.ico", sizes=[size])

            QMessageBox.information(self, "Éxito", "Conversión a ICO completada")
            self.openNewImage(imagec)
        except Exception  as e:
            QMessageBox.critical(self, "Error", f"{str(e)}")

    def convertWebp(self):
        try:
            webp = self.error()
            if not webp:
                # QMessageBox.warning(self, "Error", "Por favor, selecciona una imagen")
                return

            imgw = Image.open(webp)
            for format_ima in ["jpeg", "png"]:
                imgw.save(f"{Path(webp).parent / Path(webp).stem}_new.{format_ima}", format_ima)

            QMessageBox.information(self, "Éxito", "Conversión a PNG y JPEG terminada.")
            self.openNewImage(webp)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{str(e)}")

    def resizeImage(self):
        try:
            image_to_change = self.error()
            if not image_to_change:
                return
            try:
                img = Image.open(image_to_change)
                img.verify()
            except Exception as ee:
                QMessageBox.critical(self, "Error", f"{str(ee)}")
                return
            self.resizeWindow = RediWindow(image_to_change)
            self.resizeWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
