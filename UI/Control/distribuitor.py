# Form implementation generated from reading ui file 'distribuitor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 263)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 20))
        self.label.setObjectName("label")
        self.txtDistribuitor = QtWidgets.QLineEdit(parent=Dialog)
        self.txtDistribuitor.setGeometry(QtCore.QRect(140, 30, 181, 20))
        self.txtDistribuitor.setObjectName("txtDistribuitor")
        self.txtIdDistribuitor = QtWidgets.QLineEdit(parent=Dialog)
        self.txtIdDistribuitor.setGeometry(QtCore.QRect(140, 80, 120, 20))
        self.txtIdDistribuitor.setObjectName("txtIdDistribuitor")
        self.btnSave = QtWidgets.QPushButton(parent=Dialog)
        self.btnSave.setGeometry(QtCore.QRect(330, 30, 101, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnBack = QtWidgets.QPushButton(parent=Dialog)
        self.btnBack.setGeometry(QtCore.QRect(330, 80, 101, 23))
        self.btnBack.setObjectName("btnBack")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 51, 20))
        self.label_3.setObjectName("label_3")
        self.txtAddress = QtWidgets.QLineEdit(parent=Dialog)
        self.txtAddress.setGeometry(QtCore.QRect(140, 120, 291, 101))
        self.txtAddress.setObjectName("txtAddress")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registro de distribuidores"))
        self.label_2.setText(_translate("Dialog", "ID del distribuidor:"))
        self.label.setText(_translate("Dialog", "Nombre del distribuidor:"))
        self.btnSave.setText(_translate("Dialog", "Guardar"))
        self.btnBack.setText(_translate("Dialog", "Volver"))
        self.label_3.setText(_translate("Dialog", "Direccion:"))
