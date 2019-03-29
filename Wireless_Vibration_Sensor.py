import serial
import numpy
seru = serial.Serial('COM6', 115200)
#byte array 
while True:
    #read byte array
    s = seru.read(54)
    if(s[0] == 126):
        if(s[15] == 127):
            if(s[22]== 8):
                print('Sensor Number: '+str(s[16]))
                print('Firmware No: '+str(s[17]))
                rms_x = (((s[24]*65536)+(s[25]*256)+s[26])& 0xffff)/100
                rms_y = (((s[27]*65536)+(s[28]*256)+s[29])& 0xffff)/100
                rms_z = (((s[30]*65536)+(s[31]*256)+s[32])& 0xffff)/100
                print('RMS X axis: '+(str(rms_x))+' mg')
                print('RMS Y axis: '+(str(rms_y))+' mg')
                print('RMS z axis: '+(str(rms_z))+' mg')
                max_x = (((s[33]* 65536)+(s[34]*256)+s[35])& 0xffff)/100
                max_y = (((s[36]*65536)+(s[37]*256)+s[38])& 0xffff)/100
                max_z = (((s[39]*65536)+(s[40]*256)+s[41])& 0xffff)/100
                print('Max Value X axis: '+(str(max_x))+' mg')
                print('Max Value Y axis: '+(str(max_y))+' mg')
                print('Max Value Z axis: '+(str(max_z))+' mg')
                min_x = (((s[42]*65536)+(s[43]*256)+s[44])& 0xffff)/100
                min_y = (((s[45]*65536)+(s[46]*256)+s[47])& 0xffff)/100
                min_z = (((s[48]*65536)+(s[49]*256)+s[50])& 0xffff)/100
                print('Min Value X axis: '+(str(min_x))+' mg')
                print('Min Value Y axis: '+(str(min_y))+' mg')
                print('Min Value Z axis: '+(str(min_z))+' mg')
                ctemp = (((s[51]*256)+s[52])& 0xffff)
                battery = ((s[18]*256)+s[19])
                voltage = 0.00322*battery
                print('Temperature in Celcius: '+(str(ctemp)))
                print('ADC Value: '+(str(battery)))
                print('Battrey Voltage: '+(str(voltage)))
            
    
    
        
    
