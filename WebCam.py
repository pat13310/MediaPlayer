# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebCam.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WebCam(object):
    def setupUi(self, WebCam):
        WebCam.setObjectName("WebCam")
        WebCam.resize(1079, 883)
        WebCam.setMinimumSize(QtCore.QSize(0, 800))
        self.centralwidget = QtWidgets.QWidget(WebCam)
        self.centralwidget.setStyleSheet("border-radius:10px;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cadre = QtWidgets.QFrame(self.centralwidget)
        self.cadre.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.492925, y2:0.972, stop:0 rgba(24, 37, 54, 255), stop:1 rgba(81, 88, 100, 255));\n"
"")
        self.cadre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cadre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cadre.setObjectName("cadre")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cadre)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Top = QtWidgets.QFrame(self.cadre)
        self.Top.setMinimumSize(QtCore.QSize(930, 40))
        self.Top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.492925, y2:0.972, stop:0 rgba(24, 37, 54, 255), stop:1 rgba(81, 88, 100, 255))")
        self.Top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top.setObjectName("Top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Top)
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_close = QtWidgets.QPushButton(self.Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_close.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border: 1px solid rgb(85, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(208, 0, 0);\n"
"}")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.pushButton_maxi = QtWidgets.QPushButton(self.Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_maxi.sizePolicy().hasHeightForWidth())
        self.pushButton_maxi.setSizePolicy(sizePolicy)
        self.pushButton_maxi.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_maxi.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(10)
        self.pushButton_maxi.setFont(font)
        self.pushButton_maxi.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border: 1px solid blue;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(69, 139, 209);\n"
"}")
        self.pushButton_maxi.setCheckable(True)
        self.pushButton_maxi.setChecked(True)
        self.pushButton_maxi.setObjectName("pushButton_maxi")
        self.horizontalLayout_2.addWidget(self.pushButton_maxi)
        spacerItem = QtWidgets.QSpacerItem(474, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.Top)
        self.frame = QtWidgets.QFrame(self.cadre)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_left = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_left.sizePolicy().hasHeightForWidth())
        self.menu_left.setSizePolicy(sizePolicy)
        self.menu_left.setMinimumSize(QtCore.QSize(0, 0))
        self.menu_left.setMaximumSize(QtCore.QSize(200, 16777215))
        self.menu_left.setStyleSheet("background-color:rgb(64, 69, 79);\n"
"border: 1px solid black;\n"
"")
        self.menu_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_left.setObjectName("menu_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_left)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.video = QtWidgets.QPushButton(self.menu_left)
        self.video.setMinimumSize(QtCore.QSize(70, 70))
        self.video.setMaximumSize(QtCore.QSize(16777215, 100))
        self.video.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color:rgb(62, 62, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.89, fx:0.5, fy:0.5, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(93, 93, 93, 255));\n"
"}\n"
"")
        self.video.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/icones/media/Misc-Video-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.video.setIcon(icon)
        self.video.setIconSize(QtCore.QSize(63, 69))
        self.video.setAutoDefault(True)
        self.video.setObjectName("video")
        self.verticalLayout_3.addWidget(self.video)
        self.picture = QtWidgets.QPushButton(self.menu_left)
        self.picture.setMinimumSize(QtCore.QSize(70, 70))
        self.picture.setMaximumSize(QtCore.QSize(16777215, 100))
        self.picture.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color:rgb(62, 62, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.89, fx:0.5, fy:0.5, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(93, 93, 93, 255));\n"
"}\n"
"")
        self.picture.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icones/icones/media/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.picture.setIcon(icon1)
        self.picture.setIconSize(QtCore.QSize(63, 61))
        self.picture.setAutoDefault(True)
        self.picture.setObjectName("picture")
        self.verticalLayout_3.addWidget(self.picture)
        self.config = QtWidgets.QPushButton(self.menu_left)
        self.config.setMinimumSize(QtCore.QSize(70, 70))
        self.config.setMaximumSize(QtCore.QSize(16777215, 100))
        self.config.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color:rgb(62, 62, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.89, fx:0.5, fy:0.5, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(93, 93, 93, 255));\n"
"}\n"
"")
        self.config.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icones/icones/media/HP-Control-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.config.setIcon(icon2)
        self.config.setIconSize(QtCore.QSize(69, 73))
        self.config.setAutoDefault(True)
        self.config.setObjectName("config")
        self.verticalLayout_3.addWidget(self.config)
        self.frame_2 = QtWidgets.QFrame(self.menu_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.chk_adjust = QtWidgets.QCheckBox(self.frame_2)
        self.chk_adjust.setGeometry(QtCore.QRect(15, 20, 117, 16))
        self.chk_adjust.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.chk_adjust.setObjectName("chk_adjust")
        self.slider_brillance = QtWidgets.QSlider(self.frame_2)
        self.slider_brillance.setGeometry(QtCore.QRect(15, 135, 130, 16))
        self.slider_brillance.setMinimumSize(QtCore.QSize(0, 0))
        self.slider_brillance.setMaximumSize(QtCore.QSize(180, 16))
        self.slider_brillance.setStyleSheet("QSlider{\n"
"border: 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 6px;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(170, 170, 255, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_brillance.setMaximum(100)
        self.slider_brillance.setProperty("value", 100)
        self.slider_brillance.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brillance.setObjectName("slider_brillance")
        self.lbl_brillance = QtWidgets.QLabel(self.frame_2)
        self.lbl_brillance.setGeometry(QtCore.QRect(15, 115, 126, 18))
        self.lbl_brillance.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_brillance.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_brillance.setFont(font)
        self.lbl_brillance.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.lbl_brillance.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_brillance.setObjectName("lbl_brillance")
        self.slider_contraste = QtWidgets.QSlider(self.frame_2)
        self.slider_contraste.setGeometry(QtCore.QRect(13, 195, 130, 16))
        self.slider_contraste.setMinimumSize(QtCore.QSize(0, 0))
        self.slider_contraste.setMaximumSize(QtCore.QSize(180, 16))
        self.slider_contraste.setStyleSheet("QSlider{\n"
"border: 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 6px;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(170, 170, 255, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_contraste.setMaximum(100)
        self.slider_contraste.setProperty("value", 100)
        self.slider_contraste.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contraste.setObjectName("slider_contraste")
        self.lbl_contraste = QtWidgets.QLabel(self.frame_2)
        self.lbl_contraste.setGeometry(QtCore.QRect(13, 175, 126, 17))
        self.lbl_contraste.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_contraste.setFont(font)
        self.lbl_contraste.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.lbl_contraste.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_contraste.setObjectName("lbl_contraste")
        self.lbl_saturation = QtWidgets.QLabel(self.frame_2)
        self.lbl_saturation.setGeometry(QtCore.QRect(13, 235, 121, 17))
        self.lbl_saturation.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_saturation.setFont(font)
        self.lbl_saturation.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.lbl_saturation.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_saturation.setObjectName("lbl_saturation")
        self.slider_saturation = QtWidgets.QSlider(self.frame_2)
        self.slider_saturation.setGeometry(QtCore.QRect(13, 260, 130, 16))
        self.slider_saturation.setMinimumSize(QtCore.QSize(0, 0))
        self.slider_saturation.setMaximumSize(QtCore.QSize(180, 16))
        self.slider_saturation.setStyleSheet("QSlider{\n"
"border: 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 6px;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(170, 170, 255, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setProperty("value", 100)
        self.slider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturation.setObjectName("slider_saturation")
        self.chk_inverse = QtWidgets.QCheckBox(self.frame_2)
        self.chk_inverse.setGeometry(QtCore.QRect(15, 50, 117, 16))
        self.chk_inverse.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.chk_inverse.setObjectName("chk_inverse")
        self.chk_grey = QtWidgets.QCheckBox(self.frame_2)
        self.chk_grey.setGeometry(QtCore.QRect(15, 80, 117, 16))
        self.chk_grey.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.chk_grey.setObjectName("chk_grey")
        self.comboCamera = QtWidgets.QComboBox(self.frame_2)
        self.comboCamera.setGeometry(QtCore.QRect(10, 300, 136, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboCamera.setFont(font)
        self.comboCamera.setStyleSheet("QComboBox{\n"
"border: 1px solid rgb(170, 85, 255);\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.443, y1:0, x2:0.483, y2:1, stop:0 rgba(170, 0, 255, 89), stop:1 rgba(170, 170, 255, 176));\n"
"border-radius:4px;\n"
"color:white;\n"
"}\n"
"\n"
"")
        self.comboCamera.setObjectName("comboCamera")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.menu_left)
        self.container = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.screen = QtWidgets.QLabel(self.container)
        self.screen.setGeometry(QtCore.QRect(45, 255, 731, 180))
        self.screen.setStyleSheet("color: rgb(255, 255, 255);")
        self.screen.setScaledContents(True)
        self.screen.setObjectName("screen")
        self.screen_2 = QtWidgets.QLabel(self.container)
        self.screen_2.setEnabled(True)
        self.screen_2.setGeometry(QtCore.QRect(120, 175, 0, 180))
        self.screen_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.screen_2.setScaledContents(True)
        self.screen_2.setObjectName("screen_2")
        self.screen_3 = QtWidgets.QLabel(self.container)
        self.screen_3.setGeometry(QtCore.QRect(125, 350, 0, 180))
        self.screen_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.screen_3.setScaledContents(True)
        self.screen_3.setObjectName("screen_3")
        self.screen_4 = QtWidgets.QLabel(self.container)
        self.screen_4.setGeometry(QtCore.QRect(120, 505, 0, 180))
        self.screen_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.screen_4.setScaledContents(True)
        self.screen_4.setObjectName("screen_4")
        self.lbl_screen = QtWidgets.QLabel(self.container)
        self.lbl_screen.setGeometry(QtCore.QRect(195, 500, 486, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(True)
        self.lbl_screen.setFont(font)
        self.lbl_screen.setStyleSheet("background-color: transparent;\n"
"color:rgb(170, 170, 255);\n"
"font-style:italic;\n"
"font-size:28px;")
        self.lbl_screen.setText("")
        self.lbl_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_screen.setObjectName("lbl_screen")
        self.horizontalLayout.addWidget(self.container)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.play = QtWidgets.QPushButton(self.cadre)
        self.play.setMinimumSize(QtCore.QSize(60, 30))
        self.play.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(9)
        self.play.setFont(font)
        self.play.setStyleSheet("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(68, 0, 102);\n"
"    background-color: rgb(211, 199, 255);\n"
"}")
        self.play.setText("")
        self.play.setObjectName("play")
        self.gridLayout.addWidget(self.play, 1, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(self.cadre)
        self.stop.setMinimumSize(QtCore.QSize(60, 0))
        self.stop.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(9)
        self.stop.setFont(font)
        self.stop.setStyleSheet("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(68, 0, 102);\n"
"    background-color: rgb(211, 199, 255);\n"
"}")
        self.stop.setText("")
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 1, 1, 1, 1)
        self.split = QtWidgets.QPushButton(self.cadre)
        self.split.setMinimumSize(QtCore.QSize(60, 30))
        self.split.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(9)
        self.split.setFont(font)
        self.split.setStyleSheet("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(68, 0, 102);\n"
"    background-color: rgb(211, 199, 255);\n"
"}")
        self.split.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icones/media/split.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.split.setIcon(icon3)
        self.split.setObjectName("split")
        self.gridLayout.addWidget(self.split, 1, 3, 1, 1)
        self.lbl_duration = QtWidgets.QLabel(self.cadre)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_duration.sizePolicy().hasHeightForWidth())
        self.lbl_duration.setSizePolicy(sizePolicy)
        self.lbl_duration.setMinimumSize(QtCore.QSize(90, 15))
        self.lbl_duration.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_duration.setFont(font)
        self.lbl_duration.setStyleSheet("background-color:transparent ;\n"
"color:white;")
        self.lbl_duration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_duration.setObjectName("lbl_duration")
        self.gridLayout.addWidget(self.lbl_duration, 1, 7, 1, 1)
        self.slider_position = QtWidgets.QSlider(self.cadre)
        self.slider_position.setMinimumSize(QtCore.QSize(600, 0))
        self.slider_position.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider_position.setStyleSheet("QSlider{\n"
"border: 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_position.setMaximum(200)
        self.slider_position.setPageStep(1)
        self.slider_position.setProperty("value", 0)
        self.slider_position.setOrientation(QtCore.Qt.Horizontal)
        self.slider_position.setObjectName("slider_position")
        self.gridLayout.addWidget(self.slider_position, 1, 5, 1, 1)
        self.record = QtWidgets.QPushButton(self.cadre)
        self.record.setMinimumSize(QtCore.QSize(60, 30))
        self.record.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(9)
        self.record.setFont(font)
        self.record.setStyleSheet("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(68, 0, 102);\n"
"    background-color: rgb(211, 199, 255);\n"
"}")
        self.record.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icones/icones/media/Record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record.setIcon(icon4)
        self.record.setIconSize(QtCore.QSize(30, 30))
        self.record.setObjectName("record")
        self.gridLayout.addWidget(self.record, 1, 2, 1, 1)
        self.label_infos2 = QtWidgets.QLabel(self.cadre)
        self.label_infos2.setStyleSheet("background-color:transparent ;\n"
"color:white;")
        self.label_infos2.setObjectName("label_infos2")
        self.gridLayout.addWidget(self.label_infos2, 2, 7, 1, 1)
        self.label_infos = QtWidgets.QLabel(self.cadre)
        self.label_infos.setStyleSheet("background-color:transparent ;\n"
"color:white;")
        self.label_infos.setText("")
        self.label_infos.setObjectName("label_infos")
        self.gridLayout.addWidget(self.label_infos, 2, 5, 1, 2)
        self.led = QtWidgets.QLabel(self.cadre)
        self.led.setMinimumSize(QtCore.QSize(20, 20))
        self.led.setMaximumSize(QtCore.QSize(25, 25))
        self.led.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.led.setText("")
        self.led.setPixmap(QtGui.QPixmap(":/icones/icones/media/led_rouge.png"))
        self.led.setScaledContents(True)
        self.led.setObjectName("led")
        self.gridLayout.addWidget(self.led, 1, 6, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.cadre)
        WebCam.setCentralWidget(self.centralwidget)

        self.retranslateUi(WebCam)
        QtCore.QMetaObject.connectSlotsByName(WebCam)

    def retranslateUi(self, WebCam):
        _translate = QtCore.QCoreApplication.translate
        WebCam.setWindowTitle(_translate("WebCam", "WebCam"))
        self.pushButton_close.setText(_translate("WebCam", "r"))
        self.pushButton_maxi.setText(_translate("WebCam", "1"))
        self.label.setText(_translate("WebCam", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#7f7fff;\">Created </span><span style=\" font-style:italic; color:#b6b6ff;\">by Xenatronics</span></p></body></html>"))
        self.chk_adjust.setText(_translate("WebCam", "Ajuster à l\'écran"))
        self.lbl_brillance.setText(_translate("WebCam", "<html><head/><body><p>Brillance  : <span style=\" color:#aaaaff;\">0</span></p></body></html>"))
        self.lbl_contraste.setText(_translate("WebCam", "<html><head/><body><p>Contraste : <span style=\" color:#aaaaff;\">0</span></p></body></html>"))
        self.lbl_saturation.setText(_translate("WebCam", "<html><head/><body><p>Saturation :   <span style=\" color:#aaaaff;\">0</span></p></body></html>"))
        self.chk_inverse.setText(_translate("WebCam", "Inverser"))
        self.chk_grey.setText(_translate("WebCam", "blanc et noir"))
        self.screen.setText(_translate("WebCam", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#6969ff;\">W</span><span style=\" font-size:48pt; color:#a3a3ff;\">ebcam</span></p></body></html>"))
        self.screen_2.setText(_translate("WebCam", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#6969ff;\">W</span><span style=\" font-size:48pt; color:#a3a3ff;\">ebcam </span><span style=\" font-size:48pt; color:#7474b6;\">2</span></p></body></html>"))
        self.screen_3.setText(_translate("WebCam", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#6969ff;\">W</span><span style=\" font-size:48pt; color:#a3a3ff;\">ebcam </span><span style=\" font-size:48pt; color:#7474b6;\">3</span></p></body></html>"))
        self.screen_4.setText(_translate("WebCam", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#6969ff;\">W</span><span style=\" font-size:48pt; color:#a3a3ff;\">ebcam </span><span style=\" font-size:48pt; color:#7474b6;\">4</span></p></body></html>"))
        self.lbl_duration.setText(_translate("WebCam", "00::00:00  "))
        self.label_infos2.setText(_translate("WebCam", "Stop"))
import webcam_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebCam = QtWidgets.QMainWindow()
    ui = Ui_WebCam()
    ui.setupUi(WebCam)
    WebCam.show()
    sys.exit(app.exec_())
