import os 
import sys
import getopt
import time

import logging


## setup logging here.
##
Logger = logging.getLogger('gpio < Y >')
Logger.addHandler(logging.StreamHandler())
Logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('envio.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
Logger.addHandler(fh)


# Sysfs constants

SYSFS_BASE_PATH     = '/sys/class/gpio'

SYSFS_EXPORT_PATH   = SYSFS_BASE_PATH + '/export'
SYSFS_UNEXPORT_PATH = SYSFS_BASE_PATH + '/unexport'

SYSFS_GPIO_PATH           = SYSFS_BASE_PATH + '/gpio{}'
SYSFS_GPIO_DIRECTION_PATH = SYSFS_GPIO_PATH + '/direction'
SYSFS_GPIO_VALUE_PATH     = SYSFS_GPIO_PATH + '/value'

SYSFS_PIN_DIRECTION_OUT = "out"

SYSFS_GPIO_VALUE_LOW   = '0'
SYSFS_GPIO_VALUE_HIGH  = '1'



class Pin():
    def __init__(self, number):
        """
        init a pin object, with the gpio number. 
        """
        self._number = number

        self.pin_setup()
        self.pin_direction()

        self._fd = open(SYSFS_GPIO_VALUE_PATH.format(number), 'r+')


    def pin_setup(self):
        try:
           self._fd = open(SYSFS_EXPORT_PATH,"w")
           self._fd.write((self._number))
           self._fd.seek(0)
        except IOError:
            print("GPIO {} already Exists, so skipping export gpio".format(self._number))  
 
    def pin_direction(self):
       """
       set up the pin direction, this is just defaulting to out, could be in or out. 
       """
       self._fd = open(SYSFS_GPIO_DIRECTION_PATH.format(self._number) , "w")
       self._fd.write(SYSFS_PIN_DIRECTION_OUT)
       self._fd.seek(0)
        
      
    def pin_high(self):
        """
        Set pin to HIGH logic setLevel
        """
        self._fd.write(SYSFS_GPIO_VALUE_HIGH)
        self._fd.seek(0)

    def pin_low(self):
        """
        Set pin to LOW logic setLevel
        """
        Logger.debug("LOW")
        self._fd.write(SYSFS_GPIO_VALUE_LOW)
        self._fd.seek(0)

    def read_state(self):
        """
        Read pin value

        @rtype: int
        @return: I{0} when LOW, I{1} when HIGH
        """
        val = self._fd.read()
        self._fd.seek(0)
        return int(val)





def main(argv):
   gpioY = ''
   gpioX = ''
   try:
      opts, args = getopt.getopt(argv,"y:x:hl:",["gpioY=","gpioX=","log="])
      if not opts:
         print("Please enter arguements...")
         sys.exit(2)
   except getopt.GetoptError:
      print('test.py  GPIO Y number -y <gpioY> GPIO X number -x <gpioX>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py  GPIO Y number -y <gpioY> GPIO X number -x <gpioX>')
         sys.exit()
      elif opt in ("-y", "--gpioY"):
         gpioY = arg
      elif opt in ("-x", "--gpioX"):
         gpioX = arg
      elif opt in ("-l", "--log"):
         logger = arg
         
   xPin = Pin((gpioX))
   yPin = Pin((gpioY))
   print(yPin.read_state())
   if(yPin.read_state == 1):
      print("triggering pin")
      while(True):
         xPin.pin_high()
         time.sleep(1)
         xPin.pin_low()
   else:
      print("should all be low...")
      xPin.pin_low() 
 
      

if __name__ == "__main__":
   main(sys.argv[1:])