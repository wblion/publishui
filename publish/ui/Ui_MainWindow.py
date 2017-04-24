#!/usr/bin/python
#-*- coding=utf-8 -*-
# Author: wangbin
import sys
sys.path.append("D:\work\Qt")
from Qt.QtWidgets import *
from Qt.QtGui import *

#from PyQt4. QtGui import *
#from ui_TileWidget import ui_TileWidget
import ui_publishTree
reload(ui_publishTree)
# from ui_publishTree import ui_publishTree
# from ui_BoderWidget import ui_BoderWidget
# try:
#     _fromUtf8 =QString.fromUtf8
# except AttributeError:
#     _fromUtf8 = lambda s: s
class Ui_MainWindow(object):
    '''
    建立总体大的结构，竖向三个Widget
    '''
    
        
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        #mainWindow.resize(1000,10000)#设置实例化出来的QMainWindow()
        self.progressBar=QProgressBar()#建立滚动条
        centralwidget = QWidget(mainWindow)#建立一个QWidget要作为中心控件
        
        mainWindow.setCentralWidget(centralwidget)#建立QMainWindow()中心控件
        centralwidget.setObjectName("centralwidget")

        QWidgetvboxLayout = QVBoxLayout(centralwidget)#建立竖向的layout
        
       # self.TileWidget=ui_TileWidget()#上部标题Widget
        self.publishTree=ui_publishTree()#中部工作区Widget
        #self.BodeWidget=ui_BoderWidget()#下部边缘Widget
        
        #QWidgetvboxLayout.addWidget(self.TileWidget)
        QWidgetvboxLayout.addWidget(self.publishTree)
        #QWidgetvboxLayout.addWidget(self.progressBar)
        #QWidgetvboxLayout.addWidget(self.BodeWidget)
        
        #QWidgetvboxLayout.addWidget(TextWidget)
        QWidgetvboxLayout.setContentsMargins(0, 0, 0, 0)#mainVboxLayout
        
        #mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())