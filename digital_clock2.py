import pifacecad
import subprocess
import os
import lirc
from time import sleep
from datetime import datetime
from pyowm.owm import OWM
from datetime import datetime, timedelta
from pytz import timezone
import pytz

sockid = lirc.init("myprogram", blocking=False)

mykey = 'b6711231325f12c5bf17a17a22d27e92'
owm = OWM(mykey)
manager = owm.weather_manager()


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()

weather_dic = {'Inchenon' : "Incheon, KR", 'London' : "London, GB", 'Paris' : "Paris, FR", 'Japan' : "Japen, JP", 'Canada' : "Canada, CA", 'USA' : "USA, US"}
alaram_time = [99,99,99]
pushed_button_number =[99]


#button4 : check termination

while not cad.swithces[4].value:
    cad.lcd.set_cursor(0,0)
    cad.lcd.write(subprocess.run(['hostname', '-I'], capture_output=True, text=True).stdout)
    now = datetime.now()
    cad.lcd.set_cursor(0,1)
    cad.lcd.write(now.strftime("$m/$d $H:$M:$S " ))
    cad.lcd.set_cursor(12,1)

    #IR sinal receving 
    pushed_button_number = lirc.nextcode()


    #remote quit() 
    if pushed_button_number ==['04']:
        break

    #alarm exec
    if alarm_time[0] != 99 and alarm_time[1] != 99 and alaram_time[2] != 99:
        if now.hour == alarm_time[0] and now.minute == alarm_time[1] and now.second == alarm_time[2]:
            

            #alarm sound out using mplayer
            cad.lcd.clear()
            cad.lcd.write("ALARM")
            os.system("mplayer alarm sound.mp3")
            alarm_time = [99,99,99]

    #button 2 : alarm set
    
    if cad.switches[2].value or pushed_button_number ==['02']:
        scanner = LCDScanf("SET : %2i:%2i:%2i%r")
        alarm_time = scanner.scan()
        #invalid value check
        while arlarm_time[0] > 24 or alarm_time[1] > 60 or alarm_time[2] > 60 : 
            scanner = LCDScanf("Alrm %2i:%2i:%2i%r")
            alarm_time = scanner.scan()
        pushed_button_number = ['99']
        slepp(1)
        cad.lcd.clear()

    #button 3. : display the setting time
    if cad.switches[3].value or pushed_button_number == ['03']:
        cad.lcd.clear()
        cad.lcd.set_cursor(0,0)
        cad.lcd.write(f"Alarm time : ")
        cad.lcd.set_cursor(0,1)
        if alarm_time[0] == 99 and alarm_time[1] == 99 and alarm_time[2] == 99:
            cad.lcd.write("None")
        else :
            cad.lcd.write(f"{alarm_time[0]:02d}:{alarm_time[1]:02d}:{alarm_time[2]:02d}")
        pushed_button_numnber = ['99']
        sleep(2)

    #button 5 : world weather select mode 
    if cad.switches[5].value or pushed_button_number == ['05']:
        cad.lcd.clear()
        scanner = LCDScanf("%m%r", custom_values=('Incheon', 'London', 'Paris', 'Japan', 'Canada', 'USA' ))
        city = scanner.scan()
        observation = manager.weather_at_place(weather_dic[city[0]])
        weather = observation.weather
        cad.lcd.clear()
        while not cad.switches[4].value :
            pushed_button_number = lirc.nextcode()
            if pushed_button_number == ['04']:
                break
            cad.lcd.set_cursor(0,0)
            cad.lcd.write(weather.detailed_status)
        pushed_button_number = ['99']
        sleep(1)



