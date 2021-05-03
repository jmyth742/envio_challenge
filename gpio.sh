#!/bin/bash

while getopts ":x:y:" opt; do
  case $opt in
    y) arg1="$OPTARG"
    ;;
    x) arg2="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

gpio_enable()
{
    echo $1 > /sys/class/gpio/export
    echo "out" > /sys/class/gpio/gpio$1/direction
}
gpio_read()
{
  var="$(cat /sys/class/gpio/gpio$1/value)"
}

gpio_write_low()
{
  echo 0 > /sys/class/gpio/gpio$1/value
}

gpio_write_high()
{
  echo 1 > /sys/class/gpio/gpio$1/value
}

gpio_enable $arg1
gpio_enable $arg2 
gpio_read $arg1



if [ $# -lt 2 ]; then
    # TODO: print usage
    echo "Please provide gpioY -y and gpioX -x pin"
    exit 1
fi
else ;
  if [ $var=="1" ] ; then
    echo "pin on"
    while :
      do
        # loop infinitely
        gpio_write_high $arg2
        sleep 1 
        gpio_write_low $arg2
        
      done
  elif [ $var=="0" ] ; then
    echo "pin off"
    gpio_write_low $arg2
  fi