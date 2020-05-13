# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wellinfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wellinfo(object):
    def setupUi(self, wellinfo):
        wellinfo.setObjectName("wellinfo")
        wellinfo.resize(216, 346)
        self.verticalLayout = QtWidgets.QVBoxLayout(wellinfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.well_description = QtWidgets.QGroupBox(wellinfo)
        self.well_description.setObjectName("well_description")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.well_description)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_block = QtWidgets.QLineEdit(self.well_description)
        self.le_block.setObjectName("le_block")
        self.gridLayout.addWidget(self.le_block, 0, 1, 1, 2)
        self.lb_layer = QtWidgets.QLabel(self.well_description)
        self.lb_layer.setObjectName("lb_layer")
        self.gridLayout.addWidget(self.lb_layer, 2, 0, 1, 2)
        self.lb_wellnum = QtWidgets.QLabel(self.well_description)
        self.lb_wellnum.setObjectName("lb_wellnum")
        self.gridLayout.addWidget(self.lb_wellnum, 1, 0, 1, 1)
        self.lb_bolck = QtWidgets.QLabel(self.well_description)
        self.lb_bolck.setObjectName("lb_bolck")
        self.gridLayout.addWidget(self.lb_bolck, 0, 0, 1, 1)
        self.le_wellnum = QtWidgets.QLineEdit(self.well_description)
        self.le_wellnum.setObjectName("le_wellnum")
        self.gridLayout.addWidget(self.le_wellnum, 1, 1, 1, 2)
        self.le_layer = QtWidgets.QLineEdit(self.well_description)
        self.le_layer.setObjectName("le_layer")
        self.gridLayout.addWidget(self.le_layer, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.well_description)
        self.layer_description = QtWidgets.QGroupBox(wellinfo)
        self.layer_description.setObjectName("layer_description")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layer_description)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layer_description)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layer_description)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.layer_description)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layer_description)
        self.label_7.setMinimumSize(QtCore.QSize(50, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layer_description)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.layer_description)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layer_description)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.layer_description)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layer_description)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.layer_description)
        self.pushButton = QtWidgets.QPushButton(wellinfo)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(wellinfo)
        QtCore.QMetaObject.connectSlotsByName(wellinfo)

    def retranslateUi(self, wellinfo):
        _translate = QtCore.QCoreApplication.translate
        wellinfo.setWindowTitle(_translate("wellinfo", "目标井参数录入"))
        self.well_description.setTitle(_translate("wellinfo", "可压性评价井描述："))
        self.lb_layer.setText(_translate("wellinfo", "所在层位："))
        self.lb_wellnum.setText(_translate("wellinfo", "井号："))
        self.lb_bolck.setText(_translate("wellinfo", "区块："))
        self.layer_description.setTitle(_translate("wellinfo", "评价层段描述："))
        self.label_4.setText(_translate("wellinfo", "顶深："))
        self.label_5.setText(_translate("wellinfo", "m"))
        self.label_7.setText(_translate("wellinfo", "底深："))
        self.label_6.setText(_translate("wellinfo", "m"))
        self.label_8.setText(_translate("wellinfo", "层段类型："))
        self.comboBox.setItemText(0, _translate("wellinfo", "页岩储层"))
        self.comboBox.setItemText(1, _translate("wellinfo", "砂岩储层"))
        self.plainTextEdit.setPlainText(_translate("wellinfo", "默认为由测井资料导入的全井段\n"
""))
        self.pushButton.setText(_translate("wellinfo", "确定选择"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wellinfo = QtWidgets.QWidget()
    ui = Ui_wellinfo()
    ui.setupUi(wellinfo)
    wellinfo.show()
    sys.exit(app.exec_())
