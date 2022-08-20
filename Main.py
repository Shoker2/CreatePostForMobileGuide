from PyQt5 import QtCore, QtWidgets
import webbrowser
import requests
import configparser

import sys
import os
import traceback
import logging
from logging.handlers import RotatingFileHandler

from FirstAdd import Ui_FA
from style import style
from Done import Ui_Done

log_file_name = 'log_records.csv'
config_path = "./config.ini"

# Создаю log файл с заголовками на первой строке, если этого файла нет
if not(os.path.exists(log_file_name)):
	with open(log_file_name, 'a+', encoding='utf-8') as f:
		f.write('timestamp,status,"text"\n')

# Настраиваю формат сохранения log файла
logging.basicConfig(handlers=[RotatingFileHandler(filename=log_file_name, encoding='utf-8', mode='a+', maxBytes=1100000, backupCount=2)],
						format=f'%(asctime)s,%(levelname)s,"%(message)s"', 
						datefmt="%F %T", 
						level=logging.DEBUG)

logging.info('Starting...')

try:
	if os.path.exists(config_path) == False:	# Проверяю наличие config файла и создаю его, если файл отсутствует
		cc = open(config_path, "w+", encoding ="utf8")
		cc.write(
			'''[general]
	url = exampleURL

	[citys]
	exampleCity = NameCity
	exampleCity2 = NameCity2'''
		)
		cc.close()

	config = configparser.ConfigParser() # Открываю config файл
	config.read(config_path, encoding ="utf8")

except Exception: # нужно, чтобы все критические ошибки сохранялись в конфиге
	logging.critical(traceback.format_exc().replace('"', '\''))

class UiFA(Ui_FA):
	def setupUi(self, main):
		try:
			logging.info('UiFA - setupUi')
			Ui_FA.setupUi(self, main)

			logging.info('SetUp style sheet')
			main.setStyleSheet(style)

			logging.info('UiFA - get citys from config')
			for key in config["citys"].keys():
				self.CityComboBox.addItem(config["citys"][key])

			self.pushButton.clicked.connect(lambda: self.Done())
			self.JsonQrButton.clicked.connect(lambda: self.GetJsonQr())
			self.OpenSiteButton.clicked.connect(lambda: self.OpenSiteQr())
		
		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

	def retranslateUi(self, main):
		try:
			logging.info('UiFA - retranslateUi')
			Ui_FA.retranslateUi(self, main)
			main.setWindowTitle("Введение данных")

		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

	def GetJsonQr(self):
		try:
			logging.info('UiFA - GetJsonQr')
			City = self.CityComboBox.currentText()
			Name = self.Title.text()

			logging.info('UiFA - get citys from config')
			for key in config["citys"].keys(): # Прохожу по списку поселений и их ключами (в конфиге)
				if config["citys"][key] == City:	# Если выбранный поселение (в выпадащем списке) совпадает с поселением в конфиге, то я беру ключ этого поселения
					City = key
					break

			json = ('{"Name":"' + Name + '","City":"' + City + '"}')

			self.JsonForQr.setText(json)
		
		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

	def OpenSiteQr(self):
		try:
			logging.info('UiFA - OpenSiteQr')
			webbrowser.open_new("http://qrcoder.ru/") # Просто открываю сайт с генератором qr кодов

		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

	def Done(self):
		try:
			logging.info('UiFA - Done')

			try:
				folder = self.folder.text()	# Тут я добавляю "/" к пути к папке, если его нет
				if folder[-1] != "/" or folder[-1] != "\\":
					folder += '/'
			except IndexError:
				pass

			City = self.CityComboBox.currentText()

			for key in config["citys"].keys(): # Прохожу по списку поселений и их ключами (в конфиге)
				if config["citys"][key] == City: # Если выбранный поселение (в выпадащем списке) совпадает с поселением в конфиге, то я беру ключ этого поселения
					City = key
					break
				
			NameMonument = self.Title.text() # Беру текст с полей
			DescriptionPost = self.Description.toPlainText()
			ImageURL = folder + self.MainImage.text()

			text = self.textEdit.toPlainText().strip()

			s = []
			k = 0
			x = 0
			one_x = True
			while True: # Тут у меня алгоритм, который ищет вставки в тексте типа "~1.png~" и разделяет текст перед этой вставкой, берёт 1.png и т.д. В итоге получится такой список [["text", "1.png"], ["", "2.png"], ["Второй текст", "3.png"]]
				t = []

				x = text.find("\n~", k+1)
				y = text.find(" ~", k+1)

				print(x, y)
				if x > y or (y > x and x == -1):
					x = y
				
				if x != -1:
					if k == 0:
						t.append(text[k:x])

						k = text.find("~", x+2)
						t.append(text[x+2:k])
					else:
						t.append(text[k+2:x])

						k = text.find("~", x+2)
						t.append(text[x+2:k])
				elif not(one_x):
					t.append(text[k+2:x])
					t.append("")
				
				else:
					t.append(text[k:x])
					t.append("")
				
				one_x = False

				s.append(t)
				if x == -1:
					break

				elif k+1 == len(text):
					break

			k = '{'
			j = -1
			try: # Тут алгоритм, которй преобразует список, который я получил ранее, в json файл типа: {"1": "text", "2": "1.png", "3":"", "4":"2.png", "5":"Второй текст", "6","3.png",
				for i in s:
					j += 1
					if i == s[-1] and s[-1][-1] == '':
						k += '"' + str(j) + '":"' + str(i[0]) + text.strip()[-1] + '", '
					else:
						k += '"' + str(j) + '":"' + str(i[0]) + '", '
					j += 1
					if str(i[1]) != "":
						k += '"' + str(j) + '":"' + folder + str(i[1]) + '", '
					else:
						k += '"' + str(j) + '":"' + str(i[1]) + '", '
			except IndexError:
				pass

			qr = folder + self.QrURL.text()
			map = self.MapURL.text()
			speech = folder + self.lineEdit.text()
			k += f'"qrcode":"{qr}", "map":"{map}", "speech":"{speech}"' # Тут я добавляю ссылку на qr код и т.д. в json и всё.
			k += '}'

			FullText = k

			try:
				Done.close()
			except:
				pass
			
			Doneui.setupUi(Done, City, NameMonument, ImageURL, DescriptionPost, FullText)
			Done.show()

		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

class UiDone(Ui_Done):
	def setupUi(self, main, City, NameMonument, ImageURL, DescriptionPost, FullText):
		try:
			logging.info('UiDone - setupUi')
			Ui_Done.setupUi(self, main)
			main.setStyleSheet(style)
			self.label_status.setText("")

			self.CityLine.setText(City)
			self.NameLine.setText(NameMonument)
			self.ImageLine.setText(ImageURL)
			self.DescBrowser.setPlainText(DescriptionPost)
			self.FullTextBrowser.setPlainText(FullText)

			self.City = City
			self.NameMonument = NameMonument
			self.ImageURL = ImageURL
			self.DescriptionPost = DescriptionPost
			self.FullText = FullText

			self.pushButton.clicked.connect(lambda: self.push())

		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

	def retranslateUi(self, main):
		try:
			logging.info('UiDone - retranslateUi')
			Ui_Done.retranslateUi(self, main)
			main.setWindowTitle("Готово")

		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))
	
	def push(self):
		try:
			logging.info('UiDone - push')
			url = config["general"]["url"]

			json = {"City": self.City, "Name":self.NameMonument, "Description":self.DescriptionPost, "ImageURL":self.ImageURL, "FullText":self.FullText}
			response = requests.post(url, json=json)

			if response.ok:
				self.label_status.setStyleSheet("color: green")
				self.label_status.setText("Успешно")
			else:
				self.label_status.setStyleSheet("color: red")
				self.label_status.setText(f"Ошибка {response.status_code}")
		
		except Exception:
			logging.critical(traceback.format_exc().replace('"', '\''))

try:
	app = QtWidgets.QApplication(sys.argv)

	FA = QtWidgets.QWidget()
	FAui = UiFA()
	FAui.setupUi(FA)

	Done = QtWidgets.QWidget()
	Doneui = UiDone()

	FA.show()

except Exception:
	logging.critical(traceback.format_exc().replace('"', '\''))
sys.exit(app.exec_())