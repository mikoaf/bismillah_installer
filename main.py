from sensor.dht import Dht
from paho.mqtt import client as mqtt

Sen = Dht()

def on_connect(client, userdata, flags, rc, pr):
    print(f"Connected with result code {rc}")
    client.subscribe("komdat/dht")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # print('haha')
    if msg.payload.decode('utf-8') == 'run':
        p = Sen.getData('run')
        print(p)
    # asyncio.create_task(handle_message(msg))

# async def handle_message(msg):
#     print('haha')
#     if msg.payload.decode("utf-8") == 'run':
#         p = await Sen.getData('run')
#         print(p)
    
def mqtt_loop():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    client.loop_forever()
    # client.loop_start()
    # try:
    #     while True:
    #         await asyncio.sleep(1)
    # except KeyboardInterrupt:
    #     client.disconnect()
    #     client.loop_stop()
    # while True:
    #     await asyncio.sleep(1)

def main():
    mqtt_loop()

if __name__ == "__main__":
    main()

# from sensor.dht import Dht
# import asyncio
# from paho.mqtt import client as mqtt
# import time

# uwu=Dht()
# while True:
#     result = uwu.getData('run')
#     print(result)
#     time.sleep(1)