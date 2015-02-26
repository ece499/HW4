import serial
serport="/dev/ttyAMA0"
ser=serial.Serial(serport,9600)#9600)
ser.write('D')
print ser.readline()
