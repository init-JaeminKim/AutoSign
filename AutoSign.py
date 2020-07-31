#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jameen/Desktop/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
#
# Created by Jaemin Kim on 7/26/20.
#
# Copyright © 2020 Jaemin Kim. All rights reserved.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import pymysql
from uuid import getnode as get_mac

class isValid(QWidget):
    def checkMacAddr(self):
        try:
            mac =  (':'.join(['{:02x}'.format((get_mac() >> ele) & 0xff)
            for ele in range(0,8*6,8)][::-1]))
            conn = pymysql.connect(host='finaltest.coochumsrn2h.ap-northeast-2.rds.amazonaws.com', port=3306, user='jkim37', password='5xFieNrS2fZJ8JZ', db='USER_DB', charset='utf8')
            curs = conn.cursor()
            sql = "select `MAC_ADDR` from ACT_USERS_TB where `MAC_ADDR` = %s and `REQ_FL` = 'ACTIVATED'"
            curs.execute(sql, (mac))
            rows = curs.fetchall()
            if curs.rowcount == 0:
                inactivated()
                exit()

        except pymysql.err.OperationalError:
            operationalErr()
            exit()
        finally:
            conn.close()
            
class inactivated(isValid):

    def __init__(self):
        super().__init__()
        self.title = 'Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.warning(self, 'Error', "사용 권한이 없습니다", QMessageBox.Ok)
        self.show()
        
class operationalErr(isValid):

    def __init__(self):
        super().__init__()
        self.title = 'Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.warning(self, 'Error', "서버와 연결할 수 없습니다", QMessageBox.Ok)
        self.show()
            
class isEmpty(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.warning(self, 'Error', "공백을 입력할 수 없습니다", QMessageBox.Ok)
        self.show()
        return
        
class bNumErr(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.warning(self, 'Error', "사업자등록번호 10자리를 입력하세요", QMessageBox.Ok)
        self.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        isValid().checkMacAddr()
        def sender(Ui_MainWindow):
            if len(self.lineEdit.text()) == 0 or len(self.lineEdit_2.text()) == 0 or len(self.lineEdit_3.text()) == 0 or len(self.lineEdit_4.text()) == 0 or len(self.lineEdit_5.text()) == 0:
                isEmpty()
            elif len(self.lineEdit_4.text()) != 10:
                bNumErr()
            else:
                cardSales.cs(self)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 410)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 311, 241))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 60, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 60, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 90, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 120, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 150, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(80, 150, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 180, 311, 61))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 250, 311, 79))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 340, 311, 16))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(sender)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoSign v1.0.0"))
        self.groupBox.setTitle(_translate("MainWindow", "Info"))
        self.label.setText(_translate("MainWindow", "대표자:"))
        self.label_2.setText(_translate("MainWindow", "생년월일:"))
        self.label_3.setText(_translate("MainWindow", "상호:"))
        self.label_4.setText(_translate("MainWindow", "사업자:"))
        self.label_5.setText(_translate("MainWindow", "계좌번호:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "국민은행"))
        self.comboBox.setItemText(1, _translate("MainWindow", "하나은행"))
        self.comboBox.setItemText(2, _translate("MainWindow", "부산은행"))
        self.comboBox.setItemText(3, _translate("MainWindow", "기업은행"))
        self.comboBox.setItemText(4, _translate("MainWindow", "농협중앙회"))
        self.comboBox.setItemText(5, _translate("MainWindow", "농협회원조합"))
        self.comboBox.setItemText(6, _translate("MainWindow", "대구은행"))
        self.comboBox.setItemText(7, _translate("MainWindow", "산업은행"))
        self.comboBox.setItemText(8, _translate("MainWindow", "새마을금고연합회"))
        self.comboBox.setItemText(9, _translate("MainWindow", "수협중앙"))
        self.comboBox.setItemText(10, _translate("MainWindow", "신한은행"))
        self.comboBox.setItemText(11, _translate("MainWindow", "신협중앙회"))
        self.comboBox.setItemText(12, _translate("MainWindow", "우리은행"))
        self.comboBox.setItemText(13, _translate("MainWindow", "한국은행"))
        self.comboBox.setItemText(14, _translate("MainWindow", "카카오뱅크"))
        self.comboBox.setItemText(15, _translate("MainWindow", "우체국"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ababab;\">Copyright © 2020 Jaemin Kim. All rights reserved.</span></p></body></html>"))
    
class cardSales:
    def cs(self):
        try:
            driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
            driver.get('https://www.cardsales.or.kr/page/member/join/joinForm');
                        
            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//a[@id='stepTab0']")))
            pAgree = driver.find_element_by_id('privacyAgreeInput').click()
            jAgree = driver.find_element_by_id('joinAgreeInput').click()
            step1 = driver.find_element_by_class_name('blue_btn').click()
            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//a[@id='stepTab1']")))
            uId = driver.find_element_by_id('loginIdInput')
            uId.send_keys("k"+self.lineEdit_4.text())
            uPwd = driver.find_element_by_id('passWdInput')
            text = open("./data/setting.txt", "r")
            lines = text.readlines()
            uPwd.send_keys(lines[3])
            uPwdC = driver.find_element_by_id('passWdCfnInput')
            uPwdC.send_keys(lines[3]) 
            uName = driver.find_element_by_id('mbrNmInput')
            uName.send_keys(lines[0])
            eMail = driver.find_element_by_id('emailInput')
            eMail.send_keys(lines[2])
            pNum = driver.find_element_by_id('mobTelNoInput')
            pNum.send_keys(lines[1])
            text.close()
            uIdC = driver.find_element_by_xpath("//dl[1]//dd[1]//button[1]").click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            authBtn = driver.find_element_by_id('authBtn').click()
            time.sleep(2)
            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//input[@id='safeKey'][contains(@value, 'MAB')]")))
            step2 = driver.find_element_by_xpath("//div[@id='stepArea1']//a[@class='blue_btn']").click()
            bNum = driver.find_element_by_id('buzNoInput')
            bNum.send_keys(self.lineEdit_4.text())
            gName = driver.find_element_by_id('merGrpNmInput')
            gName.send_keys(self.lineEdit_3.text())
            bName = driver.find_element_by_id('rsvNmInput')
            bName.send_keys(self.lineEdit.text())
            bDay = driver.find_element_by_id('rsvJuminPreInput')
            bDay.send_keys(self.lineEdit_2.text())
            card = driver.find_element_by_xpath("//option[contains(text(),'KB')]").click()
            bank = driver.find_element_by_xpath("//select[@id='bankListInput']//option[contains(text(), "+"\"%s\"" % self.comboBox.currentText()+")]").click()
            accNum = driver.find_element_by_id("stlAcctNoInput")
            accNum.send_keys(self.lineEdit_5.text())
            step3 = driver.find_element_by_xpath("//div[@id='stepArea2']//a[@class='blue_btn']").click()
            time.sleep(5)
            driver.quit()
            self.lineEdit.clear()
            self.lineEdit_2.clear_()
            self.lineEdit_3.clear_()
            self.lineEdit_4.clear_()
            self.lineEdit_5.clear_()

        except Exception as e:
            self.plainTextEdit.setPlainText(str(e))
        finally:
            driver.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

