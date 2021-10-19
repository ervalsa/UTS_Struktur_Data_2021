import os
import sys
from typing import Optional
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, QRect, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMenu, QMenuBar, QWidget
from PyQt5.QtGui import QPixmap
from pathlib import Path

app = QApplication(sys.argv)

window = QMainWindow()

window.show()
window.setWindowTitle("Image Viewer")
window.showMaximized()

class ImageNode:
    def __init__(self, image: Optional[QPixmap] = None):
        self.item = image
        self.next = None
        self.prev = None

    def insert_next(self, image: Optional[QPixmap]):
        self.next = ImageNode(image)
        self.next.prev = self
        return self.next


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.showMaximized()
        self._create_menu()
        self.current_image: Optional[ImageNode] = None

    def _create_menu(self):
        menubar = QMenuBar(parent=self)
        menubar.addAction('open', self._open_file)
        menubar.show()

    def _open_file(self):
        from os import listdir

        dialog = QFileDialog(self, "Open Images", "~/")
        dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        if (dialog.exec()):
            file = Path(dialog.selectedFiles()[0])
            directory = file.parent

            files = [
                x.absolute() for x in directory.iterdir()
                if self._is_image(x.suffix)
            ]
            files.sort(key=str)

            it = iter(files)
            self.current_image = ImageNode(QPixmap(str(next(it, ''))))

            n = self.current_image
            for item in it:
                print(item, file)
                n = n.insert_next(QPixmap(str(item)))
                if item == file:
                    self.current_image = n

            self.repaint()

    def _is_image(self, ext):
        return ext == '.png' or ext == '.xpm' or ext == '.jpg'

    def get_paint_rect(self) -> QRect:
        rect_result = QRect()
        if self.current_image and self.current_image.item:
            rect = self.current_image.item.rect()
            rect_win = self.rect()
            scale = (rect_win.width() / rect.width()) * 0.8
            rect_result.setWidth(int(rect.width() * scale))
            rect_result.setHeight(int(rect.height() * scale))

            x = int((rect_win.width() / 2) - (rect_result.width() / 2))
            y = int(rect_win.height() / 2 - rect_result.height() / 2)

            pos = QPoint()
            pos.setX(x)
            pos.setY(y)

            rect_result.moveTo(pos)

        return rect_result

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Right:
            if self.current_image and self.current_image.next:
                self.current_image = self.current_image.next
                self.repaint()
        elif a0.key() == Qt.Key_Left:
            if self.current_image and self.current_image.prev:
                self.current_image = self.current_image.prev
                self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.current_image and self.current_image.item:
            painter = QtGui.QPainter(self)
            painter.drawPixmap(self.get_paint_rect(), self.current_image.item)


window = Window()
window.show()

sys.exit(app.exec_())