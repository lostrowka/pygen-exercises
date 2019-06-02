"""


    ************** BEFORE YOU USE THIS FILE **************

    *************** PLEASE, PLEASE ASK ME ****************

    **************** HAVE SOME CHALLENGE *****************

    This file is meant to check the solution
    The ones below are plobably not the best tho


"""



"""EXERCISE 1"""
import socket
import struct


class ARP:
    def __init__(self, iface):
        """Class for maintaining ARP requests

        Args:
            iface: interface on which we want to send ARP request

        """
        self.sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 3)
        self.sock.bind((iface, 0x0806))

    def send_data(self, dest_ip: str):
        source_mac = b"\xc0\x25\xe9\x13\xef\xfc"
        dest_mac = b"\x00\x00\x00\x00\x00\x00"

        src_ip = socket.inet_aton("192.168.0.25")
        dst_ip = socket.inet_aton(dest_ip)

        # --- short struct reference ---
        # struct.pack(format, args...)
        # ! - network format (big-endian)
        # H - 2 bytes
        # B - 1 byte
        # Xs - char arr (1 byte) with X length

        eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, 0x0806)
        # TODO: Fill arp header, see hints below
        # htype - ethernet (1)
        # ptype - TCP  (see EtherType)
        # hlen - length of hardware address (how many bytes in MAC addr...)
        # plen - length of protocol address (how many bytes in IP addr...)
        # operation - 1 for request, 2 for reply (we are sending...)
        arp_hdr = struct.pack("!HHBBH6s4s6s4s", 1, 0x0800, 6, 4, 1, source_mac, src_ip, dest_mac, dst_ip)

        packet = eth_hdr + arp_hdr

        self.sock.send(packet)


"""EXERCISE 2"""
import threading
import time

from solutions import ARP
from helper import ICMP


class MyThread(threading.Thread):
    def __init__(self, freq, **kwargs):
        self.keep_running = True
        self.exit_thread = False
        self.freq = freq
        threading.Thread.__init__(self, **kwargs)

    def run(self):
        print("Thread start")
        while not self.exit_thread:
            while self.keep_running:
                self._target(*self._args)
                time.sleep(int(self.freq) / 1000)


def __main__():
    arp = ARP("wlp6s0")
    icmp = ICMP("192.168.0.1", 0)

    t1 = MyThread(1000, target=arp.send_data, args=(["192.168.0.55"]))
    t2 = MyThread(1000, target=icmp.send_data, args=([""]))

    t1.start()
    t2.start()

    print("waiting")

    input()

    print("waited")

    t1.keep_running = False
    t1.exit_thread = True
    t2.keep_running = False
    t2.exit_thread = True

    t1.join()
    t2.join()


if __name__ == "__main__":
    __main__()


"""EXERCISE 3"""

import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore

from ex3_ui import Ui_Exercise
from solutions import MyThread, ARP


class ExerciseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Exercise()
        self.ui.setupUi(self)

        self.pb = self.ui.pushButton
        self.arp = ARP("wlp6s0")
        self.thread = MyThread(1000, target=self.arp.send_data, args=(["192.168.0.55"]))
        self.thread.start()

        QtCore.QObject.connect(self.pb, QtCore.SIGNAL('clicked()'), self.start_stop_thread)

    def start_stop_thread(self):
        self.thread.keep_running = not self.thread.keep_running


def __main__():
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    gui = ExerciseMainWindow()
    gui.show()

    app.exec_()


if __name__ == "__main__":
    __main__()

# UI

from PySide2 import QtCore, QtWidgets


class Ui_Exercise(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Exercise 3")
        MainWindow.resize(240, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 80, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))

