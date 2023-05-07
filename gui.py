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

        vbox_buttons = QtWidgets.QVBoxLayout()
        vbox_buttons.addWidget(self.start_button)
        vbox_buttons.addWidget(self.stop_button)

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

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.collapse_button)
        vbox.addWidget(group_box)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.close_button)

        self.setLayout(hbox)

        self.process = None
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


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
