"""Example 03: topic hierarchy."""
import time                                   # So we can use sleep
from paho.mqtt import client as mqtt          # Import module with MQTT client
from config import BROKER_HOST, BROKER_PORT   # Import host and port from our configuration module


def on_message(client, userdata, message):
    """Callback invoked when message is received."""
    print(f'Received message: {message.topic} {message.payload.decode("utf-8")}')


def main():
    """Entrypoint of this script."""
    client = mqtt.Client('relayr')

    client.on_message = on_message

    client.connect(BROKER_HOST, BROKER_PORT)

    client.loop_start()

    # We could use multiple calls to subscribe, but can also pass a list of topic to subscribe.
    # When calling it this way we need also to provide QoS for each topic (i.e. the input should
    # be a list of tuples (string, int).
    client.subscribe([('devices/sensors/#', 0), ('control/+/temperature', 0)])

    client.publish('devices/sensors/humidity/1', '15')
    client.publish('devices/sensors/temperature/2', '30')
    client.publish('control/home/temperature', '40')

    time.sleep(1)

    client.disconnect()

    client.loop_stop()


if __name__ == '__main__':
    main()