#!/bin/python

import serial


class 2308:
    def __init__(self, interface):
        self.description = ""

    def fw_status(self):
        status = serial.cmd('IDENT')
        return status

    def analog_out(self, port, value):
        if -5000 <= value <= 5000:
           status = port.cmd('AOUT,' + port + ',' + value)
        else:
            print('invalid value')

    def analog_in(self, port):
        return port.cmd('AVAL?,'+ port)

    def digital_out(self, port, state):
        if state == '1' or state == 'ON':
            status = port.cmd('RLON,' + port)
        else if state == '0' or state == 'OFF':
            status = port.cmd('RLOFF,' + port)

        if status == '\x0DOK\x0D':
            return 'OK'
        else:
            return status

    def digital_in(self, port):


class port:
    def __init__(self, interface):
        ser = serial.Serial(interface)

    def __enter__(self):
        return self

    def cmd(command):
        self.ser.write(command)
        return ser.read()

    def __exit__(self, exc_type, exc_value, traceback):
