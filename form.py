# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(951, 727)
        Widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tabwidget = QTabWidget(Widget)
        self.tabwidget.setObjectName(u"tabwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(sizePolicy)
        self.tabwidget.setMinimumSize(QSize(490, 620))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.fault3Ind1CheckBox = QCheckBox(self.tab)
        self.fault3Ind1CheckBox.setObjectName(u"fault3Ind1CheckBox")
        self.fault3Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.fault3Ind1CheckBox, 27, 2, 1, 1)

        self.enc1StepsLabel = QLabel(self.tab)
        self.enc1StepsLabel.setObjectName(u"enc1StepsLabel")

        self.gridLayout.addWidget(self.enc1StepsLabel, 23, 1, 1, 1)

        self.valRegEdit0 = QLineEdit(self.tab)
        self.valRegEdit0.setObjectName(u"valRegEdit0")

        self.gridLayout.addWidget(self.valRegEdit0, 13, 1, 1, 1)

        self.label_36 = QLabel(self.tab)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout.addWidget(self.label_36, 23, 0, 1, 1)

        self.gotSpeedLabel0 = QLabel(self.tab)
        self.gotSpeedLabel0.setObjectName(u"gotSpeedLabel0")

        self.gridLayout.addWidget(self.gotSpeedLabel0, 7, 2, 1, 1)

        self.line_6 = QFrame(self.tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 5, 2, 1, 1)

        self.lock0Ind0CheckBox = QCheckBox(self.tab)
        self.lock0Ind0CheckBox.setObjectName(u"lock0Ind0CheckBox")
        self.lock0Ind0CheckBox.setEnabled(False)
        self.lock0Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.lock0Ind0CheckBox, 15, 2, 1, 1)

        self.fault3Ind0CheckBox = QCheckBox(self.tab)
        self.fault3Ind0CheckBox.setObjectName(u"fault3Ind0CheckBox")
        self.fault3Ind0CheckBox.setEnabled(False)
        self.fault3Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.fault3Ind0CheckBox, 14, 2, 1, 1)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 17, 1, 1, 1)

        self.writeRegEdit1 = QLineEdit(self.tab)
        self.writeRegEdit1.setObjectName(u"writeRegEdit1")

        self.gridLayout.addWidget(self.writeRegEdit1, 26, 0, 1, 1)

        self.lock0Ind1CheckBox = QCheckBox(self.tab)
        self.lock0Ind1CheckBox.setObjectName(u"lock0Ind1CheckBox")
        self.lock0Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.lock0Ind1CheckBox, 29, 2, 1, 1)

        self.scanButton = QPushButton(self.tab)
        self.scanButton.setObjectName(u"scanButton")

        self.gridLayout.addWidget(self.scanButton, 0, 0, 1, 1)

        self.bwdButton0 = QPushButton(self.tab)
        self.bwdButton0.setObjectName(u"bwdButton0")

        self.gridLayout.addWidget(self.bwdButton0, 8, 2, 1, 1)

        self.fwdButton0 = QPushButton(self.tab)
        self.fwdButton0.setObjectName(u"fwdButton0")

        self.gridLayout.addWidget(self.fwdButton0, 8, 0, 1, 1)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 5, 0, 1, 1)

        self.valRegEdit1 = QLineEdit(self.tab)
        self.valRegEdit1.setObjectName(u"valRegEdit1")

        self.gridLayout.addWidget(self.valRegEdit1, 26, 1, 1, 1)

        self.bwdButton1 = QPushButton(self.tab)
        self.bwdButton1.setObjectName(u"bwdButton1")

        self.gridLayout.addWidget(self.bwdButton1, 20, 2, 1, 1)

        self.lock1Ind1CheckBox = QCheckBox(self.tab)
        self.lock1Ind1CheckBox.setObjectName(u"lock1Ind1CheckBox")
        self.lock1Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.lock1Ind1CheckBox, 29, 1, 1, 1)

        self.lock5Ind1CheckBox = QCheckBox(self.tab)
        self.lock5Ind1CheckBox.setObjectName(u"lock5Ind1CheckBox")
        self.lock5Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.lock5Ind1CheckBox, 27, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 19, 0, 1, 1)

        self.speedSlider0 = QSlider(self.tab)
        self.speedSlider0.setObjectName(u"speedSlider0")
        self.speedSlider0.setMaximum(511)
        self.speedSlider0.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.speedSlider0, 9, 1, 1, 1)

        self.writeRegEdit0 = QLineEdit(self.tab)
        self.writeRegEdit0.setObjectName(u"writeRegEdit0")

        self.gridLayout.addWidget(self.writeRegEdit0, 13, 0, 1, 1)

        self.lock4Ind0CheckBox = QCheckBox(self.tab)
        self.lock4Ind0CheckBox.setObjectName(u"lock4Ind0CheckBox")
        self.lock4Ind0CheckBox.setEnabled(False)
        self.lock4Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.lock4Ind0CheckBox, 14, 1, 1, 1)

        self.gotRegLabel0 = QLabel(self.tab)
        self.gotRegLabel0.setObjectName(u"gotRegLabel0")

        self.gridLayout.addWidget(self.gotRegLabel0, 12, 2, 1, 1)

        self.readRegButton0 = QPushButton(self.tab)
        self.readRegButton0.setObjectName(u"readRegButton0")

        self.gridLayout.addWidget(self.readRegButton0, 12, 1, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)

        self.speedValLabel0 = QLabel(self.tab)
        self.speedValLabel0.setObjectName(u"speedValLabel0")

        self.gridLayout.addWidget(self.speedValLabel0, 9, 2, 1, 1)

        self.fwdButton1 = QPushButton(self.tab)
        self.fwdButton1.setObjectName(u"fwdButton1")

        self.gridLayout.addWidget(self.fwdButton1, 20, 0, 1, 1)

        self.lock5Ind0CheckBox = QCheckBox(self.tab)
        self.lock5Ind0CheckBox.setObjectName(u"lock5Ind0CheckBox")
        self.lock5Ind0CheckBox.setEnabled(False)
        self.lock5Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.lock5Ind0CheckBox, 14, 0, 1, 1)

        self.lock4Ind1CheckBox = QCheckBox(self.tab)
        self.lock4Ind1CheckBox.setObjectName(u"lock4Ind1CheckBox")
        self.lock4Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.lock4Ind1CheckBox, 27, 1, 1, 1)

        self.readRegEdit0 = QLineEdit(self.tab)
        self.readRegEdit0.setObjectName(u"readRegEdit0")

        self.gridLayout.addWidget(self.readRegEdit0, 12, 0, 1, 1)

        self.resetFaultButton1 = QPushButton(self.tab)
        self.resetFaultButton1.setObjectName(u"resetFaultButton1")

        self.gridLayout.addWidget(self.resetFaultButton1, 30, 0, 1, 1)

        self.connectButton = QPushButton(self.tab)
        self.connectButton.setObjectName(u"connectButton")

        self.gridLayout.addWidget(self.connectButton, 0, 2, 1, 1)

        self.speedValLabel1 = QLabel(self.tab)
        self.speedValLabel1.setObjectName(u"speedValLabel1")

        self.gridLayout.addWidget(self.speedValLabel1, 22, 2, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 17, 0, 1, 1)

        self.resetFaultButton0 = QPushButton(self.tab)
        self.resetFaultButton0.setObjectName(u"resetFaultButton0")

        self.gridLayout.addWidget(self.resetFaultButton0, 16, 0, 1, 1)

        self.readRegButton1 = QPushButton(self.tab)
        self.readRegButton1.setObjectName(u"readRegButton1")

        self.gridLayout.addWidget(self.readRegButton1, 25, 1, 1, 1)

        self.gotSpeedLabel1 = QLabel(self.tab)
        self.gotSpeedLabel1.setObjectName(u"gotSpeedLabel1")

        self.gridLayout.addWidget(self.gotSpeedLabel1, 19, 2, 1, 1)

        self.gotRegLabel1 = QLabel(self.tab)
        self.gotRegLabel1.setObjectName(u"gotRegLabel1")

        self.gridLayout.addWidget(self.gotRegLabel1, 25, 2, 1, 1)

        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 11, 0, 1, 1)

        self.enc0StepsLabel = QLabel(self.tab)
        self.enc0StepsLabel.setObjectName(u"enc0StepsLabel")

        self.gridLayout.addWidget(self.enc0StepsLabel, 10, 1, 1, 1)

        self.writeRegButton1 = QPushButton(self.tab)
        self.writeRegButton1.setObjectName(u"writeRegButton1")

        self.gridLayout.addWidget(self.writeRegButton1, 26, 2, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 19, 1, 1, 1)

        self.fg0RevsLabel = QLabel(self.tab)
        self.fg0RevsLabel.setObjectName(u"fg0RevsLabel")

        self.gridLayout.addWidget(self.fg0RevsLabel, 11, 2, 1, 1)

        self.lock2Ind0CheckBox = QCheckBox(self.tab)
        self.lock2Ind0CheckBox.setObjectName(u"lock2Ind0CheckBox")
        self.lock2Ind0CheckBox.setEnabled(False)
        self.lock2Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.lock2Ind0CheckBox, 15, 0, 1, 1)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 17, 2, 1, 1)

        self.devicesComboBox = QComboBox(self.tab)
        self.devicesComboBox.setObjectName(u"devicesComboBox")

        self.gridLayout.addWidget(self.devicesComboBox, 0, 1, 1, 1)

        self.writeRegButton0 = QPushButton(self.tab)
        self.writeRegButton0.setObjectName(u"writeRegButton0")

        self.gridLayout.addWidget(self.writeRegButton0, 13, 2, 1, 1)

        self.readRegEdit1 = QLineEdit(self.tab)
        self.readRegEdit1.setObjectName(u"readRegEdit1")

        self.gridLayout.addWidget(self.readRegEdit1, 25, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.speedSlider1 = QSlider(self.tab)
        self.speedSlider1.setObjectName(u"speedSlider1")
        self.speedSlider1.setMaximum(511)
        self.speedSlider1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.speedSlider1, 22, 1, 1, 1)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 7, 1, 1, 1)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 22, 0, 1, 1)

        self.lock1Ind0CheckBox = QCheckBox(self.tab)
        self.lock1Ind0CheckBox.setObjectName(u"lock1Ind0CheckBox")
        self.lock1Ind0CheckBox.setEnabled(False)
        self.lock1Ind0CheckBox.setCheckable(True)

        self.gridLayout.addWidget(self.lock1Ind0CheckBox, 15, 1, 1, 1)

        self.lock2Ind1CheckBox = QCheckBox(self.tab)
        self.lock2Ind1CheckBox.setObjectName(u"lock2Ind1CheckBox")
        self.lock2Ind1CheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.lock2Ind1CheckBox, 29, 0, 1, 1)

        self.enc1RevsLabel = QLabel(self.tab)
        self.enc1RevsLabel.setObjectName(u"enc1RevsLabel")

        self.gridLayout.addWidget(self.enc1RevsLabel, 23, 2, 1, 1)

        self.enc0RevsLabel = QLabel(self.tab)
        self.enc0RevsLabel.setObjectName(u"enc0RevsLabel")

        self.gridLayout.addWidget(self.enc0RevsLabel, 10, 2, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_41 = QLabel(self.tab)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout.addWidget(self.label_41, 24, 0, 1, 1)

        self.fg1RevsLabel = QLabel(self.tab)
        self.fg1RevsLabel.setObjectName(u"fg1RevsLabel")

        self.gridLayout.addWidget(self.fg1RevsLabel, 24, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.tabwidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bemfComboBox0 = QComboBox(self.tab_2)
        self.bemfComboBox0.setObjectName(u"bemfComboBox0")

        self.gridLayout_2.addWidget(self.bemfComboBox0, 3, 1, 1, 1)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 10, 0, 1, 1)

        self.mprComboBox1 = QComboBox(self.tab_2)
        self.mprComboBox1.setObjectName(u"mprComboBox1")

        self.gridLayout_2.addWidget(self.mprComboBox1, 6, 1, 1, 1)

        self.tsettingComboBox1 = QComboBox(self.tab_2)
        self.tsettingComboBox1.setObjectName(u"tsettingComboBox1")

        self.gridLayout_2.addWidget(self.tsettingComboBox1, 8, 1, 1, 1)

        self.verbSpinBox = QSpinBox(self.tab_2)
        self.verbSpinBox.setObjectName(u"verbSpinBox")
        self.verbSpinBox.setMaximum(4)
        self.verbSpinBox.setValue(2)

        self.gridLayout_2.addWidget(self.verbSpinBox, 10, 1, 1, 1)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 8, 0, 1, 1)

        self.varAdvCheckBox0 = QCheckBox(self.tab_2)
        self.varAdvCheckBox0.setObjectName(u"varAdvCheckBox0")

        self.gridLayout_2.addWidget(self.varAdvCheckBox0, 4, 2, 1, 1)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)

        self.hcAdjCheckBox0 = QCheckBox(self.tab_2)
        self.hcAdjCheckBox0.setObjectName(u"hcAdjCheckBox0")

        self.gridLayout_2.addWidget(self.hcAdjCheckBox0, 3, 2, 1, 1)

        self.mprComboBox0 = QComboBox(self.tab_2)
        self.mprComboBox0.setObjectName(u"mprComboBox0")

        self.gridLayout_2.addWidget(self.mprComboBox0, 2, 1, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_47 = QLabel(self.tab_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_2.addWidget(self.label_47, 11, 0, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)

        self.dfreqCheckBox0 = QCheckBox(self.tab_2)
        self.dfreqCheckBox0.setObjectName(u"dfreqCheckBox0")

        self.gridLayout_2.addWidget(self.dfreqCheckBox0, 2, 2, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)

        self.dfreqCheckBox1 = QCheckBox(self.tab_2)
        self.dfreqCheckBox1.setObjectName(u"dfreqCheckBox1")

        self.gridLayout_2.addWidget(self.dfreqCheckBox1, 6, 2, 1, 1)

        self.hcAdjCheckBox1 = QCheckBox(self.tab_2)
        self.hcAdjCheckBox1.setObjectName(u"hcAdjCheckBox1")

        self.gridLayout_2.addWidget(self.hcAdjCheckBox1, 7, 2, 1, 1)

        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 9, 0, 1, 1)

        self.bemfComboBox1 = QComboBox(self.tab_2)
        self.bemfComboBox1.setObjectName(u"bemfComboBox1")

        self.gridLayout_2.addWidget(self.bemfComboBox1, 7, 1, 1, 1)

        self.varAdvCheckBox1 = QCheckBox(self.tab_2)
        self.varAdvCheckBox1.setObjectName(u"varAdvCheckBox1")

        self.gridLayout_2.addWidget(self.varAdvCheckBox1, 8, 2, 1, 1)

        self.tsettingComboBox0 = QComboBox(self.tab_2)
        self.tsettingComboBox0.setObjectName(u"tsettingComboBox0")

        self.gridLayout_2.addWidget(self.tsettingComboBox0, 4, 1, 1, 1)

        self.label_48 = QLabel(self.tab_2)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_2.addWidget(self.label_48, 12, 0, 1, 1)

        self.fgSpinBox = QSpinBox(self.tab_2)
        self.fgSpinBox.setObjectName(u"fgSpinBox")
        self.fgSpinBox.setMinimum(1)
        self.fgSpinBox.setMaximum(128)
        self.fgSpinBox.setValue(11)

        self.gridLayout_2.addWidget(self.fgSpinBox, 11, 1, 1, 1)

        self.encSpinBox = QSpinBox(self.tab_2)
        self.encSpinBox.setObjectName(u"encSpinBox")
        self.encSpinBox.setMinimum(1)
        self.encSpinBox.setMaximum(3000)
        self.encSpinBox.setSingleStep(10)
        self.encSpinBox.setValue(600)

        self.gridLayout_2.addWidget(self.encSpinBox, 12, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tabwidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_3 = QWidget(self.tab_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 671, 572))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_27 = QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_13.addWidget(self.label_27)

        self.fgolselComboBox = QComboBox(self.gridLayoutWidget_3)
        self.fgolselComboBox.setObjectName(u"fgolselComboBox")

        self.verticalLayout_13.addWidget(self.fgolselComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_13, 9, 0, 1, 1)

        self.avsmenCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.avsmenCheckBox.setObjectName(u"avsmenCheckBox")

        self.gridLayout_5.addWidget(self.avsmenCheckBox, 5, 4, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_14.addWidget(self.label_18)

        self.oplcurrrtComboBox = QComboBox(self.gridLayoutWidget_3)
        self.oplcurrrtComboBox.setObjectName(u"oplcurrrtComboBox")

        self.verticalLayout_14.addWidget(self.oplcurrrtComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_25 = QLabel(self.gridLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_10.addWidget(self.label_25)

        self.swilimitthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.swilimitthrComboBox.setObjectName(u"swilimitthrComboBox")

        self.verticalLayout_10.addWidget(self.swilimitthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_10, 6, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_3.addWidget(self.label_19)

        self.isdthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.isdthrComboBox.setObjectName(u"isdthrComboBox")

        self.verticalLayout_3.addWidget(self.isdthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_28 = QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_22.addWidget(self.label_28)

        self.deadtimeComboBox = QComboBox(self.gridLayoutWidget_3)
        self.deadtimeComboBox.setObjectName(u"deadtimeComboBox")

        self.verticalLayout_22.addWidget(self.deadtimeComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_22, 7, 4, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_29 = QLabel(self.gridLayoutWidget_3)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_15.addWidget(self.label_29)

        self.brkdonethrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.brkdonethrComboBox.setObjectName(u"brkdonethrComboBox")

        self.verticalLayout_15.addWidget(self.brkdonethrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_15, 1, 5, 1, 1)

        self.locken4CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.locken4CheckBox.setObjectName(u"locken4CheckBox")

        self.gridLayout_5.addWidget(self.locken4CheckBox, 8, 4, 1, 1)

        self.vregselCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.vregselCheckBox.setObjectName(u"vregselCheckBox")

        self.gridLayout_5.addWidget(self.vregselCheckBox, 8, 5, 1, 1)

        self.rvsdrenCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.rvsdrenCheckBox.setObjectName(u"rvsdrenCheckBox")

        self.gridLayout_5.addWidget(self.rvsdrenCheckBox, 0, 5, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_26 = QLabel(self.gridLayoutWidget_3)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_11.addWidget(self.label_26)

        self.ipdcurrthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.ipdcurrthrComboBox.setObjectName(u"ipdcurrthrComboBox")

        self.verticalLayout_11.addWidget(self.ipdcurrthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_11, 8, 0, 1, 1)

        self.locken1CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.locken1CheckBox.setObjectName(u"locken1CheckBox")

        self.gridLayout_5.addWidget(self.locken1CheckBox, 5, 2, 1, 1)

        self.cloopdisCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.cloopdisCheckBox.setObjectName(u"cloopdisCheckBox")

        self.gridLayout_5.addWidget(self.cloopdisCheckBox, 9, 6, 1, 1)

        self.locken2CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.locken2CheckBox.setObjectName(u"locken2CheckBox")

        self.gridLayout_5.addWidget(self.locken2CheckBox, 5, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_33 = QLabel(self.gridLayoutWidget_3)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_18.addWidget(self.label_33)

        self.aligntimeComboBox = QComboBox(self.gridLayoutWidget_3)
        self.aligntimeComboBox.setObjectName(u"aligntimeComboBox")

        self.verticalLayout_18.addWidget(self.aligntimeComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_18, 4, 5, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_32 = QLabel(self.gridLayoutWidget_3)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_17.addWidget(self.label_32)

        self.staccelComboBox = QComboBox(self.gridLayoutWidget_3)
        self.staccelComboBox.setObjectName(u"staccelComboBox")

        self.verticalLayout_17.addWidget(self.staccelComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_17, 2, 5, 1, 1)

        self.locken5CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.locken5CheckBox.setObjectName(u"locken5CheckBox")

        self.gridLayout_5.addWidget(self.locken5CheckBox, 7, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_4.addWidget(self.label_20)

        self.ipdadvcaglComboBox = QComboBox(self.gridLayoutWidget_3)
        self.ipdadvcaglComboBox.setObjectName(u"ipdadvcaglComboBox")

        self.verticalLayout_4.addWidget(self.ipdadvcaglComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_35 = QLabel(self.gridLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_21.addWidget(self.label_35)

        self.clslpaccelComboBox = QComboBox(self.gridLayoutWidget_3)
        self.clslpaccelComboBox.setObjectName(u"clslpaccelComboBox")

        self.verticalLayout_21.addWidget(self.clslpaccelComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_21, 7, 1, 1, 1)

        self.spdctrlmdCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.spdctrlmdCheckBox.setObjectName(u"spdctrlmdCheckBox")

        self.gridLayout_5.addWidget(self.spdctrlmdCheckBox, 9, 5, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(self.gridLayoutWidget_3)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_5.addWidget(self.label_21)

        self.rvsdrthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.rvsdrthrComboBox.setObjectName(u"rvsdrthrComboBox")

        self.verticalLayout_5.addWidget(self.rvsdrthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 6, 1, 1)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_39 = QLabel(self.gridLayoutWidget_3)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_26.addWidget(self.label_39)

        self.ktlckthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.ktlckthrComboBox.setObjectName(u"ktlckthrComboBox")

        self.verticalLayout_26.addWidget(self.ktlckthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_26, 9, 4, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_31 = QLabel(self.gridLayoutWidget_3)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_16.addWidget(self.label_31)

        self.staccel2ComboBox = QComboBox(self.gridLayoutWidget_3)
        self.staccel2ComboBox.setObjectName(u"staccel2ComboBox")

        self.verticalLayout_16.addWidget(self.staccel2ComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_16, 2, 1, 1, 1)

        self.ipdrismdCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.ipdrismdCheckBox.setObjectName(u"ipdrismdCheckBox")

        self.gridLayout_5.addWidget(self.ipdrismdCheckBox, 5, 6, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_37 = QLabel(self.gridLayoutWidget_3)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_23.addWidget(self.label_37)

        self.ipdclkComboBox = QComboBox(self.gridLayoutWidget_3)
        self.ipdclkComboBox.setObjectName(u"ipdclkComboBox")

        self.verticalLayout_23.addWidget(self.ipdclkComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_23, 8, 6, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.gridLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_9.addWidget(self.label_24)

        self.op2clsthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.op2clsthrComboBox.setObjectName(u"op2clsthrComboBox")

        self.verticalLayout_9.addWidget(self.op2clsthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_9, 4, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_38 = QLabel(self.gridLayoutWidget_3)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_24.addWidget(self.label_38)

        self.fgcycleComboBox = QComboBox(self.gridLayoutWidget_3)
        self.fgcycleComboBox.setObjectName(u"fgcycleComboBox")

        self.verticalLayout_24.addWidget(self.fgcycleComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_24, 9, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_22 = QLabel(self.gridLayoutWidget_3)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_7.addWidget(self.label_22)

        self.openlcurrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.openlcurrComboBox.setObjectName(u"openlcurrComboBox")

        self.verticalLayout_7.addWidget(self.openlcurrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_23 = QLabel(self.gridLayoutWidget_3)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_8.addWidget(self.label_23)

        self.ctrlcoefComboBox = QComboBox(self.gridLayoutWidget_3)
        self.ctrlcoefComboBox.setObjectName(u"ctrlcoefComboBox")

        self.verticalLayout_8.addWidget(self.ctrlcoefComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_8, 2, 0, 1, 1)

        self.avsmmdCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.avsmmdCheckBox.setObjectName(u"avsmmdCheckBox")

        self.gridLayout_5.addWidget(self.avsmmdCheckBox, 5, 5, 1, 1)

        self.isdenCheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.isdenCheckBox.setObjectName(u"isdenCheckBox")

        self.gridLayout_5.addWidget(self.isdenCheckBox, 0, 4, 1, 1)

        self.faulten3CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.faulten3CheckBox.setObjectName(u"faulten3CheckBox")

        self.gridLayout_5.addWidget(self.faulten3CheckBox, 5, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_20.addWidget(self.label_34)

        self.hwilimitthrComboBox = QComboBox(self.gridLayoutWidget_3)
        self.hwilimitthrComboBox.setObjectName(u"hwilimitthrComboBox")

        self.verticalLayout_20.addWidget(self.hwilimitthrComboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_20, 6, 4, 1, 1)

        self.locken0CheckBox = QCheckBox(self.gridLayoutWidget_3)
        self.locken0CheckBox.setObjectName(u"locken0CheckBox")

        self.gridLayout_5.addWidget(self.locken0CheckBox, 5, 3, 1, 1)

        self.verticalLayoutWidget_12 = QWidget(self.tab_4)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(690, 10, 101, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.motor0RadioButton = QRadioButton(self.verticalLayoutWidget_12)
        self.motor0RadioButton.setObjectName(u"motor0RadioButton")
        self.motor0RadioButton.setChecked(True)

        self.verticalLayout.addWidget(self.motor0RadioButton)

        self.motor1RadioButton = QRadioButton(self.verticalLayoutWidget_12)
        self.motor1RadioButton.setObjectName(u"motor1RadioButton")

        self.verticalLayout.addWidget(self.motor1RadioButton)

        self.tabwidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.regValsTable = QTableWidget(self.tab_3)
        if (self.regValsTable.columnCount() < 5):
            self.regValsTable.setColumnCount(5)
        if (self.regValsTable.rowCount() < 44):
            self.regValsTable.setRowCount(44)
        __qtablewidgetitem = QTableWidgetItem()
        self.regValsTable.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.regValsTable.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.regValsTable.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.regValsTable.setItem(0, 3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.regValsTable.setItem(0, 4, __qtablewidgetitem4)
        self.regValsTable.setObjectName(u"regValsTable")
        self.regValsTable.setGeometry(QRect(0, 0, 551, 561))
        self.regValsTable.setRowCount(44)
        self.regValsTable.setColumnCount(5)
        self.regValsTable.horizontalHeader().setDefaultSectionSize(100)
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(560, 0, 361, 196))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.reloadRegsButton1 = QPushButton(self.gridLayoutWidget)
        self.reloadRegsButton1.setObjectName(u"reloadRegsButton1")

        self.gridLayout_7.addWidget(self.reloadRegsButton1, 2, 1, 1, 1)

        self.saveAllRegsButton = QPushButton(self.gridLayoutWidget)
        self.saveAllRegsButton.setObjectName(u"saveAllRegsButton")

        self.gridLayout_7.addWidget(self.saveAllRegsButton, 0, 0, 1, 1)

        self.reloadRegsButton0 = QPushButton(self.gridLayoutWidget)
        self.reloadRegsButton0.setObjectName(u"reloadRegsButton0")

        self.gridLayout_7.addWidget(self.reloadRegsButton0, 2, 0, 1, 1)

        self.loadAllRegsButton = QPushButton(self.gridLayoutWidget)
        self.loadAllRegsButton.setObjectName(u"loadAllRegsButton")

        self.gridLayout_7.addWidget(self.loadAllRegsButton, 0, 1, 1, 1)

        self.sendRegsButton0 = QPushButton(self.gridLayoutWidget)
        self.sendRegsButton0.setObjectName(u"sendRegsButton0")

        self.gridLayout_7.addWidget(self.sendRegsButton0, 1, 0, 1, 1)

        self.sendRegsButton1 = QPushButton(self.gridLayoutWidget)
        self.sendRegsButton1.setObjectName(u"sendRegsButton1")

        self.gridLayout_7.addWidget(self.sendRegsButton1, 1, 1, 1, 1)

        self.readCopyFlashButton0 = QPushButton(self.gridLayoutWidget)
        self.readCopyFlashButton0.setObjectName(u"readCopyFlashButton0")

        self.gridLayout_7.addWidget(self.readCopyFlashButton0, 3, 0, 1, 1)

        self.writeFlashButton0 = QPushButton(self.gridLayoutWidget)
        self.writeFlashButton0.setObjectName(u"writeFlashButton0")

        self.gridLayout_7.addWidget(self.writeFlashButton0, 4, 0, 1, 1)

        self.readCopyFlashButton1 = QPushButton(self.gridLayoutWidget)
        self.readCopyFlashButton1.setObjectName(u"readCopyFlashButton1")

        self.gridLayout_7.addWidget(self.readCopyFlashButton1, 3, 1, 1, 1)

        self.writeFlashButton1 = QPushButton(self.gridLayoutWidget)
        self.writeFlashButton1.setObjectName(u"writeFlashButton1")

        self.gridLayout_7.addWidget(self.writeFlashButton1, 4, 1, 1, 1)

        self.tabwidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_9 = QGridLayout(self.tab_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_40 = QLabel(self.tab_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_8.addWidget(self.label_40, 1, 0, 1, 1)

        self.timeLabel = QLabel(self.tab_5)
        self.timeLabel.setObjectName(u"timeLabel")

        self.gridLayout_8.addWidget(self.timeLabel, 2, 1, 1, 1)

        self.dateLabel = QLabel(self.tab_5)
        self.dateLabel.setObjectName(u"dateLabel")

        self.gridLayout_8.addWidget(self.dateLabel, 1, 1, 1, 1)

        self.label_42 = QLabel(self.tab_5)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_8.addWidget(self.label_42, 2, 0, 1, 1)

        self.fixLabel = QLabel(self.tab_5)
        self.fixLabel.setObjectName(u"fixLabel")

        self.gridLayout_8.addWidget(self.fixLabel, 0, 1, 1, 1)

        self.label_43 = QLabel(self.tab_5)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_8.addWidget(self.label_43, 3, 0, 1, 1)

        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_8.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_44 = QLabel(self.tab_5)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_8.addWidget(self.label_44, 4, 0, 1, 1)

        self.latiLabel = QLabel(self.tab_5)
        self.latiLabel.setObjectName(u"latiLabel")

        self.gridLayout_8.addWidget(self.latiLabel, 3, 1, 1, 1)

        self.longiLabel = QLabel(self.tab_5)
        self.longiLabel.setObjectName(u"longiLabel")

        self.gridLayout_8.addWidget(self.longiLabel, 4, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.tabwidget.addTab(self.tab_5, "")

        self.gridLayout_6.addWidget(self.tabwidget, 0, 0, 1, 1)

        self.logEdit = QTextEdit(Widget)
        self.logEdit.setObjectName(u"logEdit")

        self.gridLayout_6.addWidget(self.logEdit, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)


        self.retranslateUi(Widget)

        self.tabwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"bldcMortar Tools", None))
#if QT_CONFIG(accessibility)
        self.tabwidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.fault3Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"No motor", None))
        self.enc1StepsLabel.setText(QCoreApplication.translate("Widget", u"0", None))
        self.valRegEdit0.setText(QCoreApplication.translate("Widget", u"0xFF", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"Encoder 1 steps", None))
        self.gotSpeedLabel0.setText(QCoreApplication.translate("Widget", u"0 Hz", None))
        self.lock0Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"Lock detection current limit", None))
        self.fault3Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"No motor", None))
        self.writeRegEdit1.setText(QCoreApplication.translate("Widget", u"0x00", None))
        self.lock0Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"Lock detection current limit", None))
        self.scanButton.setText(QCoreApplication.translate("Widget", u"Scan", None))
        self.bwdButton0.setText(QCoreApplication.translate("Widget", u"Backward", None))
        self.fwdButton0.setText(QCoreApplication.translate("Widget", u"Forward", None))
        self.valRegEdit1.setText(QCoreApplication.translate("Widget", u"0xFF", None))
        self.bwdButton1.setText(QCoreApplication.translate("Widget", u"Backward", None))
        self.lock1Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"Speed abnormal", None))
        self.lock5Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"Stuck in closed loop", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MOTOR 1</span></p></body></html>", None))
        self.writeRegEdit0.setText(QCoreApplication.translate("Widget", u"0x00", None))
        self.lock4Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"Stuck in open loop", None))
        self.gotRegLabel0.setText(QCoreApplication.translate("Widget", u"...", None))
        self.readRegButton0.setText(QCoreApplication.translate("Widget", u"Read register", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Speed motor 0", None))
        self.speedValLabel0.setText(QCoreApplication.translate("Widget", u"0", None))
        self.fwdButton1.setText(QCoreApplication.translate("Widget", u"Forward", None))
        self.lock5Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"Stuck in closed loop", None))
        self.lock4Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"Stuck in open loop", None))
        self.readRegEdit0.setText(QCoreApplication.translate("Widget", u"0x1E", None))
        self.resetFaultButton1.setText(QCoreApplication.translate("Widget", u"Reset fault info", None))
        self.connectButton.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.speedValLabel1.setText(QCoreApplication.translate("Widget", u"0", None))
        self.resetFaultButton0.setText(QCoreApplication.translate("Widget", u"Reset fault info", None))
        self.readRegButton1.setText(QCoreApplication.translate("Widget", u"Read register", None))
        self.gotSpeedLabel1.setText(QCoreApplication.translate("Widget", u"0 Hz", None))
        self.gotRegLabel1.setText(QCoreApplication.translate("Widget", u"...", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Motor (FG 0) revs", None))
        self.enc0StepsLabel.setText(QCoreApplication.translate("Widget", u"0", None))
        self.writeRegButton1.setText(QCoreApplication.translate("Widget", u"Write register", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Speed:", None))
        self.fg0RevsLabel.setText(QCoreApplication.translate("Widget", u"0 rev", None))
        self.lock2Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"Kt abnormal", None))
        self.devicesComboBox.setCurrentText("")
        self.writeRegButton0.setText(QCoreApplication.translate("Widget", u"Write register", None))
        self.readRegEdit1.setText(QCoreApplication.translate("Widget", u"0x1E", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MOTOR 0</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Speed:", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Speed motor 1", None))
        self.lock1Ind0CheckBox.setText(QCoreApplication.translate("Widget", u"Speed abnormal", None))
        self.lock2Ind1CheckBox.setText(QCoreApplication.translate("Widget", u"Kt abnormal", None))
        self.enc1RevsLabel.setText(QCoreApplication.translate("Widget", u"0 rev", None))
        self.enc0RevsLabel.setText(QCoreApplication.translate("Widget", u"0 rev", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Encoder 0 steps", None))
        self.label_41.setText(QCoreApplication.translate("Widget", u"Motor (FG 1) revs", None))
        self.fg1RevsLabel.setText(QCoreApplication.translate("Widget", u"0 rev", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Main", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"UART verbosity level", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Motor Phase Resistance [\u03a9]", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Commutation advance [\u03bcs]", None))
        self.varAdvCheckBox0.setText(QCoreApplication.translate("Widget", u"Variable time advance", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MOTOR 0</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Motor Phase Resistance [\u03a9]", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"BEMF Constant [mV/Hz]", None))
        self.hcAdjCheckBox0.setText(QCoreApplication.translate("Widget", u"Half cycle adjust mode", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"BEMF Constant [mV/Hz]", None))
        self.label_47.setText(QCoreApplication.translate("Widget", u"FG divider (pairs of poles)", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MOTOR 1</span></p></body></html>", None))
        self.dfreqCheckBox0.setText(QCoreApplication.translate("Widget", u"Double Frequency", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Commutation advance [\u03bcs]", None))
        self.dfreqCheckBox1.setText(QCoreApplication.translate("Widget", u"Double Frequency", None))
        self.hcAdjCheckBox1.setText(QCoreApplication.translate("Widget", u"Half cycle adjust mode", None))
        self.label_46.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Other options</span></p></body></html>", None))
        self.varAdvCheckBox1.setText(QCoreApplication.translate("Widget", u"Variable time advance", None))
        self.label_48.setText(QCoreApplication.translate("Widget", u"Encoder divider (pulse/rev)", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Prefs: Motorparams", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"FGOLsel", None))
        self.avsmenCheckBox.setText(QCoreApplication.translate("Widget", u"AVSMEn", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"OpLCurrRt", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"SWiLimitThr", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"ISDThr", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"Deadtime", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"BrkDoneThr", None))
        self.locken4CheckBox.setText(QCoreApplication.translate("Widget", u"LockEn4", None))
        self.vregselCheckBox.setText(QCoreApplication.translate("Widget", u"VregSel", None))
        self.rvsdrenCheckBox.setText(QCoreApplication.translate("Widget", u"RvsDrEn", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"IPDCurrThr", None))
        self.locken1CheckBox.setText(QCoreApplication.translate("Widget", u"LockEn1", None))
        self.cloopdisCheckBox.setText(QCoreApplication.translate("Widget", u"CLoopDis", None))
        self.locken2CheckBox.setText(QCoreApplication.translate("Widget", u"LockEn2", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"AlignTime", None))
        self.label_32.setText(QCoreApplication.translate("Widget", u"StAccel", None))
        self.locken5CheckBox.setText(QCoreApplication.translate("Widget", u"LockEn5", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"IPDAdvcAgl", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"ClsLpAccel", None))
        self.spdctrlmdCheckBox.setText(QCoreApplication.translate("Widget", u"SpdCtrlMd", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"RvsDrThr", None))
        self.label_39.setText(QCoreApplication.translate("Widget", u"KtLckThr", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"StAccel2", None))
        self.ipdrismdCheckBox.setText(QCoreApplication.translate("Widget", u"IPDRIsMd", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"IPDClk", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"Op2ClsThr", None))
        self.label_38.setText(QCoreApplication.translate("Widget", u"FGcycle", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"OpenLCurr", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"CtrlCoef", None))
        self.avsmmdCheckBox.setText(QCoreApplication.translate("Widget", u"AVSMMd", None))
        self.isdenCheckBox.setText(QCoreApplication.translate("Widget", u"ISDen", None))
        self.faulten3CheckBox.setText(QCoreApplication.translate("Widget", u"FaultEn3", None))
        self.label_34.setText(QCoreApplication.translate("Widget", u"HWiLimitThr", None))
        self.locken0CheckBox.setText(QCoreApplication.translate("Widget", u"LockEn0", None))
        self.motor0RadioButton.setText(QCoreApplication.translate("Widget", u"Motor 0", None))
        self.motor1RadioButton.setText(QCoreApplication.translate("Widget", u"Motor 1", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"Prefs: SysOpts", None))

        __sortingEnabled = self.regValsTable.isSortingEnabled()
        self.regValsTable.setSortingEnabled(False)
        self.regValsTable.setSortingEnabled(__sortingEnabled)

        self.reloadRegsButton1.setText(QCoreApplication.translate("Widget", u"Reload all from drive 1", None))
        self.saveAllRegsButton.setText(QCoreApplication.translate("Widget", u"Save all to file", None))
        self.reloadRegsButton0.setText(QCoreApplication.translate("Widget", u"Reload all from drive 0", None))
        self.loadAllRegsButton.setText(QCoreApplication.translate("Widget", u"Load from file", None))
        self.sendRegsButton0.setText(QCoreApplication.translate("Widget", u"Send regs to drive 0", None))
        self.sendRegsButton1.setText(QCoreApplication.translate("Widget", u"Send regs to drive 1", None))
        self.readCopyFlashButton0.setText(QCoreApplication.translate("Widget", u"Copy flash 0 to registers 0", None))
        self.writeFlashButton0.setText(QCoreApplication.translate("Widget", u"Copy registers 0 to flash 0", None))
        self.readCopyFlashButton1.setText(QCoreApplication.translate("Widget", u"Copy flash 1 to registers 1", None))
        self.writeFlashButton1.setText(QCoreApplication.translate("Widget", u"Copy registers 0 to flash1 ", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Registry values", None))
        self.label_40.setText(QCoreApplication.translate("Widget", u"Date", None))
        self.timeLabel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.dateLabel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.label_42.setText(QCoreApplication.translate("Widget", u"Time", None))
        self.fixLabel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.label_43.setText(QCoreApplication.translate("Widget", u"Latitude", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"Fix state", None))
        self.label_44.setText(QCoreApplication.translate("Widget", u"Longitude", None))
        self.latiLabel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.longiLabel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"GPS info", None))
    # retranslateUi

