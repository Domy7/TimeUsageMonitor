# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guivBFqzY.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(771, 573)
        MainWindow.setStyleSheet(u"border: none")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.header_left_fr = QFrame(self.header_frame)
        self.header_left_fr.setObjectName(u"header_left_fr")
        self.header_left_fr.setFrameShape(QFrame.StyledPanel)
        self.header_left_fr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_fr)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_left_fr)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u"./icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_fr)

        self.header_center_fr = QFrame(self.header_frame)
        self.header_center_fr.setObjectName(u"header_center_fr")
        self.header_center_fr.setFrameShape(QFrame.StyledPanel)
        self.header_center_fr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_fr)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center_fr)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_center_fr)

        self.header_right_fr = QFrame(self.header_frame)
        self.header_right_fr.setObjectName(u"header_right_fr")
        self.header_right_fr.setFrameShape(QFrame.StyledPanel)
        self.header_right_fr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_fr)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.header_right_fr)
        self.minimize_button.setObjectName(u"minimize_button")
        icon1 = QIcon()
        icon1.addFile(u"./icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.resize_button = QPushButton(self.header_right_fr)
        self.resize_button.setObjectName(u"resize_button")
        icon2 = QIcon()
        icon2.addFile(u"./icons/icons/restore_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.resize_button)

        self.exit_button = QPushButton(self.header_right_fr)
        self.exit_button.setObjectName(u"exit_button")
        icon3 = QIcon()
        icon3.addFile(u"./icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.exit_button)


        self.horizontalLayout.addWidget(self.header_right_fr, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.center_frame = QFrame(self.centralwidget)
        self.center_frame.setObjectName(u"center_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_frame.sizePolicy().hasHeightForWidth())
        self.center_frame.setSizePolicy(sizePolicy)
        self.center_frame.setFrameShape(QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.center_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.left_menu_fr = QFrame(self.center_frame)
        self.left_menu_fr.setObjectName(u"left_menu_fr")
        self.left_menu_fr.setFrameShape(QFrame.StyledPanel)
        self.left_menu_fr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_fr)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.menu_fr = QFrame(self.left_menu_fr)
        self.menu_fr.setObjectName(u"menu_fr")
        self.menu_fr.setFrameShape(QFrame.StyledPanel)
        self.menu_fr.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_fr)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings_btn = QPushButton(self.menu_fr)
        self.settings_btn.setObjectName(u"settings_btn")
        icon4 = QIcon()
        icon4.addFile(u"./icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.settings_btn, 2, 0, 1, 1)

        self.stats_btn = QPushButton(self.menu_fr)
        self.stats_btn.setObjectName(u"stats_btn")
        icon5 = QIcon()
        icon5.addFile(u"./icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stats_btn.setIcon(icon5)
        self.stats_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.stats_btn, 0, 0, 1, 1)

        self.label_4 = QLabel(self.menu_fr)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.menu_fr)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.lock_btn = QPushButton(self.menu_fr)
        self.lock_btn.setObjectName(u"lock_btn")
        icon6 = QIcon()
        icon6.addFile(u"./icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lock_btn.setIcon(icon6)
        self.lock_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.lock_btn, 1, 0, 1, 1)

        self.label_5 = QLabel(self.menu_fr)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.menu_fr)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon7 = QIcon()
        icon7.addFile(u"./icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.label_6 = QLabel(self.menu_fr)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.menu_fr, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_fr, 0, Qt.AlignLeft)

        self.main_frame = QFrame(self.center_frame)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stats_page = QWidget()
        self.stats_page.setObjectName(u"stats_page")
        self.stackedWidget.addWidget(self.stats_page)
        self.lock_page = QWidget()
        self.lock_page.setObjectName(u"lock_page")
        self.stackedWidget.addWidget(self.lock_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_frame)

        self.right_center_fr = QFrame(self.center_frame)
        self.right_center_fr.setObjectName(u"right_center_fr")
        self.right_center_fr.setFrameShape(QFrame.StyledPanel)
        self.right_center_fr.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_center_fr)


        self.verticalLayout.addWidget(self.center_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.footer_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.footer_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TimeUsageMonitor", None))
        self.minimize_button.setText("")
        self.resize_button.setText("")
        self.exit_button.setText("")
        self.settings_btn.setText("")
        self.stats_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Limits", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.lock_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Raw Data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright PI grupa x ltd.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

