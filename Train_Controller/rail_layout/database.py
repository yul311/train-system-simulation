import os
#import requests, json
import pandas as pd
import math

class Database():
  green_line = {
      "Line" : [],              # States line from database file
      "blockNumbers" :[],       # block numbers
      "Length" :[],             # length of block
      "Grade" :[],              # gradient Level
      "maxSpeed" :[],           # Max speed for each block
      "Elevation" :[],          # Elevation for each block
      "cumulativeElevation":[], # Cumulative elevation for each blue block
      "Underground" : []        # are blocks underground
  }

  red_line = {
      "Line" : [],              # States line from database file
      "blockNumbers" :[],       # block numbers
      "Length" :[],             # length of block
      "Grade" :[],              # gradient Level
      "maxSpeed" :[],           # Max speed for each block
      "Elevation" :[],          # Elevation for each block
      "cumulativeElevation":[], # Cumulative elevation for each blue block
      "Underground" : []        # are blocks underground
  }


  #--------------------------
  # Read from files
  #--------------------------

  #---------------------------------------------------------------
  # Read Green Line Information
  #---------------------------------------------------------------
  #get path to database
  LAYOUT_PATH = os.path.join(os.getcwd(),"Train_Controller","rail_layout","greenline.xlsx") 
  xls = pd.ExcelFile(LAYOUT_PATH)

  #import xlxs for sheet green
  green = pd.read_excel(xls)
  #get path to database
  #import xlxs for sheet green
  green_line = pd.read_excel(xls)
  green_line["Line"] = green["Line"].tolist()
  # green_line["Sections"] = green["Section"].tolist()
  green_line["blockNumbers"] = green["Block Number"]
  green_line["Length"] = green["Block Length (m)"].tolist()
  green_line["Grade"] = green["Block Grade (%)"].tolist()
  green_line["maxSpeed"] = green["Speed Limit (Km/Hr)"].tolist()
  green_line["Elevation"] = green["ELEVATION (M)"].tolist()
  green_line["cumulativeElevation"] = green["CUMALTIVE ELEVATION (M)"].tolist()
  green_line["Underground"] = green["Underground"]

  xls.close()
  try:
    xls.handles = None
  except:
    pass
  
  

  #---------------------------------------------------------------
  # Read Red Line Information
  #---------------------------------------------------------------
  #get path to database
  LAYOUT_PATH = os.path.join(os.getcwd(),"Train_Controller","rail_layout","redline.xlsx") 
  xls = pd.ExcelFile(LAYOUT_PATH)

  #import xlxs for sheet green
  red = pd.read_excel(xls)
  red_line["Line"] = red["Line"].tolist()
  red_line["blockNumbers"] = red["Block Number"]
  # red_line["blockNumbers"] =   red_line["blockNumbers"].fillna(0)
  red_line["Length"] = red["Block Length (m)"].tolist()
  red_line["Grade"] = red["Block Grade (%)"].tolist()
  red_line["stationList"] = red["Station List"].tolist()
  red_line["maxSpeed"] = red["Speed Limit (Km/Hr)"].tolist()
  red_line["Elevation"] = red["ELEVATION (M)"].tolist()
  red_line["cumulativeElevation"] = red["CUMALTIVE ELEVATION (M)"].tolist()
  red_line["stationexitSide"] = red["Station Side"]
  red_line["Underground"] = red["Underground"]

  #load station data
  #station ID's, lines, are already loaded from mains sheet "red"
  #Station Name, Directions for entry/exit, 
  stations = pd.read_excel(xls, "stations")
  stations.fillna(value="N/A")
  red_line["stationID"]   = stations["StationID"]
  red_line["stationName"] = stations["Station Name"]
  
  xls.close()
  try:
    xls.handles = None
  except:
    pass