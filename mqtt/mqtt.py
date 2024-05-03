from typing import Tuple
from model_mqtt.mqtt import MqttSender
from model.response import Response, StatusResponse
from mqtt.mqttbase import MqttSend
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

class mqqts(MqttSend):
    async def MqttMsg(self, msg: str) -> Response:
        try:
            broker_address = os.getenv("BROKER")
            broker_port = int(os.getenv("PORT"))
            topic = os.getenv("TOPIC")
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            client.connect(broker_address, broker_port)
            message = msg
            client.publish(topic, message)
            client.disconnect()
            return Response(status=StatusResponse.success, message="Message Published.")
        except Exception as err:
            return Response(status=StatusResponse.error, message=str(err))
