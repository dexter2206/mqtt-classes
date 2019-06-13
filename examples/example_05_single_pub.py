"""Example 05: using helper functions - simple subscriber part."""
from paho.mqtt import publish
from config import BROKER_HOST, BROKER_PORT


def main():
    """Entrypoint of this script."""
    publish.single('devices/sensor/1', '15', qos=2, hostname=BROKER_HOST, port=BROKER_PORT)


if __name__ == '__main__':
    main()
