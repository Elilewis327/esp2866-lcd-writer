from machine import Pin as pin
from machine import PWM
import time

db7 = pin(5, pin.OUT)
db6 = pin(4, pin.OUT)
db5 = pin(0, pin.OUT)
db4 = pin(2, pin.OUT)
rs = pin(12, pin.OUT)
e = pin(14, pin.OUT)
contrast = PWM(pin(13))

def write_data(data, prewait, rsval):
	time.sleep(prewait/1000)
    	e.value(1)
    	db7.value(int(data[0]))
    	db6.value(int(data[1]))
    	db5.value(int(data[2]))
	db4.value(int(data[3]))
	rs.value(int(rsval))
	time.sleep(.010)
	e.value(0)
	#print(db7.value(), db6.value(), db5.value(), db4.value(), " - ", rs.value())


def write(data):
	data = bytearray(data, "utf-8")
	for i in range(len(data)):
		sdata = data[i]
		sdata = str(bin(sdata))
		sdata = sdata[2:]
		while len(sdata) < 8:
			sdata = str("0") + sdata
		#print(sdata)
		write_data(sdata[0:4], 1, 1)
		write_data(sdata[4:], 1, 1)

def clear():
	write_data('0000', 10, 0)
	write_data('0001', 10, 0)

def init():
	write_data('0010', 100, 0)#hundered mils for everything to powerup
	write_data('0010', 5, 0)#function set to for 4 bit operation
	write_data('0000', 5, 0)
	write_data('0000', 5, 0)# 1 - d - c -b
	write_data('1100', 5, 0)

	w.contrast.duty(400)
	w.contrast.freq(1000 )

	clear()
	write("hello")
	time.sleep(1)
	clear()



