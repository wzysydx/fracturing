# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataconvert.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dataconvert(object):
    def setupUi(self, dataconvert):
        dataconvert.setObjectName("dataconvert")
        dataconvert.resize(1186, 885)
        self.centralwidget = QtWidgets.QWidget(dataconvert)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 450, 301, 241))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(11, 51, 248, 23))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.k_ymod = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.k_ymod.setDecimals(5)
        self.k_ymod.setMinimum(-99.0)
        self.k_ymod.setObjectName("k_ymod")
        self.horizontalLayout.addWidget(self.k_ymod)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.b_ymod = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.b_ymod.setDecimals(5)
        self.b_ymod.setMinimum(-99.0)
        self.b_ymod.setObjectName("b_ymod")
        self.horizontalLayout.addWidget(self.b_ymod)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(11, 108, 260, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.k_pois = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.k_pois.setDecimals(5)
        self.k_pois.setMinimum(-99.0)
        self.k_pois.setObjectName("k_pois")
        self.horizontalLayout_2.addWidget(self.k_pois)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.b_pois = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.b_pois.setDecimals(5)
        self.b_pois.setMinimum(-99.0)
        self.b_pois.setObjectName("b_pois")
        self.horizontalLayout_2.addWidget(self.b_pois)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(11, 23, 108, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(11, 80, 96, 16))
        self.label_10.setObjectName("label_10")
        self.pb_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pb_convert.setGeometry(QtCore.QRect(530, 440, 91, 31))
        self.pb_convert.setObjectName("pb_convert")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(540, 480, 391, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 30, 221, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 3, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(390, 20, 361, 341))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.origin_data_2 = QtWidgets.QTableView(self.groupBox_5)
        self.origin_data_2.setObjectName("origin_data_2")
        self.verticalLayout_3.addWidget(self.origin_data_2)
        self.gp_conventional_log = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_conventional_log.setGeometry(QtCore.QRect(20, 20, 361, 341))
        self.gp_conventional_log.setObjectName("gp_conventional_log")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gp_conventional_log)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.con_logdata = QtWidgets.QTableView(self.gp_conventional_log)
        self.con_logdata.setObjectName("con_logdata")
        self.verticalLayout_2.addWidget(self.con_logdata)
        self.gp_handled_data = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_handled_data.setGeometry(QtCore.QRect(780, 20, 341, 341))
        self.gp_handled_data.setObjectName("gp_handled_data")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gp_handled_data)
        self.verticalLayout.setObjectName("verticalLayout")
        self.handled_data = QtWidgets.QTableView(self.gp_handled_data)
        self.handled_data.setObjectName("handled_data")
        self.verticalLayout.addWidget(self.handled_data)
        dataconvert.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dataconvert)
        self.statusbar.setObjectName("statusbar")
        dataconvert.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(dataconvert)
        self.toolBar.setObjectName("toolBar")
        dataconvert.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(dataconvert)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1186, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        dataconvert.setMenuBar(self.menuBar)
        self.act_open_con = QtWidgets.QAction(dataconvert)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/image/open.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_open_con.setIcon(icon)
        self.act_open_con.setObjectName("act_open_con")
        self.toolBar.addAction(self.act_open_con)
        self.menu.addAction(self.act_open_con)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(dataconvert)
        QtCore.QMetaObject.connectSlotsByName(dataconvert)

    def retranslateUi(self, dataconvert):
        _translate = QtCore.QCoreApplication.translate
        dataconvert.setWindowTitle(_translate("dataconvert", "岩石力学强度计算"))
        self.groupBox.setTitle(_translate("dataconvert", "模量转换参数："))
        self.label.setText(_translate("dataconvert", "Es"))
        self.label_2.setText(_translate("dataconvert", "="))
        self.label_11.setText(_translate("dataconvert", "*"))
        self.label_4.setText(_translate("dataconvert", "Ed"))
        self.label_3.setText(_translate("dataconvert", "+"))
        self.label_5.setText(_translate("dataconvert", "μs"))
        self.label_6.setText(_translate("dataconvert", "="))
        self.label_12.setText(_translate("dataconvert", "*"))
        self.label_7.setText(_translate("dataconvert", "μd"))
        self.label_8.setText(_translate("dataconvert", "+"))
        self.label_9.setText(_translate("dataconvert", "动静态杨氏模量转换"))
        self.label_10.setText(_translate("dataconvert", "动静态泊松比转换"))
        self.pb_convert.setText(_translate("dataconvert", "数据转换"))
        self.groupBox_4.setTitle(_translate("dataconvert", "地应力转换参数："))
        self.label_13.setText(_translate("dataconvert", "水平最大地应力(SH)系数"))
        self.label_14.setText(_translate("dataconvert", "水平最大地应力(Sh)系数"))
        self.label_15.setText(_translate("dataconvert", "上覆压力梯度"))
        self.label_19.setText(_translate("dataconvert", "地层压力系数"))
        self.groupBox_5.setTitle(_translate("dataconvert", "阵列声波测井数据"))
        self.gp_conventional_log.setTitle(_translate("dataconvert", "常规测井数据"))
        self.gp_handled_data.setTitle(_translate("dataconvert", "测井数据处理结果"))
        self.toolBar.setWindowTitle(_translate("dataconvert", "toolBar"))
        self.menu.setTitle(_translate("dataconvert", "文件"))
        self.act_open_con.setText(_translate("dataconvert", "打开常规测井文件(&O)"))
        self.act_open_con.setShortcut(_translate("dataconvert", "Ctrl+O"))
import res_convert_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataconvert = QtWidgets.QMainWindow()
    ui = Ui_dataconvert()
    ui.setupUi(dataconvert)
    dataconvert.show()
    sys.exit(app.exec_())
