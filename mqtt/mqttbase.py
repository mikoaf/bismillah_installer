from abc import ABC,abstractmethod
from model_mqtt.mqtt import MqttSender
from model.response import Response
from typing import Tuple
import asyncio

class MqttSend(ABC):
    @abstractmethod
    def MqttMsg(self,msg:str)->Response:
        pass