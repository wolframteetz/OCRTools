# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1348, 811)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxEingang = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxEingang.sizePolicy().hasHeightForWidth())
        self.groupBoxEingang.setSizePolicy(sizePolicy)
        self.groupBoxEingang.setObjectName("groupBoxEingang")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxEingang)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetQuellordner = QtWidgets.QListWidget(self.groupBoxEingang)
        self.listWidgetQuellordner.setObjectName("listWidgetQuellordner")
        self.gridLayout.addWidget(self.listWidgetQuellordner, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.groupBoxEingang)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditQuellordner = QtWidgets.QLineEdit(self.groupBoxEingang)
        self.lineEditQuellordner.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditQuellordner.setObjectName("lineEditQuellordner")
        self.gridLayout.addWidget(self.lineEditQuellordner, 1, 0, 1, 1)
        self.toolButtonQuellordner = QtWidgets.QToolButton(self.groupBoxEingang)
        self.toolButtonQuellordner.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolButtonQuellordner.setObjectName("toolButtonQuellordner")
        self.gridLayout.addWidget(self.toolButtonQuellordner, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBoxEingang)
        self.groupBoxBild = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxBild.sizePolicy().hasHeightForWidth())
        self.groupBoxBild.setSizePolicy(sizePolicy)
        self.groupBoxBild.setMinimumSize(QtCore.QSize(600, 800))
        self.groupBoxBild.setObjectName("groupBoxBild")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxBild)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widgetBild = QtWidgets.QWidget(self.groupBoxBild)
        self.widgetBild.setObjectName("widgetBild")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widgetBild)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelBild = RubberbandEnhancedLabel(self.widgetBild)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBild.sizePolicy().hasHeightForWidth())
        self.labelBild.setSizePolicy(sizePolicy)
        self.labelBild.setMinimumSize(QtCore.QSize(400, 600))
        self.labelBild.setObjectName("labelBild")
        self.gridLayout_3.addWidget(self.labelBild, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widgetBild, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBoxBild)
        self.groupBoxDokumenttyp = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDokumenttyp.sizePolicy().hasHeightForWidth())
        self.groupBoxDokumenttyp.setSizePolicy(sizePolicy)
        self.groupBoxDokumenttyp.setObjectName("groupBoxDokumenttyp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxDokumenttyp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDokumenttyp = QtWidgets.QLabel(self.groupBoxDokumenttyp)
        self.labelDokumenttyp.setObjectName("labelDokumenttyp")
        self.verticalLayout.addWidget(self.labelDokumenttyp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditDokumenttyp = QtWidgets.QLineEdit(self.groupBoxDokumenttyp)
        self.lineEditDokumenttyp.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditDokumenttyp.setObjectName("lineEditDokumenttyp")
        self.horizontalLayout.addWidget(self.lineEditDokumenttyp)
        self.toolButtonDokumenttyp = QtWidgets.QToolButton(self.groupBoxDokumenttyp)
        self.toolButtonDokumenttyp.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolButtonDokumenttyp.setObjectName("toolButtonDokumenttyp")
        self.horizontalLayout.addWidget(self.toolButtonDokumenttyp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBoxDokumenttyp)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_3.addWidget(self.groupBoxDokumenttyp)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBoxEingang.setTitle(_translate("Form", "Eingang"))
        self.label.setText(_translate("Form", "Quellordner"))
        self.toolButtonQuellordner.setText(_translate("Form", "..."))
        self.groupBoxBild.setTitle(_translate("Form", "Bild"))
        self.labelBild.setText(_translate("Form", "Draggable_Graphics_View"))
        self.groupBoxDokumenttyp.setTitle(_translate("Form", "Dokumenttyp"))
        self.labelDokumenttyp.setText(_translate("Form", "JSON Strukturdatei"))
        self.toolButtonDokumenttyp.setText(_translate("Form", "..."))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Taste"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Element"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "b"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Form", "brief"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "x"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("Form", "absender"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("Form", "n"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(1, _translate("Form", "name"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "y"))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("Form", "adressat"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("Form", "n"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(1, _translate("Form", "name"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

from rubberbandenhancedlabel import RubberbandEnhancedLabel
