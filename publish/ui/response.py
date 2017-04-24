#!/usr/bin/python
#-*- coding=utf-8 -*-
import os
import sys
#sys.path.append(r"F:\work\lib")
sys.path.append(r"E:\text\lib")
sys.path.append(r"\\bjserver2\plugin\lib\SysPyQt")

from CustomLibs.SysLib.FileInformation import FileInformation
from Qt.QtWidgets import *
from Qt.QtGui import *
import Ui_MainWindow
reload(Ui_MainWindow)
from Ui_MainWindow import Ui_MainWindow
import pulisListsWidgetresponse
from pulisListsWidgetresponse import pulisListsWidgetresponse
#from Config import Config
try:
    _fromUtf8 =QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Response(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        #super(Response,self).__init__(parent)
        #mainwindow = QMainWindow(parent)
        #self.setupUi(mainwindow)
        #mainwindow.show()
        
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(_fromUtf8("发布工具"))
        #self.setTi("mayaplayblastWin")
        #self.mayaplayblastinstance=mayaplayblast()
        self.setupUi(self)
        self.getElems()
        self.setDefault()
        self.setupConnections()
        #self.setDefault()
    def getElems(self):
	#滚动条
	self.progressBarBel=self.progressBar
        #竖向第一个widget
        self.tilePathLabelbel=self.TileWidget.tilelaber#第一个Widget中的label
        #竖向第二个widget
        self.Treewidgetbel=self.publishTree.ui_publishTree#Treewidge
      
        #竖向第三个widget
        self.publishButtonbel=self.BodeWidget.publishQPushButton#发布的按钮
        
        
        #Tree的右键菜单
	self.RightTreewidgetbel=self.publishTree.ui_publishTree.deleteaction#右键删除菜单
	
        #增加tree的item
        self.addTreeitembel=self.publishTree.SetTreeStyle
    def setDefault(self):
	self.progressBarBel.hide()
        pass

    def setupConnections(self):
        QObject.connect(self.Treewidgetbel,SIGNAL('getdropfilepath'), self.on_Treewidgetbel_drop)
        QObject.connect(self.publishButtonbel,SIGNAL('clicked()'), self.on_publishButtonbel_clicked)
	    QObject.connect(self.RightTreewidgetbel,SIGNAL('triggered()'), self.on_RightTreewidgetbel_triggered)
        
    def on_Treewidgetbel_drop(self,*args):
        for pathlist in args[0]:
	    try:
		ids=False
		fileformat,filebodyName,ProjectName,MatchesName,shotNumber,Stagename,versionName=FileInformation.AnalysisElementsFromFileName(pathlist)
		ids=True
	    except Exception, e:
		print e
	    if ids:
		if not fileformat:
		    fileformat=".sequence"
		filepathlists,TreeItemlists=pulisListsWidgetresponse.getTreeItem(self.Treewidgetbel)
		if pathlist not in filepathlists:
		    self.addTreeitembel(pathlist, ProjectName, MatchesName, 
			               shotNumber, 
			               Stagename, 
			               versionName,fileformat)
		#if not self.PulishlistWidget.findItems(pathlist,Qt.MatchFlags()):
		#    self.PulishlistWidget.addItem(pathlist)
		
    def on_RightTreewidgetbel_triggered(self):
	SelectItems=self.Treewidgetbel.selectedItems()
	for SelectItem in SelectItems:
	    itemIndexNumber=self.Treewidgetbel.indexOfTopLevelItem(SelectItem)
	    self.Treewidgetbel.takeTopLevelItem(itemIndexNumber)
	    
    def on_publishButtonbel_clicked(self):
        filepathlists,TreeItemlists=pulisListsWidgetresponse.getTreeItem(self.Treewidgetbel)
	self.progressBarBel.setValue(0)
	self.progressBarBel.show()
	self.progressBarBel.setMinimum(0)    
	self.progressBarBel.setMaximum(len(TreeItemlists)-1)	
	for TreeItem,index in TreeItemlists:
	    #print TreeItem.fileformatbel.text()
	    if pulisListsWidgetresponse.publishFile(self,TreeItem):
		itemIndexNumber=self.Treewidgetbel.indexOfTopLevelItem(TreeItem)
		self.Treewidgetbel.takeTopLevelItem(itemIndexNumber)
	    self.progressBarBel.setValue(index)
	QThread.msleep(1200)
	self.progressBarBel.hide()
        #print self.Treewidgetbel.topLevelItemCount()
        #items=self.Treewidgetbel.topLevelItem(1)
        #print items.FilepathLabel.text()
        #print self.Treewidgetbel.cellWidget(row, column)
        #print items.data(0,0)
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    #app.setStyle('windows')
    app.setStyleSheet('QMainWindow{border:1px solid rgb(45,45,45); background:rgb(45,45,45);}\
                    QMessageBox{background:rgb(45,45,45);}\
                    QLabel{color:rgb(200, 200, 200)}    \
                    QPushButton{background:rgb(90, 0, 0);color:rgb(100, 100, 100); width:49px; height:30px} \
                    QComboBox{border:3px solid rgb(45, 45, 45);background:rgb(50, 50, 50); color:rgb(180,180,180)}\
                    QListWidget{border:1px solid rgb(45,45,45); background:transparent}\
                    #QTreeWidget{border:1px solid rgb(30,30,30); background:transparent}\
                    QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
                    #QTreeWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(0,0,0); padding:15px} \
                    QListWidget::item{border:3px solid rgb(45, 45, 45); background:rgb(50, 50, 50); color:rgb(180,180,180); padding:15px}  \
                    QListWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(45,45,45); padding:15px} \
                    QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
                    QListView::item:selected:active{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:12px} \
                    QScrollBar:vertical {border: 2px solid rgb(80, 80, 80);background:rgb(50, 50, 50); width:20px; margin: 22px 0 22px 0;} \
                    QScrollBar::handle:vertical {background:rgb(95, 95, 95); min-height: 20px;}\
                    QScrollBar::add-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
                                                    subcontrol-position: bottom;subcontrol-origin: margin;}\
                    QScrollBar::sub-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
                                                    subcontrol-position: top;subcontrol-origin: margin;}\
                    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {border: 1px solid rgb(80, 80, 80); \
                                                    width:4px; height:4px; background:rgb(50, 50, 50);}\
                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}\
                    ')
    #mainWindow = QMainWindow()
    #mainWindow.setWindowTitle("Swapte")
    ui = Response()
    #ui.setupUi(mainWindow)
    #mainWindow.show()
    ui.show()
    sys.exit(app.exec_())