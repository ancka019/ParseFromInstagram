# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/anna/input_path/DataSet.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 250)
        self.Followersbutton = QtWidgets.QPushButton(Dialog)
        self.Followersbutton.setGeometry(QtCore.QRect(0, 100, 171, 32))
        self.Followersbutton.setObjectName("Followersbutton")
        self.DownloadButton = QtWidgets.QPushButton(Dialog)
        self.DownloadButton.setGeometry(QtCore.QRect(0, 130, 171, 32))
        self.DownloadButton.setObjectName("DownloadButton")
        self.PostsButton = QtWidgets.QPushButton(Dialog)
        self.PostsButton.setGeometry(QtCore.QRect(0, 160, 171, 32))
        self.PostsButton.setObjectName("PostsButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 211, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 161, 20))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setTabletTracking(True)
        self.textEdit.setObjectName("textEdit")
        self.TimeButton = QtWidgets.QPushButton(Dialog)
        self.TimeButton.setGeometry(QtCore.QRect(0, 190, 171, 32))
        self.TimeButton.setObjectName("TimeButton")
        self.DataSetButton = QtWidgets.QPushButton(Dialog)
        self.DataSetButton.setGeometry(QtCore.QRect(0, 220, 171, 32))
        self.DataSetButton.setObjectName("DataSetButton")
        self.labelError = QtWidgets.QLabel(Dialog)
        self.labelError.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.CheckBoxFollowers = QtWidgets.QCheckBox(Dialog)
        self.CheckBoxFollowers.setGeometry(QtCore.QRect(180, 100, 171, 20))
        self.CheckBoxFollowers.setObjectName("CheckBoxFollowers")
        self.checkBoxDownload = QtWidgets.QCheckBox(Dialog)
        self.checkBoxDownload.setGeometry(QtCore.QRect(180, 120, 151, 31))
        self.checkBoxDownload.setObjectName("checkBoxDownload")
        self.checkBoxUrl = QtWidgets.QCheckBox(Dialog)
        self.checkBoxUrl.setGeometry(QtCore.QRect(180, 150, 161, 31))
        self.checkBoxUrl.setObjectName("checkBoxUrl")
        self.checkBoxTime = QtWidgets.QCheckBox(Dialog)
        self.checkBoxTime.setGeometry(QtCore.QRect(180, 180, 151, 20))
        self.checkBoxTime.setObjectName("checkBoxTime")
        self.checkBoxDataSet = QtWidgets.QCheckBox(Dialog)
        self.checkBoxDataSet.setGeometry(QtCore.QRect(180, 210, 151, 20))
        self.checkBoxDataSet.setObjectName("checkBoxDataSet")
        self.DataSetButton_2 = QtWidgets.QPushButton(Dialog)
        self.DataSetButton_2.setGeometry(QtCore.QRect(180, 70, 171, 32))
        self.DataSetButton_2.setObjectName("DataSetButton_2")
        self.DownloadButton.raise_()
        self.Followersbutton.raise_()
        self.PostsButton.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.TimeButton.raise_()
        self.DataSetButton.raise_()
        self.labelError.raise_()
        self.CheckBoxFollowers.raise_()
        self.checkBoxDownload.raise_()
        self.checkBoxUrl.raise_()
        self.checkBoxTime.raise_()
        self.checkBoxDataSet.raise_()
        self.DataSetButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parse from Instagram"))
        self.Followersbutton.setText(_translate("Dialog", "список подписчиков"))
        self.DownloadButton.setText(_translate("Dialog", "скачать контент"))
        self.PostsButton.setText(_translate("Dialog", "ссылки на посты "))
        self.label.setText(_translate("Dialog", "Введите login пользователя"))
        self.TimeButton.setText(_translate("Dialog", "Время публикаций"))
        self.DataSetButton.setText(_translate("Dialog", "Cобрать датасет"))
        self.CheckBoxFollowers.setText(_translate("Dialog", "Cписок Подписчиков"))
        self.checkBoxDownload.setText(_translate("Dialog", "скачать контент"))
        self.checkBoxUrl.setText(_translate("Dialog", "ссылки на посты "))
        self.checkBoxTime.setText(_translate("Dialog", "Время публикаций"))
        self.checkBoxDataSet.setText(_translate("Dialog", "Cобрать датасет"))
        self.DataSetButton_2.setText(_translate("Dialog", "Cобрать датасет"))