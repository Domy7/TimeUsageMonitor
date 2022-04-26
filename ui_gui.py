# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 727)
        MainWindow.setStyleSheet("border: none")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setStyleSheet(":pressed {\n"
"    background-color: rgb(172, 226, 255)\n"
"}")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_left_fr = QtWidgets.QFrame(self.header_frame)
        self.header_left_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_left_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_left_fr.setObjectName("header_left_fr")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_left_fr)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_btn = QtWidgets.QPushButton(self.header_left_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menu_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(32, 32))
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_4.addWidget(self.menu_btn, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.header_left_fr)
        self.header_center_fr = QtWidgets.QFrame(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_center_fr.sizePolicy().hasHeightForWidth())
        self.header_center_fr.setSizePolicy(sizePolicy)
        self.header_center_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_center_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_center_fr.setObjectName("header_center_fr")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_center_fr)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_title_lbl = QtWidgets.QLabel(self.header_center_fr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_title_lbl.sizePolicy().hasHeightForWidth())
        self.main_title_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_lbl.setFont(font)
        self.main_title_lbl.setObjectName("main_title_lbl")
        self.horizontalLayout_3.addWidget(self.main_title_lbl)
        self.horizontalLayout.addWidget(self.header_center_fr)
        self.header_right_fr = QtWidgets.QFrame(self.header_frame)
        self.header_right_fr.setStyleSheet("")
        self.header_right_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_fr.setObjectName("header_right_fr")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_right_fr)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize_button = QtWidgets.QPushButton(self.header_right_fr)
        self.minimize_button.setStyleSheet(":hover {\n"
"    background-color: rgb(48, 158, 255)\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: rgb(146, 188, 255)\n"
"}")
        self.minimize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setIconSize(QtCore.QSize(32, 16))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.resize_button = QtWidgets.QPushButton(self.header_right_fr)
        self.resize_button.setStyleSheet(":hover {\n"
"    background-color: rgb(48, 158, 255)\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: rgb(146, 188, 255)\n"
"}")
        self.resize_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.resize_button.setIcon(icon2)
        self.resize_button.setIconSize(QtCore.QSize(32, 16))
        self.resize_button.setObjectName("resize_button")
        self.horizontalLayout_2.addWidget(self.resize_button)
        self.exit_button = QtWidgets.QPushButton(self.header_right_fr)
        self.exit_button.setStyleSheet(":hover {\n"
"    background-color: rgb(255, 28, 77)\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: rgb(255, 179, 180);\n"
"}")
        self.exit_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon3)
        self.exit_button.setIconSize(QtCore.QSize(32, 16))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_2.addWidget(self.exit_button)
        self.horizontalLayout.addWidget(self.header_right_fr, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_frame.sizePolicy().hasHeightForWidth())
        self.center_frame.setSizePolicy(sizePolicy)
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.center_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.left_menu_fr = QtWidgets.QFrame(self.center_frame)
        self.left_menu_fr.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_menu_fr.setStyleSheet(":pressed {\n"
"    background-color: rgb(172, 226, 255)\n"
"}")
        self.left_menu_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_fr.setObjectName("left_menu_fr")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.left_menu_fr)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menu_fr = QtWidgets.QFrame(self.left_menu_fr)
        self.menu_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_fr.setObjectName("menu_fr")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_fr)
        self.gridLayout.setObjectName("gridLayout")
        self.settings_btn = QtWidgets.QPushButton(self.menu_fr)
        self.settings_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QtCore.QSize(32, 32))
        self.settings_btn.setObjectName("settings_btn")
        self.gridLayout.addWidget(self.settings_btn, 2, 0, 1, 1)
        self.data_btn = QtWidgets.QPushButton(self.menu_fr)
        self.data_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.data_btn.setIcon(icon5)
        self.data_btn.setIconSize(QtCore.QSize(32, 32))
        self.data_btn.setObjectName("data_btn")
        self.gridLayout.addWidget(self.data_btn, 3, 0, 1, 1)
        self.settings_lbl = QtWidgets.QLabel(self.menu_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings_lbl.setFont(font)
        self.settings_lbl.setObjectName("settings_lbl")
        self.gridLayout.addWidget(self.settings_lbl, 2, 1, 1, 1)
        self.stats_btn = QtWidgets.QPushButton(self.menu_fr)
        self.stats_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stats_btn.setIcon(icon6)
        self.stats_btn.setIconSize(QtCore.QSize(32, 32))
        self.stats_btn.setObjectName("stats_btn")
        self.gridLayout.addWidget(self.stats_btn, 0, 0, 1, 1)
        self.lock_lbl = QtWidgets.QLabel(self.menu_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lock_lbl.setFont(font)
        self.lock_lbl.setObjectName("lock_lbl")
        self.gridLayout.addWidget(self.lock_lbl, 1, 1, 1, 1)
        self.stats_lbl = QtWidgets.QLabel(self.menu_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stats_lbl.setFont(font)
        self.stats_lbl.setObjectName("stats_lbl")
        self.gridLayout.addWidget(self.stats_lbl, 0, 1, 1, 1)
        self.data_lbl = QtWidgets.QLabel(self.menu_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_lbl.setFont(font)
        self.data_lbl.setObjectName("data_lbl")
        self.gridLayout.addWidget(self.data_lbl, 3, 1, 1, 1)
        self.lock_btn = QtWidgets.QPushButton(self.menu_fr)
        self.lock_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/key.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lock_btn.setIcon(icon7)
        self.lock_btn.setIconSize(QtCore.QSize(32, 32))
        self.lock_btn.setObjectName("lock_btn")
        self.gridLayout.addWidget(self.lock_btn, 1, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.menu_fr, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_8.addWidget(self.left_menu_fr, 0, QtCore.Qt.AlignLeft)
        self.main_frame = QtWidgets.QFrame(self.center_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.centralWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.centralWidget.setObjectName("centralWidget")
        self.stats_page = QtWidgets.QWidget()
        self.stats_page.setObjectName("stats_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.stats_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stats_title_fr = QtWidgets.QFrame(self.stats_page)
        self.stats_title_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_title_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_title_fr.setObjectName("stats_title_fr")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.stats_title_fr)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.stats_title_lbl = QtWidgets.QLabel(self.stats_title_fr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_title_lbl.sizePolicy().hasHeightForWidth())
        self.stats_title_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stats_title_lbl.setFont(font)
        self.stats_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.stats_title_lbl.setObjectName("stats_title_lbl")
        self.horizontalLayout_10.addWidget(self.stats_title_lbl)
        self.refresh_chart_btn = QtWidgets.QPushButton(self.stats_title_fr)
        self.refresh_chart_btn.setStyleSheet(":pressed {\n"
"    background-color: rgb(172, 226, 255)\n"
"}")
        self.refresh_chart_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_chart_btn.setIcon(icon8)
        self.refresh_chart_btn.setIconSize(QtCore.QSize(20, 20))
        self.refresh_chart_btn.setObjectName("refresh_chart_btn")
        self.horizontalLayout_10.addWidget(self.refresh_chart_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.stats_title_fr, 0, QtCore.Qt.AlignTop)
        self.stats_body_fr = QtWidgets.QFrame(self.stats_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_body_fr.sizePolicy().hasHeightForWidth())
        self.stats_body_fr.setSizePolicy(sizePolicy)
        self.stats_body_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_body_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_body_fr.setObjectName("stats_body_fr")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.stats_body_fr)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.chart_container = QtWidgets.QWidget(self.stats_body_fr)
        self.chart_container.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_container.sizePolicy().hasHeightForWidth())
        self.chart_container.setSizePolicy(sizePolicy)
        self.chart_container.setMinimumSize(QtCore.QSize(0, 0))
        self.chart_container.setObjectName("chart_container")
        self.horizontalLayout_11.addWidget(self.chart_container)
        self.verticalLayout_3.addWidget(self.stats_body_fr)
        self.centralWidget.addWidget(self.stats_page)
        self.lock_page = QtWidgets.QWidget()
        self.lock_page.setObjectName("lock_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lock_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lock_title_fr = QtWidgets.QFrame(self.lock_page)
        self.lock_title_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lock_title_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lock_title_fr.setObjectName("lock_title_fr")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.lock_title_fr)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lock_title_lbl = QtWidgets.QLabel(self.lock_title_fr)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lock_title_lbl.setFont(font)
        self.lock_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lock_title_lbl.setObjectName("lock_title_lbl")
        self.verticalLayout_5.addWidget(self.lock_title_lbl)
        self.verticalLayout_4.addWidget(self.lock_title_fr, 0, QtCore.Qt.AlignTop)
        self.lock_body_fr = QtWidgets.QFrame(self.lock_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lock_body_fr.sizePolicy().hasHeightForWidth())
        self.lock_body_fr.setSizePolicy(sizePolicy)
        self.lock_body_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lock_body_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lock_body_fr.setObjectName("lock_body_fr")
        self.verticalLayout_4.addWidget(self.lock_body_fr)
        self.centralWidget.addWidget(self.lock_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.settings_title_fr = QtWidgets.QFrame(self.settings_page)
        self.settings_title_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_title_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_title_fr.setObjectName("settings_title_fr")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.settings_title_fr)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.settings_title_lbl = QtWidgets.QLabel(self.settings_title_fr)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.settings_title_lbl.setFont(font)
        self.settings_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_title_lbl.setObjectName("settings_title_lbl")
        self.verticalLayout_7.addWidget(self.settings_title_lbl)
        self.verticalLayout_6.addWidget(self.settings_title_fr, 0, QtCore.Qt.AlignTop)
        self.settings_body_fr = QtWidgets.QFrame(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_body_fr.sizePolicy().hasHeightForWidth())
        self.settings_body_fr.setSizePolicy(sizePolicy)
        self.settings_body_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_body_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_body_fr.setObjectName("settings_body_fr")
        self.verticalLayout_6.addWidget(self.settings_body_fr)
        self.centralWidget.addWidget(self.settings_page)
        self.data_page = QtWidgets.QWidget()
        self.data_page.setObjectName("data_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.data_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.data_title_fr = QtWidgets.QFrame(self.data_page)
        self.data_title_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_title_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_title_fr.setObjectName("data_title_fr")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.data_title_fr)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.data_title_lbl = QtWidgets.QLabel(self.data_title_fr)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.data_title_lbl.setFont(font)
        self.data_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.data_title_lbl.setObjectName("data_title_lbl")
        self.verticalLayout_9.addWidget(self.data_title_lbl)
        self.verticalLayout_8.addWidget(self.data_title_fr, 0, QtCore.Qt.AlignTop)
        self.data_body_fr = QtWidgets.QFrame(self.data_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_body_fr.sizePolicy().hasHeightForWidth())
        self.data_body_fr.setSizePolicy(sizePolicy)
        self.data_body_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_body_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_body_fr.setObjectName("data_body_fr")
        self.verticalLayout_8.addWidget(self.data_body_fr)
        self.centralWidget.addWidget(self.data_page)
        self.verticalLayout_2.addWidget(self.centralWidget)
        self.horizontalLayout_8.addWidget(self.main_frame)
        self.right_center_fr = QtWidgets.QFrame(self.center_frame)
        self.right_center_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_center_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_center_fr.setObjectName("right_center_fr")
        self.horizontalLayout_8.addWidget(self.right_center_fr)
        self.verticalLayout.addWidget(self.center_frame)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setStyleSheet(":pressed {\n"
"    background-color: rgb(172, 226, 255)\n"
"}")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.footer_left_fr = QtWidgets.QFrame(self.footer_frame)
        self.footer_left_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_left_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_left_fr.setObjectName("footer_left_fr")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.footer_left_fr)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.version_lbl = QtWidgets.QLabel(self.footer_left_fr)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.version_lbl.setFont(font)
        self.version_lbl.setObjectName("version_lbl")
        self.horizontalLayout_7.addWidget(self.version_lbl, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_5.addWidget(self.footer_left_fr)
        self.footer_right_fr = QtWidgets.QFrame(self.footer_frame)
        self.footer_right_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_right_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_right_fr.setObjectName("footer_right_fr")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.footer_right_fr)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.question_btn = QtWidgets.QPushButton(self.footer_right_fr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_btn.sizePolicy().hasHeightForWidth())
        self.question_btn.setSizePolicy(sizePolicy)
        self.question_btn.setIconSize(QtCore.QSize(16, 16))
        self.question_btn.setObjectName("question_btn")
        self.horizontalLayout_6.addWidget(self.question_btn, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.footer_right_fr)
        self.size_grip = QtWidgets.QFrame(self.footer_frame)
        self.size_grip.setMinimumSize(QtCore.QSize(16, 16))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_5.addWidget(self.size_grip)
        self.verticalLayout.addWidget(self.footer_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.centralWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_btn.setText(_translate("MainWindow", "Menu"))
        self.main_title_lbl.setText(_translate("MainWindow", "TimeUsageMonitor"))
        self.settings_lbl.setText(_translate("MainWindow", "Settings"))
        self.lock_lbl.setText(_translate("MainWindow", "Limits"))
        self.stats_lbl.setText(_translate("MainWindow", "Stats"))
        self.data_lbl.setText(_translate("MainWindow", "Data"))
        self.stats_title_lbl.setText(_translate("MainWindow", "Statistics"))
        self.lock_title_lbl.setText(_translate("MainWindow", "Limits"))
        self.settings_title_lbl.setText(_translate("MainWindow", "Settings"))
        self.data_title_lbl.setText(_translate("MainWindow", "Data"))
        self.version_lbl.setText(_translate("MainWindow", "Version 1.0"))
        self.question_btn.setText(_translate("MainWindow", "?"))

