import os 
import sys
import getopt
import time

# Sysfs constants

SYSFS_BASE_PATH     = '/sys/class/gpio'

SYSFS_EXPORT_PATH   = SYSFS_BASE_PATH + '/export'
SYSFS_UNEXPORT_PATH = SYSFS_BASE_PATH + '/unexport'

SYSFS_GPIO_PATH           = SYSFS_BASE_PATH + '/gpio{}'
SYSFS_GPIO_VALUE_PATH     = SYSFS_GPIO_PATH + '/value'

SYSFS_GPIO_VALUE_LOW   = '0'
SYSFS_GPIO_VALUE_HIGH  = '1'



class Pin(object):
    def __init__(self, number):
        """
        init a pin object, with the gpio number. 
        """
        self._number = number
        

        self._fd = open(SYSFS_GPIO_VALUE_PATH % number, 'r+')

    def write_pin(self):
        """
        Set pin to HIGH logic setLevel
        """
        self._fd.write(SYSFS_GPIO_VALUE_HIGH)
        self._fd.seek(0)

    def reset_pin(self):
        """
        Set pin to LOW logic setLevel
        """
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
      opts, args = getopt.getopt(argv,"hy:x:",["gpioY=","gpioX="])
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
    # if(opts == empty())
   print('gpioY is ', gpioY)
   print('gpioX is ', gpioX)

   ## set pin x and pin y
   ## current state = read(y)
   ## if y is high , toggle x on/off each second (H-L-H-L etc)
   ## else if y is low, set x low. 

if __name__ == "__main__":
   main(sys.argv[1:])