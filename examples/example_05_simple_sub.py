"""Example 05: using helper functions - simple subscriber part."""
from paho.mqtt import subscribe
from config import BROKER_HOST, BROKER_PORT


def main():
    """Entrypoint of this script."""
    message = subscribe.simple('devices/sensor/1', hostname=BROKER_HOST, port=BROKER_PORT, qos=2)
    print(f'Message topic: {message.topic}')
    print(f'Message payload: {message.payload.decode("utf-8")}')


if __name__ == '__main__':
    main()
