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
        Dialog.resize(540, 250)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(12, 30, 211, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 181, 20))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setTabletTracking(True)
        self.textEdit.setObjectName("textEdit")
        self.labelError = QtWidgets.QLabel(Dialog)
        self.labelError.setGeometry(QtCore.QRect(40, 30, 16, 16))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 321, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 60, 311, 20))
        self.textEdit_2.setMouseTracking(True)
        self.textEdit_2.setTabletTracking(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 100, 208, 100))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.CheckBoxFollowers = QtWidgets.QCheckBox(self.splitter)
        self.CheckBoxFollowers.setObjectName("CheckBoxFollowers")
        self.checkBoxDownload = QtWidgets.QCheckBox(self.splitter)
        self.checkBoxDownload.setObjectName("checkBoxDownload")
        self.checkBoxUrl = QtWidgets.QCheckBox(self.splitter)
        self.checkBoxUrl.setObjectName("checkBoxUrl")
        self.checkBoxTime = QtWidgets.QCheckBox(self.splitter)
        self.checkBoxTime.setObjectName("checkBoxTime")
        self.checkBoxDataSet = QtWidgets.QCheckBox(self.splitter)
        self.checkBoxDataSet.setObjectName("checkBoxDataSet")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(230, 100, 149, 72))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.DataSetButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.DataSetButton_2.setObjectName("DataSetButton_2")
        self.CommentBox = QtWidgets.QCheckBox(self.splitter_2)
        self.CommentBox.setObjectName("CommentBox")
        self.TagBox = QtWidgets.QCheckBox(self.splitter_2)
        self.TagBox.setObjectName("TagBox")
        self.CheckBoxFollowers_2 = QtWidgets.QCheckBox(Dialog)
        self.CheckBoxFollowers_2.setGeometry(QtCore.QRect(10, 210, 208, 14))
        self.CheckBoxFollowers_2.setObjectName("CheckBoxFollowers_2")
        self.TagBox_2 = QtWidgets.QCheckBox(Dialog)
        self.TagBox_2.setGeometry(QtCore.QRect(230, 180, 149, 19))
        self.TagBox_2.setObjectName("TagBox_2")
        self.TagBox_3 = QtWidgets.QCheckBox(Dialog)
        self.TagBox_3.setGeometry(QtCore.QRect(230, 210, 149, 19))
        self.TagBox_3.setObjectName("TagBox_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parse from Instagram"))
        self.label.setText(_translate("Dialog", "Введите логин пользователя       "))
        self.label_2.setText(_translate("Dialog", "Введите адрес файла с логинами пользователей"))
        self.CheckBoxFollowers.setText(_translate("Dialog", "Cписок Подписчиков"))
        self.checkBoxDownload.setText(_translate("Dialog", "скачать контент"))
        self.checkBoxUrl.setText(_translate("Dialog", "ссылки на посты "))
        self.checkBoxTime.setText(_translate("Dialog", "Время публикаций"))
        self.checkBoxDataSet.setText(_translate("Dialog", "Cобрать датасет по друзьям"))
        self.DataSetButton_2.setText(_translate("Dialog", "Cобрать датасет"))
        self.CommentBox.setText(_translate("Dialog", "комментарии"))
        self.TagBox.setText(_translate("Dialog", "хэштеги"))
        self.CheckBoxFollowers_2.setText(_translate("Dialog", "Cписок подписок"))
        self.TagBox_2.setText(_translate("Dialog", "Локации постов"))
        self.TagBox_3.setText(_translate("Dialog", "Формат постов"))



