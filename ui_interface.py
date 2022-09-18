from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import psutil_rc
import psutil_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 415)
        font = QFont()
        font.setFamily(u"Terminus")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{border: none;}\n"
"QProgressBar{\n"
"	background-color:rgb(20, 30, 43);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 70))
        self.header_frame.setMaximumSize(QSize(16777215, 70))
        self.header_frame.setStyleSheet(u"background-color: rgb(37, 55, 78);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.WinPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_left_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))
        self.open_close_side_bar_btn.setFlat(True)

        self.horizontalLayout_9.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignLeft)

        self.app_logo = QLabel(self.header_left_frame)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setPixmap(QPixmap(u":/icons/icons/feather/airplay.svg"))

        self.horizontalLayout_4.addWidget(self.app_logo, 0, Qt.AlignRight)

        self.label = QLabel(self.header_left_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Terminus")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.header_left_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.NoFrame)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeWindowButton = QPushButton(self.header_right_frame)
        self.minimizeWindowButton.setObjectName(u"minimizeWindowButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindowButton.setIcon(icon1)
        self.minimizeWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.minimizeWindowButton)

        self.restoreWindowButton = QPushButton(self.header_right_frame)
        self.restoreWindowButton.setObjectName(u"restoreWindowButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindowButton.setIcon(icon2)
        self.restoreWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.restoreWindowButton)

        self.closeWindowButton = QPushButton(self.header_right_frame)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowButton.setIcon(icon3)
        self.closeWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.closeWindowButton)


        self.horizontalLayout_2.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setStyleSheet(u"")
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_frame = QFrame(self.main_body_frame)
        self.side_menu_frame.setObjectName(u"side_menu_frame")
        self.side_menu_frame.setMinimumSize(QSize(40, 0))
        self.side_menu_frame.setMaximumSize(QSize(30, 16777215))
        self.side_menu_frame.setStyleSheet(u"background-color: rgb(37, 55, 78);")
        self.side_menu_frame.setFrameShape(QFrame.WinPanel)
        self.side_menu_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.left_side_menu = QFrame(self.side_menu_frame)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(60, 0))
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.left_side_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.left_side_menu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.cpu_page_btn = QPushButton(self.left_side_menu)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        self.cpu_page_btn.setMinimumSize(QSize(30, 0))
        self.cpu_page_btn.setMaximumSize(QSize(30, 16777215))
        self.cpu_page_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/feather/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon4)
        self.cpu_page_btn.setIconSize(QSize(32, 32))
        self.cpu_page_btn.setFlat(True)

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_20 = QLabel(self.left_side_menu)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMargin(5)

        self.gridLayout.addWidget(self.label_20, 4, 1, 1, 1, Qt.AlignLeft)

        self.storage_btn = QPushButton(self.left_side_menu)
        self.storage_btn.setObjectName(u"storage_btn")
        self.storage_btn.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/feather/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_btn.setIcon(icon5)
        self.storage_btn.setIconSize(QSize(32, 32))
        self.storage_btn.setFlat(True)

        self.gridLayout.addWidget(self.storage_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.battery_page_btn = QPushButton(self.left_side_menu)
        self.battery_page_btn.setObjectName(u"battery_page_btn")
        self.battery_page_btn.setMaximumSize(QSize(30, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/feather/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_page_btn.setIcon(icon6)
        self.battery_page_btn.setIconSize(QSize(32, 32))
        self.battery_page_btn.setFlat(True)

        self.gridLayout.addWidget(self.battery_page_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_23 = QLabel(self.left_side_menu)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMargin(5)

        self.gridLayout.addWidget(self.label_23, 5, 1, 1, 1, Qt.AlignLeft)

        self.activity_btn = QPushButton(self.left_side_menu)
        self.activity_btn.setObjectName(u"activity_btn")
        self.activity_btn.setMaximumSize(QSize(30, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/feather/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_btn.setIcon(icon7)
        self.activity_btn.setIconSize(QSize(32, 32))
        self.activity_btn.setFlat(True)

        self.gridLayout.addWidget(self.activity_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.system_inf_page_btn = QPushButton(self.left_side_menu)
        self.system_inf_page_btn.setObjectName(u"system_inf_page_btn")
        self.system_inf_page_btn.setMaximumSize(QSize(30, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/feather/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_inf_page_btn.setIcon(icon8)
        self.system_inf_page_btn.setIconSize(QSize(32, 32))
        self.system_inf_page_btn.setFlat(True)

        self.gridLayout.addWidget(self.system_inf_page_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_13 = QLabel(self.left_side_menu)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMargin(5)

        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)

        self.label_19 = QLabel(self.left_side_menu)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMargin(5)

        self.gridLayout.addWidget(self.label_19, 3, 1, 1, 1, Qt.AlignLeft)

        self.sensors_page_btn = QPushButton(self.left_side_menu)
        self.sensors_page_btn.setObjectName(u"sensors_page_btn")
        self.sensors_page_btn.setMaximumSize(QSize(30, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/feather/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_page_btn.setIcon(icon9)
        self.sensors_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_page_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.left_side_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignLeft)

        self.networks_page_button = QPushButton(self.left_side_menu)
        self.networks_page_button.setObjectName(u"networks_page_button")
        self.networks_page_button.setMaximumSize(QSize(36, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/feather/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_page_button.setIcon(icon10)
        self.networks_page_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.networks_page_button, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_41 = QLabel(self.left_side_menu)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMargin(4)

        self.gridLayout.addWidget(self.label_41, 6, 1, 1, 1, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.left_side_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu_frame, 0, Qt.AlignLeft)

        self.nain_body_cont_frame = QFrame(self.main_body_frame)
        self.nain_body_cont_frame.setObjectName(u"nain_body_cont_frame")
        self.nain_body_cont_frame.setFrameShape(QFrame.NoFrame)
        self.nain_body_cont_frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.nain_body_cont_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.nain_body_cont_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_page = QWidget()
        self.cpu_page.setObjectName(u"cpu_page")
        self.gridLayout_2 = QGridLayout(self.cpu_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cpu_frame = QFrame(self.cpu_page)
        self.cpu_frame.setObjectName(u"cpu_frame")
        self.cpu_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.cpu_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cpu_count = QLabel(self.cpu_frame)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_5.addWidget(self.cpu_count, 1, 1, 1, 1)

        self.cpu_per = QLabel(self.cpu_frame)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_5.addWidget(self.cpu_per, 2, 1, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")

        self.gridLayout_5.addWidget(self.cpu_main_core, 3, 1, 1, 1)

        self.label_18 = QLabel(self.cpu_frame)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_4 = QLabel(self.cpu_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_22 = QLabel(self.cpu_frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 3, 0, 1, 1)

        self.label_35 = QLabel(self.cpu_frame)
        self.label_35.setObjectName(u"label_35")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_35.setFont(font2)

        self.gridLayout_5.addWidget(self.label_35, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.cpu_frame, 0, 0, 1, 1)

        self.ram_frame = QFrame(self.cpu_page)
        self.ram_frame.setObjectName(u"ram_frame")
        self.ram_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.ram_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_11 = QLabel(self.ram_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_6.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_12 = QLabel(self.ram_frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 1, 0, 1, 1)

        self.available_ram = QLabel(self.ram_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setStyleSheet(u"border: 1px solid rgb(6,233,38);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_14 = QLabel(self.ram_frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.used_ram = QLabel(self.ram_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setStyleSheet(u"border: 1px solid rgb(6,201,233);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_16 = QLabel(self.ram_frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_frame)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setStyleSheet(u"border: 1px solid rgb(233,6,201);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_24 = QLabel(self.ram_frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 4, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_frame)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_6.addWidget(self.ram_usage, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.ram_frame, 2, 0, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_page)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(100, 100))
        self.cpu_percentage.setMaximumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.cpu_percentage, 0, 1, 1, 1)

        self.ram_percantage = spiralProgressBar(self.cpu_page)
        self.ram_percantage.setObjectName(u"ram_percantage")
        self.ram_percantage.setMinimumSize(QSize(100, 100))
        self.ram_percantage.setMaximumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.ram_percantage, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.cpu_page)
        self.system_info = QWidget()
        self.system_info.setObjectName(u"system_info")
        self.gridLayout_4 = QGridLayout(self.system_info)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.system_version = QLabel(self.system_info)
        self.system_version.setObjectName(u"system_version")

        self.gridLayout_4.addWidget(self.system_version, 4, 1, 1, 1)

        self.label_17 = QLabel(self.system_info)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.label_17.setFont(font3)

        self.gridLayout_4.addWidget(self.label_17, 5, 2, 1, 1)

        self.system_time = QLabel(self.system_info)
        self.system_time.setObjectName(u"system_time")

        self.gridLayout_4.addWidget(self.system_time, 5, 3, 1, 1)

        self.system_date = QLabel(self.system_info)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_4.addWidget(self.system_date, 5, 1, 1, 1)

        self.label_26 = QLabel(self.system_info)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.gridLayout_4.addWidget(self.label_26, 3, 2, 1, 1)

        self.system_sytem = QLabel(self.system_info)
        self.system_sytem.setObjectName(u"system_sytem")
        self.system_sytem.setFont(font2)

        self.gridLayout_4.addWidget(self.system_sytem, 1, 0, 1, 1)

        self.label_30 = QLabel(self.system_info)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout_4.addWidget(self.label_30, 4, 2, 1, 1)

        self.system_platform = QLabel(self.system_info)
        self.system_platform.setObjectName(u"system_platform")

        self.gridLayout_4.addWidget(self.system_platform, 3, 1, 1, 1)

        self.label_15 = QLabel(self.system_info)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_4.addWidget(self.label_15, 5, 0, 1, 1)

        self.system_processor = QLabel(self.system_info)
        self.system_processor.setObjectName(u"system_processor")

        self.gridLayout_4.addWidget(self.system_processor, 3, 3, 1, 1)

        self.label_28 = QLabel(self.system_info)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout_4.addWidget(self.label_28, 4, 0, 1, 1)

        self.system_machine = QLabel(self.system_info)
        self.system_machine.setObjectName(u"system_machine")

        self.gridLayout_4.addWidget(self.system_machine, 4, 3, 1, 1)

        self.label_25 = QLabel(self.system_info)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.gridLayout_4.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_45 = QLabel(self.system_info)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)

        self.gridLayout_4.addWidget(self.label_45, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.system_info)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_4 = QVBoxLayout(self.activities)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.activities)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_36)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.activity_search = QLineEdit(self.frame_4)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_8.addWidget(self.activity_search, 0, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.pushButton_5, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.tableWidget = QTableWidget(self.activities)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeIncrement(QSize(1, 1))
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.activities)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.activities)
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.verticalLayout_7 = QVBoxLayout(self.network)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.network)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 186, 946))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_40 = QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_40)

        self.net_stats_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 200))

        self.verticalLayout_8.addWidget(self.net_stats_table)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_38)

        self.net_io_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(0, 200))

        self.verticalLayout_8.addWidget(self.net_io_table)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_39)

        self.net_addresses_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        self.net_addresses_table.setObjectName(u"net_addresses_table")
        self.net_addresses_table.setMinimumSize(QSize(0, 200))

        self.verticalLayout_8.addWidget(self.net_addresses_table)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_42)

        self.net_connections_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(0, 200))

        self.verticalLayout_8.addWidget(self.net_connections_table)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.network)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_5 = QVBoxLayout(self.storage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(self.storage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_21)

        self.storageTable = QTableWidget(self.storage)
        if (self.storageTable.columnCount() < 10):
            self.storageTable.setColumnCount(10)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(9, __qtablewidgetitem44)
        self.storageTable.setObjectName(u"storageTable")
        self.storageTable.setFrameShape(QFrame.NoFrame)
        self.storageTable.horizontalHeader().setMinimumSectionSize(40)
        self.storageTable.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_5.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_6 = QVBoxLayout(self.sensors)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_37 = QLabel(self.sensors)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_37)

        self.sensorTable = QTableWidget(self.sensors)
        if (self.sensorTable.columnCount() < 6):
            self.sensorTable.setColumnCount(6)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(5, __qtablewidgetitem50)
        self.sensorTable.setObjectName(u"sensorTable")
        self.sensorTable.setGridStyle(Qt.CustomDashLine)
        self.sensorTable.setSortingEnabled(True)

        self.verticalLayout_6.addWidget(self.sensorTable)

        self.stackedWidget.addWidget(self.sensors)
        self.battery_info = QWidget()
        self.battery_info.setObjectName(u"battery_info")
        self.gridLayout_8 = QGridLayout(self.battery_info)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(20, 20, 20, 20)
        self.frame_5 = QFrame(self.battery_info)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 3, 0, 1, 1)

        self.battery_status = QLabel(self.frame_5)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_7.addWidget(self.battery_status, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 5, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame_5)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_7.addWidget(self.battery_time_left, 5, 1, 1, 1)

        self.battery_plugged = QLabel(self.frame_5)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_7.addWidget(self.battery_plugged, 6, 1, 1, 1)

        self.battery_charge = QLabel(self.frame_5)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_7.addWidget(self.battery_charge, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)

        self.battery_usage = roundProgressBar(self.battery_info)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(100, 100))
        self.battery_usage.setMaximumSize(QSize(100, 100))

        self.gridLayout_8.addWidget(self.battery_usage, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.battery_info)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.nain_body_cont_frame, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.main_body_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(150, 0))
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"background-color: rgb(37, 55, 78);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setOpenExternalLinks(True)

        self.gridLayout_10.addWidget(self.label_32, 2, 1, 1, 1, Qt.AlignTop)

        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_29, 1, 0, 1, 2)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255) !important;")
        self.label_34.setOpenExternalLinks(True)

        self.gridLayout_10.addWidget(self.label_34, 3, 1, 1, 1)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_10.addWidget(self.label_27, 0, 0, 1, 2)

        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setTextFormat(Qt.RichText)
        # self.label_31.setPixmap(QPixmap(u":/icons/icons/feather/youtube.svg"))
        self.label_31.setOpenExternalLinks(True)

        self.gridLayout_10.addWidget(self.label_31, 2, 0, 1, 1, Qt.AlignTop)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        # self.label_33.setPixmap(QPixmap(u":/icons/icons/feather/coffee.svg"))

        self.gridLayout_10.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_43 = QLabel(self.frame_7)
        self.label_43.setObjectName(u"label_43")
        # self.label_43.setPixmap(QPixmap(u":/icons/icons/feather/dollar-sign.svg"))

        self.gridLayout_10.addWidget(self.label_43, 4, 0, 1, 1)

        self.label_44 = QLabel(self.frame_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)
        self.label_44.setOpenExternalLinks(True)

        self.gridLayout_10.addWidget(self.label_44, 4, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_7, 2, 1, 1, 1, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 50))
        self.footer_frame.setMaximumSize(QSize(16777215, 50))
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.frame_8 = QFrame(self.footer_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.help_btn = QPushButton(self.footer_frame)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.help_btn, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 16777215))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.app_logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"MInsight", None))
        self.minimizeWindowButton.setText("")
        self.restoreWindowButton.setText("")
        self.closeWindowButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.cpu_page_btn.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.storage_btn.setText("")
        self.battery_page_btn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.activity_btn.setText("")
        self.system_inf_page_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.sensors_page_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.networks_page_button.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"System Memory", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N / A", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_sytem.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search process name", None))
        self.pushButton_5.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem8 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem9 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem10 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem11 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Network IO Counters", None))
        ___qtablewidgetitem12 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem13 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem14 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None));
        ___qtablewidgetitem15 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem16 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Packets Recieved", None));
        ___qtablewidgetitem17 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem18 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ErrOut", None));
        ___qtablewidgetitem19 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem20 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem21 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem22 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem23 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem24 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem25 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Ptp", None));
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem26 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Fd", None));
        ___qtablewidgetitem27 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem28 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem29 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"laddr", None));
        ___qtablewidgetitem30 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"raddr", None));
        ___qtablewidgetitem31 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem32 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"pid", None));
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Disk Partitions", None))
        ___qtablewidgetitem33 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem34 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem35 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem36 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem37 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem38 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem39 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem40 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem41 = self.storageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem42 = self.sensorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem43 = self.sensorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem44 = self.sensorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem45 = self.sensorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem46 = self.sensorTable.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        # self.label_32.setText(QCoreApplication.translate("MainWindow", u"<a href=\"https://www.youtube.com/c/SpinnTV/videos\" style=\"color: white\">YouTube/</a>", None))
        # self.label_29.setText(QCoreApplication.translate("MainWindow", u"App Designed And Developed By Khamisi Kibet.", None))
        # self.label_34.setText(QCoreApplication.translate("MainWindow", u"<a href=\"https://www.patreon.com/spinntv\" style=\"color: white\">Patreon/</a>", None))
        # self.label_27.setText(QCoreApplication.translate("MainWindow", u"About", None))
        # self.label_31.setText("")
        # self.label_33.setText("")
        # self.label_43.setText("")
        # self.label_44.setText(QCoreApplication.translate("MainWindow", u"<a href=\"https://www.paypal.com/donate/?hosted_button_id=MABAL328S94JC\" style=\"color: white\">PayPal</a>", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright Spinn Co.", None))
        # self.help_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

