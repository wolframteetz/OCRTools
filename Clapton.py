# -*- coding: utf-8 -*-
#
# Project Clapton
# File    Clapton.py
# Version 0.1a
# Python  3
# PO      Wolfram Teetz <wolframteetz@gmail.com>
#
# TODO VORSICHT BEI WIEDEREINGESCANNTEN VORLAGEN (!) BEISPIElDATENSATZ 1 FÜR ML -> Artefakte!
# TODO 156 DATEIEN TIFF IN DATENSATZ 1 (!)
# TODO AUTOMATIC CHECK OF PERSONAL DATA AFTER OCR
#
# Import PySide
# 17.44 laim 17.52 hbf 17.57 hbf

# TODO : VERIFY SHORTCUTS
# TODO : SELECT NEXT ELEMENT OF PREVIOUSLY SELECTED ELEMENT UPON "RETURN" (l 163 top level)
# TODO : HIGHLIGHT

#default_image_dir = "/Users/sir/Allianz/ocr-data/scan10sep17done/_jpg/wallenfels"
#default_json = "/Users/sir/Clapton/Clapton/Hackathon_RS.json"
from pathlib import Path
#default_image_dir = str(Path.home())+"/Allianz/ocr-data/scan10sep17done/_jpg/wallenfels"
#default_image_dir = str(Path.home())+"/Allianz/RSV_Data_1/S2680"
#default_json = str(Path.home())+"/Clapton/Clapton/Hackathon_RS.json"
default_image_dir = str(Path.home())
default_json = "/usr/local/bin/Hackathon_RS.json"

import sys
import os
import json
import re
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from rubberbandenhancedlabel import *
from mainwindow import Ui_Form

# Create a Qt application
app = QtWidgets.QApplication(sys.argv)
#app = QApplication(sys.argv)

DIRTY_QUICK_DAVID=True # Quick annotation - careful to use this flag it does not guarantee synchronization of display and json

class ClaptonWidget(QtWidgets.QWidget):
    struc = "" # JSON Structure of Document Types
    quellOrdnerSelectedFilename=""
    pixmap_realsize={"width":0,"height":0}
    def nextDocument(self):
        self.ui.listWidgetQuellordner.setCurrentRow(self.ui.listWidgetQuellordner.currentRow()+1)
    def previousDocument(self):
        self.ui.listWidgetQuellordner.setCurrentRow(self.ui.listWidgetQuellordner.currentRow()-1)
    def openElement(self):
        elements = self.ui.treeWidget.selectedItems()
        if elements is not None:
            if len(elements)>0:
                element = elements[0]
                element.setExpanded(True)
    def removeElement(self):
        print("REMOVE")
        _filepath = self.quellOrdnerSelectedFilename+".json"
        try:
            print("REMOVE"+_filepath)
            os.remove(_filepath)
            print("OK")
        except:
            pass
        self.setDokumenttyp(self.ui.lineEditDokumenttyp.text())

    def __init__(self):
        super(ClaptonWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('CLAPTON - CLassification, Anonymization, Pseudonymization and Tagging with OCR and NLP')
        self.setBaseSize(1250, 700)
        self.ui.toolButtonQuellordner.clicked.connect(self.clickSetDirectory)
        self.ui.listWidgetQuellordner.currentTextChanged.connect(self.listWidgetQuellordner_currentTextChanged)
        self.ui.labelBild.setScaledContents(True)
        self.setDirectory(default_image_dir)
        self.ui.toolButtonDokumenttyp.clicked.connect(self.clickSetDokumenttyp)
        self.setDokumenttyp(default_json)
        self.ui.treeWidget.doubleClicked.connect(self.treeWidget_itemSelectionChanged)
        returnFilter = returnKeyFilter(self.ui.treeWidget)
        self.ui.treeWidget.installEventFilter(returnFilter)
        returnFilter.returnKeyPressed.connect(self.treeWidget_itemSelectionChanged)
        #self.ui.treeWidget.itemSelectionChanged.connect(self.treeWidget_itemSelectionChanged)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Down"), self, self.nextDocument)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Up"), self, self.previousDocument)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.close)
        QtWidgets.QShortcut(QtGui.QKeySequence("Space"), self, self.nextDocument)
        QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self, self.removeElement)
        self.ui.treeWidget.setFocus()
    def clickSetDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        self.setDirectory(directory)
    def setDirectory(self, directory):
        self.ui.listWidgetQuellordner.clear() # In case there are any existing elements in the list
        if directory: # if user didn't pick a directory don't continue
            self.ui.lineEditQuellordner.setText(directory)
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                if file_name.endswith(".TIFF"):
                    self.ui.listWidgetQuellordner.addItem(file_name)  # add file to the listWidget

    def listWidgetQuellordner_currentTextChanged(self, newPixmapFilename): # load different image
        self.quellOrdnerSelectedFilename = self.ui.lineEditQuellordner.text() + "/" + newPixmapFilename
        if (len(self.ui.lineEditDokumenttyp.text())>0):
           print("CTC")
           self.setDokumenttyp(self.ui.lineEditDokumenttyp.text())
        cur_pixmap = QtGui.QPixmap(self.quellOrdnerSelectedFilename)
        self.pixmap_realsize = {"width":cur_pixmap.width(), "height":cur_pixmap.height()}
        pixmap = cur_pixmap.scaled(self.ui.widgetBild.width(), self.ui.widgetBild.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.labelBild.setPixmap(pixmap)
        elements = self.ui.treeWidget.setCurrentItem(self.ui.treeWidget.topLevelItem(0))


    def clickSetDokumenttyp(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a JSON")
        if filename: # if user didn't pick a directory don't continue
            print("FILE")
            self.setDokumenttyp(filename)
        else:
            print("NO_FILE")
    def recurse_json_to_treeWidget(self, struc):
        l=[]
        for title in struc:
            if isinstance(struc[title], str):
                #print(struc[title])
                #print(title)
                w = QtWidgets.QTreeWidgetItem([struc[title], title])
                l.append(w)
                if title == "area_px":
                    w.setBackground(0, QtGui.QColor(255,255,128))

            if isinstance(struc[title], list):
                #print(struc[title])
                w = QtWidgets.QTreeWidgetItem([struc[title][0], title])
                if len(struc[title])>1:
                    w.addChildren(self.recurse_json_to_treeWidget(struc[title][1]))
                    w.setBackground(0, w.child(0).background(0))
                #print(title)
                #print(struc[title])
                #w.addChildren(self.recurse_json_to_treeWidget(struc))
                l.append(w)
                if title == "area_px":
                    w.setBackground(0, QtGui.QColor(255,255,128))
                    areas_vector = json.loads("["+struc[title][0]+"]")
                    print("###")
                    print(areas_vector)
                #     w = QtWidgets.QTreeWidgetItem([struc[title][0], title])
                #r = self.recurse_json_to_treeWidget(struc[title][1])
                #w.addChild(r)
        return l

    def setDokumenttyp(self, filename):
        if filename: # if user didn't pick a directory don't continue
            self.ui.lineEditDokumenttyp.setText(filename)
            jsonQuelldatei = self.quellOrdnerSelectedFilename + ".json"
            if os.path.isfile(jsonQuelldatei):
                print("LOAD JSON")
                print(jsonQuelldatei)
                #self.struc = self.loadCommentedJSON(jsonQuelldatei)
                self.struc = self.loadCommentedJSON(filename)
                addstruc = self.loadCommentedJSON(jsonQuelldatei)
                self.struc.update(addstruc)
            else:
                print("LOAD GENERIC JSON")
                print(jsonQuelldatei)
                self.struc = self.loadCommentedJSON(filename)
            self.populateTreeWidgetFromStruc()

    def populateTreeWidgetFromStruc(self):

        #store_current = self.ui.treeWidget.selectedItems() #NEW TODO :: Get top level item, restore it
        self.ui.treeWidget.clear() # In case there are any existing elements in the list
        l = []  # list of QTreeWidgetItem to add
        for title in self.struc:
            w = QtWidgets.QTreeWidgetItem([self.struc[title][0], title])
            w.addChildren(self.recurse_json_to_treeWidget(self.struc[title][1]))
            w.setBackground(0, w.child(0).background(0))
            l.append(w)
        tree = self.ui.treeWidget
        tree.addTopLevelItems(l)

            ##exit(0) #####
            ##for title in self.struc:
            ##    w=QtWidgets.QTreeWidgetItem([self.struc[title][0], title])  # create QTreeWidgetItem's and append them
            ##    for child in self.struc[title][1]:
            ##        _child = self.struc[title][1][child]
            ##        print(type(_child), _child)
                    #if isinstance(_child, str):
                    #    w.addChild(QtWidgets.QTreeWidgetItem([child, child]))
                    #print(self.struc[title][1][child][1])
            ##    l.append(w)
                #l.append(QtWidgets.QTreeWidgetItem([self.struc[title][0]]))  # create QTreeWidgetItem's and append them
                #rowPosition = self.ui.treeWidget.rowCount()
                #self.ui.treeWidget.insertRow(rowPosition)
                #self.ui.treeWidget.setItem(rowPosition-1, 0, QtWidgets.QTableWidgetItem(title))
                #self.ui.treeWidget.setItem(rowPosition-1, 1, QtWidgets.QTableWidgetItem(self.struc[title][0]))
            # populate tree
            ###########

    def treeWidget_itemSelectionChanged(self):
        getSelected = self.ui.treeWidget.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            while baseNode.child(0) is not None: # Travel to a leaf
                baseNode = baseNode.child(0)
            list=[]
            self.treeWidget_recurse(list, baseNode)
            # list contains path to current element from self.struc
            # WHILE LAST LIST ELEMENT IS NOT LEAF ADD FIRST LEAF TODO:::
            print (list)
            self.setArea(list)

            #QtGui.QKeyEvent event(KeyPress, Qt::NoModifier, QString("")
            #QMouseEvent event(QEvent.MouseButtonPress, pos, 0, 0, 0);
            modifier=QtCore.Qt.NoModifier
            text=None
            event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_Down, modifier)
            QtCore.QCoreApplication.postEvent(self.ui.treeWidget, event)
            #QtCore.QCoreApplication.postEvent(self, event)

            #self.ui.treeWidget.collapseAll()

    def treeWidget_recurse(self, list, selectedItem):
        if selectedItem is not None:
          if selectedItem.parent() is not None:
              self.treeWidget_recurse(list, selectedItem.parent())
          list.append(selectedItem.text(1))

    def loadCommentedJSON(self, filename):
        with open(filename, encoding="utf-8") as data_file:
            string = data_file.read()
            jsonStructure = json.loads(removeComments(string))
            return jsonStructure

    def saveJSON(self, struc):
        jsonQuelldatei = self.quellOrdnerSelectedFilename + ".json"
        with open(jsonQuelldatei, 'w', encoding="utf-8") as data_file:
            json.dump(struc, data_file)

    def setArea(self, list):
        cstruc = self.struc
        for name in list:
            print ("BEFORE_1")
            print (cstruc)
#           if not isinstance(cstruc[name][1], str) :
            if not isinstance(cstruc[name], str) :
                cstruc = cstruc[name][1]
                if "area_px" in cstruc:
                    break
            print("AFTER_1")
            print(cstruc)
        # if cstruc.keys() contains 'area_px':

        width = self.ui.labelBild.size().width()
        height = self.ui.labelBild.size().height()
        realwidth = self.pixmap_realsize["width"]
        realheight = self.pixmap_realsize["height"]
        print(width,height,realwidth,realheight)
        height = self.ui.labelBild.size().height()
        if self.ui.labelBild.selection.isVisible():
            posstr = ""
            if self.ui.labelBild.upper_left.x() < self.ui.labelBild.lower_right.x():
                posstr += str(round(self.ui.labelBild.upper_left.x()*realwidth/width))
                posstr += ","
                posstr += str(round(self.ui.labelBild.upper_left.y()*realheight/height))
                posstr += ","
                posstr += str(round(self.ui.labelBild.lower_right.x()*realwidth/width))
                posstr += ","
                posstr += str(round(self.ui.labelBild.lower_right.y()*realheight/height))
            else:
                posstr += str(round(self.ui.labelBild.lower_right.x()*realwidth/width))
                posstr += ","
                posstr += str(round(self.ui.labelBild.lower_right.y()*realheight/height))
                posstr += ","
                posstr += str(round(self.ui.labelBild.upper_left.x()*realwidth/width))
                posstr += ","
                posstr += str(round(self.ui.labelBild.upper_left.y()*realheight/height))
        else:
            posstr = "0,0,"
            posstr += str(width)
            posstr += ","
            posstr += str(height)
        if "area_px" in cstruc:
            if self.ui.labelBild.selection.isVisible():
                print("BEFORE_2")
                print(cstruc["area_px"])
                print("AFTER_2")
                cstruc["area_px"][0] +=  "," + posstr
                print(cstruc["area_px"])
            else:
                print("BEFORE_3")
                print(cstruc["area_px"])
                print("AFTER_3")
                cstruc["area_px"][0] +=  "," + posstr
                print(cstruc["area_px"])
            if (DIRTY_QUICK_DAVID):
                selectedTreeItems = self.ui.treeWidget.selectedItems()
                if selectedTreeItems is not None:
                    if len(selectedTreeItems) > 0:
                        selectedTreeItem = selectedTreeItems[0]
                        selectedTreeItem.setBackground(0, QtGui.QColor(128,255,128))
            else:
                self.populateTreeWidgetFromStruc() # DIRTY TODO::
            self.saveJSON(self.struc)
            print ("R")
            print (cstruc)
        else:
            cstruc[name] = [cstruc[name],{"area_px" : [posstr]}]
            if (DIRTY_QUICK_DAVID):
                selectedTreeItems = self.ui.treeWidget.selectedItems()
                if selectedTreeItems is not None:
                    if len(selectedTreeItems) > 0:
                        selectedTreeItem = selectedTreeItems[0]
                        selectedTreeItem.setBackground(0, QtGui.QColor(128,255,128))
            else:
                self.populateTreeWidgetFromStruc() # DIRTY TODO::
            self.saveJSON(self.struc)
            print ("A")
            print (cstruc)

        #else WE NEED TO ADD LEAF

            #print(self.ui.treeWidget.currentRow())
        #item = self.ui.treeWidget.item( self.ui.treeWidget.currentRow(), 0)
        #if item is None: return
        #title = item.text()
        #   print (title)
        #self.ui.lineEditFeld.setText(title)
        #pagestruc = self.struc[title][1]
        #while self.ui.tableWidgetFeld.rowCount()>1: self.ui.tableWidgetFeld.removeRow(self.ui.tableWidgetFeld.rowCount()-1)
        #for element in pagestruc:
        #    print(element)
        #    rowPosition = self.ui.tableWidgetFeld.rowCount()
        #    self.ui.tableWidgetFeld.insertRow(rowPosition)
        #    self.ui.tableWidgetFeld.setItem(rowPosition - 1, 0, QtWidgets.QTableWidgetItem(element))
        #    self.ui.tableWidgetFeld.setItem(rowPosition - 1, 1, QtWidgets.QTableWidgetItem(pagestruc[element]))

class returnKeyFilter(QtCore.QObject):
    returnKeyPressed = QtCore.pyqtSignal()
    def eventFilter(self,  obj,  event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return:
                self.returnKeyPressed.emit()
                return True
        return False

def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string



#from pprint import pprint
#pprint(data)

claptonWidget = ClaptonWidget()
claptonWidget.show()

app.exec_()

#def sayHello():
#    print ("Hello World!")

# Create a Window
#mywindow = QtWidgets.QWidget()
#mywindow.resize(1024, 768)


#button = QtWidgets.QPushButton("Click me", mywindow)
#button.clicked.connect(sayHello)

#mywindow.show()

# Enter Qt application
#app.exec_()

#sys.exit(app.exec_())
