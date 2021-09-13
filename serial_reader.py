import serial
ser = serial.Serial('/dev/cu.usbserial-10', 9600)
while True:
    cc = str(ser.readline())
    print(cc[2:][:-5])