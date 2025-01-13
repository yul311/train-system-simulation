to do:
implement block grade slows acceleration *
controller need to implement calculating distance traveled for authority purposes *
configure class and variables and function correctly *
add the actual equations *
fix the qt designer to have murphy trigger faults from main page *
use metric when doing the actual equations *
doors shouldn't open when train is moving *
power = 0 no more engine moving *
beacon reader *
stuff to send to train controller *
receiving stuff from train controller *
same but wiht track model *

ctc: suggested speed -> train ctrl: power command -> train model: actual power consumption -> train ctrl *

signal pickup failure: no authority and suggested speed 

train position is in the middle of the train *

get number of passengers from track model from ticket sales *
implement random number of passenger getting off at a station 

create a train handler to deploy trains and have a train handler ui 

add train id on ui 
implement an annoucement that disappears 
implement friction 
friction coefficient for steel wheel on steel rail

add only opening doors when the current speed is zero
making all passengers get off at the last stop

NO LONGER SENDING TICKET SALES once I reach block, waiting on ctc signal