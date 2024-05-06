from typing import Tuple
from model.dht import DhtResult
from model.response import Response, StatusResponse
from sensor.dhtbase import DhtBase
import adafruit_dht
import board
class Dht(DhtBase):
    def __init__(self) -> None:
        super().__init__()
        self.dht11_sensor = adafruit_dht.DHT11(board.D26)
    def getData(self, msg: str) -> Tuple[Response, DhtResult]:
        try:
            suhu = self.dht11_sensor.temperature
            lemb = self.dht11_sensor.humidity
            # return Response(status=StatusResponse.success, message="success"), DhtResult(humidity=lemb, temp=suhu)
            return suhu, lemb
            # return suhu
        except RuntimeError as e:
            return Response(status=StatusResponse.error, message=str(e)), DhtResult(temp=0.0, humidity=0.0)
            # return "gosong"
        except Exception as error:
            self.dht11_sensor.exit()
            raise error
    
    # async def getData(self, msg: str) -> Tuple[Response, DhtResult]:
    #     dht11_pin = adafruit_dht.DHT11(board.D17)
    #     suhu = dht11_pin.temperature
    #     lemb = dht11_pin.humidity
    #     return await (Response(status=StatusResponse.success, message="success"), DhtResult(temp=suhu, humidity=lemb))