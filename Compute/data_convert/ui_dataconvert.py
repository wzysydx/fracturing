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
        self.groupBox.setGeometry(QtCore.QRect(30, 400, 191, 121))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.k_ymod = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.k_ymod.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.k_ymod.setDecimals(3)
        self.k_ymod.setMinimum(-99.0)
        self.k_ymod.setObjectName("k_ymod")
        self.horizontalLayout.addWidget(self.k_ymod)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.b_ymod = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.b_ymod.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b_ymod.setDecimals(3)
        self.b_ymod.setMinimum(-99.0)
        self.b_ymod.setObjectName("b_ymod")
        self.horizontalLayout.addWidget(self.b_ymod)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.k_pois = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.k_pois.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.k_pois.setDecimals(3)
        self.k_pois.setMinimum(-99.0)
        self.k_pois.setObjectName("k_pois")
        self.horizontalLayout_2.addWidget(self.k_pois)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.b_pois = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.b_pois.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b_pois.setDecimals(3)
        self.b_pois.setMinimum(-99.0)
        self.b_pois.setObjectName("b_pois")
        self.horizontalLayout_2.addWidget(self.b_pois)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.pb_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pb_convert.setGeometry(QtCore.QRect(430, 660, 91, 31))
        self.pb_convert.setObjectName("pb_convert")
        self.gp_conventional_log = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_conventional_log.setGeometry(QtCore.QRect(20, 20, 531, 341))
        self.gp_conventional_log.setAlignment(QtCore.Qt.AlignCenter)
        self.gp_conventional_log.setObjectName("gp_conventional_log")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gp_conventional_log)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.con_logdata = QtWidgets.QTableView(self.gp_conventional_log)
        self.con_logdata.setObjectName("con_logdata")
        self.verticalLayout_2.addWidget(self.con_logdata)
        self.gp_handled_data = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_handled_data.setGeometry(QtCore.QRect(570, 20, 551, 341))
        self.gp_handled_data.setAlignment(QtCore.Qt.AlignCenter)
        self.gp_handled_data.setObjectName("gp_handled_data")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gp_handled_data)
        self.verticalLayout.setObjectName("verticalLayout")
        self.handled_data = QtWidgets.QTableView(self.gp_handled_data)
        self.handled_data.setObjectName("handled_data")
        self.verticalLayout.addWidget(self.handled_data)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 380, 271, 231))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 212, 152))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setDecimals(3)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_2.addWidget(self.doubleSpinBox_7, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setDecimals(3)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_2.addWidget(self.doubleSpinBox_8, 4, 1, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setDecimals(3)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_2.addWidget(self.doubleSpinBox_9, 2, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_10.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_10.setDecimals(3)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_2.addWidget(self.doubleSpinBox_10, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 20, 212, 152))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_3.addWidget(self.doubleSpinBox_4, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_11.setDecimals(3)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout_3.addWidget(self.doubleSpinBox_11, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_12.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_12.setDecimals(3)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.gridLayout_3.addWidget(self.doubleSpinBox_12, 4, 1, 1, 1)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_13.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_13.setDecimals(3)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.gridLayout_3.addWidget(self.doubleSpinBox_13, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_14.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_14.setDecimals(3)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.gridLayout_3.addWidget(self.doubleSpinBox_14, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 400, 241, 161))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 30, 62, 22))
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(130, 60, 62, 22))
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.label_14.setObjectName("label_14")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(130, 90, 62, 22))
        self.doubleSpinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.label_17.setObjectName("label_17")
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dataconvert)

    def retranslateUi(self, dataconvert):
        _translate = QtCore.QCoreApplication.translate
        dataconvert.setWindowTitle(_translate("dataconvert", "岩石力学强度计算"))
        self.groupBox.setTitle(_translate("dataconvert", "模量转换参数："))
        self.label_9.setText(_translate("dataconvert", "动静态杨氏模量转换"))
        self.label.setText(_translate("dataconvert", "Es"))
        self.label_2.setText(_translate("dataconvert", "="))
        self.label_11.setText(_translate("dataconvert", "*"))
        self.label_4.setText(_translate("dataconvert", "Ed"))
        self.label_3.setText(_translate("dataconvert", "+"))
        self.label_10.setText(_translate("dataconvert", "动静态泊松比转换"))
        self.label_5.setText(_translate("dataconvert", "μs"))
        self.label_6.setText(_translate("dataconvert", "="))
        self.label_12.setText(_translate("dataconvert", "*"))
        self.label_7.setText(_translate("dataconvert", "μd"))
        self.label_8.setText(_translate("dataconvert", "+"))
        self.pb_convert.setText(_translate("dataconvert", "数据转换"))
        self.gp_conventional_log.setTitle(_translate("dataconvert", "常规测井数据"))
        self.gp_handled_data.setTitle(_translate("dataconvert", "测井数据处理结果"))
        self.groupBox_2.setTitle(_translate("dataconvert", "水平地应力计算公式选择："))
        self.label_15.setText(_translate("dataconvert", "水平最大地应力(ζh)系数"))
        self.label_18.setText(_translate("dataconvert", "Biot系数（α）"))
        self.label_20.setText(_translate("dataconvert", "地层孔隙压力系数（Pp）"))
        self.label_21.setText(_translate("dataconvert", "水平最大地应力(ζH)系数"))
        self.label_22.setText(_translate("dataconvert", "测井段以上岩石密度（g/cm3)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dataconvert", "各向同性模型"))
        self.label_16.setText(_translate("dataconvert", "水平最大地应力(ζh)系数"))
        self.label_19.setText(_translate("dataconvert", "Biot系数（α）"))
        self.label_23.setText(_translate("dataconvert", "地层孔隙压力系数"))
        self.label_24.setText(_translate("dataconvert", "水平最大地应力(ζH)系数"))
        self.label_25.setText(_translate("dataconvert", "非测井段岩石密度（g/cm3)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dataconvert", "横向各向同性模型"))
        self.groupBox_3.setTitle(_translate("dataconvert", "地层参数设置："))
        self.label_13.setText(_translate("dataconvert", "岩石骨架声波时差："))
        self.label_14.setText(_translate("dataconvert", "岩石流体声波时差："))
        self.label_17.setText(_translate("dataconvert", "岩石骨架密度："))
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