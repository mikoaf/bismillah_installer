# DHT MQTT

## Device

- Raspberry Pi 4 Model B
- DHT11

## Communication

- MQTT

## Config Files

.env

#### BROKER="mqtt.eclipseprojects.io"

#### PORT=1883

#### TOPIC="komdat/dht"

## How it works?

```mermaid

sequenceDiagram
participant pub as Publisher
participant br as Broker
participant sub as Subscriber

    sub->>br:Connect<br/>broker address: mqtt.eclipseprojects.io, port: 1883
    br->>sub:Connack<br/>
    pub->>br:Connect<br/>broker address: mqtt.eclipseprojects.io, portL 1883
    br->>pub:Connack<br/>

    sub->>br:Subscribe<br/>topic: komdat/dht
    pub->>br:Publish<br/>topic: komdat/dht

    alt if Publish<br/>true
        pub->>pub:Response mqtt
    end
    br->>sub:Message<br/>topic: komdat/dht

    alt if message<br/>run
        sub->>sub:Response dht
    end
```

## Format Response mqtt

Response(status=StatusResponse.response, message=str)

## Format Response dht

Response(status=StatusResponse.response, message=str), DhtResult(humidity=lemb, temp=suhu)

## Example Format Response

#### MQTT

- Response(status=StatusResponse.success, message="Message Published.")

#### DHT

- (Response(status=<StatusResponse.success: 0>, message='success'), DhtResult(humidity=56.0, temp=26.0))

## Contributors

- @mikoaf (mikoalfandi2801@gmail.com)
