import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication, QMainWindow

from ex3_ui import Ui_Exercise


class ExerciseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Complete Ui_Exercise class

        self.ui = Ui_Exercise()
        self.ui.setupUi(self)

        # 2. Create and start a Thread making ARP request (import from example 1 and 2).
        #    Complete closeEvent func.

        # 3. Add listener for clicked() signal on created button

    def start_stop_thread(self):
        # 4. Replace pass with start/stop thread method (Hint: Flip one of variables in thread run func)
        pass

    def closeEvent(self, event):
        # Ad 2.Uncomment this and change self.thread, if your variable is named elsewise

        # self.thread.keep_running = False
        # self.thread.exit_thread = True
        event.accept()


def __main__():
    # Do not modify anything here
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    gui = ExerciseMainWindow()
    gui.show()

    app.exec_()


if __name__ == "__main__":
    __main__()
