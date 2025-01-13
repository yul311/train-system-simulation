import sys, os, dataclasses
import threading
## import module top-level definitions ##
from CTC.ctc_office import ctcOffice as CTCOffice
from Wayside_Controller_SW.wayside_controller import WaysideController
from Track_Model.Controller import rail_lines as TrackModel
from Train_Model.classes.Train_Model import TrainModel
from Train_Controller.train_controller import TrainController

## import module top-level instances ##
from CTC.ctc_office import ctc_office
from Wayside_Controller_SW.wayside_controller import wayside_nodes
from Track_Model.Controller import greenLine as track_model_green, redLine as track_model_red

## import module UI types ##
from CTC.ui.ctc_ui_loader import CTCUI
from CTC.office_to_ui import OfficeToUI

from Wayside_Controller_SW.wayside_ui import WaysideUI
from Wayside_Controller_SW.wayside_ui import construct_ui as WaysideUIBuilder
from Wayside_Controller_SW.controller_to_ui import ControllerToUI

from Track_Model.Controller import track_model_ui as TrackModelUI

from Train_Model.Train_Model_ui_loader import TrainModelUI

from Train_Controller.train_ctrl_ui import TrainCtrlUi as TrainControllerUI

## import APIs ##
# inputs TO ctc
from CTC.track_to_ctc import TrackCTCAPI
from CTC.wayside_to_ctc import WaysideCTCAPI
# inputs TO wayside
from Wayside_Controller_SW.ctc_to_wayside import CTCWaysideAPI
from Wayside_Controller_SW.track_to_wayside import TrackWaysideAPI
# inputs TO track
from Track_Model.API.wayside_to_track import WaysideTrackAPI
from Track_Model.API.train_to_track import TrainTrackAPI
# inputs TO train mdl
from Train_Model.track_to_train import TrackTrainModelAPI
from Train_Model.tcontroller_to_train import ControllerTrainModelAPI
# inputs TO train ctl
from Train_Controller.trainmodelcontrollerAPI import TrainControllerAPI

## import simulator ##
from Main.simulation_time import sim

def construct_frontends() -> (CTCUI, WaysideUI, TrackModelUI, TrainModelUI, TrainControllerUI):
    # construct module UI instances

    ctc_ui = CTCUI()
    ctc_to_ui = OfficeToUI(ctc_ui)
    ctc_office.link_ui(ctc_to_ui)
    
    wayside_ui = WaysideUIBuilder()
    # link wayside backend to frontend
    ws_to_ui = ControllerToUI(wayside_ui)
    for ws in wayside_nodes.values():
        ws.link_ui(ws_to_ui)
    
    track_model_ui = TrackModelUI()

    train_model_ui = TrainModelUI()
    
    train_controller_ui = TrainControllerUI() #tc = None)
   

    return ctc_ui,wayside_ui,track_model_ui,train_model_ui,train_controller_ui

def link_apis():
    
    # NOTE links involving train model & train controller will be handled in track model
    
    ## construct APIs ##

    ws_to_ctc = WaysideCTCAPI(ctc_office)
    tr_to_ctc = TrackCTCAPI(ctc_office)
    
    ctc_to_ws = CTCWaysideAPI()
    tr_to_ws = TrackWaysideAPI()
    
    ws_to_tr = WaysideTrackAPI()
    
    ## link APIs ##
        
    # link ctc
    ctc_office.link_wayside(ctc_to_ws)
        
    # link wayside
    for ws in wayside_nodes.values():
        ws.link_track(ws_to_tr)
        ws.link_ctc(ws_to_ctc)

    # load base PLCs
    wayside_nodes[1].load_plc_program(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_1.plc"))
    wayside_nodes[2].load_plc_program(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_2.plc"))
    wayside_nodes[3].load_plc_program(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_3.plc"))
    wayside_nodes[4].load_plc_program(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_4.plc"))
    wayside_nodes[5].load_plc_program(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_5.plc"))


    #NOTE: This will only work for green line, a way to differentiate
    # which line from the link is needed for ctc
    # link track model
    track_model_green.set_links(tr_to_ctc,tr_to_ws)
    track_model_red.set_links(tr_to_ctc,tr_to_ws)
    
    def ctc_disp():
        ctc_to_ws.set_wayside_node(4)
        ctc_to_ws.dispatch_train(75, 15)
    
    #timer = threading.Timer(5, ctc_disp)
    #timer.start()