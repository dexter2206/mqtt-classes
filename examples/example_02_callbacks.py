"""Example 02: using callbacks."""
import logging
import time                                   # So we can use sleep
from paho.mqtt import client as mqtt          # Import module with MQTT client
from config import BROKER_HOST, BROKER_PORT   # Import host and port from our configuration module


def on_message(client, userdata, message):
    """Callback invoked for every message (see Example 01 for details."""
    logging.getLogger(client._client_id.decode('utf-8')).info(
        'Message received: %s %s',
        message.topic,
        message.payload.decode('utf-8')
    )


def on_connect(client, userdata, flags, rc):
    """Callback invoked when client connects to broker.

    Parameters:
        - client: client used for connection.
        - userdata: additional data passed to the client.
        - flags: flags returned from broker (more on that later.
        - rc: integer code indicating result. The value of 0 means successful connection.
          See e.g. https://www.eclipse.org/paho/clients/python/docs/ for explanation of other
          values of rc.
    """
    logger = logging.getLogger(client._client_id.decode('utf-8'))
    if rc == 0:
        logger.info('Client connected succesfuly.')
        client.subscribe('relayr/example-02')
    else:
        logger.error('Failed connecting to the broker. Error code: %d', rc)


def on_subscribe(client, userdata, mid, granted_qos):
    """Callback invoked when the broker responds to subscription request.

    Parameters:
        - client and userdata as usual
        - mid: message id matching the one returned by call to subscribe.
        - granted_qos: list of granted QoS' for every topic we wanted to subscribe.
    """
    logging.getLogger(client._client_id.decode('utf-8')).info(
        'Successfuly subscribed. Message ID: %s, granted_qos: %d',
        mid,
        granted_qos[0]  # We only subscribe to one topic so there's no need to print a list.
    )


def on_unsubscribe(client, userdata, mid):
    """"Callback invoked when the broker responds to unsubscribe request.

    Parameters analogous to those in on_subscribe.
    """
    logging.getLogger(client._client_id.decode('utf-8')).info('Client unsubscribed.')


def on_publish(client, userdata, mid):
    """Callback invoked when the message is published.

    Note: the meaning of "published" depends on QoS. For QoS 0 it just means that the message left the client.
    For QoS 1 and 2 it means that appropriate handshakes have been completed.
    """
    logging.getLogger(client._client_id.decode('utf-8')).info(
        'Message of id %d published successfully.',
        mid
    )


def main():
    """"Entry point of this script."""
    logging.basicConfig(level='INFO')

    client = mqtt.Client('kj-relayr')

    # Attach all the callbacks
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect
    client.on_unsubscribe = on_unsubscribe
    client.on_publish = on_publish

    client.connect(BROKER_HOST, BROKER_PORT)

    client.loop_start()

    time.sleep(1)

    client.publish('relayr/example-02', 'test message')

    time.sleep(1)

    client.unsubscribe('relayr/test')

    time.sleep(1)

    client.disconnect()

    client.loop_stop()


if __name__ == '__main__':
    main()
