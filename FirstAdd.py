# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Админ/Desktop/Post/ui/FirstAdd.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FA(object):
    def setupUi(self, FA):
        FA.setObjectName("FA")
        FA.resize(1109, 760)
        self.CityComboBox = QtWidgets.QComboBox(FA)
        self.CityComboBox.setGeometry(QtCore.QRect(20, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CityComboBox.setFont(font)
        self.CityComboBox.setObjectName("CityComboBox")
        self.Title = QtWidgets.QLineEdit(FA)
        self.Title.setGeometry(QtCore.QRect(20, 80, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.label = QtWidgets.QLabel(FA)
        self.label.setGeometry(QtCore.QRect(20, 20, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FA)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.folder = QtWidgets.QLineEdit(FA)
        self.folder.setGeometry(QtCore.QRect(210, 169, 361, 31))
        self.folder.setObjectName("folder")
        self.label_3 = QtWidgets.QLabel(FA)
        self.label_3.setGeometry(QtCore.QRect(210, 130, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FA)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FA)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.MainImage = QtWidgets.QLineEdit(FA)
        self.MainImage.setGeometry(QtCore.QRect(10, 260, 561, 31))
        self.MainImage.setObjectName("MainImage")
        self.JsonForQr = QtWidgets.QLineEdit(FA)
        self.JsonForQr.setGeometry(QtCore.QRect(20, 530, 411, 31))
        self.JsonForQr.setObjectName("JsonForQr")
        self.Description = QtWidgets.QTextEdit(FA)
        self.Description.setGeometry(QtCore.QRect(13, 360, 561, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Description.setFont(font)
        self.Description.setObjectName("Description")
        self.JsonQrButton = QtWidgets.QPushButton(FA)
        self.JsonQrButton.setGeometry(QtCore.QRect(450, 520, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.JsonQrButton.setFont(font)
        self.JsonQrButton.setObjectName("JsonQrButton")
        self.label_6 = QtWidgets.QLabel(FA)
        self.label_6.setGeometry(QtCore.QRect(20, 490, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.QrURL = QtWidgets.QLineEdit(FA)
        self.QrURL.setGeometry(QtCore.QRect(20, 610, 561, 31))
        self.QrURL.setObjectName("QrURL")
        self.OpenSiteButton = QtWidgets.QPushButton(FA)
        self.OpenSiteButton.setGeometry(QtCore.QRect(450, 560, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OpenSiteButton.setFont(font)
        self.OpenSiteButton.setObjectName("OpenSiteButton")
        self.label_7 = QtWidgets.QLabel(FA)
        self.label_7.setGeometry(QtCore.QRect(20, 570, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.MapURL = QtWidgets.QLineEdit(FA)
        self.MapURL.setGeometry(QtCore.QRect(20, 690, 561, 31))
        self.MapURL.setObjectName("MapURL")
        self.label_8 = QtWidgets.QLabel(FA)
        self.label_8.setGeometry(QtCore.QRect(20, 650, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(FA)
        self.label_9.setGeometry(QtCore.QRect(600, 410, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(FA)
        self.textEdit.setGeometry(QtCore.QRect(600, 80, 491, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(FA)
        self.pushButton.setGeometry(QtCore.QRect(920, 710, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(FA)
        self.label_10.setGeometry(QtCore.QRect(600, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(FA)
        self.lineEdit.setGeometry(QtCore.QRect(600, 450, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(FA)
        QtCore.QMetaObject.connectSlotsByName(FA)

    def retranslateUi(self, FA):
        _translate = QtCore.QCoreApplication.translate
        FA.setWindowTitle(_translate("FA", "Form"))
        self.label.setText(_translate("FA", "Заголовок"))
        self.label_2.setText(_translate("FA", "Поселение"))
        self.label_3.setText(_translate("FA", "Ссылка на папку"))
        self.label_4.setText(_translate("FA", "Описание"))
        self.label_5.setText(_translate("FA", "Ссылка на главное изображение"))
        self.Description.setHtml(_translate("FA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.JsonQrButton.setText(_translate("FA", "Сгенерировать текст"))
        self.label_6.setText(_translate("FA", "QR код"))
        self.OpenSiteButton.setText(_translate("FA", "генератор"))
        self.label_7.setText(_translate("FA", "Ссылка на QR код"))
        self.label_8.setText(_translate("FA", "Ссылка на Google maps"))
        self.label_9.setText(_translate("FA", "Ссылка на озвучку"))
        self.textEdit.setToolTip(_translate("FA", "<html><head/><body><p>Это текст полновй версии поста.</p><p>Введите ~Название изображения.png~</p><p>с новой строки или через пробел,</p><p>чтобы вставить изображение в это место</p></body></html>"))
        self.textEdit.setWhatsThis(_translate("FA", "<html><head/><body><p><br/></p></body></html>"))
        self.textEdit.setHtml(_translate("FA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("FA", "Получить данные"))
        self.label_10.setText(_translate("FA", "Полный пост"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FA = QtWidgets.QWidget()
    ui = Ui_FA()
    ui.setupUi(FA)
    FA.show()
    sys.exit(app.exec_())
