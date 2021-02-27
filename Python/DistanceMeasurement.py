# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DistanceMeasurement.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time, threading

global ser
ser = serial.Serial('COM11', baudrate=115200, timeout=10,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 124)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.labelDistance = QtWidgets.QLabel(self.centralwidget)
        self.labelDistance.setGeometry(QtCore.QRect(60, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.labelDistance.setFont(font)
        self.labelDistance.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDistance.setObjectName("labelDistance")
        self.labelcm = QtWidgets.QLabel(self.centralwidget)
        self.labelcm.setGeometry(QtCore.QRect(120, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.labelcm.setFont(font)
        self.labelcm.setAlignment(QtCore.Qt.AlignCenter)
        self.labelcm.setObjectName("labelcm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Distance Measurement"))
        self.label.setText(_translate("MainWindow", "Obsctacle Distance"))
        self.labelDistance.setText(_translate("MainWindow", "0"))
        self.labelcm.setText(_translate("MainWindow", "cm"))
        # User Code
        self.timeout = 0
        self.check_serial_event()

    def check_serial_event(self):
        self.timeout += 1
        # print (self.timeout)
        serial_thread = threading.Timer(1, self.check_serial_event)
        if ser.is_open == True:
            serial_thread.start()
            if ser.in_waiting:
                eol = b'\n'
                leneol = len(eol)
                line = bytearray()
                while True:
                    c = ser.read(1)
                    if c:
                        line += c
                        if line[-leneol:] == eol:
                            break
                    else:
                        break
                    # print (line)
                    # print (type(line))
                line = line.rstrip()
                distance = line.decode("utf-8")
                self.labelDistance.setText(distance)
                # print (distance)
                self.timeout = 0

        if self.timeout >= 10:
            ser.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

