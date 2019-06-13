"""Example 04: topic hierarchy."""
import time                                   # So we can use sleep
from paho.mqtt import client as mqtt          # Import module with MQTT client
from config import BROKER_HOST, BROKER_PORT   # Import host and port from our configuration module


PUBLISHER_QOS = 2                # Quality of Service used for publishing
SUBSCRIBER_QOS = 2               # Quality of Service with which we will subscribe
CLEAN_SESSION = True             # Should the client start with new session when connecting?

def on_message(client, userdata, message):
    """Callback invoked when message is received."""
    print(f'Received message: {message.topic} {message.payload.decode("utf-8")}')


def main():
    """Entrypoint of this script."""
    # We will use two clients: publisher and subscriber
    publisher = mqtt.Client('relayr-sender')
    subscriber = mqtt.Client('relayr-receiver', clean_session=CLEAN_SESSION)
    subscriber.on_message = on_message

    publisher.connect(BROKER_HOST, BROKER_PORT)
    subscriber.connect(BROKER_HOST, BROKER_PORT)

    publisher.loop_start()
    subscriber.loop_start()

    # We subscribe to some topic and disconnect immediately.
    subscriber.subscribe('sensors/temperature/1', SUBSCRIBER_QOS)
    subscriber.disconnect()
    subscriber.loop_stop()

    # Now wait some time and then publish the message while the subscriber is disconnected.
    time.sleep(2)
    publisher.publish('sensors/temperature/1', '15', qos=PUBLISHER_QOS)

    # Reconnect with the subscriber. Depending on QoS used we will see or not see our message.
    subscriber.connect(BROKER_HOST, BROKER_PORT)
    subscriber.loop_start()

    time.sleep(1)

    # Disconnect both clients
    subscriber.disconnect()
    subscriber.loop_stop()

    publisher.disconnect()
    publisher.loop_stop()


if __name__ == '__main__':
    main()