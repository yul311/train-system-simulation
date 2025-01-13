
import sys, os, math, json
import pandas as pd
from PySide6.QtWidgets import (QApplication, QMainWindow,  QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView, QStyleOptionGraphicsItem,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QGraphicsItem, QVBoxLayout,QGraphicsLineItem,QGraphicsTextItem)
from PySide6.QtCore import QLineF, QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF, QLine, QPoint, QPointF
from PySide6.QtGui import QPalette, QColor, QPixmap, QIntValidator, QBrush, QPen, QPainter, QCursor, QIcon,QFont
sys.path.append(os.getcwd())

from ast import literal_eval


#Import Track Module items
from Track_Model.railway.rlines import rail_lines
from Track_Model.services.conversion import *
from Track_Model.railway.train_object import train
import Track_Model.main_ui.ui as ui
from Main.simulation_time import sim

#---------------------------------------------------------------
#setup Global Variables
#---------------------------------------------------------------
from Track_Model.services.readdatabase import Database
#---------------------------------------------------------------
# Backbone for building rail nodes on graphics
#---------------------------------------------------------------
class block_nodes(QGraphicsItem):
    # call constructor of GraphicsItem
    def __init__(self, rect, pen, brush, ID, parent=None, line=""):
        # call constructor of QGraphicsItem
        super(block_nodes, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.setAcceptHoverEvents(True)
        self.pen = pen
        pw = self.pen.widthF()
        self.brush =  QBrush(Qt.blue)
        self.brush = brush
        self.ID = ID
        self.parent = parent
        self.line = line
        self.rect = QRectF(rect[0], rect[1], rect[2], rect[3])
        self.focusrect = QRectF(rect[0]-pw/2, rect[1]-pw/2,
                rect[2]+pw, rect[3]+pw)
        self.x_pos = rect[0]
        self.y_pos = rect[1]

    #return block ID
    def get_id(self):
        return self.ID
    
    def get_pos(self):
        return self.x_pos, self.y_pos
    #if mouse press event occurs
    def mousePressEvent(self, event):
        # select object
        # set item as topmost in stack
        self.setZValue(self.parent.scene.items()[0].zValue() + 1)
        self.setSelected(True)
        QGraphicsItem.mousePressEvent(self, event)
        #set blueblockIDs
        track_model_ui.selected_ID = self.ID
        track_model_ui.line_selected = self.line

    #when mouse button is released
    def mouseReleaseEvent(self, event):
        self.setZValue(self.parent.scene.items()[0].zValue() + 1)
        self.setSelected(False)
        QGraphicsItem.mousePressEvent(self, event)
    
    #call bounding rectangle
    def boundingRect(self):
        return self.rect

    #paint the rectangle to the UI
    def paint(self, painter, option, widget=None):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawRect(self.rect)
        if self.isSelected():
            self.drawFocusRect(painter)

    #if rectangle is selected draw the rectangle that shows it's selected
    def drawFocusRect(self, painter):
        self.focusbrush =  QBrush()
        self.focuspen =  QPen(Qt.DotLine)
        self.focuspen.setColor(Qt.black)
        self.focuspen.setWidthF(1.5)
        painter.setBrush(self.focusbrush)
        painter.setPen(self.focuspen)
        painter.drawRect(self.focusrect)

    #if mouse is hovering over block
    def hoverEnterEvent(self, event):
        self.pen.setStyle(Qt.DotLine)
        self.setCursor(Qt.PointingHandCursor)
        QGraphicsItem.hoverEnterEvent(self, event)

    #if mouse if no longer hovering over item
    def hoverLeaveEvent(self, event):
        self.pen.setStyle( Qt.SolidLine)
        QGraphicsItem.hoverLeaveEvent(self, event)
    
    #If block is occupied, change it's color!
    def set_block_color(self,brush):
        self.brush = brush
        self.update()

class signal_colors(QGraphicsItem):
    # call constructor of GraphicsItem
    def __init__(self, rect, pen, brush, ID, parent=block_nodes):
        # call constructor of QGraphicsItem
        super(signal_colors, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
    
        self.setAcceptHoverEvents(False)
        self.pen = pen
        self.brush =  QBrush(Qt.blue)
        self.brush = brush
        self.ID = ID
        self.parent = parent
        self.rect = QRectF(rect[0], rect[1], rect[2], rect[3])

    #return block ID
    def get_id(self):
        return self.ID
    #call bounding rectangle
    def boundingRect(self):
        return self.rect
    
    #paint the rectangle to the UI
    def paint(self, painter, option, widget=None):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(self.rect)

    #if mouse press event occurs
    def mousePressEvent(self, event):
        # select object
        # set item as topmost in stack
        self.setZValue(self.parent.scene.items()[0].zValue() + 1)
        self.setSelected(True)
        QGraphicsItem.mousePressEvent(self, event)
        #print(self.ID)

    def setbrush(self,brush):
        self.brush = brush
        self.update()

class graphics_text(QGraphicsTextItem):
    def __init__(self, x,y, train_id:str, pen, parent=block_nodes):
        # call constructor of QGraphicsItem
        super(graphics_text, self).__init__()
        self.parent = parent
        self.setAcceptHoverEvents(False)
        self.train_id = train_id
        self.x_pos = x
        self.y_pos = y
        self.text_item = QGraphicsTextItem(train_id)
        self.pen = pen
        self.text_item.setDefaultTextColor(self.pen)
    def paint(self, painter, option, widget):
        painter.setFont(QFont("Arial",20))
        painter.setPen(self.pen)
        #painter.drawText(self.x_pos, self.y_pos, self.train_id)
        self.text_item.paint(painter, option, widget)

    def set_position(self, new_x, new_y):
        self.setPos(new_x, new_y)
        self.update()

    def get_position(self):
        return self.x_pos, self.y_pos
#---------------------------------------------------------------
# Main Windows
#---------------------------------------------------------------
class track_model_ui(QMainWindow):
    def __init__(self):
        super(track_model_ui, self).__init__()
        
        icon = QIcon(os.path.join(os.getcwd(),"Other","AuroraLogo.jpg"))
        self.setWindowIcon(icon)
        
        #initialize ui
        self.ui = ui.Ui_TrackModel()
        self.ui.setupUi(self)
        #set up variables
        self.blue_selected:bool = False
        self.red_selected:bool = False
        self.green_selected:bool = False
        self.selected_ID:int = 0
        self.line_selected:str = ""
        
        self.time = None
        self.time_changed = None

        #initialize graphics
        self.setupscenes()      # setup the graphics scenes
        self.build_faulttable()
        self.build_trackmap()
        self.hide_map()
        
    #---------------------------------------------------------------
    # Main UI Timers
    #---------------------------------------------------------------
        
        #set date & time and update every second
        self.updatetimer = QTimer(self)
        self.updatetimer.timeout.connect(self.time_handler)
        self.updatetimer.setInterval(50)
        self.updatetimer.start()

        #make a timer to increase ticket by 5 sales every second
        self.ticket_timer = QTimer(self)
        self.ticket_timer.timeout.connect(self.update_ticket_sales)
        self.ticket_timer.setInterval(5000)
        self.ticket_timer.start()

    #---------------------------------------------------------------
    # Setup maps based on button click
    #---------------------------------------------------------------
        
        #if either green button is pressed setup the green map
        self.ui.buttonGreen.clicked.connect(self.setupgreentracks)
        self.ui.buttonGreenTB.clicked.connect(self.setupgreentracks)
        
        #if either blue button is pressed activate maps
        #self.ui.buttonBlue.clicked.connect(self.setupbluetracks)        
        #self.ui.buttonBlueTB.clicked.connect(self.setupbluetracks)
        
        #if either red button is clicked setup tracks
        self.ui.buttonRed.clicked.connect(self.setupredtracks)
        self.ui.buttonRedTB.clicked.connect(self.setupredtracks)
        
        # sim slider and pause button
        self.ui.simslider.valueChanged.connect(self.change_simspeed)
        self.ui.pause_button.clicked.connect(self.pause_action)

    #---------------------------------------------------------------
    # Testbench button clicks
    #---------------------------------------------------------------
        #only allow numbers to be used for environment variables input
        validator = QIntValidator()
        self.ui.trackTemperatureTB_I.setValidator(validator)
        self.ui.boardingCountTB_I.setValidator(validator)
        self.ui.throughputTB_I.setValidator(validator)
        self.ui.settempTB_Button.clicked.connect(self.setTemperature)
        self.ui.setboardingCountTB_button.clicked.connect(self.setboardingCount)
        self.ui.setThroughputTB_Button.clicked.connect(self.setThroughput)
        self.ui.switchToggle_Button.clicked.connect(self.switchtoggleTB_Button)
        self.ui.signalToggle_Button.clicked.connect(self.signaltoggleTB_Button)
        self.ui.crossingToggle_Button.clicked.connect(self.crossingtoggleTB_Button)
        #reset Faults
        self.ui.resetfaultTB_button.clicked.connect(self.reset_faults)
        
        # Train
        self.ui.inittrainTB_button.clicked.connect(self.add_train)

        #Block Inputs information
        self.ui.authorityTB_button.clicked.connect(self.authority_change)
        self.ui.occupancyTB_Button.clicked.connect(self.occupancy_change)
        self.ui.setblockLengthTB_button.clicked.connect(self.set_block_length)

    #---------------------
    # Murphy Buttons
    #---------------------
        self.ui.railtestTB_Button.clicked.connect(self.railtestTB_button_pressed)
        self.ui.circuittestTB_Button.clicked.connect(self.circuittestTB_button_pressed)
        self.ui.powertestTB_Button.clicked.connect(self.powertestTB_button_pressed)
        
    #---------------------------------------------------------------
    # Track Map Functions
    #---------------------------------------------------------------
    def updatetextTM(self):
        '''
        if(self.blue_selected == True and self.selected_ID <= len(b_block)):
            digit = self.selected_ID
            #configure segments for QLCD
            self.segmentsconfigure()
            #update block information
            self.ui.sectionSelectedTM_O.setText(str(b_block[int(digit)].get_sectionID()))
            self.ui.blockAuthorityTM_O.setText(str(b_block[int(digit)].get_authority()))
            self.ui.blockoccupancyTM_O.setText(str(b_block[digit].get_occupancy()))
            self.ui.blockNumberTM_O.display(int(b_block[int(digit)].get_blockID()))
            self.ui.blockLengthTM_O.display(str(meters_feet(b_block[int(digit)].get_block_length())))
            self.ui.blockGradeTM_O.display(str(b_block[int(digit)].get_gradLevel()))
            self.ui.maxspeedlimitTM_O.display(kph_mph(b_block[int(digit)].get_max_speed()))
            self.ui.elevationTM_O.display(meters_feet(b_block[int(digit)].get_elevation()))
            self.ui.cumulativeelevationTM_O.display(meters_feet(b_block[int(digit)].get_cumulative_elevation()))
            #Temp
            self.ui.temperatureTM_O.display(str(celcius_fahrenheit(blueLine.get_temperature())))
            #heaters
            self.ui.heatersTM_O.setText(str(blueLine.get_heater_state()))
            # Throughput
            self.ui.throughputTM_O.setText(str(blueLine.get_throughput()))
            #station info
            if(b_block[digit].stations != None):
                self.ui.stationID_O.setText(str(b_block[digit].get_station_id()))
                self.ui.stationName_O.setText(str(b_block[self.selected_ID].get_station_name()))
                self.ui.stationexit_O.setText(str(b_block[self.selected_ID].get_station_side()))
                self.ui.ticketsalesTM_O.setText(str(b_block[self.selected_ID].get_station_ticket_sales()))
            else:
                self.ui.stationID_O.setText("N/A")
                self.ui.stationName_O.setText("N/A")
                self.ui.stationexit_O.setText("N/A")
                self.ui.ticketsalesTM_O.setText("N/A")
                
            #switch info
            if(b_block[self.selected_ID].track_switches != None):
                self.ui.switchID_O.setText(str(b_block[self.selected_ID].get_switch_id()))
                self.ui.switchFrom_O.setText(str(b_block[self.selected_ID].get_switch_on_block()))
                self.ui.switchTo_O.setText(str(b_block[self.selected_ID].get_connected_to()))
            else:
                self.ui.switchID_O.setText("N/A")
                self.ui.switchFrom_O.setText("N/A")
                self.ui.switchTo_O.setText("N/A")

            #crossing info
            if(b_block[self.selected_ID].rail_crossings != None):
                self.ui.crossingID_O.setText(str(b_block[self.selected_ID].get_crossing_id()))
                self.ui.crossingstate_O.setText(str(b_block[self.selected_ID].get_crossing_state()))
            else:
                self.ui.crossingID_O.setText("N/A")
                self.ui.crossingstate_O.setText("N/A")

            #signal(Light) info
            if(b_block[self.selected_ID].track_lights != None):
                self.ui.signalID_O.setText(str(int(b_block[self.selected_ID].get_light_id())))
                self.ui.signalstate_O.setText(str(b_block[self.selected_ID].get_light_state()))
            else:
                self.ui.signalID_O.setText("N/A")
                self.ui.signalstate_O.setText("N/A")
            
            #Print Faults
            self.ui.brokenRail_O.setText(str(b_block[digit].get_failureBR()))
            self.ui.trackcircuitFailure_O.setText(str(b_block[digit].get_failureTC()))
            self.ui.powerFailure_O.setText(str(b_block[digit].get_failurePW())) 
        '''
        try:
            if(self.green_selected == True and track_model_ui.line_selected == "Green"):
                digit = self.selected_ID
                #configure segments for QLCD
                self.segmentsconfigure()
                #update block information
                self.ui.sectionSelectedTM_O.setText(str(g_block[int(digit)].get_sectionID()))
                self.ui.blockAuthorityTM_O.setText(str(meters_feet(g_block[int(digit)].get_authority())))
                self.ui.blockoccupancyTM_O.setText(str(g_block[digit].get_occupancy()))
                self.ui.blockNumberTM_O.display(int(g_block[int(digit)].get_blockID()))
                self.ui.blockLengthTM_O.display(str(meters_feet(g_block[int(digit)].get_block_length())))
                self.ui.blockGradeTM_O.display(str(g_block[int(digit)].get_gradLevel()))
                self.ui.maxspeedlimitTM_O.display(kph_mph(g_block[int(digit)].get_max_speed()))
                self.ui.elevationTM_O.display(meters_feet(g_block[int(digit)].get_elevation()))
                self.ui.cumulativeelevationTM_O.display(meters_feet(g_block[int(digit)].get_cumulative_elevation()))
                self.ui.PolarityTM_O.setText(str(g_block[digit].get_polarity()))
                self.ui.undergroundTM_O.setText(str(g_block[digit].get_underground()))

                #Temp
                self.ui.temperatureTM_O.display(str(celcius_fahrenheit(greenLine.get_temperature())))
                #heaters
                self.ui.heatersTM_O.setText(str(greenLine.get_heater_state()))
                # Throughput
                self.ui.throughputTM_O.setText(str(greenLine.get_throughput()))
                # Total Passengers
                self.ui.passengersTM_O.setText(str(greenLine.get_total_passengers()))
                #station info
                if(g_block[digit].stations != None):
                    self.ui.stationID_O.setText(str(g_block[digit].get_station_id()))
                    self.ui.stationName_O.setText(str(g_block[self.selected_ID].get_station_name()))
                    self.ui.stationexit_O.setText(str(g_block[self.selected_ID].get_station_side()))
                    self.ui.ticketsalesTM_O.setText(str(g_block[self.selected_ID].get_station_ticket_sales()))

                    if(g_block[digit].get_dwelling()):
                        self.ui.boardingTM_O.setText(str(g_block[self.selected_ID].get_boarding_passengers()))
                        self.ui.disembarkingTM_O.setText(str(g_block[self.selected_ID].get_leaving_passengers()))
                    else:
                        self.ui.boardingTM_O.setText("N/A")
                        self.ui.disembarkingTM_O.setText("N/A")
                else:
                    self.ui.stationID_O.setText("N/A")
                    self.ui.stationName_O.setText("N/A")
                    self.ui.stationexit_O.setText("N/A")
                    self.ui.ticketsalesTM_O.setText("N/A")

                
                #switch info
                if(g_block[self.selected_ID].track_switches != None):
                    self.ui.switchID_O.setText(str(g_block[self.selected_ID].get_switch_id()))
                    self.ui.switchFrom_O.setText(str(g_block[self.selected_ID].get_switch_corner_block()))
                    self.ui.switchTo_O.setText(str(g_block[self.selected_ID].get_connected_to()))
                else:
                    self.ui.switchID_O.setText("N/A")
                    self.ui.switchFrom_O.setText("N/A")
                    self.ui.switchTo_O.setText("N/A")

                
                if(g_block[self.selected_ID].track_switches != None or g_block[digit].stations != None):
                    if(g_block[self.selected_ID].track_switches != None):
                        self.ui.beacon_O.setText(str(g_block[digit].get_switch_beaconb()))
                        self.ui.beacon2_O.setText(str(g_block[digit].get_switch_beaconc()))
                    elif(g_block[digit].stations != None):
                        self.ui.beacon_O.setText(str(g_block[digit].get_station_beacon1()))
                        self.ui.beacon2_O.setText(str(g_block[digit].get_station_beacon2()))
                else:
                    self.ui.beacon_O.setText("N/A")
                    self.ui.beacon2_O.setText("N/A")


                #crossing info
                if(g_block[self.selected_ID].rail_crossings != None):
                    self.ui.crossingID_O.setText(str(g_block[self.selected_ID].get_crossing_id()))
                    if (str(g_block[digit].get_crossing_state()) == "False"):
                        self.ui.crossingstate_O.setText("Raised")  
                    else:
                        self.ui.crossingstate_O.setText("Lowered")
                else:
                    self.ui.crossingID_O.setText("N/A")
                    self.ui.crossingstate_O.setText("N/A")

                #signal(Light) info
                if(g_block[self.selected_ID].track_lights != None):
                    self.ui.signalID_O.setText(str(g_block[self.selected_ID].get_light_id()))
                    self.ui.signalstate_O.setText(str(g_block[self.selected_ID].get_light_state()))
                else:
                    self.ui.signalID_O.setText("N/A")
                    self.ui.signalstate_O.setText("N/A")
                
                #Print Faults
                self.ui.brokenRail_O.setText(str(g_block[digit].get_failureBR()))
                self.ui.trackcircuitFailure_O.setText(str(g_block[digit].get_failureTC()))
                self.ui.powerFailure_O.setText(str(g_block[digit].get_failurePW())) 
        except AttributeError:
            pass

        try:
            if(self.red_selected == True and track_model_ui.line_selected == "Red"):
                digit = self.selected_ID
                #configure segments for QLCD
                self.segmentsconfigure()
                #update block information
                self.ui.sectionSelectedTM_O.setText(str(r_block[int(digit)].get_sectionID()))
                self.ui.blockAuthorityTM_O.setText(str(meters_feet(r_block[int(digit)].get_authority())))
                self.ui.blockoccupancyTM_O.setText(str(r_block[digit].get_occupancy()))
                self.ui.blockNumberTM_O.display(int(r_block[int(digit)].get_blockID()))
                self.ui.blockLengthTM_O.display(str(meters_feet(r_block[int(digit)].get_block_length())))
                self.ui.blockGradeTM_O.display(str(r_block[int(digit)].get_gradLevel()))
                self.ui.maxspeedlimitTM_O.display(kph_mph(r_block[int(digit)].get_max_speed()))
                self.ui.elevationTM_O.display(meters_feet(r_block[int(digit)].get_elevation()))
                self.ui.cumulativeelevationTM_O.display(meters_feet(r_block[int(digit)].get_cumulative_elevation()))
                self.ui.PolarityTM_O.setText(str(r_block[digit].get_polarity()))
                self.ui.undergroundTM_O.setText(str(r_block[digit].get_underground()))
                #Temp
                self.ui.temperatureTM_O.display(str(celcius_fahrenheit(redLine.get_temperature())))
                #heaters
                self.ui.heatersTM_O.setText(str(redLine.get_heater_state()))
                self.ui.throughputTM_O.setText(str(redLine.get_throughput()))
                # Total Passengers
                self.ui.passengersTM_O.setText(str(redLine.get_total_passengers()))
                #station info
                if(r_block[digit].stations != None):
                    self.ui.stationID_O.setText(str(r_block[digit].get_station_id()))
                    self.ui.stationName_O.setText(str(r_block[self.selected_ID].get_station_name()))
                    self.ui.stationexit_O.setText(str(r_block[self.selected_ID].get_station_side()))
                    self.ui.ticketsalesTM_O.setText(str(r_block[self.selected_ID].get_station_ticket_sales()))

                    if(r_block[digit].get_dwelling()):
                        self.ui.boardingTM_O.setText(str(r_block[self.selected_ID].get_boarding_passengers()))
                        self.ui.disembarkingTM_O.setText(str(r_block[self.selected_ID].get_leaving_passengers()))
                    else:
                        self.ui.boardingTM_O.setText("N/A")
                        self.ui.disembarkingTM_O.setText("N/A")
                else:
                    self.ui.stationID_O.setText("N/A")
                    self.ui.stationName_O.setText("N/A")
                    self.ui.stationexit_O.setText("N/A")
                    self.ui.ticketsalesTM_O.setText("N/A")
                
                #switch info
                if(r_block[self.selected_ID].track_switches != None):
                    self.ui.switchID_O.setText(str(r_block[self.selected_ID].get_switch_id()))
                    self.ui.switchFrom_O.setText(str(r_block[self.selected_ID].get_switch_corner_block()))
                    self.ui.switchTo_O.setText(str(r_block[self.selected_ID].get_connected_to()))
                else:
                    self.ui.switchID_O.setText("N/A")
                    self.ui.switchFrom_O.setText("N/A")
                    self.ui.switchTo_O.setText("N/A")

                
                if(r_block[self.selected_ID].track_switches != None or r_block[digit].stations != None):
                    if(r_block[self.selected_ID].track_switches != None):
                        self.ui.beacon_O.setText(str(r_block[digit].get_switch_beaconb()))
                        self.ui.beacon2_O.setText(str(r_block[digit].get_switch_beaconc()))
                    elif(r_block[digit].stations != None):
                        self.ui.beacon_O.setText(str(r_block[digit].get_station_beacon1()))
                        self.ui.beacon2_O.setText(str(r_block[digit].get_station_beacon2()))
                else:
                    self.ui.beacon_O.setText("N/A")
                    self.ui.beacon2_O.setText("N/A")



                #crossing info
                if(r_block[self.selected_ID].rail_crossings != None):
                    self.ui.crossingID_O.setText(str(r_block[self.selected_ID].get_crossing_id()))
                    if (str(r_block[digit].get_crossing_state()) == "False"):
                        self.ui.crossingstate_O.setText("Raised")  
                    else:
                        self.ui.crossingstate_O.setText("Lowered")
                else:
                    self.ui.crossingID_O.setText("N/A")
                    self.ui.crossingstate_O.setText("N/A")

                #signal(Light) info
                if(r_block[self.selected_ID].track_lights != None):
                    self.ui.signalID_O.setText(str(r_block[self.selected_ID].get_light_id()))
                    self.ui.signalstate_O.setText(str(r_block[self.selected_ID].get_light_state()))
                else:
                    self.ui.signalID_O.setText("N/A")
                    self.ui.signalstate_O.setText("N/A")
                
                #Print Faults
                self.ui.brokenRail_O.setText(str(r_block[digit].get_failureBR()))
                self.ui.trackcircuitFailure_O.setText(str(r_block[digit].get_failureTC()))
                self.ui.powerFailure_O.setText(str(r_block[digit].get_failurePW())) 
        except AttributeError:
            pass
    #------------------------
    # Fault Lists Functions
    #------------------------
    def updatefaultlist(self):
            if (self.ui.faultlistTable.rowCount() >= 1):
                '''
                if (self.blue_selected):
                    for i in range(len(blueLine.block_list)):
                        if(blueLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                            self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem("Failure"))
                        else:
                            self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem(""))
                        if(blueLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                            self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem("Failure"))
                        else:
                            self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem(""))

                        if(blueLine.block_list[i].get_failurePW() == "Power Failure!"):
                            self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem("Failure"))
                        else:
                            self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem(""))
                '''
                try:
                    if(self.green_selected == True):
                        for i in range(len(greenLine.block_list)):
                            if(greenLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                                self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem(""))
                            if(greenLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                                self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem(""))

                            if(greenLine.block_list[i].get_failurePW() == "Power Failure!"):
                                self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem(""))
                except AttributeError:
                    pass

                try:
                    if(self.red_selected == True):
                        for i in range(len(redLine.block_list)):
                            if(redLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                                self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 3, QTableWidgetItem(""))
                            if(redLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                                self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 4, QTableWidgetItem(""))

                            if(redLine.block_list[i].get_failurePW() == "Power Failure!"):
                                self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(i, 5, QTableWidgetItem(""))
                except AttributeError:
                    pass

                try:
                    if(self.red_selected == True and self.green_selected):
                        x=0
                        for i in range(len(greenLine.block_list)):
                            if(greenLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                                self.ui.faultlistTable.setItem(x, 3, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 3, QTableWidgetItem(""))
                            if(greenLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                                self.ui.faultlistTable.setItem(x, 4, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 4, QTableWidgetItem(""))

                            if(greenLine.block_list[i].get_failurePW() == "Power Failure!"):
                                self.ui.faultlistTable.setItem(x, 5, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 5, QTableWidgetItem(""))
                            x = x+1 

                        for i in range(len(redLine.block_list)):
                            if(redLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                                self.ui.faultlistTable.setItem(x, 3, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 3, QTableWidgetItem(""))
                            if(redLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                                self.ui.faultlistTable.setItem(x, 4, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 4, QTableWidgetItem(""))

                            if(redLine.block_list[i].get_failurePW() == "Power Failure!"):
                                self.ui.faultlistTable.setItem(x, 5, QTableWidgetItem("Failure"))
                            else:
                                self.ui.faultlistTable.setItem(x, 5, QTableWidgetItem(""))
                            x = x+1 

                except AttributeError:
                    pass
                        
    #------------------------
    # testbench Core
    #------------------------    
    def railtestTB_button_pressed(self):
        #if(self.blue_selected == True):
        #    blueLine.block_list[self.selected_ID].set_failureBR(True)
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            greenLine.block_list[self.selected_ID].set_failureBR(True)
            greenLine.set_occupancy(self.selected_ID, True)
        
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            r_block[self.selected_ID].set_failureBR(True)
            redLine.set_occupancy(self.selected_ID, True)
        else:
            pass

    def circuittestTB_button_pressed(self):
        #if(self.blue_selected == True):
        #    blueLine.block_list[self.selected_ID].set_failureTC(True)
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            greenLine.block_list[self.selected_ID].set_failureTC(True)
            greenLine.set_occupancy(self.selected_ID, True)
        
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            redLine.block_list[self.selected_ID].set_failureTC(True)
            redLine.set_occupancy(self.selected_ID, True)
        else:
            pass
   
    def powertestTB_button_pressed(self):
        #if(self.blue_selected == True):
        #    blueLine.block_list[self.selected_ID].set_failurePW(True)
        if(self.red_selected == True and track_model_ui.line_selected == "Green"):
            greenLine.block_list[self.selected_ID].set_failurePW(True)
            greenLine.set_occupancy(self.selected_ID, True)
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            redLine.block_list[self.selected_ID].set_failurePW(True)
            redLine.set_occupancy(self.selected_ID, True)
        else:
            pass
    
    def set_block_length(self):
        #if (self.ui.setblockLengthTB_I.text() != "" and self.blue_selected == True):
        #    b_block[self.selected_ID].set_block_length(feet_meters(float(self.ui.setblockLengthTB_I.text())))
        if(self.green_selected == True and self.ui.setblockLengthTB_I.text() != "" and track_model_ui.line_selected == "Green"):
            g_block[self.selected_ID].set_block_length(feet_meters(float(self.ui.setblockLengthTB_I.text())))
        if(self.red_selected == True and self.ui.setblockLengthTB_I.text() != "" and track_model_ui.line_selected == "Red"):
           r_block[self.selected_ID].set_block_length(feet_meters(int(self.ui.setblockLengthTB_I.text())))
        else:
            pass

    def reset_faults(self):
        '''
            if(self.blue_selected == True):
            b_block[self.selected_ID].set_failure(False, False, False) #reset all 3 failures
            painted = False
            for x in range(len(Database.bluedatabase["switchID"])):
                if(self.selected_ID == Database.bluedatabase["switchblockA"][x]):
                    brush =  QBrush(QColor(0, 255, 255))
                    brush.setStyle(Qt.Dense3Pattern)
                    item1 = b_block_list[b_block[self.selected_ID].get_blockID()]
                    item1.set_block_color(brush)
                    painted = True
                    break
                elif(self.selected_ID == Database.bluedatabase["switchblockB"][x]):
                    switchblock =  Database.bluedatabase["switchblockA"][x]
                    connectedblock = b_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock):                        
                        brush =  QBrush(QColor( 30, 229, 224))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    break
                elif(self.selected_ID == Database.bluedatabase["switchblockC"][x]):
                    switchblock =  Database.bluedatabase["switchblockA"][x]
                    connectedblock = b_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock):
                        brush =  QBrush(QColor(0, 255, 255))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    
                    break
            if painted == True:
                return
                #if block is a station
            if(b_block[self.selected_ID].stations != None):
                if(math.isnan(b_block[self.selected_ID].get_station_id()) == False):
                    items = b_block_list[self.selected_ID]
                    brush = QBrush(QColor(192,21,133))
                    brush.setStyle(Qt.Dense1Pattern)
                    items.set_block_color(brush)
            #insert Crossing here
            elif(b_block[self.selected_ID].rail_crossings != None):
                pass
            else:
                items = b_block_list[self.selected_ID]
                brush = QBrush(QColor(128,128,128))
                brush.setStyle(Qt.SolidPattern)
                items.set_block_color(brush)
        '''                   
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            g_block[self.selected_ID].set_failure(False, False, False) #reset all 3 failures
            painted = False
            greenLine.set_occupancy(self.selected_ID, False)

            for x in range(len(Database.greendatabase["switchID"])):
                if(self.selected_ID == Database.greendatabase["switchblockA"][x]):
                    brush =  QBrush(QColor(0, 255, 255))
                    brush.setStyle(Qt.Dense3Pattern)
                    item1 = g_block_list[g_block[self.selected_ID].get_blockID()]
                    item1.set_block_color(brush)
                    painted = True
                    break
                elif(self.selected_ID == Database.greendatabase["switchblockB"][x]):
                    switchblock =  Database.greendatabase["switchblockA"][x]
                    connectedblock = g_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock): 
                        brush =  QBrush(QColor( 30, 229, 224))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = g_block_list[g_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = g_block_list[g_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    break
                elif(self.selected_ID == Database.greendatabase["switchblockC"][x]):
                    switchblock =  Database.greendatabase["switchblockA"][x]
                    connectedblock = g_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock):
                        brush =  QBrush(QBrush(QColor(0, 255, 255)))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = g_block_list[g_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = g_block_list[g_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    
                    break
            if painted == True:
                return
                #if block is a station
            if(g_block[self.selected_ID].stations != None):
                if(math.isnan(g_block[self.selected_ID].get_station_id()) == False):
                    items = g_block_list[self.selected_ID]
                    brush = QBrush(QColor(192,21,133))
                    brush.setStyle(Qt.Dense1Pattern)
                    items.set_block_color(brush)
            #insert Crossing here
            elif(g_block[self.selected_ID].rail_crossings != None):
                pass
            else:
                items = g_block_list[self.selected_ID]
                brush = QBrush(QColor(128,128,128))
                brush.setStyle(Qt.SolidPattern)
                items.set_block_color(brush)
                           
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            r_block[self.selected_ID].set_failure(False, False, False) #reset all 3 failures
            painted = False
            redLine.set_occupancy(self.selected_ID, False)

            for x in range(len(Database.reddatabase["switchID"])):
                if(self.selected_ID == Database.reddatabase["switchblockA"][x]):
                    brush =  QBrush(QColor(0, 255, 255))
                    brush.setStyle(Qt.Dense3Pattern)
                    item1 = r_block_list[r_block[self.selected_ID].get_blockID()]
                    item1.set_block_color(brush)
                    painted = True
                    break
                elif(self.selected_ID == Database.reddatabase["switchblockB"][x]):
                    switchblock =  Database.reddatabase["switchblockA"][x]
                    connectedblock = r_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock): 
                        brush =  QBrush(QColor( 30, 229, 224))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = r_block_list[r_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = r_block_list[r_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    break
                elif(self.selected_ID == Database.reddatabase["switchblockC"][x]):
                    switchblock =  Database.reddatabase["switchblockA"][x]
                    connectedblock = r_block[switchblock].get_connected_to()
                    if (self.selected_ID == connectedblock):
                        brush =  QBrush(QBrush(QColor(0, 255, 255)))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = r_block_list[r_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    else:
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = r_block_list[r_block[self.selected_ID].get_blockID()]
                        item1.set_block_color(brush) 
                        painted = True
                    
                    break
            if painted == True:
                return
                #if block is a station
            if(r_block[self.selected_ID].stations != None):
                if(math.isnan(r_block[self.selected_ID].get_station_id()) == False):
                    items = r_block_list[self.selected_ID]
                    brush = QBrush(QColor(192,21,133))
                    brush.setStyle(Qt.Dense1Pattern)
                    items.set_block_color(brush)
            #insert Crossing here
            elif(r_block[self.selected_ID].rail_crossings != None):
                pass
            else:
                items = r_block_list[self.selected_ID]
                brush = QBrush(QColor(128,128,128))
                brush.setStyle(Qt.SolidPattern)
                items.set_block_color(brush)
                    
    def signaltoggleTB_Button(self):
        #if(self.blue_selected == True and b_block[self.selected_ID].track_lights != None):
        #    b_block[self.selected_ID].change_light_state()
        if(self.green_selected == True and track_model_ui.line_selected == "Green" and g_block[self.selected_ID].track_lights != None):
            g_block[self.selected_ID].change_light_state()
        if(self.red_selected == True and track_model_ui.line_selected == "Red" and r_block[self.selected_ID].track_lights != None):
               r_block[self.selected_ID].change_light_state() 
        else:
            pass

    def crossingtoggleTB_Button(self):
        #if(self.blue_selected == True and b_block[self.selected_ID].rail_crossings != None):
        #    b_block[self.selected_ID].change_crossing_state()
        if(self.green_selected == True and track_model_ui.line_selected == "Green" and g_block[self.selected_ID].rail_crossings != None):
            g_block[self.selected_ID].change_crossing_state()
        if(self.red_selected == True and track_model_ui.line_selected == "Red" and r_block[self.selected_ID].rail_crossings != None):
            r_block[self.selected_ID].change_crossing_state()

    def switchtoggleTB_Button(self):
        '''
        if(self.blue_selected == True and b_block[self.selected_ID].track_switches != None):
                    if (b_block[self.selected_ID].get_failurePW() == "Normal Operation"):
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_switch_on_block()]
                        item1.set_block_color(brush)
                        item2 = b_block_list[b_block[self.selected_ID].get_connected_to()]
                        item2.set_block_color(brush)        
                        switchidtemp = b_block[self.selected_ID].get_switch_id()
                        for i in range(len(blueLine.block_list)):
                            if(b_block[i].track_switches != None):
                                if(b_block[i].get_switch_id() == switchidtemp):
                                    b_block[i].set_connected_to()
                        
                        brush =  QBrush(QColor(0,255,255))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[self.selected_ID].get_switch_on_block()]
                        item1.set_block_color(brush)
                                                
                        brush =  QBrush(QColor( 30, 229, 224))
                        brush.setStyle(Qt.Dense3Pattern)
                        item2 = b_block_list[b_block[self.selected_ID].get_connected_to()]
                        item2.set_block_color(brush)        
        '''
        if(self.green_selected == True and track_model_ui.line_selected == "Green" and g_block[self.selected_ID].track_switches != None):
            if (g_block[self.selected_ID].get_failurePW() == "Normal Operation"):
                brush =  QBrush(QColor(0, 139, 139))
                brush.setStyle(Qt.Dense3Pattern)
                item1 = g_block_list[g_block[self.selected_ID].get_switch_corner_block()]
                item1.set_block_color(brush)
                item2 = g_block_list[g_block[self.selected_ID].get_connected_to()]
                item2.set_block_color(brush)        
                switchidtemp = g_block[self.selected_ID].get_switch_id()
                for i in range(len(greenLine.block_list)):
                    if(g_block[i].track_switches != None):
                        if(g_block[i].get_switch_id() == switchidtemp):
                            g_block[i].set_connected_to()
                
                brush =  QBrush(QColor(0,255,255))
                brush.setStyle(Qt.Dense3Pattern)
                item1 = g_block_list[g_block[self.selected_ID].get_switch_corner_block()]
                item1.set_block_color(brush)
                item2 = g_block_list[g_block[self.selected_ID].get_connected_to()]
                item2.set_block_color(brush)

        if(self.red_selected == True and track_model_ui.line_selected == "Red" and r_block[self.selected_ID].track_switches != None):
            if (r_block[self.selected_ID].get_failurePW() == "Normal Operation"):
                brush =  QBrush(QBrush(QColor(60, 179, 113)))
                brush.setStyle(Qt.Dense3Pattern)
                item1 = r_block_list[r_block[self.selected_ID].get_switch_on_block()]
                item1.set_block_color(brush)
                item2 = r_block_list[r_block[self.selected_ID].get_connected_to()]
                item2.set_block_color(brush)        
                switchidtemp = r_block[self.selected_ID].get_switch_id()
                for i in range(len(redLine.block_list)):
                    if(r_block[i].track_switches != None):
                        if(r_block[i].get_switch_id() == switchidtemp):
                            r_block[i].set_connected_to()
                
                brush =  QBrush(QColor(0,255,255))
                brush.setStyle(Qt.Dense3Pattern)
                item1 = r_block_list[r_block[self.selected_ID].get_switch_on_block()]
                item1.set_block_color(brush)
                item2 = r_block_list[r_block[self.selected_ID].get_connected_to()]
                item2.set_block_color(brush)

    def setTemperature(self): 
        #if (self.ui.trackTemperatureTB_I.text() != "" and self.blue_selected == True):
        #    blueLine.set_temperature(fahrenheit_celcius(int(self.ui.trackTemperatureTB_I.text())))
        if (self.ui.trackTemperatureTB_I.text() != "" and track_model_ui.line_selected == "Green" and self.green_selected == True):
            greenLine.set_temperature(fahrenheit_celcius(int(self.ui.trackTemperatureTB_I.text())))
        if (self.ui.trackTemperatureTB_I.text() != "" and track_model_ui.line_selected == "Red" and self.red_selected == True):
            redLine.set_temperature(fahrenheit_celcius(int(self.ui.trackTemperatureTB_I.text())))

    def setboardingCount(self):
        #if(self.blue_selected == True):
        #    if(self.ui.boardingCountTB_I.text() != "" and b_block[self.selected_ID].stations != None):
        #        b_block[self.selected_ID].set_ticket_sales(int(self.ui.boardingCountTB_I.text()))
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            if(self.ui.boardingCountTB_I.text() != "" and g_block[self.selected_ID].stations != None):
                g_block[self.selected_ID].set_ticket_sales(int(self.ui.boardingCountTB_I.text()))
        
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            if(self.ui.boardingCountTB_I.text() != "" and r_block[self.selected_ID].stations != None):
                r_block[self.selected_ID].set_ticket_sales(int(self.ui.boardingCountTB_I.text()))             

    def setThroughput(self):
        #if(self.blue_selected == True):
        #    if(self.ui.throughputTB_I.text() != ""):
        #        blueLine.set_throughput(int(self.ui.throughputTB_I.text()))
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            if(self.ui.throughputTB_I.text() != ""):
                greenLine.set_throughput(int(self.ui.throughputTB_I.text()))
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            if(self.ui.throughputTB_I.text() != ""):
                redLine.set_throughput(int(self.ui.throughputTB_I.text()))

    def updatetextTB(self):
        #update table (row, column, item)
        '''
       if(self.blue_selected == True and self.selected_ID <= len(b_block)):
            digit = self.selected_ID
            #configure segments for QLCD
            self.TBsegmentsconfigure()
            #update block information
            self.ui.sectionSelectedTB_O.setText(str(b_block[int(digit)].get_sectionID()))
            self.ui.blockAuthorityTB_O.setText(str(meters_feet((b_block[int(digit)].get_authority()))))
            self.ui.blockoccupancyTB_O.setText(str(b_block[digit].get_occupancy()))
            self.ui.blockNumberTB_O.display(int(b_block[int(digit)].get_blockID()))

            self.ui.blockLengthTB_O.display(str(meters_feet(b_block[int(digit)].get_block_length())))
            self.ui.blockGradeTB_O.display(str(b_block[int(digit)].get_gradLevel()))
            self.ui.maxspeedlimitTB_O.display(kph_mph(b_block[int(digit)].get_max_speed()))

            self.ui.elevationTB_O.display(meters_feet(b_block[int(digit)].get_elevation()))
            self.ui.cumulativeelevationTB_O.display(meters_feet(b_block[int(digit)].get_cumulative_elevation()))
            #Temp
            self.ui.temperatureTB_O.display(str(celcius_fahrenheit(blueLine.get_temperature())))
            #heaters
            self.ui.heatersTB_O.setText(str(blueLine.get_heater_state()))
            self.ui.throughputTB_O.setText(str(blueLine.get_throughput()))

            #station info
            if(b_block[digit].stations != None):
                self.ui.stationIDTB_O.setText(str(b_block[digit].get_station_id()))
                self.ui.stationNameTB_O.setText(str(b_block[digit].get_station_name()))
                self.ui.stationexitTB_O.setText(str(b_block[digit].get_station_side()))
                self.ui.ticketsalesTB_O.setText(str(b_block[digit].get_station_ticket_sales()))
            else:
                self.ui.stationIDTB_O.setText("N/A")
                self.ui.stationNameTB_O.setText("N/A")
                self.ui.stationexitTB_O.setText("N/A")
                self.ui.ticketsalesTB_O.setText("N/A")

            #switch info
            if(b_block[digit].track_switches != None):
                self.ui.switchIDTB_O.setText(str(b_block[digit].get_switch_id()))
                self.ui.switchFromTB_O.setText(str(b_block[digit].get_switch_on_block()))
                self.ui.switchToTB_O.setText(str(b_block[digit].get_connected_to()))
            else:
                self.ui.switchIDTB_O.setText("N/A")
                self.ui.switchFromTB_O.setText("N/A")
                self.ui.switchToTB_O.setText("N/A")

            #crossing info
            if(b_block[digit].rail_crossings != None):
                self.ui.crossingIDTB_O.setText(str(b_block[digit].get_crossing_id()))
                self.ui.crossingStateTB_O.setText(str(b_block[digit].get_crossing_state()))
            else:
                self.ui.crossingIDTB_O.setText("N/A")
                self.ui.crossingStateTB_O.setText("N/A")

            #signal(Light) info
            if(b_block[digit].track_lights != None):
                self.ui.signalIDTB_O.setText(str(b_block[digit].get_light_id()))
                self.ui.signalStateTB_O.setText(str(b_block[digit].get_light_state()))
            else:
                self.ui.signalIDTB_O.setText("N/A")
                self.ui.signalStateTB_O.setText("N/A")         

            #print Faults
            self.ui.brokenrailTB_O.setText(str(b_block[digit].get_failureBR()))
            self.ui.trackcircuitFailureTB_O.setText(str(b_block[digit].get_failureTC()))
            self.ui.powerFailureTB_O.setText(str(b_block[digit].get_failurePW()))
        '''
        try:
            if(self.green_selected == True and track_model_ui.line_selected == "Green"):
                digit = self.selected_ID
                #configure segments for QLCD
                self.TBsegmentsconfigure()
                #update block information
                self.ui.sectionSelectedTB_O.setText(str(g_block[int(digit)].get_sectionID()))
                self.ui.blockAuthorityTB_O.setText(str(meters_feet(g_block[int(digit)].get_authority())))
                self.ui.blockoccupancyTB_O.setText(str(g_block[digit].get_occupancy()))
                self.ui.blockNumberTB_O.display(int(g_block[int(digit)].get_blockID()))

                self.ui.blockLengthTB_O.display(str(meters_feet(g_block[int(digit)].get_block_length())))
                self.ui.blockGradeTB_O.display(str(g_block[int(digit)].get_gradLevel()))
                self.ui.maxspeedlimitTB_O.display(kph_mph(g_block[int(digit)].get_max_speed()))

                self.ui.elevationTB_O.display(meters_feet(g_block[int(digit)].get_elevation()))
                self.ui.cumulativeelevationTB_O.display(meters_feet(g_block[int(digit)].get_cumulative_elevation()))
                #Temp
                self.ui.temperatureTB_O.display(str(celcius_fahrenheit(greenLine.get_temperature())))
                #heaters
                self.ui.heatersTB_O.setText(str(greenLine.get_heater_state()))
                self.ui.throughputTB_O.setText(str(greenLine.get_throughput()))
                self.ui.PolarityTB_O.setText(str(g_block[digit].get_polarity()))
                self.ui.undrgroundTB_O.setText(str(g_block[digit].get_underground()))


                if(g_block[self.selected_ID].track_switches != None or g_block[digit].stations != None):
                    if(g_block[self.selected_ID].track_switches != None):
                        self.ui.beaconTB_O.setText(str(g_block[digit].get_switch_beaconb()))
                        self.ui.beacon2TB_O.setText(str(g_block[digit].get_switch_beaconc()))
                    elif(g_block[digit].stations != None):
                        self.ui.beaconTB_O.setText(str(g_block[digit].get_station_beacon1()))
                        self.ui.beacon2TB_O.setText(str(g_block[digit].get_station_beacon2()))
                else:
                    self.ui.beaconTB_O.setText("N/A")
                    self.ui.beacon2TB_O.setText("N/A")

                #station info
                if(g_block[digit].stations != None):
                    self.ui.stationIDTB_O.setText(str(g_block[digit].get_station_id()))
                    self.ui.stationNameTB_O.setText(str(g_block[digit].get_station_name()))
                    self.ui.stationexitTB_O.setText(str(g_block[digit].get_station_side()))
                    self.ui.ticketsalesTB_O.setText(str(g_block[digit].get_station_ticket_sales()))
                else:
                    self.ui.stationIDTB_O.setText("N/A")
                    self.ui.stationNameTB_O.setText("N/A")
                    self.ui.stationexitTB_O.setText("N/A")
                    self.ui.ticketsalesTB_O.setText("N/A")
                #switch info
                if(g_block[digit].track_switches != None):
                    self.ui.switchIDTB_O.setText(str(g_block[digit].get_switch_id()))
                    self.ui.switchToTB_O.setText(str(g_block[digit].get_connected_to()))
                    self.ui.switchFromTB_O.setText(str(g_block[digit].get_switch_corner_block()))
                else:
                    self.ui.switchIDTB_O.setText("N/A")
                    self.ui.switchFromTB_O.setText("N/A")
                    self.ui.switchToTB_O.setText("N/A")
                    
                #crossing info
                if(g_block[digit].rail_crossings != None):
                    self.ui.crossingIDTB_O.setText(str(g_block[digit].get_crossing_id()))
                    if (str(g_block[digit].get_crossing_state()) == "False"):
                        self.ui.crossingStateTB_O.setText("Raised")  
                    else:
                        self.ui.crossingStateTB_O.setText("Lowered")
                else:
                    self.ui.crossingIDTB_O.setText("N/A")
                    self.ui.crossingStateTB_O.setText("N/A")

                #signal(Light) info
                if(g_block[digit].track_lights != None):
                    self.ui.signalIDTB_O.setText(str(g_block[digit].get_light_id()))
                    self.ui.signalStateTB_O.setText(str(g_block[digit].get_light_state()))
                else:
                    self.ui.signalIDTB_O.setText("N/A")
                    self.ui.signalStateTB_O.setText("N/A")         

                #print Faults
                self.ui.brokenrailTB_O.setText(str(g_block[digit].get_failureBR()))
                self.ui.trackcircuitFailureTB_O.setText(str(g_block[digit].get_failureTC()))
                self.ui.powerFailureTB_O.setText(str(g_block[digit].get_failurePW()))
        except AttributeError:
            pass

        try:
            if(self.red_selected == True and track_model_ui.line_selected == "Red"):
                digit = self.selected_ID
                #configure segments for QLCD
                self.TBsegmentsconfigure()
                #update block information
                self.ui.sectionSelectedTB_O.setText(str(r_block[int(digit)].get_sectionID()))
                self.ui.blockAuthorityTB_O.setText(str(meters_feet(r_block[int(digit)].get_authority())))
                self.ui.blockoccupancyTB_O.setText(str(r_block[digit].get_occupancy()))
                self.ui.blockNumberTB_O.display(int(r_block[int(digit)].get_blockID()))

                self.ui.blockLengthTB_O.display(str(meters_feet(r_block[int(digit)].get_block_length())))
                self.ui.blockGradeTB_O.display(str(r_block[int(digit)].get_gradLevel()))
                self.ui.maxspeedlimitTB_O.display(kph_mph(r_block[int(digit)].get_max_speed()))

                self.ui.elevationTB_O.display(meters_feet(r_block[int(digit)].get_elevation()))
                self.ui.cumulativeelevationTB_O.display(meters_feet(r_block[int(digit)].get_cumulative_elevation()))
                #Temp
                self.ui.temperatureTB_O.display(str(celcius_fahrenheit(greenLine.get_temperature())))
                #heaters
                self.ui.heatersTB_O.setText(str(greenLine.get_heater_state()))
                self.ui.throughputTB_O.setText(str(greenLine.get_throughput()))
                self.ui.PolarityTB_O.setText(str(r_block[digit].get_polarity()))
                self.ui.undrgroundTB_O.setText(str(r_block[digit].get_underground()))


                if(r_block[self.selected_ID].track_switches != None or r_block[digit].stations != None):
                    if(r_block[self.selected_ID].track_switches != None):
                        self.ui.beaconTB_O.setText(str(r_block[digit].get_switch_beaconb()))
                        self.ui.beacon2TB_O.setText(str(r_block[digit].get_switch_beaconc()))
                    elif(r_block[digit].stations != None):
                        self.ui.beaconTB_O.setText(str(r_block[digit].get_station_beacon1()))
                        self.ui.beacon2TB_O.setText(str(r_block[digit].get_station_beacon2()))
                else:
                    self.ui.beaconTB_O.setText("N/A")
                    self.ui.beacon2TB_O.setText("N/A")

                #station info
                if(r_block[digit].stations != None):
                    self.ui.stationIDTB_O.setText(str(r_block[digit].get_station_id()))
                    self.ui.stationNameTB_O.setText(str(r_block[digit].get_station_name()))
                    self.ui.stationexitTB_O.setText(str(r_block[digit].get_station_side()))
                    self.ui.ticketsalesTB_O.setText(str(r_block[digit].get_station_ticket_sales()))
                else:
                    self.ui.stationIDTB_O.setText("N/A")
                    self.ui.stationNameTB_O.setText("N/A")
                    self.ui.stationexitTB_O.setText("N/A")
                    self.ui.ticketsalesTB_O.setText("N/A")
                #switch info
                if(r_block[digit].track_switches != None):
                    self.ui.switchIDTB_O.setText(str(r_block[digit].get_switch_id()))
                    self.ui.switchToTB_O.setText(str(r_block[digit].get_connected_to()))
                    self.ui.switchFromTB_O.setText(str(r_block[digit].get_switch_corner_block()))
                else:
                    self.ui.switchIDTB_O.setText("N/A")
                    self.ui.switchFromTB_O.setText("N/A")
                    self.ui.switchToTB_O.setText("N/A")
                    
                #crossing info
                if(r_block[digit].rail_crossings != None):
                    self.ui.crossingIDTB_O.setText(str(r_block[digit].get_crossing_id()))
                    if (str(r_block[digit].get_crossing_state()) == "False"):
                        self.ui.crossingStateTB_O.setText("Raised")  
                    else:
                        self.ui.crossingStateTB_O.setText("Lowered")
                else:
                    self.ui.crossingIDTB_O.setText("N/A")
                    self.ui.crossingStateTB_O.setText("N/A")

                #signal(Light) info
                if(r_block[digit].track_lights != None):
                    self.ui.signalIDTB_O.setText(str(r_block[digit].get_light_id()))
                    self.ui.signalStateTB_O.setText(str(r_block[digit].get_light_state()))
                else:
                    self.ui.signalIDTB_O.setText("N/A")
                    self.ui.signalStateTB_O.setText("N/A")         

                #print Faults
                self.ui.brokenrailTB_O.setText(str(r_block[digit].get_failureBR()))
                self.ui.trackcircuitFailureTB_O.setText(str(r_block[digit].get_failureTC()))
                self.ui.powerFailureTB_O.setText(str(r_block[digit].get_failurePW()))
        except AttributeError:
            pass

    def occupancy_change(self):
        #if(self.blue_selected == True):
        #    blueLine.change_occupancy(self.selected_ID)
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            greenLine.change_occupancy(self.selected_ID)
        
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            redLine.change_occupancy(self.selected_ID)
        else:
            pass

    def authority_change(self):
        #if(self.blue_selected == True):
        #    if(self.ui.authorityTB_I.text() != ""):
        #        b_block[self.selected_ID].change_authority(feet_meters(int(self.ui.authorityTB_I.text())))
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            if(self.ui.authorityTB_I.text() != ""):
                g_block[self.selected_ID].change_authority(feet_meters(int(self.ui.authorityTB_I.text())))
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            if(self.ui.authorityTB_I.text() != ""):
                r_block[self.selected_ID].change_authority(feet_meters(int(self.ui.authorityTB_I.text())))

    #-------------------------------------------------------------------
    # get Functions Below
    #-------------------------------------------------------------------
    @property
    def selected_ID(self):
        return self.__selected_ID

    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    @selected_ID.setter
    def selected_ID(self, idcode):
        self.__selected_ID = idcode
        
    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    @selected_ID.setter
    def selected_ID(self, idcode):
        self.__selected_ID = idcode  

    #----------------------   
    # Basic UI Functions Below
    #---------------------
    #show updated time
    def showtime(self):
        #self.ui.dateTime.setDateTime(QDateTime.currentDateTime())
        self.ui.time_label.setText(sim.get_curr_string())

    #---------------------
    # Handle all the updates
    #---------------------
    def time_handler(self):
        self.update_occupancy_map()
        self.update_train_block()
        self.update_light_states()
        self.showtime()
        self.updatetextTM()
        self.updatetextTB()
        self.updatefaultlist()
        self.scene.update()
    
    def change_simspeed(self,value):
        sim.set_sim_speed(value)

    def pause_action(self):
        if sim.running:
            sim.stop()
        else:
            sim.start()
    
    def update_ticket_sales(self):
        '''
        For lack of a timer in my backend, making a timer here to increase
        ticket sales every 5 seconds
        '''
        greenLine.increase_ticket_sales()
        redLine.increase_ticket_sales()

    #---------------------
    # setup the Rail Lines
    #---------------------
    #def setupbluetracks(self):    
        #if blue buttons are clicked setup the QGraphicsView
    #    self.blue_selected  = True
    #    self.red_selected   = False
    #    self.green_selected = False
    #    self.build_map()
    #    self.build_faulttable()

    def setupredtracks(self):
        self.blue_selected  = False
        if self.red_selected == True:
            self.red_selected = False
        else:
            self.red_selected   = True

        self.hide_map()
        self.display_map()
        self.build_faulttable()      

    def setupgreentracks(self):
        #if blue buttons are clicked setup the QGraphicsView
        self.blue_selected  = False
        if self.green_selected == True:
            self.green_selected = False
        else:
            self.green_selected = True
            
        self.hide_map()
        self.display_map()
        self.build_faulttable()

    #---------------------
    # Build map, fault table, configure scenes
    #---------------------
    #initialize the graphics view
    def setupscenes(self):
        self.scene = QGraphicsScene(self)
        self.view = self.ui.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-500,-500,1500,1500)
        self.ui.graphicsView.centerOn(300,0)
        self.scene.installEventFilter(self)
        self.ui.graphicsView.viewport().installEventFilter(self)
        self.ui.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.ui.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.scale = (0.8,0.8)
        self.startPos = None

        self.scene = QGraphicsScene(self)
        self.view = self.ui.graphicsView_2.setScene(self.scene)
        self.scene.setSceneRect(-500,-500,1500,1500)
        self.ui.graphicsView_2.centerOn(300,0)
        self.scene.installEventFilter(self)
        self.ui.graphicsView_2.viewport().installEventFilter(self)
        self.ui.graphicsView_2.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.ui.graphicsView_2.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.scale = (0.8,0.8)
        self.startPos = None

    #Configure Number Segments on Track Model
    def segmentsconfigure(self):

        #initialize block number segment
        self.ui.blockNumberTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockNumberTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockNumberTM_O.setPalette(QColor(255,255,255))

        #initialize block length segment
        self.ui.blockLengthTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockLengthTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockLengthTM_O.setPalette(QColor(255,255,255))

        #initialize block grade segment
        self.ui.blockGradeTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockGradeTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockGradeTM_O.setPalette(QColor(255,255,255))

        #initialize max speed segement
        self.ui.maxspeedlimitTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.maxspeedlimitTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.maxspeedlimitTM_O.setPalette(QColor(255,255,255))

        #initialize temperature segment
        self.ui.temperatureTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.temperatureTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.temperatureTM_O.setPalette(QColor(255,255,255))

        #initialize cumulative elevation segment
        self.ui.cumulativeelevationTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.cumulativeelevationTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.cumulativeelevationTM_O.setPalette(QColor(255,255,255))

        #initialize elevation segment
        self.ui.elevationTM_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.elevationTM_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.elevationTM_O.setPalette(QColor(255,255,255))

    #Configure Number Segments on TestBench
    def TBsegmentsconfigure(self):
        #initialize block number segmenet
        self.ui.blockNumberTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockNumberTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockNumberTB_O.setPalette(QColor(255,255,255))

        #initialize block length segment
        self.ui.blockLengthTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockLengthTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockLengthTB_O.setPalette(QColor(255,255,255))

        #initialize block grade segment
        self.ui.blockGradeTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.blockGradeTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.blockGradeTB_O.setPalette(QColor(255,255,255))

        #initialize max speed segment
        self.ui.maxspeedlimitTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.maxspeedlimitTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.maxspeedlimitTB_O.setPalette(QColor(255,255,255))

        #initialize temperature segment
        self.ui.temperatureTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.temperatureTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.temperatureTB_O.setPalette(QColor(255,255,255))

        #initialize cumulative elevation segmenet
        self.ui.cumulativeelevationTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.cumulativeelevationTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.cumulativeelevationTB_O.setPalette(QColor(255,255,255))

        #initialize elevation segment
        self.ui.elevationTB_O.setSegmentStyle(QLCDNumber.Flat)
        self.ui.elevationTB_O.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
        self.ui.elevationTB_O.setPalette(QColor(255,255,255))

    #build the maps for graphicsview and color objects
    def build_trackmap(self):
        #clear the graphics
        self.view = self.ui.graphicsView.setScene(self.scene)
        self.view = self.ui.graphicsView_2.setScene(self.scene)
        
        '''
        if (self.blue_selected == True):
            #--------------------------------
            # Build Blue Rail Line
            #-------------------------------
            self.scene.setSceneRect(-500,-500,1500,1500)
            self.ui.graphicsView_2.centerOn(300,0)
            
            #make and draw the squares!
            n = len(Database.bluedatabase["blockNumbers"])
            graph = [[0,0], [60,0], [120,0], [180,0],[240,0],[300,0],
                    [360,50],[420,100],[480,150],[540,200],[600,250],
                    [360,-50],[420,-100],[480,-150],[540,-200],[600,-250]]
            for q in range(n):
                b_block_list["block_"+str(q)]=q
            i=0
            for x,y in graph:
                if(Database.bluedatabase["stationList"][i] >= 0):
                    b_light_list[i] = self.addLight((x,y-10,10,10),"light_"+str(i))
                    b_block_list[i] = self.addstationsquare((x,y,50,20),2.0,i)
                    i=i+1
                elif(Database.bluedatabase["switchList"][i] > 0):
                    b_light_list[i] = self.addLight((x,y-10,10,10),"light_"+str(i))
                    b_block_list[i] = self.addswitchsquare((x,y,50,20),2.0, i)
                    i=i+1
                else:
                    b_light_list[i] = self.addLight((x,y,10,10),"light_"+str(i))
                    b_block_list[i] = self.addbasicSquare((x,y+10,50,20),2.0, i)
                    i=i+1 
                    
         #Color the switch blocks and lights on them
            for x in range(len(b_block)):
                for y in range(len(Database.bluedatabase["switchID"])):
                    if(Database.bluedatabase["switchList"][x] == Database.bluedatabase["switchID"][y]):
                        brush =  QBrush(QColor(0,255,255))
                        brush.setStyle(Qt.Dense3Pattern)
                        item1 = b_block_list[b_block[x].get_switch_on_block()]
                        item1.set_block_color(brush)
                        
                        brush =  QBrush(QColor( 30, 229, 224))
                        brush.setStyle(Qt.Dense3Pattern)
                        item2 = b_block_list[b_block[x].get_connected_to()]
                        item2.set_block_color(brush)
                        
                        brush =  QBrush(QColor(0, 139, 139))
                        brush.setStyle(Qt.Dense3Pattern)
                        item2 = b_block_list[b_block[x].get_alternate_connection()]
                        item2.set_block_color(brush)
                        
                        
            brush =  QBrush(QColor("Green"))
            brush.setStyle(Qt.SolidPattern)
            item1 = b_light_list[6]
            item1.setbrush(brush)
            item2 = b_light_list[5]
            item2.setbrush(brush) 
        '''
        

        #-------------------------------
        # Build Green Rail Line
        #-------------------------------
        #load green line x,y variables
        #set all 0's which became "NaN" back to 0
        x_pos = Database.greendatabase["x"]
        y_pos = Database.greendatabase["y"]
        
        #error x and y become NaN 
        for i in range(len(g_block)):
            #for z in range(len(Database.greendatabase["switchID"])):#here to increase I
            if(Database.greendatabase["stationList"][i] > 0):
                g_block_list[i] = self.addstationsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Green")
                g_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(g_block[i].track_lights != None):
                    g_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            elif(Database.greendatabase["switchList"][i] > 0):
                g_block_list[i] = self.addswitchsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Green")
                g_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(g_block[i].track_lights != None):
                    g_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            elif(Database.greendatabase["crossingList"][i] > 0):
                g_block_list[i] = self.addswitchsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Green")
                g_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(g_block[i].track_lights != None):
                    g_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            else:
                g_block_list[i] = self.addbasicSquare((x_pos[i],y_pos[i],50,20),2.0,i, "Green")
                g_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(g_block[i].track_lights != None):
                    g_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))

        #Color the switch blocks and lights on them
        for x in range(len(g_block)):
            for y in range(len(Database.greendatabase["switchID"])):
                if(Database.greendatabase["switchList"][x] == Database.greendatabase["switchID"][y]):
                    brush =  QBrush(QColor(0,255,255))
                    brush.setStyle(Qt.Dense3Pattern)
                    item1 = g_block_list[g_block[x].get_switch_corner_block()]
                    item1.set_block_color(brush)
                    
                    brush =  QBrush(QColor( 30, 229, 224))
                    brush.setStyle(Qt.Dense3Pattern)
                    item2 = g_block_list[g_block[x].get_connected_to()]
                    item2.set_block_color(brush)
                    
                    brush =  QBrush(QColor(0, 139, 139))
                    brush.setStyle(Qt.Dense3Pattern)
                    item2 = g_block_list[g_block[x].get_alternate_connection()]
                    item2.set_block_color(brush)

                    '''
                    #Set Light states to green on the two connected switch blocks
                    #light state is "green" or "red"
                    if(g_block[x].stations == None and g_block[x].track_lights != None):
                        brush =  QBrush(QColor(g_block[x].get_light_state()))
                        brush.setStyle(Qt.SolidPattern)
                        item1 = g_light_list[g_block[x].get_switch_corner_block()]

                        item1.setbrush(brush)
                        brush =  QBrush(QColor(g_block[x].get_light_state()))
                        brush.setStyle(Qt.SolidPattern)
                        item2 = g_light_list[g_block[x].get_connected_to()]
                        item2.setbrush(brush)
                    '''

        
        for x in range(len(g_block)):
            for y in range(len(Database.greendatabase["crossingID"])):
                if(Database.greendatabase["crossingList"][x] == Database.greendatabase["crossingID"][y]):
                    brush =  QBrush(QColor( 0, 0, 128))
                    brush.setStyle(Qt.SolidPattern)
                    item1 = g_block_list[g_block[x].get_blockID()]
                    item1.set_block_color(brush)
        
        #-------------------------------
        # Build Red Rail Line
        #-------------------------------
        #load Red line x,y variables
        #set all 0's which became "NaN" back to 0
        x_pos = Database.reddatabase["x"]
        y_pos = Database.reddatabase["y"]
        
        #error x and y become NaN 
        for i in range(len(r_block)):
            #for z in range(len(Database.reddatabase["switchID"])):#here to increase I
            if(Database.reddatabase["stationList"][i] > 0):
                r_block_list[i] = self.addstationsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Red")
                r_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(r_block[i].track_lights != None):
                    r_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            elif(Database.reddatabase["switchList"][i] > 0):
                r_block_list[i] = self.addswitchsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Red")
                r_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(r_block[i].track_lights != None):
                    r_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            elif(Database.reddatabase["crossingList"][i] > 0):
                r_block_list[i] = self.addswitchsquare((x_pos[i],y_pos[i],50,20),2.0,i, "Red")
                r_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(r_block[i].track_lights != None):
                    r_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))
            else:
                r_block_list[i] = self.addbasicSquare((x_pos[i],y_pos[i],50,20),2.0,i, "Red")
                r_block_text[i] = self.add_block_text(int(x_pos[i]),int(y_pos[i]),str(i))
                if(r_block[i].track_lights != None):
                    r_light_list[i] = self.addLight((x_pos[i],y_pos[i]-10,10,10),"light_"+str(i))

        #Color the switch blocks and lights on them
        for x in range(len(r_block)):
            for y in range(len(Database.reddatabase["switchID"])):
                if(Database.reddatabase["switchList"][x] == Database.reddatabase["switchID"][y]):
                    brush =  QBrush(QColor(0,255,255))
                    brush.setStyle(Qt.Dense3Pattern)
                    item1 = r_block_list[r_block[x].get_switch_corner_block()]
                    item1.set_block_color(brush)
                    
                    brush =  QBrush(QColor( 30, 229, 224))
                    brush.setStyle(Qt.Dense3Pattern)
                    item2 = r_block_list[r_block[x].get_connected_to()]
                    item2.set_block_color(brush)
                    
                    brush =  QBrush(QColor(0, 139, 139))
                    brush.setStyle(Qt.Dense3Pattern)
                    item2 = r_block_list[r_block[x].get_alternate_connection()]
                    item2.set_block_color(brush)

                    '''
                     #Set Light states to green on the two connected switch blocks
                    #light state is "green" or "red"
                    if(r_block[x].stations == None and r_block[x].track_lights != None):
                        brush =  QBrush(QColor(r_block[x].get_light_state()))
                        brush.setStyle(Qt.SolidPattern)
                        item1 = r_light_list[r_block[x].get_switch_corner_block()]

                        print(x)
                        item1.setbrush(brush)
                        brush =  QBrush(QColor(r_block[x].get_light_state()))
                        brush.setStyle(Qt.SolidPattern)
                        #item2 = r_light_list[r_block[x].get_connected_to()]
                        #item2.setbrush(brush)
                    '''

                   
        for x in range(len(r_block)):
            for y in range(len(Database.reddatabase["crossingID"])):
                if(Database.reddatabase["crossingList"][x] == Database.reddatabase["crossingID"][y]):
                    brush =  QBrush(QColor( 0, 0, 128))
                    brush.setStyle(Qt.SolidPattern)
                    item1 = r_block_list[r_block[x].get_blockID()]
                    item1.set_block_color(brush)
        
        #--------------------------------
        # Build Green Rail Line on Testbench
        #-------------------------------
        self.view = self.ui.graphicsView_2.setScene(self.scene)
        self.scene.setSceneRect(-1000,-1000,2500,2500)
        self.ui.graphicsView_2.centerOn(500,500)
        
    def hide_map(self):
        for i in range(len(g_block)):
            g_block_list[i].setVisible(False)
            g_block_text[i].setVisible(False)
            if(g_block[i].track_lights != None):
                g_light_list[i].setVisible(False)
        
        for i in range(len(r_block)):
            r_block_list[i].setVisible(False)
            r_block_text[i].setVisible(False)
            if(r_block[i].track_lights != None):
                r_light_list[i].setVisible(False)
                
    def display_map(self):
        #Set map to visible
        if self.green_selected == True:
            for i in range(len(g_block)):
                g_block_list[i].setVisible(True)
                g_block_text[i].setVisible(True)
                if(g_block[i].track_lights != None):
                    g_light_list[i].setVisible(True)
        
        if self.red_selected == True:
            for i in range(len(r_block)):
                r_block_list[i].setVisible(True)
                r_block_text[i].setVisible(True)
                if(r_block[i].track_lights != None):
                    r_light_list[i].setVisible(True)

    def build_faulttable(self):
        #delete all rows
        self.ui.faultlistTable.clearContents()
        self.ui.faultlistTable.setRowCount(0)

        '''
        if(self.blue_selected):
            x=0
            for i in range(len(blueLine.block_list)):
                self.ui.faultlistTable.insertRow(self.ui.faultlistTable.rowCount())
                self.ui.faultlistTable.setItem(x,0, QTableWidgetItem(str(blueLine.get_line())))
                self.ui.faultlistTable.setItem(x,1, QTableWidgetItem(str(blueLine.block_list[i].get_sectionID())))
                self.ui.faultlistTable.setItem(x,2, QTableWidgetItem(str(blueLine.block_list[i].get_blockID())))
                if(blueLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                    self.ui.faultlistTable.setItem(x,3, QTableWidgetItem(blueLine.block_list[i].get_failureBR()))
                if(blueLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                    self.ui.faultlistTable.setItem(x,4, QTableWidgetItem(blueLine.block_list[i].get_failureTC()))
                if(blueLine.block_list[i].get_failureTC() == "Power Failure!"):
                    self.ui.faultlistTable.setItem(x,5, QTableWidgetItem(blueLine.block_list[i].get_failurePW()))
                x = x+1
        '''
        
        if(self.green_selected and self.red_selected):
            x=0
            for i in range(len(greenLine.block_list)):
                self.ui.faultlistTable.insertRow(self.ui.faultlistTable.rowCount())
                self.ui.faultlistTable.setItem(x,0, QTableWidgetItem(str(greenLine.get_line())))
                self.ui.faultlistTable.setItem(x,1, QTableWidgetItem(str(greenLine.block_list[i].get_sectionID())))
                self.ui.faultlistTable.setItem(x,2, QTableWidgetItem(str(greenLine.block_list[i].get_blockID())))
                if(greenLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                    self.ui.faultlistTable.setItem(x,3, QTableWidgetItem(greenLine.block_list[i].get_failureBR()))
                if(greenLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                    self.ui.faultlistTable.setItem(x,4, QTableWidgetItem(greenLine.block_list[i].get_failureTC()))
                if(greenLine.block_list[i].get_failureTC() == "Power Failure!"):
                    self.ui.faultlistTable.setItem(x,5, QTableWidgetItem(greenLine.block_list[i].get_failurePW()))
                x = x+1
            for i in range(len(redLine.block_list)):
                self.ui.faultlistTable.insertRow(self.ui.faultlistTable.rowCount())
                self.ui.faultlistTable.setItem(x,0, QTableWidgetItem(str(redLine.get_line())))
                self.ui.faultlistTable.setItem(x,1, QTableWidgetItem(str(redLine.block_list[i].get_sectionID())))
                self.ui.faultlistTable.setItem(x,2, QTableWidgetItem(str(redLine.block_list[i].get_blockID())))
                if(redLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                    self.ui.faultlistTable.setItem(x,3, QTableWidgetItem(redLine.block_list[i].get_failureBR()))
                if(redLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                    self.ui.faultlistTable.setItem(x,4, QTableWidgetItem(redLine.block_list[i].get_failureTC()))
                if(redLine.block_list[i].get_failureTC() == "Power Failure!"):
                    self.ui.faultlistTable.setItem(x,5, QTableWidgetItem(redLine.block_list[i].get_failurePW()))
                x = x+1 

        elif(self.green_selected == True and self.red_selected == False):
            x=0
            for i in range(len(greenLine.block_list)):
                self.ui.faultlistTable.insertRow(self.ui.faultlistTable.rowCount())
                self.ui.faultlistTable.setItem(x,0, QTableWidgetItem(str(greenLine.get_line())))
                self.ui.faultlistTable.setItem(x,1, QTableWidgetItem(str(greenLine.block_list[i].get_sectionID())))
                self.ui.faultlistTable.setItem(x,2, QTableWidgetItem(str(greenLine.block_list[i].get_blockID())))
                if(greenLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                    self.ui.faultlistTable.setItem(x,3, QTableWidgetItem(greenLine.block_list[i].get_failureBR()))
                if(greenLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                    self.ui.faultlistTable.setItem(x,4, QTableWidgetItem(greenLine.block_list[i].get_failureTC()))
                if(greenLine.block_list[i].get_failureTC() == "Power Failure!"):
                    self.ui.faultlistTable.setItem(x,5, QTableWidgetItem(greenLine.block_list[i].get_failurePW()))
                x = x+1
        elif(self.red_selected == True and self.green_selected == False):
            x=0
            for i in range(len(redLine.block_list)):
                self.ui.faultlistTable.insertRow(self.ui.faultlistTable.rowCount())
                self.ui.faultlistTable.setItem(x,0, QTableWidgetItem(str(redLine.get_line())))
                self.ui.faultlistTable.setItem(x,1, QTableWidgetItem(str(redLine.block_list[i].get_sectionID())))
                self.ui.faultlistTable.setItem(x,2, QTableWidgetItem(str(redLine.block_list[i].get_blockID())))
                if(redLine.block_list[i].get_failureBR() == "Broken Rail Fault!"):
                    self.ui.faultlistTable.setItem(x,3, QTableWidgetItem(redLine.block_list[i].get_failureBR()))
                if(redLine.block_list[i].get_failureTC() == "Track Circuit Failure!"):
                    self.ui.faultlistTable.setItem(x,4, QTableWidgetItem(redLine.block_list[i].get_failureTC()))
                if(redLine.block_list[i].get_failureTC() == "Power Failure!"):
                    self.ui.faultlistTable.setItem(x,5, QTableWidgetItem(redLine.block_list[i].get_failurePW()))
                x = x+1

    #---------------------------------------------------------------
    # Alternate Functions
    #---------------------------------------------------------------
    #Create block items, Stations, Lights, switches, basic blocks, and crossings
    #add text
    def add_block_text(self,x,y, id):
        pen = QColor(0,0,0)
        item = graphics_text(x,y,id, pen, self)
        item.setPos(x+7,y-20)
        self.scene.addItem(item)
        return item

    def add_train_text(self, x, y, id):
        pen = QColor(255,255,255)
        item = graphics_text(x,y,id, pen, self)
        item.setPos(x+13,y-2)
        self.scene.addItem(item)
        return item

    #add Light
    def addLight(self,rect,id):
        pen = QPen(Qt.SolidLine)
        pen.setColor(QColor(255,255,255))
        pen.setWidth(2)
        brush = QBrush(QColor(255,0,0))
        brush.setStyle(Qt.SolidPattern)
        item = signal_colors(rect, pen, brush, id,self)
        self.scene.addItem(item)
        return item
    
    #add track block
    def addbasicSquare(self, rect, pw, tooltip, line):
        pen =  QPen(Qt.SolidLine)
        pen.setColor(QColor(112,128,144))
        pen.setWidth(pw)
        brush =  QBrush(QColor(128,128,128))
        brush.setStyle(Qt.SolidPattern)
        item = block_nodes(rect, pen, brush, tooltip, self, line)
        self.scene.addItem(item)
        return item
    
    #add station block
    def addstationsquare(self, rect, pw, tooltip, line):
        pen =  QPen(Qt.SolidLine)
        pen.setColor(QColor (255, 0, 0))
        pen.setWidth(pw)
        brush =  QBrush(QColor(192,21,133))
        brush.setStyle(Qt.Dense1Pattern)
        item = block_nodes(rect, pen, brush, tooltip, self, line)
        self.scene.addItem(item)
        return item
        
    #add switch block
    def addswitchsquare(self, rect, pw, tooltip, line):
        pen =  QPen(Qt.SolidLine)
        pen.setColor(QColor(255, 0, 0))
        pen.setWidth(pw)
        brush =  QBrush(QColor(60, 179, 113))
        brush.setStyle(Qt.Dense3Pattern)
        item = block_nodes(rect, pen, brush, tooltip, self, line)
        self.scene.addItem(item)
        return item   

    #add crossing block
    def addcrossingsquare(self, rect, pw, tooltip, line):
        pen =  QPen(Qt.SolidLine)
        pen.setColor(QColor(255, 0, 0))
        pen.setWidth(pw)
        brush =  QBrush(QColor(60, 179, 113))
        brush.setStyle(Qt.Dense3Pattern)
        item = block_nodes(rect, pen, brush, tooltip, self, line)
        self.scene.addItem(item)
        return item   

    #Pull events for QViewer
    def eventFilter(self, source, event):
        if (source == self.ui.graphicsView.viewport() and 
            event.type() == QEvent.Wheel):
                if event.angleDelta().y() > 0:
                    scale = 1.25
                else:
                    scale = .8
                self.ui.graphicsView.scale(scale, scale)
                return True
                # do not propagate the event to the scroll area scrollbars
        elif (source == self.ui.graphicsView_2.viewport() and 
            event.type() == QEvent.Wheel):
                if event.angleDelta().y() > 0:
                    scale = 1.25
                else:
                    scale = .8
                self.ui.graphicsView_2.scale(scale, scale)
                # do not propagate the event to the scroll area scrollbars
                return True

        return super().eventFilter(source,event)

#---------------------------------------------------------------
# Train Functions
#---------------------------------------------------------------
    def update_train_block(self):
        #blueLine.update_trains()
        greenLine.update_trains()
        redLine.update_trains()
            
    def add_train(self):
        #if(self.blue_selected == True):
            #if the occupancy of the Yard is false, set it true and make a train
        #    if(b_block[0].get_occupancy() == False):
        #        blueLine.add_train(
        if(self.green_selected == True and track_model_ui.line_selected == "Green"):
            if(g_block[0].get_occupancy() == False):
                greenLine.add_train()
    
        if(self.red_selected == True and track_model_ui.line_selected == "Red"):
            if(r_block[0].get_occupancy() == False):
                redLine.add_train()

    def delete_train(self, train_id, line):
        if line == "green":
            greenLine.delete_train(train_id)
        
        if line == "red":
            redLine.delete_train(train_id)    
        
    def update_occupancy_map(self):
        if(self.green_selected == True):
            #If the block has a failure turn it orangish-yellow
            for i in range(len(greenLine.block_list)):
                if(g_block[i].get_failure_exists() == True):
                    items = g_block_list[g_block[i].get_blockID()]
                    items.set_block_color(QColor(255,165,0))
                elif(g_block[i].get_failure_exists() == True and g_block[i].get_occupancy() == True):
                    items = g_block_list[g_block[i].get_blockID()]
                    items.set_block_color(QColor(255,165,0))
                elif(greenLine.block_list[i].get_occupancy() == True):
                    train_block = g_block_list[g_block[i].get_blockID()]
                    if(g_block[i].stations != None):
                        if(greenLine.block_list[i].get_dwelling()):
                            brush =  QBrush(QColor(139, 0, 139))
                            brush.setStyle(Qt.Dense2Pattern)
                            train_block.set_block_color(brush)
                            train_block.setZValue(0)
                        else:
                            brush =  QBrush(QColor(153, 50, 204))
                            brush.setStyle(Qt.SolidPattern)
                            train_block.set_block_color(brush)
                            train_block.setZValue(0)  
                    else:
                        brush =  QBrush(QColor(153, 50, 204))
                        brush.setStyle(Qt.SolidPattern)
                        train_block.set_block_color(brush)
                        train_block.setZValue(0)  
                                    
                    try:
                        for train_id, value in greenLine.trains.items():
                            if value != "Yard":
                                if (g_block[i].get_blockID() == greenLine.trains[train_id].get_train_position()):
                                    x_pos, y_pos = g_block_list[g_block[i].get_blockID()].get_pos()
                                    if (greenLine.trains[train_id].get_train_position() == 0 and greenLine.trains[train_id].get_in_yard() == True):
                                            if greenLine.trains[train_id].get_in_yard() == True and g_train_list[train_id] == None:
                                                g_train_list[int(train_id)] = self.add_train_text(int(x_pos),int(y_pos),str(train_id))
                                                g_train_list[int(train_id)].set_position(x_pos+18,y_pos-2)
                                                g_train_list[int(train_id)].setZValue(1)
                                                break
                                    elif(greenLine.trains[train_id].get_train_position() == 0 and greenLine.trains[train_id].get_in_yard() == False and greenLine.trains[train_id].get_yard_delay() == False):
                                        self.scene.removeItem(g_train_list[train_id])
                                        g_train_list[train_id] = None
                                        self.delete_train(train_id, "green")
                                    else:
                                        greenLine.trains[train_id].set_change_in_yard(False)
                                        x_pos, y_pos = g_block_list[g_block[i].get_blockID()].get_pos()
                                        if g_train_list[int(train_id)]:
                                            g_train_list[int(train_id)].set_position(x_pos+18,y_pos-2)
                                            g_train_list[int(train_id)].setZValue(1)
                                        greenLine.trains[int(train_id)].set_yard_delay(False)
                                    
                    except KeyError:
                        pass
                else:
                    painted = False
                    #if there is a a switch, change its colors based on their states
                    painted = self.green_switch_update_colors(i)
                    if painted == True:
                        continue
                    #if block is a station
                    if(g_block[i].stations != None):
                        if(math.isnan(g_block[i].get_station_id()) == False):
                            not_train_block = g_block_list[i]
                            brush = QBrush(QColor(192,21,133))
                            brush.setStyle(Qt.Dense1Pattern)
                            not_train_block.set_block_color(brush)
                    #crossings
                    elif(g_block[i].rail_crossings != None):
                        #change crossing color based on state
                        #if crossing is raised
                        if (g_block[i].get_crossing_state() == False):
                            crossing_block = g_block_list[i]
                            brush =  QBrush(QColor(200,55 , 0))
                            brush.setStyle(Qt.Dense3Pattern)
                            crossing_block.set_block_color(brush)
                        else: #if crossing is lowered
                            crossing_block = g_block_list[i]
                            brush =  QBrush(QColor(0,0,255))
                            brush.setStyle(Qt.Dense3Pattern)
                            crossing_block.set_block_color(brush)
                    else:
                        if(g_block[i].get_failure_exists()== False):
                            not_train_block = g_block_list[i]
                            brush = QBrush(QColor(128,128,128))
                            brush.setStyle(Qt.SolidPattern)
                            not_train_block.set_block_color(brush)
                        else:
                            not_train_block = g_block_list[i]
                            not_train_block.set_block_color(QColor(255,165,0))

        if(self.red_selected == True):
            #If the block has a failure turn it orangish-yellow
            for i in range(len(redLine.block_list)):
                if(r_block[i].get_failure_exists() == True):
                    items = r_block_list[r_block[i].get_blockID()]
                    items.set_block_color(QColor(255,165,0))
                elif(r_block[i].get_failure_exists() == True and r_block[i].get_occupancy() == True):
                    items = r_block_list[r_block[i].get_blockID()]
                    items.set_block_color(QColor(255,165,0))
                elif(redLine.block_list[i].get_occupancy() == True):
                    train_block = r_block_list[g_block[i].get_blockID()]
                    if(r_block[i].stations != None):
                        if(redLine.block_list[i].get_dwelling()):
                            brush =  QBrush(QColor(139, 0, 139))
                            brush.setStyle(Qt.Dense2Pattern)
                            train_block.set_block_color(brush)
                            train_block.setZValue(0)
                        else:
                            brush =  QBrush(QColor(153, 50, 204))
                            brush.setStyle(Qt.SolidPattern)
                            train_block.set_block_color(brush)
                            train_block.setZValue(0)  
                    else:
                        brush =  QBrush(QColor(153, 50, 204))
                        brush.setStyle(Qt.SolidPattern)
                        train_block.set_block_color(brush)
                        train_block.setZValue(0)  
                    
                    try:
                        for train_id, value in redLine.trains.items():
                            if value != "Yard":
                                if (r_block[i].get_blockID() == redLine.trains[train_id].get_train_position()):
                                    x_pos, y_pos = r_block_list[r_block[i].get_blockID()].get_pos()
                                    if (redLine.trains[train_id].get_train_position() == 0 and redLine.trains[train_id].get_in_yard() == True):
                                            if redLine.trains[train_id].get_in_yard() == True and r_train_list[train_id] == None:
                                                r_train_list[int(train_id)] = self.add_train_text(int(x_pos),int(y_pos),str(train_id))
                                                r_train_list[int(train_id)].set_position(x_pos+18,y_pos-2)
                                                r_train_list[int(train_id)].setZValue(1)
                                                break
                                    elif(redLine.trains[train_id].get_train_position() == 0 and redLine.trains[train_id].get_in_yard() == False and redLine.trains[train_id].get_yard_delay() == False):
                                        self.scene.removeItem(r_train_list[train_id])
                                        r_train_list[train_id] = None
                                        self.delete_train(train_id, "red")
                                    else:
                                        redLine.trains[train_id].set_change_in_yard(False)
                                        x_pos, y_pos = r_block_list[r_block[i].get_blockID()].get_pos()
                                        if r_train_list[int(train_id)]:
                                            r_train_list[int(train_id)].set_position(x_pos+18,y_pos-2)
                                            r_train_list[int(train_id)].setZValue(1)
                                        redLine.trains[int(train_id)].set_yard_delay(False)
                    except KeyError:
                        pass

                else:
                    painted = False
                    #if there is a a switch, change its colors based on their states
                    painted = self.red_switch_update_colors(i)
                    if painted == True:
                        continue
                    #if block is a station
                    if(r_block[i].stations != None):
                        if(math.isnan(r_block[i].get_station_id()) == False):
                            not_train_block = r_block_list[i]
                            brush = QBrush(QColor(192,21,133))
                            brush.setStyle(Qt.Dense1Pattern)
                            not_train_block.set_block_color(brush)
                    #crossings
                    elif(r_block[i].rail_crossings != None):
                        #change crossing color based on state
                        #if crossing is raised
                        if (r_block[i].get_crossing_state() == False):
                            crossing_block = r_block_list[i]
                            brush =  QBrush(QColor(200,55 , 0))
                            brush.setStyle(Qt.Dense3Pattern)
                            crossing_block.set_block_color(brush)
                        else: #if crossing is lowered
                            crossing_block = r_block_list[i]
                            brush =  QBrush(QColor(0,0,255))
                            brush.setStyle(Qt.Dense3Pattern)
                            crossing_block.set_block_color(brush)
                    else:
                        if(r_block[i].get_failure_exists()== False):
                            not_train_block = r_block_list[i]
                            brush = QBrush(QColor(128,128,128))
                            brush.setStyle(Qt.SolidPattern)
                            not_train_block.set_block_color(brush)
                        else:
                            not_train_block = r_block_list[i]
                            not_train_block.set_block_color(QColor(255,165,0))
                        
    #Update light states based on their backend status
    def update_light_states(self):
        #if self.blue_selected == True:
        #    pass
        if self.green_selected == True:
            for i in range(len(greenLine.block_list)):
                if(g_block[i].track_lights != None):
                    item1 = g_light_list[g_block[i].get_light_id()]
                    color = g_block[i].get_light_state()
                    brush = QBrush(QColor(color))
                    item1.setbrush(brush)

        if self.red_selected == True:
            for i in range(len(redLine.block_list)):
                if(r_block[i].track_lights != None):
                    item1 = r_light_list[r_block[i].get_light_id()]
                    color = r_block[i].get_light_state()
                    brush = QBrush(QColor(color))
                    item1.setbrush(brush)
                    
    #Update switch colors from the update_occupancy function
    def green_switch_update_colors(self,i):
        painted = None
        for x in range(len(Database.greendatabase["switchID"])):
                        if(i == Database.greendatabase["switchblockA"][x]):
                            switchblock =  Database.greendatabase["switchOn"][x]
                            corner_block = g_block[switchblock].get_switch_corner_block()
                            brush =  QBrush(QColor(0, 255, 255))
                            brush.setStyle(Qt.Dense3Pattern)
                            not_train_block = g_block_list[corner_block]
                            not_train_block.set_block_color(brush)
                            painted = True
                            break
                        elif(i == Database.greendatabase["switchblockB"][x]):
                            switchblock =  Database.greendatabase["switchOn"][x]
                            connectedblock = g_block[switchblock].get_connected_to()
                            if (i == connectedblock): 
                                brush =  QBrush(QColor(0, 255, 255))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  g_block_list[connectedblock]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            else:
                                brush =  QBrush(QColor(0, 139, 139))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  g_block_list[i]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            break
                        elif(i == Database.greendatabase["switchblockC"][x]):
                            switchblock =  Database.greendatabase["switchOn"][x]
                            connectedblock = g_block[switchblock].get_connected_to()
                            if (i == connectedblock):
                                #brush =  QBrush(QColor(30, 229, 224))
                                brush =  QBrush(QColor(0, 255, 255))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  g_block_list[connectedblock]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            else:
                                brush =  QBrush(QColor(0, 139, 139))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  g_block_list[i]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            continue
        return painted
  
    def red_switch_update_colors(self,i):
        painted = None
        for x in range(len(Database.reddatabase["switchID"])):
                        if(i == Database.reddatabase["switchblockA"][x]):
                            switchblock =  Database.reddatabase["switchOn"][x]
                            corner_block = r_block[switchblock].get_switch_corner_block()
                            brush =  QBrush(QColor(0, 255, 255))
                            brush.setStyle(Qt.Dense3Pattern)
                            not_train_block = r_block_list[corner_block]
                            not_train_block.set_block_color(brush)
                            painted = True
                            break
                        elif(i == Database.reddatabase["switchblockB"][x]):
                            switchblock =  Database.reddatabase["switchOn"][x]
                            connectedblock = r_block[switchblock].get_connected_to()
                            if (i == connectedblock): 
                                brush =  QBrush(QColor(0, 255, 255))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  r_block_list[connectedblock]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            else:
                                brush =  QBrush(QColor(0, 139, 139))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  r_block_list[i]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            break
                        elif(i == Database.reddatabase["switchblockC"][x]):
                            switchblock =  Database.reddatabase["switchOn"][x]
                            connectedblock = r_block[switchblock].get_connected_to()
                            if (i == connectedblock):
                                #brush =  QBrush(QColor(30, 229, 224))
                                brush =  QBrush(QColor(0, 255, 255))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  r_block_list[connectedblock]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            else:
                                brush =  QBrush(QColor(0, 139, 139))
                                brush.setStyle(Qt.Dense3Pattern)
                                not_train_block =  r_block_list[i]
                                not_train_block.set_block_color(brush) 
                                painted = True
                            continue
        return painted
        
#---------------------------------------------------------------
# Build the Rail systems
# Note: build the blocks, then the stations, switches, lights, crossings
# then connect the switches to the track blocks
#---------------------------------------------------------------

'''
def build_blue_rail_system(line_name:str):
    #build rail Line

    blueLine = rail_lines(line_name) # make blue line
    #Build track blocks
    for i in range(len(Database.bluedatabase["blockNumbers"])):
        blueLine.build_rail_blocks(int(Database.bluedatabase["blockNumbers"][i]),Database.bluedatabase["Sections"][i],
                                   Database.bluedatabase["Length"][i], Database.bluedatabase["Elevation"][i],
                                   Database.bluedatabase["cumulativeElevation"][i],
                                   Database.bluedatabase["Grade"][i], Database.bluedatabase["maxSpeed"][i],
                                    False, False, Database.bluedatabase["polarity"][i],0)
        #print(blueLine.block_list[i].get_blockID(42))
    b_block = blueLine.block_list
    
    #build train stations on blocksex
    if (len(Database.bluedatabase["stationID"]) > 0):    
        stattemp = 0
        for i in range(len(blueLine.block_list)):
            if(Database.bluedatabase["stationList"][i] == Database.bluedatabase["stationID"][stattemp]):
                if(stattemp <= len(Database.bluedatabase["stationID"])):
                    b_block[i].build_station(int(Database.bluedatabase["stationID"][stattemp]),
                                            Database.bluedatabase["stationName"][stattemp],
                                            Database.bluedatabase["Underground"][stattemp],
                                            0,
                                            Database.bluedatabase["stationexitSide"][stattemp]
                                            )
                    stattemp = stattemp + 1


    #for i in range(len(Line.block_list)):
    #    if(b_block[i].stations != None):
    #        print(b_block[i].get_station_id())
    

    #print(Database.bluedatabase["switchID"])
    #Build switches on blocks
  #create switches if ID is on the switchblockA
    if (len(Database.bluedatabase["switchID"]) > 0):
        for i in range(len(blueLine.block_list)):
            for y in range(len(Database.bluedatabase["switchID"])):
                if(Database.bluedatabase["switchList"][i]== Database.bluedatabase["switchID"][y]):
                    blueLine.block_list[i].build_switch(Database.bluedatabase["switchID"][y])
                            
    #set Switch Connections
        for i in range(len(blueLine.block_list)):
            for y in range(len(Database.bluedatabase["switchID"])):
                if(Database.bluedatabase["switchList"][i] == Database.bluedatabase["switchID"][y]):
                    b_block[i].set_switch_connections(int(Database.bluedatabase["switchblockA"][y]), 
                        int(Database.bluedatabase["switchblockB"][y]),
                            int(Database.bluedatabase["switchblockC"][y]),
                            int(Database.bluedatabase["switchblockA"][y]))
                    
    #Insert stuff that deals with lights here
    if(len(Database.bluedatabase["lightID"]) > 0):
        for i in range(len(blueLine.block_list)):
            blueLine.block_list[i].build_light(Database.bluedatabase["lightList"][i])

    #Set Light States
    for i in range(len(blueLine.block_list)):
        for y in range(len(Database.bluedatabase["switchblockA"])):
            if (i == Database.bluedatabase["switchblockA"][y]):
                    b_block[i].track_lights.set_light_state("Green")
            if (i == Database.bluedatabase["switchblockB"][y]):
                    b_block[i].track_lights.set_light_state("Green")

    #set blueline time to travel
    for i in range(len(blueLine.block_list)):
        distance = b_block[i].get_block_length()
        #print("distance: " + str(distance))
        speed = b_block[i].get_max_speed() * 1000 #1000 km/hr
        #print("speed: "+ str(speed))
        seconds_in_hour = 3600
        time = (distance/speed)*seconds_in_hour
        #print("time: "+ str(time))
        b_block[i].set_time_to_travel(time)

    #for i in range(len(blueLine.block_list)):
    #    if(blueLine.block_list[i].track_switches != None):
    #        print(b_block[i].get_switch_id())    
    
    return blueLine
'''

def build_green_rail_system(line_name:str):
    #build rail Line

    greenLine = rail_lines(line_name) # make blue line
    #Build track blocks
    for i in range(len(Database.greendatabase["blockNumbers"])):
        greenLine.build_rail_blocks(Database.greendatabase["blockNumbers"][i],Database.greendatabase["Sections"][i],
                                   Database.greendatabase["Length"][i], Database.greendatabase["Elevation"][i],
                                   Database.greendatabase["cumulativeElevation"][i],
                                   Database.greendatabase["Grade"][i], Database.greendatabase["maxSpeed"][i],
                                    False, False, Database.greendatabase["polarity"][i], Database.greendatabase["Underground"][i])
    g_block = greenLine.block_list

    #beacon information
    # THIS/LAST Station, Next station, door side of |This/last|[x changes in length for x 
    # blocks --> with x values], [block grade,.,.], 
    # [speed: x changes length, for the next x blocks , block length,(next x blocks, block length)]
    # ,[elevation,.,.,.], [cumulative elev,.,.,.]
    #,[underground:no changes, for X blocks, x]||
    #->else [1 changes,after x blocks, block values 0, 2 blocks, value 1 ]

    station_beacon1_list = {0:[[0,9,2,[0,63,64,65]],[None]],
                            1:[[1,3,0,[2,151,1,13,14,15,16]],["Dir 0"]], 
                            2: [[None],[1,2,11,[9,8,7,6,5,4,3,2]]], 
                            3: [[3,4,2,[16,17,18,19,20,21,22]],[1,3,2,[16,15,14,13]]], 
                            4 :[[4,5,2,[22,23,24,25,26,27,28,29]],[4,5,2,[22,21,20,19,18,17,16]]], 
                            5 :[[5,6,1,[31,32,33,34,35,36,37,38,39]],[None]], 
                            6: [[6,7,2,[39,40,41,42,43,44,45,46,47,48]],[6,4,2,[141,142,143,144,145,146,147,148,149,150]]], 
                            7: [[7,8,2,[48,49,50,51,52,53,54,55,56,57]],[7,6,2,[132,133,134,135,136,137,138,139,140,141]]], 
                            8: [[8,9,2,[57]],[8,7,2,[123,124,125,126,127,128,129,130,131,132]]], 
                            9: [[9,10,1,[65,66,67,68,69,70,71,72,73]],[9,8,1,[114,115,116,117,118,119,120,121,122,123]]], 
                            10: [[10,11,1,[73,74,75,76]],[10,9,1,[105,106,107,108,109,110,111,112,113,114]]], 
                            11: [[11,12,2,[77,78,79,80,81,82,83,84,85]],[11,10,2,[77,101,152,102,103,104,105]]], 
                            12: [[12,13,2,[88,89,90,91,92,93,94,95,96]],[None]], 
                            13: [["Dir 1"], [13,11,2,[96,97,98,99,100]]] 
                            }

    station_beacon2_list = {0: None,  
                            1: None,
                            2: None,
                            3: None,
                            4: None,
                            5: None,
                            6: None,
                            7: None, 
                            8: None, 
                            9: None,
                            10: None, 
                            11: None, 
                            12: None, 
                            13: None, 
                            } #[[],[]],  
    
    #build train stations on blocks
    if (len(Database.greendatabase["stationID"]) > 0):    
        for x in range(len(greenLine.block_list)):
            for y in range(len( Database.greendatabase["stationID"])):
                if(Database.greendatabase["stationList"][x] == Database.greendatabase["stationID"][y]):
                        g_block[x].build_station(int(Database.greendatabase["stationID"][y]),
                                                Database.greendatabase["stationName"][y],
                                                Database.greendatabase["Underground"][y],
                                                5, #Passengers waiting at all times
                                                Database.greendatabase["stationexitSide"][y],
                                                station_beacon1_list[y],
                                                station_beacon2_list[y])
    
    #beaconB
    switch_beaconb_list = {0: [["Error"],[3,2,1,[12,11,10,9]]],
                           1: [[10,11,1,[76,77]],["Error"]],
                           2: [[11,12,2,[86,87,88]],["Error"]],
                           3: [[4,5,2,[30,31]],["Error"]],
                           4: [[8,9,2,[58,59,60,61,62]],["Error"]],
                           5: [[8,9,2,[62,63,64,65]],["Error"]],
                           }
    
    #BeaconC
    switch_beaconc_list = {0: [[1,3,0,[1,13,14,15,16]],["Error"]],
                           1: [["Error"],[11,10,2,[101,152,102,103,104,105]]],
                           2: [["Error"],[13,11,2,[100,85,84,83,82,81,80,79,78,77]]],
                           3: [["Error"],[6,4,2,[150,29,28,27,26,25,24,23,22]]],
                           4: [[0,9,2,[0,63,64,65]],["Error"]],
                           5: [[0,9,2,[0,63,64,65]],["Error"]],
                           }

    #create switches if ID is on the switchblockA
    if (len(Database.greendatabase["switchID"]) > 0):
        for i in range(len(greenLine.block_list)):
            for y in range(len(Database.greendatabase["switchID"])):
                if(Database.greendatabase["switchList"][i]== Database.greendatabase["switchID"][y]):
                    greenLine.block_list[i].build_switch(Database.greendatabase["switchID"][y], switch_beaconb_list[y],
                                                        switch_beaconc_list[y])
    # for each switch leg and corner, and switch. Set the blocks and identify where beacons will be placed
    # also identify which block to call the beacon data from.
    if (len(Database.greendatabase["switchID"]) > 0):
        for i in range(len(greenLine.block_list)):
            for y in range(len(Database.greendatabase["switchID"])):
                if(i == Database.greendatabase["switchblockB"][y]):
                    greenLine.block_list[i].set_switch_leg_b(int(Database.greendatabase["switchblockB"][y]))
                    greenLine.block_list[i].set_block_switch_on(int(Database.greendatabase["switchOn"][y]))
                    greenLine.block_list[i].set_switch_corner(int(Database.greendatabase["switchblockA"][y]))
                elif(i == Database.greendatabase["switchblockC"][y]):
                    greenLine.block_list[i].set_switch_leg_c(int(Database.greendatabase["switchblockC"][y]))
                    greenLine.block_list[i].set_block_switch_on(int(Database.greendatabase["switchOn"][y]))
                    greenLine.block_list[i].set_switch_corner(int(Database.greendatabase["switchblockA"][y]))
                elif(i == Database.greendatabase["switchblockA"][y]):
                    greenLine.block_list[i].set_switch_corner(int(Database.greendatabase["switchblockA"][y]))
                    greenLine.block_list[i].set_block_switch_on(int(Database.greendatabase["switchOn"][y]))
                    greenLine.block_list[i].set_switch_leg_c(int(Database.greendatabase["switchblockC"][y]))
                    greenLine.block_list[i].set_switch_leg_b(int(Database.greendatabase["switchblockB"][y]))
                else:
                    pass
                

    #set Switch Connections
    for i in range(len(greenLine.block_list)):
        for y in range(len(Database.greendatabase["switchID"])):
            if(Database.greendatabase["switchList"][i] == Database.greendatabase["switchID"][y]):
                g_block[i].set_switch_connections(int(Database.greendatabase["switchblockA"][y]), 
                    int(Database.greendatabase["switchblockB"][y]),
                        int(Database.greendatabase["switchblockC"][y]),
                        int(Database.greendatabase["switchOn"][y]))

    #build lights
    for i in range(len(greenLine.block_list)):
            for y in range(len(Database.greendatabase["lightID"])):
                if(Database.greendatabase["lightList"][i] == Database.greendatabase["lightID"][y]):
                        g_block[i].build_light(int(Database.greendatabase["lightList"][i]))

    if(len(Database.greendatabase["crossingID"])> 0):
        for i in range(len(greenLine.block_list)):
            for y in range(len(Database.greendatabase["crossingID"])):
                if(Database.greendatabase["crossingList"][i] >= Database.greendatabase["crossingID"][y]):
                    g_block[i].build_crossing(int(Database.greendatabase["crossingID"][y]))
                    
            

    #set greenLine time to travel
    #print(range(len(greenLine.block_list)))
    for i in range(len(greenLine.block_list)):
        distance = g_block[i].get_block_length()
        speed = g_block[i].get_max_speed()
        seconds_in_hour = 1
        time = (distance/speed)*seconds_in_hour
        g_block[i].set_time_to_travel(time)
        #print("block " + str(i) + " time to travel: " + str(time))

    return greenLine

# Build the Red Line
def build_red_rail_system(linename:str):
 #build rail Line

    redLine = rail_lines(linename) # make blue line
    #Build track blocks
    for i in range(len(Database.reddatabase["blockNumbers"])):
        redLine.build_rail_blocks(Database.reddatabase["blockNumbers"][i],Database.reddatabase["Sections"][i],
                                   Database.reddatabase["Length"][i], Database.reddatabase["Elevation"][i],
                                   Database.reddatabase["cumulativeElevation"][i],
                                   Database.reddatabase["Grade"][i], Database.reddatabase["maxSpeed"][i]*.277778,
                                    False, False, Database.reddatabase["polarity"][i], Database.reddatabase["Underground"][i])
    r_block = redLine.block_list
    
    #beacon information
    # direction, THIS/LAST Station, Next station,[x changes in length for x 
    # blocks --> with x values], [block grade,.,.], 
    # [speed: x changes length, for the next x blocks , block length,(next x blocks, block length)]
    # ,[elevation,.,.,.], [cumulative elev,.,.,.]
    #,[underground:no changes, for X blocks, x]||
    #->else [1 changes,after x blocks, block values 0, 2 blocks, value 1 ]
   
    station_beacon1_list = {0: [[0,1,2,[0,9,8,7]],["Error"]],
                            1: [[1,2,2,[7,6,5,4,3,2,1]],[1,0,2,[8,9,0]]],
                            2: [[2,3,2,[16,17,18,19,20,21]],[2,1,2,[16]]],
                            3: [[3,4,2,[21,22,23,24,25]],[3,2,2,[21,20,19,18,17,16]]],
                            4: [[4,5,2,[25,26,27]],[4,3,2,[25,24,23,22,21]]],
                            5: [[5,6,2,[35,36,37,38]],[6,5,2,[35,34,33]]],
                            6: [[6,7,2,[48,49,50,51,52]],[6,5,2,[48,47,46,45,44]]], 
                            7: [["Dir 1"],[7,6,2,[60,61,62,63,64,65,78,66]]]
                            }

    station_beacon2_list = {0: None,  
                            1: None,
                            2: None,
                            3: None,
                            4: None,
                            5: None,
                            6: None,
                            7: None
                            } #[[],[]],  
    
    #build train stations on blocks
    #print(len(Database.reddatabase["stationID"]))
    #print("---------------------------------")
    if (len(Database.reddatabase["stationID"]) > 0):    
        for x in range(len(redLine.block_list)):
            for y in range(len(Database.reddatabase["stationID"])):
                if(Database.reddatabase["stationList"][x] == Database.reddatabase["stationID"][y]):
                        r_block[x].build_station(int(Database.reddatabase["stationID"][y]),
                                                Database.reddatabase["stationName"][y],
                                                Database.reddatabase["Underground"][y],
                                                5, #Passengers waiting at all times
                                                Database.reddatabase["stationexitSide"][y],
                                                station_beacon1_list[y],
                                                station_beacon2_list[y])

    #beaconB
    switch_beaconb_list = {0: [[0,1,2,[0,9,8,7]],["Error"]],
                           1: [[1,2,2,[1,16]],[2,1,2,[1,2,3,4,5,6,7]]],
                           2: [[4,5,2,[28,29,30,31,32]],[5,4,2,[28,27,26,25]]],
                           3: [[4,5,2,[32,33,34,35]],[5,4,2,[32,31,30,29,28]]],
                           4: [[5,6,2,[39,40,41,42,43]],[6,5,2,[39,38,37,36,35]]],
                           5: [[5,6,2,[43,44,45,46,47,48]],[6,5,2,[43,42,41,40,39]]],
                           6: [[6,7,2,[53,54,55,56,57,58,59,60]],[7,6,2,[53,52,51,50,49,48]]]
                           }
    
    #BeaconC
    switch_beaconc_list = {0: [[2,1,2,[10,9,8,7]],["Dir 0"]],
                           1: [["Error"],[2,1,2,[15,14,13,12,11,10]]],
                           2: [[4,5,2,[77,76,75,74,73,72]],[5,4,2,[77,27,26,25]]],
                           3: [[4,5,2,[72,33,34,35]],[5,4,2,[72,73,74,75,76,77]]],
                           4: [[5,6,2,[71,70,69,68,67]],[6,5,2,[71,38,37,36,35]]],
                           5: [[5,6,2,[67,44,45,46,47,48]],[6,5,2,[67,68,69,70,71]]],
                           6: [["Error"],[7,6,2,[66,52,51,50,49,48]]]
                           }

    #create switches if ID is on the switchblockA
    if (len(Database.reddatabase["switchID"]) > 0):
        for i in range(len(redLine.block_list)):
            for y in range(len(Database.reddatabase["switchID"])):
                if(Database.reddatabase["switchList"][i]== Database.reddatabase["switchID"][y]):
                    redLine.block_list[i].build_switch(Database.reddatabase["switchID"][y], switch_beaconb_list[y],
                                                        switch_beaconc_list[y])


    # for each switch leg and corner, and switch. Set the blocks and identify where beacons will be placed
    # also identify which block to call the beacon data from.
    if (len(Database.reddatabase["switchID"]) > 0):
        for i in range(len(redLine.block_list)):
            for y in range(len(Database.reddatabase["switchID"])):
                if(i == Database.reddatabase["switchblockB"][y]):
                    redLine.block_list[i].set_switch_leg_b(int(Database.reddatabase["switchblockB"][y]))
                    redLine.block_list[i].set_block_switch_on(int(Database.reddatabase["switchOn"][y]))
                    redLine.block_list[i].set_switch_corner(int(Database.reddatabase["switchblockA"][y]))
                elif(i == Database.reddatabase["switchblockC"][y]):
                    redLine.block_list[i].set_switch_leg_c(int(Database.reddatabase["switchblockC"][y]))
                    redLine.block_list[i].set_block_switch_on(int(Database.reddatabase["switchOn"][y]))
                    redLine.block_list[i].set_switch_corner(int(Database.reddatabase["switchblockA"][y]))
                elif(i == Database.reddatabase["switchblockA"][y]):
                    redLine.block_list[i].set_switch_corner(int(Database.reddatabase["switchblockA"][y]))
                    redLine.block_list[i].set_block_switch_on(int(Database.reddatabase["switchOn"][y]))
                    redLine.block_list[i].set_switch_leg_c(int(Database.reddatabase["switchblockC"][y]))
                    redLine.block_list[i].set_switch_leg_b(int(Database.reddatabase["switchblockB"][y]))
                else:
                    pass
                

    #set Switch Connections
    for i in range(len(redLine.block_list)):
        for y in range(len(Database.reddatabase["switchID"])):
            if(Database.reddatabase["switchList"][i] == Database.reddatabase["switchID"][y]):
                r_block[i].set_switch_connections(int(Database.reddatabase["switchblockA"][y]), 
                    int(Database.reddatabase["switchblockB"][y]),
                        int(Database.reddatabase["switchblockC"][y]),
                        int(Database.reddatabase["switchOn"][y]))

    #build lights
    for i in range(len(redLine.block_list)):
            for y in range(len(Database.reddatabase["lightID"])):
                if(Database.reddatabase["lightList"][i] == Database.reddatabase["lightID"][y]):
                        r_block[i].build_light(Database.reddatabase["lightList"][i])


    if(len(Database.reddatabase["crossingID"])> 0):
        for i in range(len(redLine.block_list)):
            for y in range(len(Database.reddatabase["crossingID"])):
                if(Database.reddatabase["crossingList"][i] >= Database.reddatabase["crossingID"][y]):
                    r_block[i].build_crossing(int(Database.reddatabase["crossingID"][y]))
                    
    #set redLine time to travel
    #print(range(len(redLine.block_list)))
    for i in range(len(redLine.block_list)):
        distance = r_block[i].get_block_length()
        speed = r_block[i].get_max_speed()
        seconds_in_hour = 1
        time = (distance/speed)*seconds_in_hour
        r_block[i].set_time_to_travel(time)
        #print("block " + str(i) + " time to travel: " + str(time))

    return redLine

# ------------------------------
#setup railway
# ------------------------------
#Blue Line
blueLine = None
#blueLine = build_blue_rail_system("blue")
#b_block = blueLine.block_list
#b_block_list = {}
#b_light_list = {}

#Green Line items
greenLine = build_green_rail_system("green")
g_block = greenLine.block_list
g_block_list = {}
g_light_list = {}
g_train_list = {}
for i in range(1,150):
    g_train_list[i] = None
g_block_text = {}
#Red Line items
redLine = build_red_rail_system("red")
r_block = redLine.block_list
r_block_list = {}
r_light_list = {}
r_train_list = {}
for i in range(1,70):
    r_train_list[i] = None
r_block_text = {}
#train global objects
if __name__ == "__main__":

    #setup redline items
    #redLine = build_red_rail_system("red")
    #r_block = redLine.block_list

    app = QApplication(sys.argv)
    railway = track_model_ui()

    #window = track_model_ui()
    #window.show()

    sys.exit(app.exec())