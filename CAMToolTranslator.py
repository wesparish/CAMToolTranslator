#!/usr/bin/env python

import csv

class ToolBase:
  def __init__():
    self.cutterName = "End Mill Name"
    self.cutterType = "Flat Mill"
    self.cutterDiam = 0.0
    self.cutterFluteLen = 0.0
    self.cutterOAL = 0.0
    self.cutterHolder = None
    self.coolant = "Flood"
    self.rpm = 0
    self.ipm = 0

class CAMToolListBase:
  def __init__():
    self.toolList = []

  def loadFile():
    print "Not implemented"
    return False

class SprutCAMToolList(CAMToolListBase):
  def __init__(self, inputFile = "input/sprut_input.csv", delimiter = ';'):
    self.inputFile = inputFile
    self.delimiter = delimiter

    self.ID = 0 #INTEGER 
    self.NAME = "NAME" #STRING 
    self.MILL_TYPE = 0 #INTEGER 
    self.L = 0.0 #DOUBLE 
    self.D = 0.0 #DOUBLE 
    self.RC = 0.0 #DOUBLE 
    self.R = 0.0 #DOUBLE 
    self.A = 0.0 #DOUBLE 
    self.H = 0.0 #DOUBLE
    self.d1 = 0.0 #DOUBLE
    self.MEASUREMENT_UNITS = 0 #INTEGER
    self.ROTATIONS_PER_MIN = 0.0 #DOUBLE
    self.CUTTING_SPEED = 0.0 #DOUBLE
    self.SPINDLE_DIRECTION = 0 #INTEGER
    self.TEETH_NUMBER = 0 #INTEGER
    self.MATERIAL = "STRING" #STRING
    self.DURABILITY = 0.0 #DOUBLE
    self.FEEDRATE = 0.0 #DOUBLE
    self.NUMPOS = 0 #INTEGER
    self.NUMSTORE = 0 #INTEGER
    self.HOLDER = "STRING" #STRING
    self.COMMENT = "STRING" #STRING
    self.FORMLENGTH = 0.0 #DOUBLE
    self.WORKLENGTH = 0.0 #DOUBLE
    self.MINDEPTH = 0.0 #DOUBLE
    self.DEPTH = 0.0 #DOUBLE
    self.MAXDEPTH = 0.0 #DOUBLE
    self.MINFN = 0.0 #DOUBLE
    self.MAXFN = 0.0 #DOUBLE
    self.OPERATION = 0 #INTEGER
    self.MATERIALGROUP = 0 #INTEGER
    self.FROMMATERIAL = 0 #INTEGER
    self.BESTMATERIAL = 0 #INTEGER
    self.TOMATERIAL = 0 #INTEGER
    self.FEED_SPEED = "STRING" #STRING
    self.RA_FN = "STRING" #STRING
    self.APxFN_VC = "STRING" #STRING
    self.ADAPTER = "STRING" #STRING
    self.CURVE = "STRING" #STRING
    self.USECURVE = False #BOOLEAN
    self.OVERHANG = 0.0 #DOUBLE
    self.RCOR = 0 #INTEGER
    self.LCOR = 0 #INTEGER;

  def loadFile(self):
    with open(self.inputFile, 'rb') as f:
      reader = csv.reader(f, delimiter=self.delimiter, quoting=csv.QUOTE_NONE)
      for row in reader:
        print row
        self.toolList += ""

class Fusion360ToolList(CAMToolListBase):
  def __init__():
    pass

if __name__ == "__main__":
  print "CAMToolTranslator starting..."

  sprutLoader = SprutCAMToolList(inputFile = "input/sprut_input.csv")
  sprutLoader.loadFile()

  print "CAMToolTranslator finished"
