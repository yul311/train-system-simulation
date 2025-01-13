import re,inspect,threading,dataclasses

## toplevs ##
from Train_Model.classes.Train_Model import TrainModel
from Train_Controller.train_controller import TrainController

## tm-tc APIs ##
from Train_Model.tcontroller_to_train import ControllerTrainModelAPI
from Train_Controller.trainmodelcontrollerAPI import TrainControllerAPI

## tr-tm APIs ##
from Train_Model.track_to_train import TrackTrainModelAPI
from Track_Model.API.train_to_track import TrainTrackAPI

def construct_train(track_model_instance: any):
    
    #print("Train builder called")
    controller = TrainController()
    model = TrainModel()
    
    tm_to_tc = TrainControllerAPI(controller)
    tc_to_tm = ControllerTrainModelAPI(model)
    
    tr_to_tm = TrackTrainModelAPI(model)
    tm_to_tr = TrainTrackAPI(track_model_instance)
    
    model.link_train_control(tm_to_tc)
    model.link_track_model(tm_to_tr)
    
    controller.link_train_model(tc_to_tm)
    
    return model, controller, tr_to_tm
    
    