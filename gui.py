import subprocess
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(flags=QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.start_button = QtWidgets.QPushButton('Start')
        self.stop_button = QtWidgets.QPushButton('Stop')
        self.close_button = QtWidgets.QPushButton('X')

        self.start_button.setStyleSheet('QPushButton { background-color: #1abc9c; color: white; border-radius: 20px; }')
        self.stop_button.setStyleSheet('QPushButton { background-color: #e74c3c; color: white; border-radius: 20px; }')
        self.close_button.setStyleSheet('''
            QPushButton {
                width: 100px;
                height: 100px;
                background-color: #0d009c;
                border-radius: 50px;
                color: white;
                font-size: 25px;
                border: none;
                outline: none;
            }
            QPushButton:hover {
                background-color: #19137a;
            }
        ''')

        self.start_button.clicked.connect(self.start_script)
        self.stop_button.clicked.connect(self.stop_script)
        self.stop_button.setEnabled(False)
        self.close_button.clicked.connect(self.close_2)

        vbox_buttons = QtWidgets.QHBoxLayout()
        vbox_buttons.addWidget(self.start_button)
        vbox_buttons.addWidget(self.stop_button)

        # Add close button to vbox_buttons
        hbox_close = QtWidgets.QHBoxLayout()
        hbox_close.addStretch()
        hbox_close.addWidget(self.close_button)
        vbox_buttons.addLayout(hbox_close)

        group_box = QtWidgets.QGroupBox('Actions')
        group_box.setStyleSheet('''
            QGroupBox {
                background-color: transparent;
                font-size: 20px;
                color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
        ''')
        group_box.setLayout(vbox_buttons)

        self.collapse_button = QtWidgets.QPushButton('')
        self.collapse_button.clicked.connect(lambda: group_box.setVisible(not group_box.isVisible()))
        self.collapse_button.setStyleSheet('''
            QPushButton {
                width: 100px;
                height: 100px;
                background-color: #0d009c;
                border-radius: 50px;
                color: white;
                font-size: 25px;
                border: none;
                outline: none;
            }
            QPushButton:hover {
                background-color: #19137a;
            }
        ''')
        self.collapse_button.setIcon(QtGui.QIcon('Game_icon.png'))
        self.collapse_button.setIconSize(QtCore.QSize(30, 30))

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.collapse_button)
        hbox.addStretch()
        hbox.addWidget(group_box)

        vbox_main = QtWidgets.QVBoxLayout()
        vbox_main.addLayout(hbox)
        # Remove self.close_button from here
        self.setLayout(vbox_main)

        self.process = None
        self.draggable = True
        self.offset = None
        self.collapse_offset = None

    def start_script(self):
        self.process = subprocess.Popen(['python', 'mini.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_script(self):
        self.process.terminate()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def close_2(self):
        self.stop_script()
        self.close()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if event.pos() in self.collapse_button.geometry():
                self.collapse_offset = event.pos()
            else:
                self.offset = event.pos()
        else:
            super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)
        elif self.collapse_offset is not None and self.draggable:
            # Calculate the difference between the current position of the collapse button and the previous position
            delta = event.pos() - self.collapse_offset
            # Move the whole widget by the same amount as the collapse button
            self.move(self.pos() + delta)
            # Update the collapse button offset to the new position
            self.collapse_offset = event.pos()
        else:
            super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        if self.collapse_offset is not None:
            self.collapse_offset = None
        else:
            self.offset = None
            super().mouseReleaseEvent(event)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
