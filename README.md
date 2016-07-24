# BlackStarCommunicator
Software for communication with the Black Star 2308 I/O interface.

The Black Star 2308 is a input/output module with the following features
- 8 12-bit 4096mV analog inputs
- 4 12-bit +/- 5 or +/- 10V analog outputs
- 8 digital inputs
- 8 relay outputs

It is usefull as a low speed test instrument, but could probably also be used as the hadware interface of a simple PLC.

The communication inteface is based on RS232C using 9600 baud 8N1. The communication protocol is utilizing simple ASCII commands, terminated by a carriage return (0x0D). This enables the use of a seral console for communication (e.g. minicom or PuTTy), however is is sometimes uefull to have a simple command line tool for usage in scipts.

This project goal is to implement the complete command set in Python.


The complete manual is available at: [http://www.mediafire.com/download/417d3ymb0tvj431/Black+Star+2308.pdf](http://www.mediafire.com/download/417d3ymb0tvj431/Black+Star+2308.pdf)
