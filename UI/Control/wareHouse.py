# Form implementation generated from reading ui file 'wareHouse.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 151)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 81, 20))
        self.label.setObjectName("label")
        self.txtWarehouse = QtWidgets.QLineEdit(parent=Dialog)
        self.txtWarehouse.setGeometry(QtCore.QRect(140, 30, 181, 20))
        self.txtWarehouse.setObjectName("txtWarehouse")
        self.txtIdWarehouse = QtWidgets.QLineEdit(parent=Dialog)
        self.txtIdWarehouse.setGeometry(QtCore.QRect(140, 80, 120, 20))
        self.txtIdWarehouse.setObjectName("txtIdWarehouse")
        self.btnSave = QtWidgets.QPushButton(parent=Dialog)
        self.btnSave.setGeometry(QtCore.QRect(330, 30, 101, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnBack = QtWidgets.QPushButton(parent=Dialog)
        self.btnBack.setGeometry(QtCore.QRect(330, 80, 101, 23))
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Regitro de bodegas"))
        self.label_2.setText(_translate("Dialog", "ID de la bodega:"))
        self.label.setText(_translate("Dialog", "Nueva Bodega:"))
        self.btnSave.setText(_translate("Dialog", "Guardar"))
        self.btnBack.setText(_translate("Dialog", "Volver"))
