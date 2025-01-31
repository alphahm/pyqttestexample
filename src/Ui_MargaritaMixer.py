# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/MargaritaMixer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MargaritaMixer(object):
    def setupUi(self, MargaritaMixer):
        MargaritaMixer.setObjectName("MargaritaMixer")
        MargaritaMixer.resize(536, 368)
        self.gridLayout = QtWidgets.QGridLayout(MargaritaMixer)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(MargaritaMixer)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(MargaritaMixer)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tripleSecSpinBox = QtWidgets.QSpinBox(MargaritaMixer)
        self.tripleSecSpinBox.setMaximum(11)
        self.tripleSecSpinBox.setProperty("value", 4)
        self.tripleSecSpinBox.setObjectName("tripleSecSpinBox")
        self.gridLayout.addWidget(self.tripleSecSpinBox, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(MargaritaMixer)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.limeJuiceLineEdit = QtWidgets.QLineEdit(MargaritaMixer)
        self.limeJuiceLineEdit.setObjectName("limeJuiceLineEdit")
        self.gridLayout.addWidget(self.limeJuiceLineEdit, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(MargaritaMixer)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.iceHorizontalSlider = QtWidgets.QSlider(MargaritaMixer)
        self.iceHorizontalSlider.setMinimum(0)
        self.iceHorizontalSlider.setMaximum(20)
        self.iceHorizontalSlider.setProperty("value", 12)
        self.iceHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iceHorizontalSlider.setObjectName("iceHorizontalSlider")
        self.gridLayout.addWidget(self.iceHorizontalSlider, 3, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(MargaritaMixer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.tequilaScrollBar = QtWidgets.QScrollBar(MargaritaMixer)
        self.tequilaScrollBar.setEnabled(True)
        self.tequilaScrollBar.setMaximum(11)
        self.tequilaScrollBar.setProperty("value", 8)
        self.tequilaScrollBar.setSliderPosition(8)
        self.tequilaScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.tequilaScrollBar.setObjectName("tequilaScrollBar")
        self.gridLayout.addWidget(self.tequilaScrollBar, 0, 1, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(MargaritaMixer)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.speedButton1 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton1.setObjectName("speedButton1")
        self.speedButtonGroup = QtWidgets.QButtonGroup(MargaritaMixer)
        self.speedButtonGroup.setObjectName("speedButtonGroup")
        self.speedButtonGroup.addButton(self.speedButton1)
        self.gridLayout_2.addWidget(self.speedButton1, 0, 0, 1, 1)
        self.speedButton3 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton3.setObjectName("speedButton3")
        self.speedButtonGroup.addButton(self.speedButton3)
        self.gridLayout_2.addWidget(self.speedButton3, 0, 2, 1, 1)
        self.speedButton4 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton4.setObjectName("speedButton4")
        self.speedButtonGroup.addButton(self.speedButton4)
        self.gridLayout_2.addWidget(self.speedButton4, 1, 0, 1, 1)
        self.speedButton5 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton5.setChecked(True)
        self.speedButton5.setObjectName("speedButton5")
        self.speedButtonGroup.addButton(self.speedButton5)
        self.gridLayout_2.addWidget(self.speedButton5, 1, 1, 1, 1)
        self.speedButton6 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton6.setObjectName("speedButton6")
        self.speedButtonGroup.addButton(self.speedButton6)
        self.gridLayout_2.addWidget(self.speedButton6, 1, 2, 1, 1)
        self.speedButton9 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton9.setObjectName("speedButton9")
        self.speedButtonGroup.addButton(self.speedButton9)
        self.gridLayout_2.addWidget(self.speedButton9, 3, 2, 1, 1)
        self.speedButton8 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton8.setObjectName("speedButton8")
        self.speedButtonGroup.addButton(self.speedButton8)
        self.gridLayout_2.addWidget(self.speedButton8, 3, 1, 1, 1)
        self.speedButton7 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton7.setObjectName("speedButton7")
        self.speedButtonGroup.addButton(self.speedButton7)
        self.gridLayout_2.addWidget(self.speedButton7, 3, 0, 1, 1)
        self.speedButton2 = QtWidgets.QRadioButton(self.groupBox)
        self.speedButton2.setObjectName("speedButton2")
        self.speedButtonGroup.addButton(self.speedButton2)
        self.gridLayout_2.addWidget(self.speedButton2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.retranslateUi(MargaritaMixer)
        self.buttonBox.accepted.connect(MargaritaMixer.accept)
        self.buttonBox.rejected.connect(MargaritaMixer.reject)
        QtCore.QMetaObject.connectSlotsByName(MargaritaMixer)
        MargaritaMixer.setTabOrder(self.buttonBox, self.tripleSecSpinBox)
        MargaritaMixer.setTabOrder(self.tripleSecSpinBox, self.limeJuiceLineEdit)
        MargaritaMixer.setTabOrder(self.limeJuiceLineEdit, self.iceHorizontalSlider)
        MargaritaMixer.setTabOrder(self.iceHorizontalSlider, self.speedButton1)
        MargaritaMixer.setTabOrder(self.speedButton1, self.speedButton2)
        MargaritaMixer.setTabOrder(self.speedButton2, self.speedButton3)

    def retranslateUi(self, MargaritaMixer):
        _translate = QtCore.QCoreApplication.translate
        MargaritaMixer.setWindowTitle(_translate("MargaritaMixer", "Margarita Mixer"))
        self.label.setText(_translate("MargaritaMixer", "Tequila"))
        self.label_2.setText(_translate("MargaritaMixer", "Triple Sec"))
        self.tripleSecSpinBox.setToolTip(_translate("MargaritaMixer", "Jiggers of triple sec"))
        self.label_3.setText(_translate("MargaritaMixer", "Lime Juice"))
        self.limeJuiceLineEdit.setToolTip(_translate("MargaritaMixer", "Jiggers of lime juice"))
        self.limeJuiceLineEdit.setText(_translate("MargaritaMixer", "12.0"))
        self.label_4.setText(_translate("MargaritaMixer", "Ice"))
        self.iceHorizontalSlider.setToolTip(_translate("MargaritaMixer", "Chunks of ice"))
        self.buttonBox.setToolTip(_translate("MargaritaMixer", "Press OK to make the drinks"))
        self.tequilaScrollBar.setToolTip(_translate("MargaritaMixer", "Jiggers of tequila"))
        self.groupBox.setToolTip(_translate("MargaritaMixer", "Speed of the blender"))
        self.groupBox.setTitle(_translate("MargaritaMixer", "Blender Speed"))
        self.speedButton1.setText(_translate("MargaritaMixer", "&Mix"))
        self.speedButton3.setText(_translate("MargaritaMixer", "&Puree"))
        self.speedButton4.setText(_translate("MargaritaMixer", "&Chop"))
        self.speedButton5.setText(_translate("MargaritaMixer", "&Karate Chop"))
        self.speedButton6.setText(_translate("MargaritaMixer", "&Beat"))
        self.speedButton9.setText(_translate("MargaritaMixer", "&Vaporize"))
        self.speedButton8.setText(_translate("MargaritaMixer", "&Liquefy"))
        self.speedButton7.setText(_translate("MargaritaMixer", "&Smash"))
        self.speedButton2.setText(_translate("MargaritaMixer", "&Whip"))
