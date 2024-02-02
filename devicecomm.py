import serial

ser = serial.Serial()
class devicecom:
  def connect(port):   
   if (ser.is_open):
    return True
   else:
    ser.baudrate = 9600
    ser.port = port
    ser.timeout = 1
    try:
     ser.open()
    except:
     return False  
   return True
  
  def tx(msg):
   try:
    ser.write(msg)  
   except:
    raise Exception("serial port write failed")

  def txrx(msg,len):  
   try:
    ser.write(msg) 
    resp = ser.read(len)
   except: 
    raise Exception("serial port write/read failed")
   return(resp)
  def disconnect():
   ser.close()














