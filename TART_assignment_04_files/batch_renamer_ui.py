# Form implementation generated from reading ui file 'batch_renamer.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 740)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 771, 381))
        self.listWidget.setObjectName("listWidget")
        self.runBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(670, 540, 113, 21))
        self.runBtn.setObjectName("runBtn")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 771, 37))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rename = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_rename.setObjectName("label_rename")
        self.horizontalLayout.addWidget(self.label_rename)
        self.filepath = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.filepath.setObjectName("filepath")
        self.horizontalLayout.addWidget(self.filepath)
        self.browseBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout.addWidget(self.browseBtn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 182, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.rename = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.rename.setObjectName("rename")
        self.horizontalLayout_2.addWidget(self.rename)
        self.copy = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.copy.setMaximumSize(QtCore.QSize(300, 20))
        self.copy.setObjectName("copy")
        self.horizontalLayout_2.addWidget(self.copy)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(240, 40, 191, 23))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_filetype = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_filetype.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_filetype.setObjectName("label_filetype")
        self.horizontalLayout_3.addWidget(self.label_filetype)
        self.filetypes = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.filetypes.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filetypes.setObjectName("filetypes")
        self.horizontalLayout_3.addWidget(self.filetypes)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(460, 40, 331, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_prefix = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_prefix.setObjectName("label_prefix")
        self.horizontalLayout_4.addWidget(self.label_prefix)
        self.prefix = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_5)
        self.prefix.setMaximumSize(QtCore.QSize(200, 16777215))
        self.prefix.setObjectName("prefix")
        self.horizontalLayout_4.addWidget(self.prefix)
        self.label_suffix = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_suffix.setObjectName("label_suffix")
        self.horizontalLayout_4.addWidget(self.label_suffix)
        self.suffix_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_5)
        self.suffix_2.setObjectName("suffix_2")
        self.horizontalLayout_4.addWidget(self.suffix_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 80, 511, 23))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.stringstofind = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.stringstofind.setMaximumSize(QtCore.QSize(230, 16777215))
        self.stringstofind.setObjectName("stringstofind")
        self.horizontalLayout_5.addWidget(self.stringstofind)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.stringstoreplace = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.stringstoreplace.setMaximumSize(QtCore.QSize(200, 16777215))
        self.stringstoreplace.setObjectName("stringstoreplace")
        self.horizontalLayout_5.addWidget(self.stringstoreplace)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 110, 771, 23))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newFolderEdit = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.newFolderEdit.setObjectName("newFolderEdit")
        self.horizontalLayout_6.addWidget(self.newFolderEdit)
        self.filepathEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_6)
        self.filepathEdit.setObjectName("filepathEdit")
        self.horizontalLayout_6.addWidget(self.filepathEdit)
        self.forceoverwrite = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.forceoverwrite.setGeometry(QtCore.QRect(670, 80, 131, 20))
        self.forceoverwrite.setObjectName("forceoverwrite")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.label_rename.setText(_translate("MainWindow", "FilePath "))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "mode"))
        self.rename.setText(_translate("MainWindow", "rename"))
        self.copy.setText(_translate("MainWindow", "copy"))
        self.label_filetype.setText(_translate("MainWindow", "Filetypes"))
        self.label_prefix.setText(_translate("MainWindow", "prefix"))
        self.label_suffix.setText(_translate("MainWindow", "suffix"))
        self.label_6.setText(_translate("MainWindow", "Strings to Find "))
        self.label_7.setText(_translate("MainWindow", "Strings to Replace"))
        self.newFolderEdit.setText(_translate("MainWindow", "New Folder (Optional)"))
        self.forceoverwrite.setText(_translate("MainWindow", "Force overwrite "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
