"""Example 06: loop_forever."""
from paho.mqtt import client as mqtt          # Import module with MQTT client
from config import BROKER_HOST, BROKER_PORT   # Import host and port from our configuration module

def on_message(client, userdata, message):
    """Callback invoked when message is received."""
    print(f'Received message: {message.topic} {message.payload.decode("utf-8")}')

def main():
    client = mqtt.Client('relayr-forever')
    client.on_message = on_message

    client.connect(BROKER_HOST, BROKER_PORT)
    client.subscribe('relayr/forever')
    client.loop_forever()

if __name__ == '__main__':
    main()