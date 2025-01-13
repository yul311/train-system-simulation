# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_TB.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_TrackModel(object):
    def setupUi(self, TrackModel):
        if not TrackModel.objectName():
            TrackModel.setObjectName(u"TrackModel")
        TrackModel.resize(1261, 894)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrackModel.sizePolicy().hasHeightForWidth())
        TrackModel.setSizePolicy(sizePolicy)
        TrackModel.setDocumentMode(True)
        TrackModel.setDockNestingEnabled(False)
        self.simulationSpeedBlock = QWidget(TrackModel)
        self.simulationSpeedBlock.setObjectName(u"simulationSpeedBlock")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.simulationSpeedBlock.sizePolicy().hasHeightForWidth())
        self.simulationSpeedBlock.setSizePolicy(sizePolicy1)
        self.tabWidget = QTabWidget(self.simulationSpeedBlock)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 50, 1261, 791))
        self.tabWidget.setDocumentMode(True)
        self.trackMap = QWidget()
        self.trackMap.setObjectName(u"trackMap")
        self.faultsGroup = QGroupBox(self.trackMap)
        self.faultsGroup.setObjectName(u"faultsGroup")
        self.faultsGroup.setGeometry(QRect(580, 10, 351, 111))
        self.verticalLayoutWidget_3 = QWidget(self.faultsGroup)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 160, 80))
        self.faultsLabelBlock = QVBoxLayout(self.verticalLayoutWidget_3)
        self.faultsLabelBlock.setObjectName(u"faultsLabelBlock")
        self.faultsLabelBlock.setContentsMargins(0, 0, 0, 0)
        self.brokenRail = QLabel(self.verticalLayoutWidget_3)
        self.brokenRail.setObjectName(u"brokenRail")
        self.brokenRail.setFrameShape(QFrame.NoFrame)
        self.brokenRail.setFrameShadow(QFrame.Sunken)

        self.faultsLabelBlock.addWidget(self.brokenRail)

        self.trackcircuitFailure = QLabel(self.verticalLayoutWidget_3)
        self.trackcircuitFailure.setObjectName(u"trackcircuitFailure")

        self.faultsLabelBlock.addWidget(self.trackcircuitFailure)

        self.powerFailure = QLabel(self.verticalLayoutWidget_3)
        self.powerFailure.setObjectName(u"powerFailure")

        self.faultsLabelBlock.addWidget(self.powerFailure)

        self.verticalLayoutWidget_4 = QWidget(self.faultsGroup)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(170, 20, 160, 81))
        self.faultsoutputBlock = QVBoxLayout(self.verticalLayoutWidget_4)
        self.faultsoutputBlock.setObjectName(u"faultsoutputBlock")
        self.faultsoutputBlock.setContentsMargins(0, 0, 0, 0)
        self.brokenRail_O = QLabel(self.verticalLayoutWidget_4)
        self.brokenRail_O.setObjectName(u"brokenRail_O")

        self.faultsoutputBlock.addWidget(self.brokenRail_O)

        self.trackcircuitFailure_O = QLabel(self.verticalLayoutWidget_4)
        self.trackcircuitFailure_O.setObjectName(u"trackcircuitFailure_O")

        self.faultsoutputBlock.addWidget(self.trackcircuitFailure_O)

        self.powerFailure_O = QLabel(self.verticalLayoutWidget_4)
        self.powerFailure_O.setObjectName(u"powerFailure_O")

        self.faultsoutputBlock.addWidget(self.powerFailure_O)

        self.stationdevicesgroup = QGroupBox(self.trackMap)
        self.stationdevicesgroup.setObjectName(u"stationdevicesgroup")
        self.stationdevicesgroup.setGeometry(QRect(940, 20, 231, 531))
        self.horizontalLayoutWidget_12 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(10, 270, 171, 31))
        self.switchidblock = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.switchidblock.setObjectName(u"switchidblock")
        self.switchidblock.setContentsMargins(0, 0, 0, 0)
        self.switchlabe_ID_TM = QLabel(self.horizontalLayoutWidget_12)
        self.switchlabe_ID_TM.setObjectName(u"switchlabe_ID_TM")

        self.switchidblock.addWidget(self.switchlabe_ID_TM)

        self.switchID_O = QLabel(self.horizontalLayoutWidget_12)
        self.switchID_O.setObjectName(u"switchID_O")

        self.switchidblock.addWidget(self.switchID_O)

        self.horizontalLayoutWidget_11 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(10, 300, 211, 31))
        self.trackswitchOutputsTB_2 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.trackswitchOutputsTB_2.setObjectName(u"trackswitchOutputsTB_2")
        self.trackswitchOutputsTB_2.setContentsMargins(0, 0, 0, 0)
        self.trackswitchdirectionLabel_TB_2 = QLabel(self.horizontalLayoutWidget_11)
        self.trackswitchdirectionLabel_TB_2.setObjectName(u"trackswitchdirectionLabel_TB_2")

        self.trackswitchOutputsTB_2.addWidget(self.trackswitchdirectionLabel_TB_2)

        self.switchFrom_O = QLabel(self.horizontalLayoutWidget_11)
        self.switchFrom_O.setObjectName(u"switchFrom_O")

        self.trackswitchOutputsTB_2.addWidget(self.switchFrom_O)

        self.directionLabelTB_2 = QLabel(self.horizontalLayoutWidget_11)
        self.directionLabelTB_2.setObjectName(u"directionLabelTB_2")

        self.trackswitchOutputsTB_2.addWidget(self.directionLabelTB_2)

        self.switchTo_O = QLabel(self.horizontalLayoutWidget_11)
        self.switchTo_O.setObjectName(u"switchTo_O")

        self.trackswitchOutputsTB_2.addWidget(self.switchTo_O)

        self.horizontalLayoutWidget_17 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(10, 340, 171, 31))
        self.crossingIDblock_TM = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.crossingIDblock_TM.setObjectName(u"crossingIDblock_TM")
        self.crossingIDblock_TM.setContentsMargins(0, 0, 0, 0)
        self.crossingIDlabel_TM = QLabel(self.horizontalLayoutWidget_17)
        self.crossingIDlabel_TM.setObjectName(u"crossingIDlabel_TM")

        self.crossingIDblock_TM.addWidget(self.crossingIDlabel_TM)

        self.crossingID_O = QLabel(self.horizontalLayoutWidget_17)
        self.crossingID_O.setObjectName(u"crossingID_O")

        self.crossingIDblock_TM.addWidget(self.crossingID_O)

        self.horizontalLayoutWidget_18 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(10, 370, 171, 31))
        self.crossinstateblock = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.crossinstateblock.setObjectName(u"crossinstateblock")
        self.crossinstateblock.setContentsMargins(0, 0, 0, 0)
        self.crossingstatelabel_TM = QLabel(self.horizontalLayoutWidget_18)
        self.crossingstatelabel_TM.setObjectName(u"crossingstatelabel_TM")

        self.crossinstateblock.addWidget(self.crossingstatelabel_TM)

        self.crossingstate_O = QLabel(self.horizontalLayoutWidget_18)
        self.crossingstate_O.setObjectName(u"crossingstate_O")

        self.crossinstateblock.addWidget(self.crossingstate_O)

        self.horizontalLayoutWidget_19 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(10, 410, 171, 31))
        self.signalIDblock = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.signalIDblock.setObjectName(u"signalIDblock")
        self.signalIDblock.setContentsMargins(0, 0, 0, 0)
        self.signalidlabelTM = QLabel(self.horizontalLayoutWidget_19)
        self.signalidlabelTM.setObjectName(u"signalidlabelTM")

        self.signalIDblock.addWidget(self.signalidlabelTM)

        self.signalID_O = QLabel(self.horizontalLayoutWidget_19)
        self.signalID_O.setObjectName(u"signalID_O")

        self.signalIDblock.addWidget(self.signalID_O)

        self.horizontalLayoutWidget_20 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(10, 440, 171, 31))
        self.signalIstateblock = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.signalIstateblock.setObjectName(u"signalIstateblock")
        self.signalIstateblock.setContentsMargins(0, 0, 0, 0)
        self.signalstatelableTM = QLabel(self.horizontalLayoutWidget_20)
        self.signalstatelableTM.setObjectName(u"signalstatelableTM")

        self.signalIstateblock.addWidget(self.signalstatelableTM)

        self.signalstate_O = QLabel(self.horizontalLayoutWidget_20)
        self.signalstate_O.setObjectName(u"signalstate_O")

        self.signalIstateblock.addWidget(self.signalstate_O)

        self.horizontalLayoutWidget_15 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(10, 200, 171, 31))
        self.beacon1block_3 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.beacon1block_3.setObjectName(u"beacon1block_3")
        self.beacon1block_3.setContentsMargins(0, 0, 0, 0)
        self.beacon1label_TM = QLabel(self.horizontalLayoutWidget_15)
        self.beacon1label_TM.setObjectName(u"beacon1label_TM")

        self.beacon1block_3.addWidget(self.beacon1label_TM)

        self.beacon_O = QLabel(self.horizontalLayoutWidget_15)
        self.beacon_O.setObjectName(u"beacon_O")

        self.beacon1block_3.addWidget(self.beacon_O)

        self.horizontalLayoutWidget_13 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(10, 20, 171, 31))
        self.stationidblock = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.stationidblock.setObjectName(u"stationidblock")
        self.stationidblock.setContentsMargins(0, 0, 0, 0)
        self.stationlabel_ID_TM = QLabel(self.horizontalLayoutWidget_13)
        self.stationlabel_ID_TM.setObjectName(u"stationlabel_ID_TM")

        self.stationidblock.addWidget(self.stationlabel_ID_TM)

        self.stationID_O = QLabel(self.horizontalLayoutWidget_13)
        self.stationID_O.setObjectName(u"stationID_O")

        self.stationidblock.addWidget(self.stationID_O)

        self.horizontalLayoutWidget_16 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(10, 230, 171, 31))
        self.beacon2block = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.beacon2block.setObjectName(u"beacon2block")
        self.beacon2block.setContentsMargins(0, 0, 0, 0)
        self.beacon2label_TM = QLabel(self.horizontalLayoutWidget_16)
        self.beacon2label_TM.setObjectName(u"beacon2label_TM")

        self.beacon2block.addWidget(self.beacon2label_TM)

        self.beacon2_O = QLabel(self.horizontalLayoutWidget_16)
        self.beacon2_O.setObjectName(u"beacon2_O")

        self.beacon2block.addWidget(self.beacon2_O)

        self.horizontalLayoutWidget_14 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(10, 170, 171, 31))
        self.exitsideblock = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.exitsideblock.setObjectName(u"exitsideblock")
        self.exitsideblock.setContentsMargins(0, 0, 0, 0)
        self.stationexit_TM = QLabel(self.horizontalLayoutWidget_14)
        self.stationexit_TM.setObjectName(u"stationexit_TM")

        self.exitsideblock.addWidget(self.stationexit_TM)

        self.stationexit_O = QLabel(self.horizontalLayoutWidget_14)
        self.stationexit_O.setObjectName(u"stationexit_O")

        self.exitsideblock.addWidget(self.stationexit_O)

        self.horizontalLayoutWidget_26 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_26.setObjectName(u"horizontalLayoutWidget_26")
        self.horizontalLayoutWidget_26.setGeometry(QRect(10, 50, 171, 31))
        self.stationnameTMblock = QHBoxLayout(self.horizontalLayoutWidget_26)
        self.stationnameTMblock.setObjectName(u"stationnameTMblock")
        self.stationnameTMblock.setContentsMargins(0, 0, 0, 0)
        self.stationlabel_ID_TM_3 = QLabel(self.horizontalLayoutWidget_26)
        self.stationlabel_ID_TM_3.setObjectName(u"stationlabel_ID_TM_3")

        self.stationnameTMblock.addWidget(self.stationlabel_ID_TM_3)

        self.stationName_O = QLabel(self.horizontalLayoutWidget_26)
        self.stationName_O.setObjectName(u"stationName_O")

        self.stationnameTMblock.addWidget(self.stationName_O)

        self.horizontalLayoutWidget_36 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_36.setObjectName(u"horizontalLayoutWidget_36")
        self.horizontalLayoutWidget_36.setGeometry(QRect(10, 140, 171, 31))
        self.ticketsalesblock = QHBoxLayout(self.horizontalLayoutWidget_36)
        self.ticketsalesblock.setObjectName(u"ticketsalesblock")
        self.ticketsalesblock.setContentsMargins(0, 0, 0, 0)
        self.ticketsales_label = QLabel(self.horizontalLayoutWidget_36)
        self.ticketsales_label.setObjectName(u"ticketsales_label")

        self.ticketsalesblock.addWidget(self.ticketsales_label)

        self.ticketsalesTM_O = QLabel(self.horizontalLayoutWidget_36)
        self.ticketsalesTM_O.setObjectName(u"ticketsalesTM_O")

        self.ticketsalesblock.addWidget(self.ticketsalesTM_O)

        self.horizontalLayoutWidget_41 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_41.setObjectName(u"horizontalLayoutWidget_41")
        self.horizontalLayoutWidget_41.setGeometry(QRect(10, 470, 171, 31))
        self.polarityblockTM = QHBoxLayout(self.horizontalLayoutWidget_41)
        self.polarityblockTM.setObjectName(u"polarityblockTM")
        self.polarityblockTM.setContentsMargins(0, 0, 0, 0)
        self.polaritylabelTM = QLabel(self.horizontalLayoutWidget_41)
        self.polaritylabelTM.setObjectName(u"polaritylabelTM")

        self.polarityblockTM.addWidget(self.polaritylabelTM)

        self.PolarityTM_O = QLabel(self.horizontalLayoutWidget_41)
        self.PolarityTM_O.setObjectName(u"PolarityTM_O")

        self.polarityblockTM.addWidget(self.PolarityTM_O)

        self.horizontalLayoutWidget_45 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_45.setObjectName(u"horizontalLayoutWidget_45")
        self.horizontalLayoutWidget_45.setGeometry(QRect(10, 80, 171, 31))
        self.departedtrainsblock = QHBoxLayout(self.horizontalLayoutWidget_45)
        self.departedtrainsblock.setObjectName(u"departedtrainsblock")
        self.departedtrainsblock.setContentsMargins(0, 0, 0, 0)
        self.departedtrains = QLabel(self.horizontalLayoutWidget_45)
        self.departedtrains.setObjectName(u"departedtrains")

        self.departedtrainsblock.addWidget(self.departedtrains)

        self.disembarkingTM_O = QLabel(self.horizontalLayoutWidget_45)
        self.disembarkingTM_O.setObjectName(u"disembarkingTM_O")

        self.departedtrainsblock.addWidget(self.disembarkingTM_O)

        self.horizontalLayoutWidget_46 = QWidget(self.stationdevicesgroup)
        self.horizontalLayoutWidget_46.setObjectName(u"horizontalLayoutWidget_46")
        self.horizontalLayoutWidget_46.setGeometry(QRect(10, 110, 171, 31))
        self.boardingblock = QHBoxLayout(self.horizontalLayoutWidget_46)
        self.boardingblock.setObjectName(u"boardingblock")
        self.boardingblock.setContentsMargins(0, 0, 0, 0)
        self.currentriders_label = QLabel(self.horizontalLayoutWidget_46)
        self.currentriders_label.setObjectName(u"currentriders_label")

        self.boardingblock.addWidget(self.currentriders_label)

        self.boardingTM_O = QLabel(self.horizontalLayoutWidget_46)
        self.boardingTM_O.setObjectName(u"boardingTM_O")

        self.boardingblock.addWidget(self.boardingTM_O)

        self.lineselectionsGroup = QGroupBox(self.trackMap)
        self.lineselectionsGroup.setObjectName(u"lineselectionsGroup")
        self.lineselectionsGroup.setGeometry(QRect(20, 10, 541, 61))
        self.horizontalLayoutWidget = QWidget(self.lineselectionsGroup)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 521, 31))
        self.lineselectionsBlock = QHBoxLayout(self.horizontalLayoutWidget)
        self.lineselectionsBlock.setObjectName(u"lineselectionsBlock")
        self.lineselectionsBlock.setContentsMargins(0, 0, 0, 0)
        self.buttonRed = QPushButton(self.horizontalLayoutWidget)
        self.buttonRed.setObjectName(u"buttonRed")
        self.buttonRed.setEnabled(True)
        self.buttonRed.setCheckable(True)
        self.buttonRed.setAutoExclusive(True)

        self.lineselectionsBlock.addWidget(self.buttonRed)

        self.buttonGreen = QPushButton(self.horizontalLayoutWidget)
        self.buttonGreen.setObjectName(u"buttonGreen")
        self.buttonGreen.setEnabled(True)
        self.buttonGreen.setCheckable(True)
        self.buttonGreen.setAutoExclusive(True)

        self.lineselectionsBlock.addWidget(self.buttonGreen)

        self.graphicsView = QGraphicsView(self.trackMap)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 80, 541, 661))
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.blockinfoGroup_3 = QGroupBox(self.trackMap)
        self.blockinfoGroup_3.setObjectName(u"blockinfoGroup_3")
        self.blockinfoGroup_3.setGeometry(QRect(580, 130, 351, 421))
        self.verticalLayoutWidget_13 = QWidget(self.blockinfoGroup_3)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(10, 20, 160, 281))
        self.blockinfolabelsBlock_4 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.blockinfolabelsBlock_4.setObjectName(u"blockinfolabelsBlock_4")
        self.blockinfolabelsBlock_4.setContentsMargins(0, 0, 0, 0)
        self.segmentSelected_4 = QLabel(self.verticalLayoutWidget_13)
        self.segmentSelected_4.setObjectName(u"segmentSelected_4")

        self.blockinfolabelsBlock_4.addWidget(self.segmentSelected_4)

        self.blockauthoritylabelTB_3 = QLabel(self.verticalLayoutWidget_13)
        self.blockauthoritylabelTB_3.setObjectName(u"blockauthoritylabelTB_3")

        self.blockinfolabelsBlock_4.addWidget(self.blockauthoritylabelTB_3)

        self.blockoccupancylabelTB_3 = QLabel(self.verticalLayoutWidget_13)
        self.blockoccupancylabelTB_3.setObjectName(u"blockoccupancylabelTB_3")

        self.blockinfolabelsBlock_4.addWidget(self.blockoccupancylabelTB_3)

        self.label_2 = QLabel(self.verticalLayoutWidget_13)
        self.label_2.setObjectName(u"label_2")

        self.blockinfolabelsBlock_4.addWidget(self.label_2)

        self.blockNumber_4 = QLabel(self.verticalLayoutWidget_13)
        self.blockNumber_4.setObjectName(u"blockNumber_4")

        self.blockinfolabelsBlock_4.addWidget(self.blockNumber_4)

        self.blockLength_4 = QLabel(self.verticalLayoutWidget_13)
        self.blockLength_4.setObjectName(u"blockLength_4")

        self.blockinfolabelsBlock_4.addWidget(self.blockLength_4)

        self.blockGrade_4 = QLabel(self.verticalLayoutWidget_13)
        self.blockGrade_4.setObjectName(u"blockGrade_4")

        self.blockinfolabelsBlock_4.addWidget(self.blockGrade_4)

        self.maxspeedLimit_4 = QLabel(self.verticalLayoutWidget_13)
        self.maxspeedLimit_4.setObjectName(u"maxspeedLimit_4")

        self.blockinfolabelsBlock_4.addWidget(self.maxspeedLimit_4)

        self.label_27 = QLabel(self.verticalLayoutWidget_13)
        self.label_27.setObjectName(u"label_27")

        self.blockinfolabelsBlock_4.addWidget(self.label_27)

        self.label_28 = QLabel(self.verticalLayoutWidget_13)
        self.label_28.setObjectName(u"label_28")

        self.blockinfolabelsBlock_4.addWidget(self.label_28)

        self.verticalLayoutWidget_14 = QWidget(self.blockinfoGroup_3)
        self.verticalLayoutWidget_14.setObjectName(u"verticalLayoutWidget_14")
        self.verticalLayoutWidget_14.setGeometry(QRect(220, 20, 93, 281))
        self.blockinfooutputBlock_4 = QVBoxLayout(self.verticalLayoutWidget_14)
        self.blockinfooutputBlock_4.setObjectName(u"blockinfooutputBlock_4")
        self.blockinfooutputBlock_4.setContentsMargins(0, 0, 0, 0)
        self.sectionSelectedTM_O = QLabel(self.verticalLayoutWidget_14)
        self.sectionSelectedTM_O.setObjectName(u"sectionSelectedTM_O")

        self.blockinfooutputBlock_4.addWidget(self.sectionSelectedTM_O)

        self.blockAuthorityTM_O = QLabel(self.verticalLayoutWidget_14)
        self.blockAuthorityTM_O.setObjectName(u"blockAuthorityTM_O")

        self.blockinfooutputBlock_4.addWidget(self.blockAuthorityTM_O)

        self.blockoccupancyTM_O = QLabel(self.verticalLayoutWidget_14)
        self.blockoccupancyTM_O.setObjectName(u"blockoccupancyTM_O")

        self.blockinfooutputBlock_4.addWidget(self.blockoccupancyTM_O)

        self.undergroundTM_O = QLabel(self.verticalLayoutWidget_14)
        self.undergroundTM_O.setObjectName(u"undergroundTM_O")

        self.blockinfooutputBlock_4.addWidget(self.undergroundTM_O)

        self.blockNumberTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.blockNumberTM_O.setObjectName(u"blockNumberTM_O")
        font = QFont()
        font.setBold(True)
        self.blockNumberTM_O.setFont(font)
        self.blockNumberTM_O.setDigitCount(8)
        self.blockNumberTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.blockNumberTM_O)

        self.blockLengthTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.blockLengthTM_O.setObjectName(u"blockLengthTM_O")
        self.blockLengthTM_O.setFont(font)
        self.blockLengthTM_O.setDigitCount(8)
        self.blockLengthTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.blockLengthTM_O)

        self.blockGradeTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.blockGradeTM_O.setObjectName(u"blockGradeTM_O")
        self.blockGradeTM_O.setFont(font)
        self.blockGradeTM_O.setDigitCount(8)
        self.blockGradeTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.blockGradeTM_O)

        self.maxspeedlimitTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.maxspeedlimitTM_O.setObjectName(u"maxspeedlimitTM_O")
        self.maxspeedlimitTM_O.setFont(font)
        self.maxspeedlimitTM_O.setDigitCount(8)
        self.maxspeedlimitTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.maxspeedlimitTM_O)

        self.elevationTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.elevationTM_O.setObjectName(u"elevationTM_O")
        self.elevationTM_O.setFont(font)
        self.elevationTM_O.setDigitCount(8)
        self.elevationTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.elevationTM_O)

        self.cumulativeelevationTM_O = QLCDNumber(self.verticalLayoutWidget_14)
        self.cumulativeelevationTM_O.setObjectName(u"cumulativeelevationTM_O")
        self.cumulativeelevationTM_O.setFont(font)
        self.cumulativeelevationTM_O.setDigitCount(8)
        self.cumulativeelevationTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_4.addWidget(self.cumulativeelevationTM_O)

        self.verticalLayoutWidget_19 = QWidget(self.blockinfoGroup_3)
        self.verticalLayoutWidget_19.setObjectName(u"verticalLayoutWidget_19")
        self.verticalLayoutWidget_19.setGeometry(QRect(310, 20, 67, 281))
        self.blockinfoscaleBlock_4 = QVBoxLayout(self.verticalLayoutWidget_19)
        self.blockinfoscaleBlock_4.setObjectName(u"blockinfoscaleBlock_4")
        self.blockinfoscaleBlock_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.blockinfoscaleBlock_4.addItem(self.verticalSpacer_4)

        self.label_29 = QLabel(self.verticalLayoutWidget_19)
        self.label_29.setObjectName(u"label_29")

        self.blockinfoscaleBlock_4.addWidget(self.label_29)

        self.label_30 = QLabel(self.verticalLayoutWidget_19)
        self.label_30.setObjectName(u"label_30")

        self.blockinfoscaleBlock_4.addWidget(self.label_30)

        self.label_31 = QLabel(self.verticalLayoutWidget_19)
        self.label_31.setObjectName(u"label_31")

        self.blockinfoscaleBlock_4.addWidget(self.label_31)

        self.label_32 = QLabel(self.verticalLayoutWidget_19)
        self.label_32.setObjectName(u"label_32")

        self.blockinfoscaleBlock_4.addWidget(self.label_32)

        self.ft_label3_4 = QLabel(self.verticalLayoutWidget_19)
        self.ft_label3_4.setObjectName(u"ft_label3_4")

        self.blockinfoscaleBlock_4.addWidget(self.ft_label3_4)

        self.horizontalLayoutWidget_42 = QWidget(self.blockinfoGroup_3)
        self.horizontalLayoutWidget_42.setObjectName(u"horizontalLayoutWidget_42")
        self.horizontalLayoutWidget_42.setGeometry(QRect(10, 310, 211, 31))
        self.temperatureblock_4 = QHBoxLayout(self.horizontalLayoutWidget_42)
        self.temperatureblock_4.setObjectName(u"temperatureblock_4")
        self.temperatureblock_4.setContentsMargins(0, 0, 0, 0)
        self.temperature_4 = QLabel(self.horizontalLayoutWidget_42)
        self.temperature_4.setObjectName(u"temperature_4")

        self.temperatureblock_4.addWidget(self.temperature_4)

        self.temperatureTM_O = QLCDNumber(self.horizontalLayoutWidget_42)
        self.temperatureTM_O.setObjectName(u"temperatureTM_O")
        self.temperatureTM_O.setFont(font)
        self.temperatureTM_O.setSegmentStyle(QLCDNumber.Outline)

        self.temperatureblock_4.addWidget(self.temperatureTM_O)

        self.label_33 = QLabel(self.horizontalLayoutWidget_42)
        self.label_33.setObjectName(u"label_33")

        self.temperatureblock_4.addWidget(self.label_33)

        self.horizontalLayoutWidget_43 = QWidget(self.blockinfoGroup_3)
        self.horizontalLayoutWidget_43.setObjectName(u"horizontalLayoutWidget_43")
        self.horizontalLayoutWidget_43.setGeometry(QRect(10, 340, 211, 31))
        self.heatersblock_4 = QHBoxLayout(self.horizontalLayoutWidget_43)
        self.heatersblock_4.setObjectName(u"heatersblock_4")
        self.heatersblock_4.setContentsMargins(0, 0, 0, 0)
        self.heaters_4 = QLabel(self.horizontalLayoutWidget_43)
        self.heaters_4.setObjectName(u"heaters_4")

        self.heatersblock_4.addWidget(self.heaters_4)

        self.heatersTM_O = QLabel(self.horizontalLayoutWidget_43)
        self.heatersTM_O.setObjectName(u"heatersTM_O")

        self.heatersblock_4.addWidget(self.heatersTM_O)

        self.horizontalLayoutWidget_35 = QWidget(self.blockinfoGroup_3)
        self.horizontalLayoutWidget_35.setObjectName(u"horizontalLayoutWidget_35")
        self.horizontalLayoutWidget_35.setGeometry(QRect(10, 380, 171, 31))
        self.throughputblock = QHBoxLayout(self.horizontalLayoutWidget_35)
        self.throughputblock.setObjectName(u"throughputblock")
        self.throughputblock.setContentsMargins(0, 0, 0, 0)
        self.signalstatelableTM_2 = QLabel(self.horizontalLayoutWidget_35)
        self.signalstatelableTM_2.setObjectName(u"signalstatelableTM_2")

        self.throughputblock.addWidget(self.signalstatelableTM_2)

        self.throughputTM_O = QLabel(self.horizontalLayoutWidget_35)
        self.throughputTM_O.setObjectName(u"throughputTM_O")

        self.throughputblock.addWidget(self.throughputTM_O)

        self.horizontalLayoutWidget_47 = QWidget(self.blockinfoGroup_3)
        self.horizontalLayoutWidget_47.setObjectName(u"horizontalLayoutWidget_47")
        self.horizontalLayoutWidget_47.setGeometry(QRect(180, 380, 171, 31))
        self.throughputblock_2 = QHBoxLayout(self.horizontalLayoutWidget_47)
        self.throughputblock_2.setObjectName(u"throughputblock_2")
        self.throughputblock_2.setContentsMargins(0, 0, 0, 0)
        self.signalstatelableTM_3 = QLabel(self.horizontalLayoutWidget_47)
        self.signalstatelableTM_3.setObjectName(u"signalstatelableTM_3")

        self.throughputblock_2.addWidget(self.signalstatelableTM_3)

        self.passengersTM_O = QLabel(self.horizontalLayoutWidget_47)
        self.passengersTM_O.setObjectName(u"passengersTM_O")

        self.throughputblock_2.addWidget(self.passengersTM_O)

        self.stationdevicesgroup_2 = QGroupBox(self.trackMap)
        self.stationdevicesgroup_2.setObjectName(u"stationdevicesgroup_2")
        self.stationdevicesgroup_2.setGeometry(QRect(580, 560, 591, 191))
        self.ticketsalesTM_O_3 = QLabel(self.stationdevicesgroup_2)
        self.ticketsalesTM_O_3.setObjectName(u"ticketsalesTM_O_3")
        self.ticketsalesTM_O_3.setGeometry(QRect(120, 130, 60, 29))
        self.stationlabel_ID_TM_5 = QLabel(self.stationdevicesgroup_2)
        self.stationlabel_ID_TM_5.setObjectName(u"stationlabel_ID_TM_5")
        self.stationlabel_ID_TM_5.setGeometry(QRect(10, 20, 471, 161))
        self.stationlabel_ID_TM_5.setPixmap(QPixmap(u"Track_Model/main_ui/color key.png"))
        self.stationlabel_ID_TM_5.setScaledContents(True)
        self.tabWidget.addTab(self.trackMap, "")
        self.faultList = QWidget()
        self.faultList.setObjectName(u"faultList")
        self.faultlistTable = QTableWidget(self.faultList)
        if (self.faultlistTable.columnCount() < 6):
            self.faultlistTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.faultlistTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.faultlistTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.faultlistTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.faultlistTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.faultlistTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.faultlistTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.faultlistTable.setObjectName(u"faultlistTable")
        self.faultlistTable.setEnabled(True)
        self.faultlistTable.setGeometry(QRect(370, 10, 631, 711))
        self.faultlistTable.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.faultlistTable.setSortingEnabled(False)
        self.faultlistTable.setWordWrap(True)
        self.tabWidget.addTab(self.faultList, "")
        self.Testbench = QWidget()
        self.Testbench.setObjectName(u"Testbench")
        self.lineselectionsGroupTB = QGroupBox(self.Testbench)
        self.lineselectionsGroupTB.setObjectName(u"lineselectionsGroupTB")
        self.lineselectionsGroupTB.setGeometry(QRect(10, 20, 541, 71))
        self.horizontalLayoutWidget_3 = QWidget(self.lineselectionsGroupTB)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 30, 521, 31))
        self.lineselectionsBlockTB = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.lineselectionsBlockTB.setObjectName(u"lineselectionsBlockTB")
        self.lineselectionsBlockTB.setContentsMargins(0, 0, 0, 0)
        self.buttonRedTB = QPushButton(self.horizontalLayoutWidget_3)
        self.buttonRedTB.setObjectName(u"buttonRedTB")
        self.buttonRedTB.setEnabled(True)
        self.buttonRedTB.setCheckable(True)
        self.buttonRedTB.setAutoExclusive(True)

        self.lineselectionsBlockTB.addWidget(self.buttonRedTB)

        self.buttonGreenTB = QPushButton(self.horizontalLayoutWidget_3)
        self.buttonGreenTB.setObjectName(u"buttonGreenTB")
        self.buttonGreenTB.setEnabled(True)
        self.buttonGreenTB.setCheckable(True)
        self.buttonGreenTB.setAutoExclusive(True)

        self.lineselectionsBlockTB.addWidget(self.buttonGreenTB)

        self.testbenchInputsGroupTB = QGroupBox(self.Testbench)
        self.testbenchInputsGroupTB.setObjectName(u"testbenchInputsGroupTB")
        self.testbenchInputsGroupTB.setGeometry(QRect(570, 0, 341, 281))
        font2 = QFont()
        font2.setBold(False)
        self.testbenchInputsGroupTB.setFont(font2)
        self.verticalLayoutWidget_7 = QWidget(self.testbenchInputsGroupTB)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 20, 161, 91))
        self.environmentlabelsTBBlock = QVBoxLayout(self.verticalLayoutWidget_7)
        self.environmentlabelsTBBlock.setObjectName(u"environmentlabelsTBBlock")
        self.environmentlabelsTBBlock.setContentsMargins(0, 0, 0, 0)
        self.Derailment_2 = QLabel(self.verticalLayoutWidget_7)
        self.Derailment_2.setObjectName(u"Derailment_2")

        self.environmentlabelsTBBlock.addWidget(self.Derailment_2)

        self.trackcircuitFailure_2 = QLabel(self.verticalLayoutWidget_7)
        self.trackcircuitFailure_2.setObjectName(u"trackcircuitFailure_2")

        self.environmentlabelsTBBlock.addWidget(self.trackcircuitFailure_2)

        self.throughputTBlabel = QLabel(self.verticalLayoutWidget_7)
        self.throughputTBlabel.setObjectName(u"throughputTBlabel")

        self.environmentlabelsTBBlock.addWidget(self.throughputTBlabel)

        self.verticalLayoutWidget_8 = QWidget(self.testbenchInputsGroupTB)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(170, 20, 141, 91))
        self.environmentOutputsTBBlock = QVBoxLayout(self.verticalLayoutWidget_8)
        self.environmentOutputsTBBlock.setObjectName(u"environmentOutputsTBBlock")
        self.environmentOutputsTBBlock.setContentsMargins(0, 0, 0, 0)
        self.trackTemperatureTB_I = QLineEdit(self.verticalLayoutWidget_8)
        self.trackTemperatureTB_I.setObjectName(u"trackTemperatureTB_I")

        self.environmentOutputsTBBlock.addWidget(self.trackTemperatureTB_I)

        self.boardingCountTB_I = QLineEdit(self.verticalLayoutWidget_8)
        self.boardingCountTB_I.setObjectName(u"boardingCountTB_I")

        self.environmentOutputsTBBlock.addWidget(self.boardingCountTB_I)

        self.throughputTB_I = QLineEdit(self.verticalLayoutWidget_8)
        self.throughputTB_I.setObjectName(u"throughputTB_I")

        self.environmentOutputsTBBlock.addWidget(self.throughputTB_I)

        self.horizontalLayoutWidget_10 = QWidget(self.testbenchInputsGroupTB)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(10, 110, 301, 31))
        self.environmentalinputsblock = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.environmentalinputsblock.setObjectName(u"environmentalinputsblock")
        self.environmentalinputsblock.setContentsMargins(0, 0, 0, 0)
        self.settempTB_Button = QPushButton(self.horizontalLayoutWidget_10)
        self.settempTB_Button.setObjectName(u"settempTB_Button")

        self.environmentalinputsblock.addWidget(self.settempTB_Button)

        self.setboardingCountTB_button = QPushButton(self.horizontalLayoutWidget_10)
        self.setboardingCountTB_button.setObjectName(u"setboardingCountTB_button")

        self.environmentalinputsblock.addWidget(self.setboardingCountTB_button)

        self.setThroughputTB_Button = QPushButton(self.horizontalLayoutWidget_10)
        self.setThroughputTB_Button.setObjectName(u"setThroughputTB_Button")

        self.environmentalinputsblock.addWidget(self.setThroughputTB_Button)

        self.horizontalLayoutWidget_39 = QWidget(self.testbenchInputsGroupTB)
        self.horizontalLayoutWidget_39.setObjectName(u"horizontalLayoutWidget_39")
        self.horizontalLayoutWidget_39.setGeometry(QRect(10, 140, 301, 30))
        self.AuthOccblock = QHBoxLayout(self.horizontalLayoutWidget_39)
        self.AuthOccblock.setObjectName(u"AuthOccblock")
        self.AuthOccblock.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.horizontalLayoutWidget_39)
        self.label_19.setObjectName(u"label_19")

        self.AuthOccblock.addWidget(self.label_19)

        self.occupancyTB_Button = QPushButton(self.horizontalLayoutWidget_39)
        self.occupancyTB_Button.setObjectName(u"occupancyTB_Button")

        self.AuthOccblock.addWidget(self.occupancyTB_Button)

        self.horizontalLayoutWidget_40 = QWidget(self.testbenchInputsGroupTB)
        self.horizontalLayoutWidget_40.setObjectName(u"horizontalLayoutWidget_40")
        self.horizontalLayoutWidget_40.setGeometry(QRect(10, 180, 311, 30))
        self.AuthOccblock_2 = QHBoxLayout(self.horizontalLayoutWidget_40)
        self.AuthOccblock_2.setObjectName(u"AuthOccblock_2")
        self.AuthOccblock_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_40)
        self.label.setObjectName(u"label")

        self.AuthOccblock_2.addWidget(self.label)

        self.authorityTB_I = QLineEdit(self.horizontalLayoutWidget_40)
        self.authorityTB_I.setObjectName(u"authorityTB_I")

        self.AuthOccblock_2.addWidget(self.authorityTB_I)

        self.horizontalLayoutWidget_24 = QWidget(self.testbenchInputsGroupTB)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(10, 240, 321, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.adjustblocklabelTB = QLabel(self.horizontalLayoutWidget_24)
        self.adjustblocklabelTB.setObjectName(u"adjustblocklabelTB")

        self.horizontalLayout_4.addWidget(self.adjustblocklabelTB)

        self.setblockLengthTB_I = QLineEdit(self.horizontalLayoutWidget_24)
        self.setblockLengthTB_I.setObjectName(u"setblockLengthTB_I")

        self.horizontalLayout_4.addWidget(self.setblockLengthTB_I)

        self.label_18 = QLabel(self.horizontalLayoutWidget_24)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_18)

        self.setblockLengthTB_button = QPushButton(self.horizontalLayoutWidget_24)
        self.setblockLengthTB_button.setObjectName(u"setblockLengthTB_button")

        self.horizontalLayout_4.addWidget(self.setblockLengthTB_button)

        self.authorityTB_button = QPushButton(self.testbenchInputsGroupTB)
        self.authorityTB_button.setObjectName(u"authorityTB_button")
        self.authorityTB_button.setGeometry(QRect(210, 210, 93, 28))
        self.trackcontrollerInputsGroupTB = QGroupBox(self.Testbench)
        self.trackcontrollerInputsGroupTB.setObjectName(u"trackcontrollerInputsGroupTB")
        self.trackcontrollerInputsGroupTB.setGeometry(QRect(570, 280, 341, 321))
        self.horizontalLayoutWidget_5 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 150, 291, 31))
        self.signalBlockTB = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.signalBlockTB.setObjectName(u"signalBlockTB")
        self.signalBlockTB.setContentsMargins(0, 0, 0, 0)
        self.blocksignalControl = QLabel(self.horizontalLayoutWidget_5)
        self.blocksignalControl.setObjectName(u"blocksignalControl")

        self.signalBlockTB.addWidget(self.blocksignalControl)

        self.signalToggle_Button = QPushButton(self.horizontalLayoutWidget_5)
        self.signalToggle_Button.setObjectName(u"signalToggle_Button")
        self.signalToggle_Button.setEnabled(True)

        self.signalBlockTB.addWidget(self.signalToggle_Button)

        self.horizontalLayoutWidget_6 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 250, 291, 31))
        self.crossingBlockTB = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.crossingBlockTB.setObjectName(u"crossingBlockTB")
        self.crossingBlockTB.setContentsMargins(0, 0, 0, 0)
        self.crossingControlLabel = QLabel(self.horizontalLayoutWidget_6)
        self.crossingControlLabel.setObjectName(u"crossingControlLabel")

        self.crossingBlockTB.addWidget(self.crossingControlLabel)

        self.crossingToggle_Button = QPushButton(self.horizontalLayoutWidget_6)
        self.crossingToggle_Button.setObjectName(u"crossingToggle_Button")
        self.crossingToggle_Button.setEnabled(True)

        self.crossingBlockTB.addWidget(self.crossingToggle_Button)

        self.horizontalLayoutWidget_4 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 50, 291, 31))
        self.trackSwitchBlockTB = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.trackSwitchBlockTB.setObjectName(u"trackSwitchBlockTB")
        self.trackSwitchBlockTB.setContentsMargins(0, 0, 0, 0)
        self.trackcontrolSwitch = QLabel(self.horizontalLayoutWidget_4)
        self.trackcontrolSwitch.setObjectName(u"trackcontrolSwitch")

        self.trackSwitchBlockTB.addWidget(self.trackcontrolSwitch)

        self.switchToggle_Button = QPushButton(self.horizontalLayoutWidget_4)
        self.switchToggle_Button.setObjectName(u"switchToggle_Button")
        self.switchToggle_Button.setCheckable(False)
        self.switchToggle_Button.setAutoExclusive(False)

        self.trackSwitchBlockTB.addWidget(self.switchToggle_Button)

        self.horizontalLayoutWidget_7 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 80, 261, 31))
        self.trackswitchOutputsTB = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.trackswitchOutputsTB.setObjectName(u"trackswitchOutputsTB")
        self.trackswitchOutputsTB.setContentsMargins(0, 0, 0, 0)
        self.trackswitchdirectionLabel_TB = QLabel(self.horizontalLayoutWidget_7)
        self.trackswitchdirectionLabel_TB.setObjectName(u"trackswitchdirectionLabel_TB")

        self.trackswitchOutputsTB.addWidget(self.trackswitchdirectionLabel_TB)

        self.switchFromTB_O = QLabel(self.horizontalLayoutWidget_7)
        self.switchFromTB_O.setObjectName(u"switchFromTB_O")

        self.trackswitchOutputsTB.addWidget(self.switchFromTB_O)

        self.directionLabelTB = QLabel(self.horizontalLayoutWidget_7)
        self.directionLabelTB.setObjectName(u"directionLabelTB")

        self.trackswitchOutputsTB.addWidget(self.directionLabelTB)

        self.switchToTB_O = QLabel(self.horizontalLayoutWidget_7)
        self.switchToTB_O.setObjectName(u"switchToTB_O")

        self.trackswitchOutputsTB.addWidget(self.switchToTB_O)

        self.horizontalLayoutWidget_8 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 180, 151, 31))
        self.signalOutputBlockTB = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.signalOutputBlockTB.setObjectName(u"signalOutputBlockTB")
        self.signalOutputBlockTB.setContentsMargins(0, 0, 0, 0)
        self.signalLabel_TB = QLabel(self.horizontalLayoutWidget_8)
        self.signalLabel_TB.setObjectName(u"signalLabel_TB")

        self.signalOutputBlockTB.addWidget(self.signalLabel_TB)

        self.signalStateTB_O = QLabel(self.horizontalLayoutWidget_8)
        self.signalStateTB_O.setObjectName(u"signalStateTB_O")

        self.signalOutputBlockTB.addWidget(self.signalStateTB_O)

        self.horizontalLayoutWidget_9 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 280, 151, 31))
        self.crossingControlOutputsTB = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.crossingControlOutputsTB.setObjectName(u"crossingControlOutputsTB")
        self.crossingControlOutputsTB.setContentsMargins(0, 0, 0, 0)
        self.crossingLabel_TB = QLabel(self.horizontalLayoutWidget_9)
        self.crossingLabel_TB.setObjectName(u"crossingLabel_TB")

        self.crossingControlOutputsTB.addWidget(self.crossingLabel_TB)

        self.crossingStateTB_O = QLabel(self.horizontalLayoutWidget_9)
        self.crossingStateTB_O.setObjectName(u"crossingStateTB_O")
        self.crossingStateTB_O.setEnabled(True)

        self.crossingControlOutputsTB.addWidget(self.crossingStateTB_O)

        self.horizontalLayoutWidget_23 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(10, 20, 151, 31))
        self.switchidblock_3 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.switchidblock_3.setObjectName(u"switchidblock_3")
        self.switchidblock_3.setContentsMargins(0, 0, 0, 0)
        self.switchlabe_ID_TM_3 = QLabel(self.horizontalLayoutWidget_23)
        self.switchlabe_ID_TM_3.setObjectName(u"switchlabe_ID_TM_3")

        self.switchidblock_3.addWidget(self.switchlabe_ID_TM_3)

        self.switchIDTB_O = QLabel(self.horizontalLayoutWidget_23)
        self.switchIDTB_O.setObjectName(u"switchIDTB_O")

        self.switchidblock_3.addWidget(self.switchIDTB_O)

        self.horizontalLayoutWidget_27 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_27.setObjectName(u"horizontalLayoutWidget_27")
        self.horizontalLayoutWidget_27.setGeometry(QRect(10, 120, 151, 31))
        self.signalIDblock_2 = QHBoxLayout(self.horizontalLayoutWidget_27)
        self.signalIDblock_2.setObjectName(u"signalIDblock_2")
        self.signalIDblock_2.setContentsMargins(0, 0, 0, 0)
        self.signalidlabelTM_2 = QLabel(self.horizontalLayoutWidget_27)
        self.signalidlabelTM_2.setObjectName(u"signalidlabelTM_2")

        self.signalIDblock_2.addWidget(self.signalidlabelTM_2)

        self.signalIDTB_O = QLabel(self.horizontalLayoutWidget_27)
        self.signalIDTB_O.setObjectName(u"signalIDTB_O")

        self.signalIDblock_2.addWidget(self.signalIDTB_O)

        self.horizontalLayoutWidget_25 = QWidget(self.trackcontrollerInputsGroupTB)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(10, 220, 151, 31))
        self.crossingIDblock_TM_2 = QHBoxLayout(self.horizontalLayoutWidget_25)
        self.crossingIDblock_TM_2.setObjectName(u"crossingIDblock_TM_2")
        self.crossingIDblock_TM_2.setContentsMargins(0, 0, 0, 0)
        self.crossingIDlabel_TM_2 = QLabel(self.horizontalLayoutWidget_25)
        self.crossingIDlabel_TM_2.setObjectName(u"crossingIDlabel_TM_2")

        self.crossingIDblock_TM_2.addWidget(self.crossingIDlabel_TM_2)

        self.crossingIDTB_O = QLabel(self.horizontalLayoutWidget_25)
        self.crossingIDTB_O.setObjectName(u"crossingIDTB_O")

        self.crossingIDblock_TM_2.addWidget(self.crossingIDTB_O)

        self.graphicsView_2 = QGraphicsView(self.Testbench)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(10, 100, 541, 651))
        self.graphicsView_2.setDragMode(QGraphicsView.ScrollHandDrag)
        self.murphyInputsGroupTB = QGroupBox(self.Testbench)
        self.murphyInputsGroupTB.setObjectName(u"murphyInputsGroupTB")
        self.murphyInputsGroupTB.setGeometry(QRect(570, 600, 341, 151))
        self.verticalLayoutWidget_15 = QWidget(self.murphyInputsGroupTB)
        self.verticalLayoutWidget_15.setObjectName(u"verticalLayoutWidget_15")
        self.verticalLayoutWidget_15.setGeometry(QRect(10, 20, 160, 80))
        self.murphylabelsBlockTB = QVBoxLayout(self.verticalLayoutWidget_15)
        self.murphylabelsBlockTB.setObjectName(u"murphylabelsBlockTB")
        self.murphylabelsBlockTB.setContentsMargins(0, 0, 0, 0)
        self.brokenTrackLabelTB_M = QLabel(self.verticalLayoutWidget_15)
        self.brokenTrackLabelTB_M.setObjectName(u"brokenTrackLabelTB_M")

        self.murphylabelsBlockTB.addWidget(self.brokenTrackLabelTB_M)

        self.trackcircuitFailureTB_M = QLabel(self.verticalLayoutWidget_15)
        self.trackcircuitFailureTB_M.setObjectName(u"trackcircuitFailureTB_M")

        self.murphylabelsBlockTB.addWidget(self.trackcircuitFailureTB_M)

        self.powerFailureLabelTB_M = QLabel(self.verticalLayoutWidget_15)
        self.powerFailureLabelTB_M.setObjectName(u"powerFailureLabelTB_M")

        self.murphylabelsBlockTB.addWidget(self.powerFailureLabelTB_M)

        self.verticalLayoutWidget_16 = QWidget(self.murphyInputsGroupTB)
        self.verticalLayoutWidget_16.setObjectName(u"verticalLayoutWidget_16")
        self.verticalLayoutWidget_16.setGeometry(QRect(170, 20, 160, 100))
        self.murphyOutputsBlockTB = QVBoxLayout(self.verticalLayoutWidget_16)
        self.murphyOutputsBlockTB.setObjectName(u"murphyOutputsBlockTB")
        self.murphyOutputsBlockTB.setContentsMargins(0, 0, 0, 0)
        self.railtestTB_Button = QPushButton(self.verticalLayoutWidget_16)
        self.railtestTB_Button.setObjectName(u"railtestTB_Button")

        self.murphyOutputsBlockTB.addWidget(self.railtestTB_Button)

        self.circuittestTB_Button = QPushButton(self.verticalLayoutWidget_16)
        self.circuittestTB_Button.setObjectName(u"circuittestTB_Button")

        self.murphyOutputsBlockTB.addWidget(self.circuittestTB_Button)

        self.powertestTB_Button = QPushButton(self.verticalLayoutWidget_16)
        self.powertestTB_Button.setObjectName(u"powertestTB_Button")

        self.murphyOutputsBlockTB.addWidget(self.powertestTB_Button)

        self.resetfaultTB_button = QPushButton(self.murphyInputsGroupTB)
        self.resetfaultTB_button.setObjectName(u"resetfaultTB_button")
        self.resetfaultTB_button.setGeometry(QRect(210, 120, 75, 23))
        self.faultsGroupTB = QGroupBox(self.Testbench)
        self.faultsGroupTB.setObjectName(u"faultsGroupTB")
        self.faultsGroupTB.setGeometry(QRect(920, 0, 331, 111))
        self.verticalLayoutWidget_17 = QWidget(self.faultsGroupTB)
        self.verticalLayoutWidget_17.setObjectName(u"verticalLayoutWidget_17")
        self.verticalLayoutWidget_17.setGeometry(QRect(9, 20, 171, 80))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.brokentrackLabelTB = QLabel(self.verticalLayoutWidget_17)
        self.brokentrackLabelTB.setObjectName(u"brokentrackLabelTB")

        self.verticalLayout_9.addWidget(self.brokentrackLabelTB)

        self.trackcircuitfailureLabelTB = QLabel(self.verticalLayoutWidget_17)
        self.trackcircuitfailureLabelTB.setObjectName(u"trackcircuitfailureLabelTB")

        self.verticalLayout_9.addWidget(self.trackcircuitfailureLabelTB)

        self.powerfailureLabelTB = QLabel(self.verticalLayoutWidget_17)
        self.powerfailureLabelTB.setObjectName(u"powerfailureLabelTB")

        self.verticalLayout_9.addWidget(self.powerfailureLabelTB)

        self.verticalLayoutWidget_18 = QWidget(self.faultsGroupTB)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(180, 20, 141, 81))
        self.faultsoutputBlockTB = QVBoxLayout(self.verticalLayoutWidget_18)
        self.faultsoutputBlockTB.setObjectName(u"faultsoutputBlockTB")
        self.faultsoutputBlockTB.setContentsMargins(0, 0, 0, 0)
        self.brokenrailTB_O = QLabel(self.verticalLayoutWidget_18)
        self.brokenrailTB_O.setObjectName(u"brokenrailTB_O")

        self.faultsoutputBlockTB.addWidget(self.brokenrailTB_O)

        self.trackcircuitFailureTB_O = QLabel(self.verticalLayoutWidget_18)
        self.trackcircuitFailureTB_O.setObjectName(u"trackcircuitFailureTB_O")

        self.faultsoutputBlockTB.addWidget(self.trackcircuitFailureTB_O)

        self.powerFailureTB_O = QLabel(self.verticalLayoutWidget_18)
        self.powerFailureTB_O.setObjectName(u"powerFailureTB_O")

        self.faultsoutputBlockTB.addWidget(self.powerFailureTB_O)

        self.blockinfoGroup_2 = QGroupBox(self.Testbench)
        self.blockinfoGroup_2.setObjectName(u"blockinfoGroup_2")
        self.blockinfoGroup_2.setGeometry(QRect(920, 120, 331, 361))
        self.verticalLayoutWidget_9 = QWidget(self.blockinfoGroup_2)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 20, 120, 261))
        self.blockinfolabelsBlock_2 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.blockinfolabelsBlock_2.setObjectName(u"blockinfolabelsBlock_2")
        self.blockinfolabelsBlock_2.setContentsMargins(0, 0, 0, 0)
        self.segmentSelected_2 = QLabel(self.verticalLayoutWidget_9)
        self.segmentSelected_2.setObjectName(u"segmentSelected_2")

        self.blockinfolabelsBlock_2.addWidget(self.segmentSelected_2)

        self.blockauthoritylabelTB = QLabel(self.verticalLayoutWidget_9)
        self.blockauthoritylabelTB.setObjectName(u"blockauthoritylabelTB")

        self.blockinfolabelsBlock_2.addWidget(self.blockauthoritylabelTB)

        self.blockoccupancylabelTB = QLabel(self.verticalLayoutWidget_9)
        self.blockoccupancylabelTB.setObjectName(u"blockoccupancylabelTB")

        self.blockinfolabelsBlock_2.addWidget(self.blockoccupancylabelTB)

        self.undergroundTBlabel = QLabel(self.verticalLayoutWidget_9)
        self.undergroundTBlabel.setObjectName(u"undergroundTBlabel")

        self.blockinfolabelsBlock_2.addWidget(self.undergroundTBlabel)

        self.blockNumber_2 = QLabel(self.verticalLayoutWidget_9)
        self.blockNumber_2.setObjectName(u"blockNumber_2")

        self.blockinfolabelsBlock_2.addWidget(self.blockNumber_2)

        self.blockLength_2 = QLabel(self.verticalLayoutWidget_9)
        self.blockLength_2.setObjectName(u"blockLength_2")

        self.blockinfolabelsBlock_2.addWidget(self.blockLength_2)

        self.blockGrade_2 = QLabel(self.verticalLayoutWidget_9)
        self.blockGrade_2.setObjectName(u"blockGrade_2")

        self.blockinfolabelsBlock_2.addWidget(self.blockGrade_2)

        self.maxspeedLimit_2 = QLabel(self.verticalLayoutWidget_9)
        self.maxspeedLimit_2.setObjectName(u"maxspeedLimit_2")

        self.blockinfolabelsBlock_2.addWidget(self.maxspeedLimit_2)

        self.label_11 = QLabel(self.verticalLayoutWidget_9)
        self.label_11.setObjectName(u"label_11")

        self.blockinfolabelsBlock_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget_9)
        self.label_12.setObjectName(u"label_12")

        self.blockinfolabelsBlock_2.addWidget(self.label_12)

        self.verticalLayoutWidget_10 = QWidget(self.blockinfoGroup_2)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(170, 20, 93, 267))
        self.blockinfooutputBlock_2 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.blockinfooutputBlock_2.setObjectName(u"blockinfooutputBlock_2")
        self.blockinfooutputBlock_2.setContentsMargins(0, 0, 0, 0)
        self.sectionSelectedTB_O = QLabel(self.verticalLayoutWidget_10)
        self.sectionSelectedTB_O.setObjectName(u"sectionSelectedTB_O")

        self.blockinfooutputBlock_2.addWidget(self.sectionSelectedTB_O)

        self.blockAuthorityTB_O = QLabel(self.verticalLayoutWidget_10)
        self.blockAuthorityTB_O.setObjectName(u"blockAuthorityTB_O")

        self.blockinfooutputBlock_2.addWidget(self.blockAuthorityTB_O)

        self.blockoccupancyTB_O = QLabel(self.verticalLayoutWidget_10)
        self.blockoccupancyTB_O.setObjectName(u"blockoccupancyTB_O")

        self.blockinfooutputBlock_2.addWidget(self.blockoccupancyTB_O)

        self.undrgroundTB_O = QLabel(self.verticalLayoutWidget_10)
        self.undrgroundTB_O.setObjectName(u"undrgroundTB_O")

        self.blockinfooutputBlock_2.addWidget(self.undrgroundTB_O)

        self.blockNumberTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.blockNumberTB_O.setObjectName(u"blockNumberTB_O")
        self.blockNumberTB_O.setFont(font)
        self.blockNumberTB_O.setDigitCount(8)
        self.blockNumberTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.blockNumberTB_O)

        self.blockLengthTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.blockLengthTB_O.setObjectName(u"blockLengthTB_O")
        self.blockLengthTB_O.setFont(font)
        self.blockLengthTB_O.setDigitCount(8)
        self.blockLengthTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.blockLengthTB_O)

        self.blockGradeTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.blockGradeTB_O.setObjectName(u"blockGradeTB_O")
        self.blockGradeTB_O.setFont(font)
        self.blockGradeTB_O.setDigitCount(8)
        self.blockGradeTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.blockGradeTB_O)

        self.maxspeedlimitTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.maxspeedlimitTB_O.setObjectName(u"maxspeedlimitTB_O")
        self.maxspeedlimitTB_O.setFont(font)
        self.maxspeedlimitTB_O.setDigitCount(8)
        self.maxspeedlimitTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.maxspeedlimitTB_O)

        self.elevationTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.elevationTB_O.setObjectName(u"elevationTB_O")
        self.elevationTB_O.setFont(font)
        self.elevationTB_O.setDigitCount(8)
        self.elevationTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.elevationTB_O)

        self.cumulativeelevationTB_O = QLCDNumber(self.verticalLayoutWidget_10)
        self.cumulativeelevationTB_O.setObjectName(u"cumulativeelevationTB_O")
        self.cumulativeelevationTB_O.setFont(font)
        self.cumulativeelevationTB_O.setDigitCount(8)
        self.cumulativeelevationTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.blockinfooutputBlock_2.addWidget(self.cumulativeelevationTB_O)

        self.verticalLayoutWidget_2 = QWidget(self.blockinfoGroup_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(270, 20, 41, 261))
        self.blockinfoscaleBlock_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.blockinfoscaleBlock_2.setObjectName(u"blockinfoscaleBlock_2")
        self.blockinfoscaleBlock_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.blockinfoscaleBlock_2.addItem(self.verticalSpacer_2)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.blockinfoscaleBlock_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.blockinfoscaleBlock_2.addWidget(self.label_14)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.blockinfoscaleBlock_2.addWidget(self.label_15)

        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.blockinfoscaleBlock_2.addWidget(self.label_16)

        self.ft_label3_2 = QLabel(self.verticalLayoutWidget_2)
        self.ft_label3_2.setObjectName(u"ft_label3_2")

        self.blockinfoscaleBlock_2.addWidget(self.ft_label3_2)

        self.horizontalLayoutWidget_33 = QWidget(self.blockinfoGroup_2)
        self.horizontalLayoutWidget_33.setObjectName(u"horizontalLayoutWidget_33")
        self.horizontalLayoutWidget_33.setGeometry(QRect(10, 290, 211, 31))
        self.temperatureblock_2 = QHBoxLayout(self.horizontalLayoutWidget_33)
        self.temperatureblock_2.setObjectName(u"temperatureblock_2")
        self.temperatureblock_2.setContentsMargins(0, 0, 0, 0)
        self.temperature_2 = QLabel(self.horizontalLayoutWidget_33)
        self.temperature_2.setObjectName(u"temperature_2")

        self.temperatureblock_2.addWidget(self.temperature_2)

        self.temperatureTB_O = QLCDNumber(self.horizontalLayoutWidget_33)
        self.temperatureTB_O.setObjectName(u"temperatureTB_O")
        self.temperatureTB_O.setFont(font)
        self.temperatureTB_O.setSegmentStyle(QLCDNumber.Outline)

        self.temperatureblock_2.addWidget(self.temperatureTB_O)

        self.label_17 = QLabel(self.horizontalLayoutWidget_33)
        self.label_17.setObjectName(u"label_17")

        self.temperatureblock_2.addWidget(self.label_17)

        self.horizontalLayoutWidget_34 = QWidget(self.blockinfoGroup_2)
        self.horizontalLayoutWidget_34.setObjectName(u"horizontalLayoutWidget_34")
        self.horizontalLayoutWidget_34.setGeometry(QRect(10, 320, 211, 31))
        self.heatersblock_2 = QHBoxLayout(self.horizontalLayoutWidget_34)
        self.heatersblock_2.setObjectName(u"heatersblock_2")
        self.heatersblock_2.setContentsMargins(0, 0, 0, 0)
        self.heaters_2 = QLabel(self.horizontalLayoutWidget_34)
        self.heaters_2.setObjectName(u"heaters_2")

        self.heatersblock_2.addWidget(self.heaters_2)

        self.heatersTB_O = QLabel(self.horizontalLayoutWidget_34)
        self.heatersTB_O.setObjectName(u"heatersTB_O")

        self.heatersblock_2.addWidget(self.heatersTB_O)

        self.AuthorityboolTB = QLabel(self.blockinfoGroup_2)
        self.AuthorityboolTB.setObjectName(u"AuthorityboolTB")
        self.AuthorityboolTB.setGeometry(QRect(120, 50, 51, 20))
        self.environmentalvariablesGroup_3 = QGroupBox(self.Testbench)
        self.environmentalvariablesGroup_3.setObjectName(u"environmentalvariablesGroup_3")
        self.environmentalvariablesGroup_3.setGeometry(QRect(920, 480, 331, 271))
        self.horizontalLayoutWidget_29 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_29.setObjectName(u"horizontalLayoutWidget_29")
        self.horizontalLayoutWidget_29.setGeometry(QRect(10, 110, 171, 31))
        self.beacon1TBblock = QHBoxLayout(self.horizontalLayoutWidget_29)
        self.beacon1TBblock.setObjectName(u"beacon1TBblock")
        self.beacon1TBblock.setContentsMargins(0, 0, 0, 0)
        self.beacon1label_TM_2 = QLabel(self.horizontalLayoutWidget_29)
        self.beacon1label_TM_2.setObjectName(u"beacon1label_TM_2")

        self.beacon1TBblock.addWidget(self.beacon1label_TM_2)

        self.beaconTB_O = QLabel(self.horizontalLayoutWidget_29)
        self.beaconTB_O.setObjectName(u"beaconTB_O")

        self.beacon1TBblock.addWidget(self.beaconTB_O)

        self.horizontalLayoutWidget_30 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_30.setObjectName(u"horizontalLayoutWidget_30")
        self.horizontalLayoutWidget_30.setGeometry(QRect(10, 20, 171, 31))
        self.stationidblock_2 = QHBoxLayout(self.horizontalLayoutWidget_30)
        self.stationidblock_2.setObjectName(u"stationidblock_2")
        self.stationidblock_2.setContentsMargins(0, 0, 0, 0)
        self.stationlabel_ID_TM_2 = QLabel(self.horizontalLayoutWidget_30)
        self.stationlabel_ID_TM_2.setObjectName(u"stationlabel_ID_TM_2")

        self.stationidblock_2.addWidget(self.stationlabel_ID_TM_2)

        self.stationIDTB_O = QLabel(self.horizontalLayoutWidget_30)
        self.stationIDTB_O.setObjectName(u"stationIDTB_O")

        self.stationidblock_2.addWidget(self.stationIDTB_O)

        self.horizontalLayoutWidget_31 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_31.setObjectName(u"horizontalLayoutWidget_31")
        self.horizontalLayoutWidget_31.setGeometry(QRect(10, 140, 171, 31))
        self.beacon2block_2 = QHBoxLayout(self.horizontalLayoutWidget_31)
        self.beacon2block_2.setObjectName(u"beacon2block_2")
        self.beacon2block_2.setContentsMargins(0, 0, 0, 0)
        self.beacon2label_TM_2 = QLabel(self.horizontalLayoutWidget_31)
        self.beacon2label_TM_2.setObjectName(u"beacon2label_TM_2")

        self.beacon2block_2.addWidget(self.beacon2label_TM_2)

        self.beacon2TB_O = QLabel(self.horizontalLayoutWidget_31)
        self.beacon2TB_O.setObjectName(u"beacon2TB_O")

        self.beacon2block_2.addWidget(self.beacon2TB_O)

        self.horizontalLayoutWidget_32 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_32.setObjectName(u"horizontalLayoutWidget_32")
        self.horizontalLayoutWidget_32.setGeometry(QRect(10, 80, 171, 31))
        self.beacon1block_2 = QHBoxLayout(self.horizontalLayoutWidget_32)
        self.beacon1block_2.setObjectName(u"beacon1block_2")
        self.beacon1block_2.setContentsMargins(0, 0, 0, 0)
        self.stationexit_TM_2 = QLabel(self.horizontalLayoutWidget_32)
        self.stationexit_TM_2.setObjectName(u"stationexit_TM_2")

        self.beacon1block_2.addWidget(self.stationexit_TM_2)

        self.stationexitTB_O = QLabel(self.horizontalLayoutWidget_32)
        self.stationexitTB_O.setObjectName(u"stationexitTB_O")

        self.beacon1block_2.addWidget(self.stationexitTB_O)

        self.horizontalLayoutWidget_28 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_28.setObjectName(u"horizontalLayoutWidget_28")
        self.horizontalLayoutWidget_28.setGeometry(QRect(10, 50, 171, 31))
        self.stationnameTMblock_2 = QHBoxLayout(self.horizontalLayoutWidget_28)
        self.stationnameTMblock_2.setObjectName(u"stationnameTMblock_2")
        self.stationnameTMblock_2.setContentsMargins(0, 0, 0, 0)
        self.stationlabel_ID_TM_4 = QLabel(self.horizontalLayoutWidget_28)
        self.stationlabel_ID_TM_4.setObjectName(u"stationlabel_ID_TM_4")

        self.stationnameTMblock_2.addWidget(self.stationlabel_ID_TM_4)

        self.stationNameTB_O = QLabel(self.horizontalLayoutWidget_28)
        self.stationNameTB_O.setObjectName(u"stationNameTB_O")

        self.stationnameTMblock_2.addWidget(self.stationNameTB_O)

        self.horizontalLayoutWidget_38 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_38.setObjectName(u"horizontalLayoutWidget_38")
        self.horizontalLayoutWidget_38.setGeometry(QRect(10, 170, 171, 31))
        self.throughputblock_4 = QHBoxLayout(self.horizontalLayoutWidget_38)
        self.throughputblock_4.setObjectName(u"throughputblock_4")
        self.throughputblock_4.setContentsMargins(0, 0, 0, 0)
        self.signalstatelableTM_5 = QLabel(self.horizontalLayoutWidget_38)
        self.signalstatelableTM_5.setObjectName(u"signalstatelableTM_5")

        self.throughputblock_4.addWidget(self.signalstatelableTM_5)

        self.throughputTB_O = QLabel(self.horizontalLayoutWidget_38)
        self.throughputTB_O.setObjectName(u"throughputTB_O")

        self.throughputblock_4.addWidget(self.throughputTB_O)

        self.horizontalLayoutWidget_37 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_37.setObjectName(u"horizontalLayoutWidget_37")
        self.horizontalLayoutWidget_37.setGeometry(QRect(10, 200, 171, 31))
        self.throughputblock_3 = QHBoxLayout(self.horizontalLayoutWidget_37)
        self.throughputblock_3.setObjectName(u"throughputblock_3")
        self.throughputblock_3.setContentsMargins(0, 0, 0, 0)
        self.signalstatelableTM_4 = QLabel(self.horizontalLayoutWidget_37)
        self.signalstatelableTM_4.setObjectName(u"signalstatelableTM_4")

        self.throughputblock_3.addWidget(self.signalstatelableTM_4)

        self.ticketsalesTB_O = QLabel(self.horizontalLayoutWidget_37)
        self.ticketsalesTB_O.setObjectName(u"ticketsalesTB_O")

        self.throughputblock_3.addWidget(self.ticketsalesTB_O)

        self.verticalLayoutWidget = QWidget(self.environmentalvariablesGroup_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 20, 111, 41))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inittrainTB_button = QPushButton(self.verticalLayoutWidget)
        self.inittrainTB_button.setObjectName(u"inittrainTB_button")

        self.verticalLayout.addWidget(self.inittrainTB_button)

        self.horizontalLayoutWidget_44 = QWidget(self.environmentalvariablesGroup_3)
        self.horizontalLayoutWidget_44.setObjectName(u"horizontalLayoutWidget_44")
        self.horizontalLayoutWidget_44.setGeometry(QRect(10, 230, 171, 31))
        self.polarityblockTB = QHBoxLayout(self.horizontalLayoutWidget_44)
        self.polarityblockTB.setObjectName(u"polarityblockTB")
        self.polarityblockTB.setContentsMargins(0, 0, 0, 0)
        self.polaritylabelTB = QLabel(self.horizontalLayoutWidget_44)
        self.polaritylabelTB.setObjectName(u"polaritylabelTB")

        self.polarityblockTB.addWidget(self.polaritylabelTB)

        self.PolarityTB_O = QLabel(self.horizontalLayoutWidget_44)
        self.PolarityTB_O.setObjectName(u"PolarityTB_O")

        self.polarityblockTB.addWidget(self.PolarityTB_O)

        self.tabWidget.addTab(self.Testbench, "")
        self.trackmodelheaderLabel = QLabel(self.simulationSpeedBlock)
        self.trackmodelheaderLabel.setObjectName(u"trackmodelheaderLabel")
        self.trackmodelheaderLabel.setGeometry(QRect(80, 0, 211, 51))
        font3 = QFont()
        font3.setPointSize(20)
        self.trackmodelheaderLabel.setFont(font3)
        self.image = QLabel(self.simulationSpeedBlock)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 71, 51))
        self.image.setPixmap(QPixmap(u"Track_Model/main_ui/AuroraLogo.jpg"))
        self.image.setScaledContents(True)
        self.horizontalLayoutWidget_2 = QWidget(self.simulationSpeedBlock)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(1070, 10, 171, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.time_label = QLabel(self.horizontalLayoutWidget_2)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout_2.addWidget(self.time_label)

        self.yellow = QLabel(self.simulationSpeedBlock)
        self.yellow.setObjectName(u"yellow")
        self.yellow.setGeometry(QRect(0, 0, 1261, 51))
        self.yellow.setFrameShape(QFrame.WinPanel)
        self.yellow.setPixmap(QPixmap(u"Track_Model/main_ui/aurora_banner.jpg"))
        self.yellow.setScaledContents(True)
        self.layoutWidget = QWidget(self.simulationSpeedBlock)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(540, 7, 271, 52))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_6)

        self.simslider = QSlider(self.layoutWidget)
        self.simslider.setObjectName(u"simslider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(5)
        sizePolicy4.setHeightForWidth(self.simslider.sizePolicy().hasHeightForWidth())
        self.simslider.setSizePolicy(sizePolicy4)
        self.simslider.setCursor(QCursor(Qt.SizeHorCursor))
        self.simslider.setMinimum(1)
        self.simslider.setMaximum(60)
        self.simslider.setSingleStep(1)
        self.simslider.setPageStep(10)
        self.simslider.setOrientation(Qt.Horizontal)
        self.simslider.setInvertedAppearance(False)
        self.simslider.setInvertedControls(False)
        self.simslider.setTickPosition(QSlider.TicksBelow)
        self.simslider.setTickInterval(10)

        self.verticalLayout_2.addWidget(self.simslider)

        self.pause_button = QPushButton(self.simulationSpeedBlock)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setGeometry(QRect(410, 10, 75, 31))
        TrackModel.setCentralWidget(self.simulationSpeedBlock)
        self.yellow.raise_()
        self.tabWidget.raise_()
        self.trackmodelheaderLabel.raise_()
        self.image.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.layoutWidget.raise_()
        self.pause_button.raise_()
        self.menubar = QMenuBar(TrackModel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1261, 26))
        self.menubar.setDefaultUp(True)
        self.menuTraick_Model = QMenu(self.menubar)
        self.menuTraick_Model.setObjectName(u"menuTraick_Model")
        self.menuFault_List = QMenu(self.menubar)
        self.menuFault_List.setObjectName(u"menuFault_List")
        self.menuFault_List.setTearOffEnabled(False)
        self.menuFault_List.setSeparatorsCollapsible(True)
        self.menuTestBench = QMenu(self.menubar)
        self.menuTestBench.setObjectName(u"menuTestBench")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        TrackModel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TrackModel)
        self.statusbar.setObjectName(u"statusbar")
        TrackModel.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTraick_Model.menuAction())
        self.menubar.addAction(self.menuFault_List.menuAction())
        self.menubar.addAction(self.menuTestBench.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(TrackModel)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TrackModel)
    # setupUi

    def retranslateUi(self, TrackModel):
        TrackModel.setWindowTitle(QCoreApplication.translate("TrackModel", u"Track Model", None))
        self.faultsGroup.setTitle(QCoreApplication.translate("TrackModel", u"Faults on Selected Block", None))
        self.brokenRail.setText(QCoreApplication.translate("TrackModel", u"Broken Rail", None))
        self.trackcircuitFailure.setText(QCoreApplication.translate("TrackModel", u"Track Circuit Failure", None))
        self.powerFailure.setText(QCoreApplication.translate("TrackModel", u"Power Failure", None))
        self.brokenRail_O.setText("")
        self.trackcircuitFailure_O.setText("")
        self.powerFailure_O.setText("")
        self.stationdevicesgroup.setTitle(QCoreApplication.translate("TrackModel", u"Stations/Devices", None))
        self.switchlabe_ID_TM.setText(QCoreApplication.translate("TrackModel", u"Switch ID:", None))
        self.switchID_O.setText("")
        self.trackswitchdirectionLabel_TB_2.setText(QCoreApplication.translate("TrackModel", u"Switch Connections", None))
        self.switchFrom_O.setText("")
        self.directionLabelTB_2.setText(QCoreApplication.translate("TrackModel", u"<---->", None))
        self.switchTo_O.setText("")
        self.crossingIDlabel_TM.setText(QCoreApplication.translate("TrackModel", u"Crossing ID:", None))
        self.crossingID_O.setText("")
        self.crossingstatelabel_TM.setText(QCoreApplication.translate("TrackModel", u"Crossing State:", None))
        self.crossingstate_O.setText("")
        self.signalidlabelTM.setText(QCoreApplication.translate("TrackModel", u"Signal ID:", None))
        self.signalID_O.setText("")
        self.signalstatelableTM.setText(QCoreApplication.translate("TrackModel", u"Signal State:", None))
        self.signalstate_O.setText("")
        self.beacon1label_TM.setText(QCoreApplication.translate("TrackModel", u"Beacon 1:", None))
        self.beacon_O.setText("")
        self.stationlabel_ID_TM.setText(QCoreApplication.translate("TrackModel", u"Station ID:", None))
        self.stationID_O.setText("")
        self.beacon2label_TM.setText(QCoreApplication.translate("TrackModel", u"Beacon 2:", None))
        self.beacon2_O.setText("")
        self.stationexit_TM.setText(QCoreApplication.translate("TrackModel", u"Exit Side:", None))
        self.stationexit_O.setText("")
        self.stationlabel_ID_TM_3.setText(QCoreApplication.translate("TrackModel", u"Station Name:", None))
        self.stationName_O.setText("")
        self.ticketsales_label.setText(QCoreApplication.translate("TrackModel", u"Ticket Sales:", None))
        self.ticketsalesTM_O.setText("")
        self.polaritylabelTM.setText(QCoreApplication.translate("TrackModel", u"Polarity:", None))
        self.PolarityTM_O.setText("")
        self.departedtrains.setText(QCoreApplication.translate("TrackModel", u"Disembarking:", None))
        self.disembarkingTM_O.setText("")
        self.currentriders_label.setText(QCoreApplication.translate("TrackModel", u"Boarding:", None))
        self.boardingTM_O.setText("")
        self.lineselectionsGroup.setTitle(QCoreApplication.translate("TrackModel", u"Line Selection", None))
        self.buttonRed.setText(QCoreApplication.translate("TrackModel", u"Red Line", None))
        self.buttonGreen.setText(QCoreApplication.translate("TrackModel", u"Green Line", None))
        self.blockinfoGroup_3.setTitle(QCoreApplication.translate("TrackModel", u"Block Information", None))
        self.segmentSelected_4.setText(QCoreApplication.translate("TrackModel", u"Section", None))
        self.blockauthoritylabelTB_3.setText(QCoreApplication.translate("TrackModel", u"Authority", None))
        self.blockoccupancylabelTB_3.setText(QCoreApplication.translate("TrackModel", u"Occupancy", None))
        self.label_2.setText(QCoreApplication.translate("TrackModel", u"Underground", None))
        self.blockNumber_4.setText(QCoreApplication.translate("TrackModel", u"Block", None))
        self.blockLength_4.setText(QCoreApplication.translate("TrackModel", u"Block Length", None))
        self.blockGrade_4.setText(QCoreApplication.translate("TrackModel", u"Block Grade", None))
        self.maxspeedLimit_4.setText(QCoreApplication.translate("TrackModel", u"Max Speed Limit", None))
        self.label_27.setText(QCoreApplication.translate("TrackModel", u"Elevation", None))
        self.label_28.setText(QCoreApplication.translate("TrackModel", u"Cumulative Elevation", None))
        self.sectionSelectedTM_O.setText("")
        self.blockAuthorityTM_O.setText("")
        self.blockoccupancyTM_O.setText("")
        self.undergroundTM_O.setText("")
        self.label_29.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.label_30.setText(QCoreApplication.translate("TrackModel", u" %", None))
        self.label_31.setText(QCoreApplication.translate("TrackModel", u" MPH", None))
        self.label_32.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.ft_label3_4.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.temperature_4.setText(QCoreApplication.translate("TrackModel", u"Temperature", None))
        self.label_33.setText(QCoreApplication.translate("TrackModel", u" \u00b0F", None))
        self.heaters_4.setText(QCoreApplication.translate("TrackModel", u"Heaters", None))
        self.heatersTM_O.setText("")
        self.signalstatelableTM_2.setText(QCoreApplication.translate("TrackModel", u"Throughput: ", None))
        self.throughputTM_O.setText("")
        self.signalstatelableTM_3.setText(QCoreApplication.translate("TrackModel", u"Total Passengers:", None))
        self.passengersTM_O.setText("")
        self.stationdevicesgroup_2.setTitle(QCoreApplication.translate("TrackModel", u"Color Key", None))
        self.ticketsalesTM_O_3.setText("")
        self.stationlabel_ID_TM_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trackMap), QCoreApplication.translate("TrackModel", u"Track Map", None))
        ___qtablewidgetitem = self.faultlistTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TrackModel", u"Rail Line", None));
        ___qtablewidgetitem1 = self.faultlistTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TrackModel", u"Block Segment", None));
        ___qtablewidgetitem2 = self.faultlistTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TrackModel", u"Block Number", None));
        ___qtablewidgetitem3 = self.faultlistTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TrackModel", u"Broken Rail Fault", None));
        ___qtablewidgetitem4 = self.faultlistTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TrackModel", u"Track Circuit Fault", None));
        ___qtablewidgetitem5 = self.faultlistTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TrackModel", u"Power Failure", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.faultList), QCoreApplication.translate("TrackModel", u"Faults List", None))
        self.lineselectionsGroupTB.setTitle(QCoreApplication.translate("TrackModel", u"Line Selection", None))
        self.buttonRedTB.setText(QCoreApplication.translate("TrackModel", u"Red Line", None))
        self.buttonGreenTB.setText(QCoreApplication.translate("TrackModel", u"Green Line", None))
        self.testbenchInputsGroupTB.setTitle(QCoreApplication.translate("TrackModel", u"Set Environmental Inputs", None))
        self.Derailment_2.setText(QCoreApplication.translate("TrackModel", u"Ambient Temperature ( \u00b0F)", None))
        self.trackcircuitFailure_2.setText(QCoreApplication.translate("TrackModel", u"Ticket Sales", None))
        self.throughputTBlabel.setText(QCoreApplication.translate("TrackModel", u"Total Throughput", None))
        self.settempTB_Button.setText(QCoreApplication.translate("TrackModel", u"Temperature", None))
        self.setboardingCountTB_button.setText(QCoreApplication.translate("TrackModel", u"Ticket Sales", None))
        self.setThroughputTB_Button.setText(QCoreApplication.translate("TrackModel", u"Throughput", None))
        self.label_19.setText(QCoreApplication.translate("TrackModel", u"Block Occupancy", None))
        self.occupancyTB_Button.setText(QCoreApplication.translate("TrackModel", u"Occupancy", None))
        self.label.setText(QCoreApplication.translate("TrackModel", u"Block Authority Distance (Ft): ", None))
        self.adjustblocklabelTB.setText(QCoreApplication.translate("TrackModel", u"Adjust Block Length", None))
        self.label_18.setText(QCoreApplication.translate("TrackModel", u"  Ft ", None))
        self.setblockLengthTB_button.setText(QCoreApplication.translate("TrackModel", u"Set Length", None))
        self.authorityTB_button.setText(QCoreApplication.translate("TrackModel", u"Set Authority", None))
        self.trackcontrollerInputsGroupTB.setTitle(QCoreApplication.translate("TrackModel", u"Track Controller Inputs", None))
        self.blocksignalControl.setText(QCoreApplication.translate("TrackModel", u"Block Signal Control", None))
        self.signalToggle_Button.setText(QCoreApplication.translate("TrackModel", u"Toggle Signal", None))
        self.crossingControlLabel.setText(QCoreApplication.translate("TrackModel", u"Crossing Control", None))
        self.crossingToggle_Button.setText(QCoreApplication.translate("TrackModel", u"Toggle Crossing", None))
        self.trackcontrolSwitch.setText(QCoreApplication.translate("TrackModel", u"Track Switch Control", None))
        self.switchToggle_Button.setText(QCoreApplication.translate("TrackModel", u"Toggle Switch", None))
        self.trackswitchdirectionLabel_TB.setText(QCoreApplication.translate("TrackModel", u"Switich Connections    ", None))
        self.switchFromTB_O.setText("")
        self.directionLabelTB.setText(QCoreApplication.translate("TrackModel", u"<---->", None))
        self.switchToTB_O.setText("")
        self.signalLabel_TB.setText(QCoreApplication.translate("TrackModel", u"Signal State", None))
        self.signalStateTB_O.setText("")
        self.crossingLabel_TB.setText(QCoreApplication.translate("TrackModel", u"Crossing State", None))
        self.crossingStateTB_O.setText("")
        self.switchlabe_ID_TM_3.setText(QCoreApplication.translate("TrackModel", u"Switch ID", None))
        self.switchIDTB_O.setText("")
        self.signalidlabelTM_2.setText(QCoreApplication.translate("TrackModel", u"Signal ID", None))
        self.signalIDTB_O.setText("")
        self.crossingIDlabel_TM_2.setText(QCoreApplication.translate("TrackModel", u"Crossing ID", None))
        self.crossingIDTB_O.setText("")
        self.murphyInputsGroupTB.setTitle(QCoreApplication.translate("TrackModel", u"Murphy Inputs (Track Faults)", None))
        self.brokenTrackLabelTB_M.setText(QCoreApplication.translate("TrackModel", u"Broken Rail", None))
        self.trackcircuitFailureTB_M.setText(QCoreApplication.translate("TrackModel", u"Track Circuit Failure", None))
        self.powerFailureLabelTB_M.setText(QCoreApplication.translate("TrackModel", u"Power Failure", None))
        self.railtestTB_Button.setText(QCoreApplication.translate("TrackModel", u"Test Rail", None))
        self.circuittestTB_Button.setText(QCoreApplication.translate("TrackModel", u"Test Circuit", None))
        self.powertestTB_Button.setText(QCoreApplication.translate("TrackModel", u"Test Power", None))
        self.resetfaultTB_button.setText(QCoreApplication.translate("TrackModel", u"Reset Fault", None))
        self.faultsGroupTB.setTitle(QCoreApplication.translate("TrackModel", u"Faults on Selected Block", None))
        self.brokentrackLabelTB.setText(QCoreApplication.translate("TrackModel", u"Broken Rail", None))
        self.trackcircuitfailureLabelTB.setText(QCoreApplication.translate("TrackModel", u"Track Circuit Failure", None))
        self.powerfailureLabelTB.setText(QCoreApplication.translate("TrackModel", u"Power Failure", None))
        self.brokenrailTB_O.setText("")
        self.trackcircuitFailureTB_O.setText("")
        self.powerFailureTB_O.setText("")
        self.blockinfoGroup_2.setTitle(QCoreApplication.translate("TrackModel", u"Block Information", None))
        self.segmentSelected_2.setText(QCoreApplication.translate("TrackModel", u"Section", None))
        self.blockauthoritylabelTB.setText(QCoreApplication.translate("TrackModel", u"Authority", None))
        self.blockoccupancylabelTB.setText(QCoreApplication.translate("TrackModel", u"Occupancy", None))
        self.undergroundTBlabel.setText(QCoreApplication.translate("TrackModel", u"Underground", None))
        self.blockNumber_2.setText(QCoreApplication.translate("TrackModel", u"Block", None))
        self.blockLength_2.setText(QCoreApplication.translate("TrackModel", u"Block Length", None))
        self.blockGrade_2.setText(QCoreApplication.translate("TrackModel", u"Block Grade", None))
        self.maxspeedLimit_2.setText(QCoreApplication.translate("TrackModel", u"Max Speed Limit", None))
        self.label_11.setText(QCoreApplication.translate("TrackModel", u"Elevation", None))
        self.label_12.setText(QCoreApplication.translate("TrackModel", u"Cumulative Elevation", None))
        self.sectionSelectedTB_O.setText("")
        self.blockAuthorityTB_O.setText("")
        self.blockoccupancyTB_O.setText("")
        self.undrgroundTB_O.setText("")
        self.label_13.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.label_14.setText(QCoreApplication.translate("TrackModel", u" %", None))
        self.label_15.setText(QCoreApplication.translate("TrackModel", u" MPH", None))
        self.label_16.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.ft_label3_2.setText(QCoreApplication.translate("TrackModel", u" Ft", None))
        self.temperature_2.setText(QCoreApplication.translate("TrackModel", u"Temperature", None))
        self.label_17.setText(QCoreApplication.translate("TrackModel", u" \u00b0F", None))
        self.heaters_2.setText(QCoreApplication.translate("TrackModel", u"Heaters", None))
        self.heatersTB_O.setText("")
        self.AuthorityboolTB.setText("")
        self.environmentalvariablesGroup_3.setTitle(QCoreApplication.translate("TrackModel", u"Stations/Devices", None))
        self.beacon1label_TM_2.setText(QCoreApplication.translate("TrackModel", u"Beacon 1", None))
        self.beaconTB_O.setText("")
        self.stationlabel_ID_TM_2.setText(QCoreApplication.translate("TrackModel", u"Station ID", None))
        self.stationIDTB_O.setText("")
        self.beacon2label_TM_2.setText(QCoreApplication.translate("TrackModel", u"Beacon 2", None))
        self.beacon2TB_O.setText("")
        self.stationexit_TM_2.setText(QCoreApplication.translate("TrackModel", u"Exit Side", None))
        self.stationexitTB_O.setText("")
        self.stationlabel_ID_TM_4.setText(QCoreApplication.translate("TrackModel", u"Station Name:", None))
        self.stationNameTB_O.setText("")
        self.signalstatelableTM_5.setText(QCoreApplication.translate("TrackModel", u"Throughput", None))
        self.throughputTB_O.setText("")
        self.signalstatelableTM_4.setText(QCoreApplication.translate("TrackModel", u"Ticket Sales", None))
        self.ticketsalesTB_O.setText("")
        self.inittrainTB_button.setText(QCoreApplication.translate("TrackModel", u"Initialize Train", None))
        self.polaritylabelTB.setText(QCoreApplication.translate("TrackModel", u"Polarity:", None))
        self.PolarityTB_O.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Testbench), QCoreApplication.translate("TrackModel", u"Testbench", None))
        self.trackmodelheaderLabel.setText(QCoreApplication.translate("TrackModel", u"Track Model", None))
        self.image.setText("")
        self.time_label.setText(QCoreApplication.translate("TrackModel", u"timelabel", None))
        self.yellow.setText("")
        self.label_6.setText(QCoreApplication.translate("TrackModel", u"<html><head/><body><p align=\"center\">Simulation speed</p></body></html>", None))
        self.pause_button.setText(QCoreApplication.translate("TrackModel", u"Pause", None))
        self.menuTraick_Model.setTitle(QCoreApplication.translate("TrackModel", u"File", None))
        self.menuFault_List.setTitle(QCoreApplication.translate("TrackModel", u"Edit", None))
        self.menuTestBench.setTitle(QCoreApplication.translate("TrackModel", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("TrackModel", u"Help", None))
    # retranslateUi

