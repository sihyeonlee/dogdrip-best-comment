# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dogdrip.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1016, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(1016, 630))
        mainWindow.setMaximumSize(QSize(1016, 630))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 991, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 15, 971, 25))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.button_search = QPushButton(self.layoutWidget)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setCheckable(True)
        self.button_search.setChecked(False)
        self.button_search.setAutoDefault(True)

        self.gridLayout.addWidget(self.button_search, 0, 6, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.input_like = QLineEdit(self.layoutWidget)
        self.input_like.setObjectName(u"input_like")
        self.input_like.setEnabled(True)
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setKerning(False)
        self.input_like.setFont(font1)
        self.input_like.setAcceptDrops(True)
        self.input_like.setFrame(True)
        self.input_like.setDragEnabled(False)

        self.gridLayout.addWidget(self.input_like, 0, 5, 1, 1)

        self.input_start_page = QLineEdit(self.layoutWidget)
        self.input_start_page.setObjectName(u"input_start_page")
        self.input_start_page.setEnabled(True)
        self.input_start_page.setFont(font1)
        self.input_start_page.setAcceptDrops(True)
        self.input_start_page.setFrame(True)
        self.input_start_page.setDragEnabled(False)

        self.gridLayout.addWidget(self.input_start_page, 0, 1, 1, 1)

        self.button_reset = QPushButton(self.layoutWidget)
        self.button_reset.setObjectName(u"button_reset")

        self.gridLayout.addWidget(self.button_reset, 0, 7, 1, 1)

        self.input_end_page = QLineEdit(self.layoutWidget)
        self.input_end_page.setObjectName(u"input_end_page")
        self.input_end_page.setEnabled(True)
        self.input_end_page.setFont(font1)
        self.input_end_page.setAcceptDrops(True)
        self.input_end_page.setFrame(True)
        self.input_end_page.setDragEnabled(False)

        self.gridLayout.addWidget(self.input_end_page, 0, 3, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 70, 991, 491))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.table_result = QTableWidget(self.frame_2)
        if (self.table_result.columnCount() < 3):
            self.table_result.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_result.setObjectName(u"table_result")
        self.table_result.setGeometry(QRect(10, 40, 971, 441))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(10)
        font2.setKerning(True)
        self.table_result.setFont(font2)
        self.table_result.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_result.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_result.setTabKeyNavigation(True)
        self.table_result.setProperty("showDropIndicator", False)
        self.table_result.setDragEnabled(True)
        self.table_result.setDragDropOverwriteMode(False)
        self.table_result.setDragDropMode(QAbstractItemView.DragOnly)
        self.table_result.setAlternatingRowColors(True)
        self.table_result.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.table_result.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_result.setTextElideMode(Qt.ElideMiddle)
        self.table_result.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_result.setShowGrid(True)
        self.table_result.setGridStyle(Qt.SolidLine)
        self.table_result.setSortingEnabled(False)
        self.table_result.setWordWrap(True)
        self.table_result.setCornerButtonEnabled(True)
        self.table_result.setRowCount(0)
        self.table_result.setColumnCount(3)
        self.table_result.horizontalHeader().setCascadingSectionResizes(True)
        self.table_result.horizontalHeader().setDefaultSectionSize(250)
        self.table_result.horizontalHeader().setHighlightSections(True)
        self.table_result.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_result.horizontalHeader().setStretchLastSection(True)
        self.table_result.verticalHeader().setVisible(False)
        self.table_result.verticalHeader().setCascadingSectionResizes(False)
        self.info_result_2 = QLabel(self.frame_2)
        self.info_result_2.setObjectName(u"info_result_2")
        self.info_result_2.setGeometry(QRect(11, 10, 951, 21))
        self.info_result_2.setFont(font)
        self.info_result_2.setFocusPolicy(Qt.NoFocus)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 570, 991, 51))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.layoutWidget_2 = QWidget(self.frame_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 15, 971, 25))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_step = QLabel(self.layoutWidget_2)
        self.label_step.setObjectName(u"label_step")
        self.label_step.setFont(font)
        self.label_step.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.label_step, 0, 1, 1, 1)

        self.label_status = QLabel(self.layoutWidget_2)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setFont(font)
        self.label_status.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.label_status, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.button_search.clicked.connect(mainWindow.search)
        self.button_reset.clicked.connect(mainWindow.reset)
        self.table_result.itemDoubleClicked.connect(mainWindow.openurl)

        self.button_search.setDefault(True)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Dogdrip_Comment", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\ub9c8\uc9c0\ub9c9 \ud398\uc774\uc9c0", None))
        self.button_search.setText(QCoreApplication.translate("mainWindow", u"\uac80\uc0c9", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\uc2dc\uc791 \ud398\uc774\uc9c0", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\ub313\uae00 \ucd94\ucc9c \uc218", None))
        self.button_reset.setText(QCoreApplication.translate("mainWindow", u"\ucd08\uae30\ud654", None))
        ___qtablewidgetitem = self.table_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\ub313\uae00 \ub0b4\uc6a9", None));
        ___qtablewidgetitem1 = self.table_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\ucd94\ucc9c \uc218", None));
        ___qtablewidgetitem2 = self.table_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\uac8c\uc2dc\uae00 \uc8fc\uc18c", None));
        self.info_result_2.setText(QCoreApplication.translate("mainWindow", u"\uac80\uc0c9 \uacb0\uacfc", None))
        self.label_step.setText("")
        self.label_status.setText(QCoreApplication.translate("mainWindow", u"\ud604\uc7ac \uc0c1\ud0dc : \uac80\uc0c9 \ub300\uae30", None))
    # retranslateUi

