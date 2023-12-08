import json
import asyncio
import websockets
import serial
from datetime import datetime
import time

#define your port to connect your computer
ser = serial.Serial(
    # port='COM7',           # Change this to your serial port 
    port='COM5',           # Change this to your serial port 
    baudrate=9600,
    # timeout=1
)
async def mettlerweightsend(websocket):
    global ser
    while True:
        
        #Read data
        data = ser.read_all()
        # Decode bytes to string 
        data_mettler = data.decode('utf-8')
        text_all = data_mettler.split() 
        if len(text_all) > 1: 
            #Select index 1 (weights)
            weight = text_all[1]   #Select index weights
            print(weight)
            time.sleep(1)
        #Sent data in Json
        await websocket.send(json.dumps({
            'data': 'here\'s some data!',
            'count': " ",
            # 'mettlerweightin': weights,
            'mettlerweightin': weight,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }))

        #print(f'> {count}')
        await asyncio.sleep(1)

if __name__ == "__main__":
    
    start_server = websockets.serve(mettlerweightsend, '172.17.22.18', 1901)
    # start_server = websockets.serve(mettlerweightsend, '172.17.22.17', 1900)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

















