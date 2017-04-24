#!/usr/bin/python
#-*- coding=utf-8 -*-
import sys
sys.path.append("D:\work\Qt")
import Qt
import re
#from Qt import 
from Qt.QtWidgets import *
from Qt.QtGui import *


class ui_publishTree(QWidget):#总框架的第一行widget(tile wideget)
    def __init__(self,parent=None):
        super(ui_publishTree,self).__init__(parent)
        self.setupUI()
        #self.getElems()
        #self.setupConnections()
    def setupUI(self):
        self.TileWidgetHboxlayout=QHBoxLayout(self)
        
        #self.grouop=QButtonGroup()
        
        self.ui_publishTree= CouTreewidget(self)
        #self.ui_publishTree.setDragDropMode(arg0)
        self.ui_publishTree.setAcceptDrops(True)
        self.ui_publishTree.headerItem().setText(0,"文件路径")
        self.ui_publishTree.headerItem().setText(1,"项目名字")
        self.ui_publishTree.headerItem().setText(2,"场次号")
        self.ui_publishTree.headerItem().setText(3,"镜头号")
        self.ui_publishTree.headerItem().setText(4,"阶段名字")
        self.ui_publishTree.headerItem().setText(5,"版本号")
        #filepath="E:/ddf/bb.jpg"
        #projectName="XYJ"
        #matchName="Sc07"
        #shotNumberName="070"
        #stageName="LGT"
        #versionName="V003"
        #self.SetTreeStyle(filepath, projectName, matchName, shotNumberName, 
                         #stageName, versionName)
        self.TileWidgetHboxlayout.addWidget(self.ui_publishTree)
    def getElems(self):
        self.ui_publishTreebel=self.ui_publishTree
    def setupConnections(self):
        QObject.connect(self.ui_publishTreebel, SIGNAL('getdropfilepath'), self.ui_publishTreebel_drop)
    def ui_publishTreebel_drop(self,*args):
        for pathlist in args[0]:
            print pathlist
            #if not self.PulishlistWidget.findItems(pathlist,Qt.MatchFlags()):
            #    self.PulishlistWidget.addItem(pathlist)        
    def SetTreeStyle(self,filepath,projectName,matchName,shotNumberName,stageName,versionName,fileformat):
        TreeWidget=self.ui_publishTree
        self.TreeWidgetItem=QTreeWidgetItem(TreeWidget)
        self.TreeWidgetItem.fileformatbel=QLabel(fileformat)#文件后缀
        ItemNumber=TreeWidget.topLevelItemCount()-1
        self.TreeWidgetItem.FilepathLabel=QLabel(filepath)#文件路径
        self.TreeWidgetItem.projectNameLabel=QLabel(projectName)#项目名字
        self.TreeWidgetItem.matchNameLabel=QLabel(matchName)#场次名字
        self.TreeWidgetItem.shotNumberNameLabel=QLabel(shotNumberName)#镜头名字
        self.TreeWidgetItem.stageNameLabel=QLabel(stageName)#阶段名字
        self.TreeWidgetItem.versionNameLabel=QLabel(versionName)#版本号
        
        
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),0,self.TreeWidgetItem.FilepathLabel)
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),1,self.TreeWidgetItem.projectNameLabel)
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),2,self.TreeWidgetItem.matchNameLabel)
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),3,self.TreeWidgetItem.shotNumberNameLabel)
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),4,self.TreeWidgetItem.stageNameLabel)
        TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),5,self.TreeWidgetItem.versionNameLabel)
#class CoyTreeWidgetItem(QTreeWidgetItem):
    #ItemNumber=TreeWidget.topLevelItemCount()-1
    #self.FilepathLabel=QLabel(filepath)#文件路径
    #self.projectNameLabel=QLabel(projectName)#项目名字
    #self.matchNameLabel=QLabel(matchName)#场次名字
    #self.shotNumberNameLabel=QLabel(shotNumberName)#镜头名字
    #self.stageNameLabel=QLabel(stageName)#阶段名字
    #self.versionNameLabel=QLabel(versionName)#版本号
   
   
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),0,self.FilepathLabel)
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),1,self.projectNameLabel)
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),2,self.matchNameLabel)
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),3,self.shotNumberNameLabel)
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),4,self.stageNameLabel)
    #TreeWidget.setItemWidget(TreeWidget.topLevelItem(ItemNumber),5,self.versionNameLabel)    
   
   
class CouTreewidget(QTreeWidget):
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)#
        self.contextMenu = QMenu(self)
        self.deleteaction = QAction(u"删除文件",self)
        self.contextMenu.addAction(self.deleteaction)
    def contextMenuEvent(self, event):
        self.contextMenu.exec_(event.globalPos())
    def dragMoveEvent(self, event):
        event.acceptProposedAction()
    def dragEnterEvent(self, event):
        event.acceptProposedAction()#这里很关键允许外外界的文件拖拽进入。
    def dropEvent(self, event):
        print "cc"
        R=r"^/?(.*)"
        RfindPath=re.compile(R)
        mimeData = event.mimeData()
        pathlists=[RfindPath.findall(url.path().__str__())[0] for url in mimeData.urls() if RfindPath.findall(url.path().__str__()) ]
        #print pathlists
        self.emit(SIGNAL("getdropfilepath"), pathlists)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ui_publishTree()
    ui.show()
    sys.exit(app.exec_())