import asyncio
import websockets
from queue import Queue
import cv2
from dlclive import DLCLive, Processor
from model import *
import base64
import numpy as np
from io import BytesIO
import json
class count:
    def __init__(self):
        self.frameCount = 0
        
        
countRef = count()


def initLoad():
    
    start_server = websockets.serve(handler, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    
    
async def process_frames(websocket, queue):    
    print("___process_frames___")
    while True:
        
        if not queue.empty():     
            frame = queue.get()            
            processed_frame = SegmentFrames(frame)            
            try:        
                message = json.dumps({"type": "pose","num" : str(countRef.frameCount), "data": processed_frame.tolist()})
                await websocket.send(message)                

                countRef.frameCount += 1
                
            except websockets.exceptions.ConnectionClosed:
                
                print("Client disconnected")
                break
            except Exception as e:
                print(f" process_frames Error: {e}")
                break
            
        else:
            await asyncio.sleep(0.01)
                  

async def receive_frames(websocket, queue):
    
    try:
                
        async for message in websocket:            
            if message == "reset":
                print("Frame Count Reseted...")
                countRef.frameCount = 0
            else:
                binary_data = base64.b64decode(message)  
                np_img = np.frombuffer(binary_data, np.uint8)   
                img = cv2.imdecode(np_img, cv2.IMREAD_UNCHANGED)  
                queue.put(img)     
            
    except websockets.exceptions.ConnectionClosedOK:
        print(f"Connection closed normally.")
        
        
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
        
        
    except Exception as e:
        print(f"receive_frames Error: {e}")
        


async def handler(websocket, path):
    countRef.frameCount = 0
    print("Client connected")
    
    queue = Queue()
     
    
    loop = asyncio.get_event_loop()
    processing_task = loop.create_task(process_frames(websocket, queue))
    
    await receive_frames(websocket, queue)
    await processing_task





if __name__ == '__main__':
    initLoad()



