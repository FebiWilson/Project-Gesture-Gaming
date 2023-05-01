from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import subprocess
import sys

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Script Controller")

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_script)
        self.start_button.setGeometry(50, 50, 100, 50)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_script)
        self.stop_button.setGeometry(50, 120, 100, 50)

    def start_script(self):
        # Replace "python script.py" with the command to start your script
        self.process = subprocess.Popen(["python", "mini.py"])

    def stop_script(self):
        self.process.terminate()
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
