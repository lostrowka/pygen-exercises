from PySide2 import QtCore, QtWidgets


class Ui_Exercise(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Exercise 3")
        MainWindow.resize(240, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 1.1. Create new button with centralWidget parent

        # 1.2. Set button's geometry to QtCore.QRect(80, 50, 80, 25)

        # 1.3. Set object's name

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        # 1.4. Set button's text
