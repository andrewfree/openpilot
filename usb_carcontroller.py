#!/usr/bin/env python
from evdev import InputDevice
from select import select
import time
import numpy as np
import zmq

from cereal import car

import selfdrive.messaging as messaging
from selfdrive.services import service_list
from common.realtime import Ratekeeper

from common.fingerprints import fingerprint

if __name__ == "__main__":
  # ***** connect to joystick *****
  # USB Gamepad Controller
  dev = InputDevice("/dev/input/event1")
  print dev

  button_values = [0]*13
  axis_values = [0]*7

  # ***** connect to car *****
  context = zmq.Context()
  logcan = messaging.sub_sock(context, service_list['can'].port)
  sendcan = messaging.pub_sock(context, service_list['sendcan'].port)

  CP = fingerprint(logcan)
  print('from selfdrive.car.'+CP.carName+'.interface import CarInterface')
  exec('from selfdrive.car.'+CP.carName+'.interface import CarInterface')

  CI = CarInterface(CP, sendcan)

  rk = Ratekeeper(100)

  while 1:
    # **** handle joystick ****
    r, w, x = select([dev], [], [], 0.0)
    if dev in r:
      for event in dev.read():
        print event
        ## Button events
        if event.type == 1:
          btn = event.code - 303
          if btn >= 1 and btn < 13:
            button_values[btn] = int(event.value)

        # # Axis move events
        if event.type == 3:
          ## Left Joystick
          if event.code == 0:
            axis_values[event.code] = np.clip(-event.value/32768.0, -1.0, 1.0)
          elif event.code == 1:
            axis_values[event.code] = np.clip(-event.value/32768.0, -1.0, 1.0)
          ## Left and Right Triggers
          elif event.code in [2,5]:
            if event.code == 2:
                event.value = -event.value
            axis_values[2] = np.clip(event.value/1023.0, -1.0, 1.0)
          ## Right Joystick
          elif event.code == 3:
            axis_values[event.code] = np.clip(-event.value/32768.0, -1.0, 1.0)
          elif event.code == 4:
            axis_values[event.code] = np.clip(-event.value/32768.0, -1.0, 1.0)
          ## D-Pad (left)
          elif event.code == 16:
            print event.value
            axis_values[5] = -int(event.value)
          elif event.code == 17:
            axis_values[6] = -int(event.value)

    print axis_values, button_values
    # **** handle car ****

    CC = car.CarControl.new_message()

    CC.enabled = True

    CC.actuators.gas = float(np.clip(-axis_values[0], 0, 1.0))
    CC.actuators.brake = float(np.clip(axis_values[0], 0, 1.0))
    CC.actuators.steer = float(axis_values[2])

    CC.hudControl.speedVisible = bool(button_values[1])
    CC.hudControl.lanesVisible = bool(button_values[2])
    CC.hudControl.leadVisible = bool(button_values[3])

    CC.cruiseControl.override = bool(button_values[0])
    CC.cruiseControl.cancel = bool(button_values[-1])

    CC.hudControl.setSpeed = float(axis_values[2] * 100.0)

    # TODO: test alerts
    CC.hudControl.visualAlert = "none"
    CC.hudControl.audibleAlert = "none"

    print CC

    CS = CI.update(CC)
    print CS

    if not CI.apply(CC):
      print "CONTROLS FAILED"

    rk.keep_time()
