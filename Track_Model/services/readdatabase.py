
import os
#import requests, json
import pandas as pd
import math


class Database():
  '''
  bluedatabase = {
      "authority" : [],
      "Line" : [],              # States line from database file
      "Sections" :[],           # States section from database file
      "blockNumbers" :[],       # block numbers
      "Length" :[],             # length of block
      "Grade" :[],              # gradient Level
      "maxSpeed" :[],           # Max speed for each block
      "stationID" :[],          # station ID
      "stationList": [],        # Station Name's for each station on blue line
      "stationexitSide": [],    # Station exit side
      "switchList": [],         # List of all switches on line
      "lightList": [],          # List of all lights on line
      "lightID" : [],           # Light ID's for each switch on blue line
      "Elevation" :[],          # Elevation for each block
      "cumulativeElevation":[], # Cumulative elevation for each blue block
      "switchblockA" : [],      # each switch's block A
      "switchblockB" : [],      # each switches 2nd connection
      "switchblockC" : [],      # each section's 3rd connection
      "stationName" : [],       # each station on line.
      "Underground" : []        # are blocks underground
  }
  '''

  greendatabase = {
      "authority" : [],
      "Line" : [],              # States line from database file
      "Sections" :[],           # States section from database file
      "blockNumbers" :[],       # block numbers
      "Length" :[],             # length of block
      "Grade" :[],              # gradient Level
      "maxSpeed" :[],           # Max speed for each block
      "stationID" :[],          # station ID
      "stationList": [],        # Station Name's for each station on blue line
      "stationexitSide": [],    # Station exit side
      "switchList": [],         # List of all switches on line
      "lightList": [],          # List of all lights on line
      "lightID" : [],           # Light ID's for each switch on blue line
      "crossingList": [],       # list of all crossings
      "crossingID": [],         # ID's of all crossings
      "Elevation" :[],          # Elevation for each block
      "cumulativeElevation":[], # Cumulative elevation for each blue block
      "switchblockA" : [],      # each switch's block A
      "switchblockB" : [],      # each switches 2nd connection
      "switchblockC" : [],      # each section's 3rd connection
      "switchOn": [],           # block each switch is on
      "stationName" : [],       # each station on line.
      "Underground" : [],       # are blocks underground
      "polarity" : [],          # Block polarity
      "traversalTime" : []      # time it take to traverse block
  }


  reddatabase = {
      "authority" : [],
      "Line" : [],              # States line from database file
      "Sections" :[],           # States section from database file
      "blockNumbers" :[],       # block numbers
      "Length" :[],             # length of block
      "Grade" :[],              # gradient Level
      "maxSpeed" :[],           # Max speed for each block
      "stationID" :[],          # station ID
      "stationList": [],        # Station Name's for each station on blue line
      "stationexitSide": [],    # Station exit side
      "switchList": [],         # List of all switches on line
      "lightList": [],          # List of all lights on line
      "lightID" : [],           # Light ID's for each switch on blue line
      "crossingList": [],       # list of all crossings
      "crossingID": [],         # Crossing of all IDs
      "Elevation" :[],          # Elevation for each block
      "cumulativeElevation":[], # Cumulative elevation for each blue block
      "switchblockA" : [],      # each switch's block A
      "switchblockB" : [],      # each switches 2nd connection
      "switchblockC" : [],      # each section's 3rd connection
      "switchOn": [],           # Block switch is on
      "stationName" : [],       # each station on line.
      "Underground" : [],       # are blocks underground
      "polarity" : [],          # Polarity of each block
      "traversalTime" : []      # traversal time of each block
  }


  #--------------------------
  # Read from files
  #--------------------------
  
  '''
  #get path to database
  LAYOUT_PATH = os.path.join(os.getcwd(),"Track_Model","data","blueline.xlsx") 
  xls = pd.ExcelFile(LAYOUT_PATH)
  #import xlxs for sheet blue
  blue = pd.read_excel(xls)
  
  bluedatabase["Line"] = blue["Line"].tolist()
  bluedatabase["Sections"] = blue["Section"].tolist()
  bluedatabase["blockNumbers"] = blue["Block Number"].tolist()
  bluedatabase["Length"] = blue["Block Length (m)"].tolist()
  bluedatabase["Grade"] = blue["Block Grade (%)"].tolist()
  bluedatabase["stationList"] = blue["StationList"].tolist()
  bluedatabase["maxSpeed"] = blue["Speed Limit (Km/Hr)"].tolist()
  bluedatabase["switchList"] = blue["SwitchList"].tolist()
  bluedatabase["Elevation"] = blue["ELEVATION (M)"].tolist()
  bluedatabase["cumulativeElevation"] = blue["CUMALTIVE ELEVATION (M)"].tolist()
  bluedatabase["lightList"] = blue["LightList"].tolist()
  bluedatabase["polarity"] = blue["Polarity"].tolist()
  bluedatabase["Underground"] = blue["Underground"].tolist()
  #load switdh information
  #switchID has already been loaded above
  switches = pd.read_excel(xls, "switches")
  bluedatabase["switchID"] = switches["SwitchID"].tolist()
  bluedatabase["switchblockA"] = switches["BlockA"].tolist()
  bluedatabase["switchblockB"] = switches["BlockB"].tolist()
  bluedatabase["switchblockC"] = switches["BlockC"].tolist()

  #load station data
  #station ID's, lines, are already loaded from mains sheet "blue"
  #Station Name, Directions for entry/exit, 
  stations = pd.read_excel(xls, "stations")
  bluedatabase["stationID"]   = stations["StationID"]
  bluedatabase["stationName"] = stations["Station Name"]
  bluedatabase["Underground"] = stations["Underground"]
  bluedatabase["stationexitSide"] = stations["Exit"]

  lights = pd.read_excel(xls, "lights")
  bluedatabase["lightID"] = lights["Light ID"]
  '''
  #---------------------------------------------------------------
  # Read Green Line Information
  #---------------------------------------------------------------
  #get path to database
  LAYOUT_PATH = os.path.join(os.getcwd(),"Track_Model","data","greenline.xlsx") 
  xls = pd.ExcelFile(LAYOUT_PATH)

  #import xlxs for sheet green
  green = pd.read_excel(xls)
  greendatabase["Line"] = green["Line"].tolist()
  greendatabase["Sections"] = green["Section"].tolist()
  greendatabase["blockNumbers"] = green["Block Number"]
  greendatabase["blockNumbers"] =   greendatabase["blockNumbers"].fillna(0)
  greendatabase["Length"] = green["Block Length (m)"].tolist()
  greendatabase["Grade"] = green["Block Grade (%)"].tolist()
  greendatabase["stationList"] = green["Station List"].tolist()
  greendatabase["maxSpeed"] = green["Speed Limit (Km/Hr)"].tolist()
  greendatabase["switchList"] = green["Switch List"].tolist()
  greendatabase["lightList"] = green["Light List"]
  greendatabase["Elevation"] = green["ELEVATION (M)"].tolist()
  greendatabase["cumulativeElevation"] = green["CUMALTIVE ELEVATION (M)"].tolist()
  greendatabase["stationexitSide"] = green["Station Side"]
  greendatabase["traverseTime"] = green["seconds to traverse block"]
  greendatabase["x"] = green["X"].tolist()
  greendatabase["y"] = green["Y"].tolist()
  greendatabase["polarity"] = green["Polarity"]
  greendatabase["crossingList"] = green["Crossing List"]
  greendatabase["Underground"] = green["Underground"]
  
  
  #load crossing information
  #switchID has already been loaded above
  crossings = pd.read_excel(xls, "crossings")
  greendatabase["crossingID"] = crossings["Crossing ID"]

  #load switch information
  #switchID has already been loaded above
  switches = pd.read_excel(xls, "switches")
  greendatabase["switchID"] = switches["SwitchID"]
  greendatabase["switchblockA"] = switches["BlockA"]
  greendatabase["switchblockB"] = switches["BlockB"]
  greendatabase["switchblockC"] = switches["BlockC"]
  greendatabase["switchOn"] = switches["blockOn"]
  
    #load light information
  lights = pd.read_excel(xls, "lights")
  greendatabase["lightID"]   = lights["Light ID"]
  #load station data
  #station ID's, lines, are already loaded from mains sheet "green"
  #Station Name, Directions for entry/exit, 
  stations = pd.read_excel(xls, "stations")
  stations.fillna(value="N/A")
  greendatabase["stationID"]   = stations["StationID"]
  greendatabase["stationName"] = stations["Station Name"]


   #---------------------------------------------------------------
  # Read Red Line Information
  #---------------------------------------------------------------
  #get path to database
  LAYOUT_PATH = os.path.join(os.getcwd(),"Track_Model","data","redline.xlsx") 
  xls = pd.ExcelFile(LAYOUT_PATH)

  #import xlxs for sheet green
  red = pd.read_excel(xls)
  reddatabase["Line"] = red["Line"].tolist()
  reddatabase["Sections"] = red["Section"].tolist()
  reddatabase["blockNumbers"] = red["Block Number"]
  reddatabase["blockNumbers"] =   reddatabase["blockNumbers"].fillna(0)
  reddatabase["Length"] = red["Block Length (m)"].tolist()
  reddatabase["Grade"] = red["Block Grade (%)"].tolist()
  reddatabase["stationList"] = red["Station List"].tolist()
  reddatabase["maxSpeed"] = red["Speed Limit (Km/Hr)"].tolist()
  reddatabase["switchList"] = red["Switch List"].tolist()
  reddatabase["lightList"] = red["Light List"].tolist()
  reddatabase["Elevation"] = red["ELEVATION (M)"].tolist()
  reddatabase["cumulativeElevation"] = red["CUMALTIVE ELEVATION (M)"].tolist()
  reddatabase["stationexitSide"] = red["Station Side"]
  reddatabase["traverseTime"] = red["seconds to traverse block"]
  reddatabase["x"] = red["X"].tolist()
  reddatabase["y"] = red["Y"].tolist()
  reddatabase["polarity"] = red["Polarity"]
  reddatabase["crossingList"] = red["Crossing List"]
  reddatabase["Underground"] = red["Underground"]
  #load crossing information
  #switchID has already been loaded above
  crossings = pd.read_excel(xls, "crossings")
  reddatabase["crossingID"] = crossings["Crossing ID"]

  #load switch information
  #switchID has already been loaded above
  switches = pd.read_excel(xls, "switches")
  reddatabase["switchID"] = switches["SwitchID"]
  reddatabase["switchblockA"] = switches["BlockA"]
  reddatabase["switchblockB"] = switches["BlockB"]
  reddatabase["switchblockC"] = switches["BlockC"]
  reddatabase["switchOn"] = switches["blockOn"]
  
    #load light information
  lights = pd.read_excel(xls, "lights")
  reddatabase["lightID"] = lights["Lightids"]
  print(reddatabase["lightList"])
  print(reddatabase["lightID"])
  #load station data
  #station ID's, lines, are already loaded from mains sheet "red"
  #Station Name, Directions for entry/exit, 
  stations = pd.read_excel(xls, "stations")
  stations.fillna(value="N/A")
  reddatabase["stationID"]   = stations["StationID"]
  reddatabase["stationName"] = stations["Station Name"]