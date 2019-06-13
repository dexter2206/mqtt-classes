"""Example 01: basic usage of MQTT client

Note: this does not follow the best practices and serves only as a basic
examples of paho.mqtt usage.
"""
import time                                   # So we can use sleep
from paho.mqtt import client as mqtt          # Import module with MQTT client
from config import BROKER_HOST, BROKER_PORT   # Import host and port from our configuration module


def on_message(client, userdata, message):
    """Callback invoked for every received message.

    Note: we should make sure this function does NOT raise any exception.
    It will be run in a separate thread of execution and the exception will
    go unnoticed.

    The parameters are:
       - client: the client that received message
       - userdata: additional parameter passed with client construction (see next examples)
       - message: the message object itself.
    The message object has topic, qos and payload properties. Note that payload is stored
    as bytes, which is why below we decode them to string.
    """
    print(f'{message.topic} {message.payload.decode("utf-8")}') # Print message topic and payload


def main():
    """"Entry point of this script."""
    client = mqtt.Client('kj-relayr')         # Create client. The parameter is our client-id

    # Callback is attached by assigning it to on_message attribute of client.
    # From now on our on_message function will
    client.on_message = on_message

    # Connect to the broker - we pass host and port (port is optional).
    client.connect(BROKER_HOST, BROKER_PORT)

    # Start the network loop. Without that the client won't be able to receive messages.
    # Internally it starts separate thread of execution in which all the incoming messages
    # are processed.
    client.loop_start()

    # Subscribe to relayr/test topic
    result, mid = client.subscribe('relayr/test')

    # Methods that publish/subscribe return result (status code) indicating if operation succeeded (result=0) or not
    # as well as message id. This message id can be used for tracking purposes.
    print(f'Result: {result}, message_id: {mid}')

    # Publish message to the same topic
    client.publish('relayr/test', 'test message')

    # It takes nonzero time before broker receives message and propagates it to subscribed clients.
    # Therefore we artificially stop execution for a second for it to happen. During this time,
    # our client should receive the message and we should see it printed to stdout.
    time.sleep(1)

    # Disconnect from the broker.
    client.disconnect()

    # Stop the event loop. This will shut the background thread down.
    client.loop_stop()


if __name__ == '__main__':
    main()
