from pydantic import BaseModel

class MqttSender(BaseModel):
    message:str