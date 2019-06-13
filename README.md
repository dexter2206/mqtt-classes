# Configuration
All examples use hostname and broker stored in `config.py` file. Edit it to match the broker you want to use.

# Suggested exercises

1. Write command line utilities `mqtt_sub` and `mqtt_pub` similar to `mosquitto_sub` and `mosquitto_pub` 
  (usage of mosquitto will be demonstrated during classes). Both utilities should accept broker hostname and port
  supplied by `-h` and `-p` parameters respectively. They should also support `-q` parameter for specifying Quality of Service.
   - `mqtt_sub` should allow subscription to arbitrary topic specified by its only positional parameter. All received messages
     should be printed to stdout. In addition it should support `-v` (for verbose) option, if specified topics of received
     messages should also be printed. You could also add `-d` switch that will allow printing timestamp (or date+time) at which
     message has been received.
   - `mqtt_pub` should allow publishing arbitrary payload to arbitrary topic specified by its second and first positional
     arguments respectively.
     
   If you are not familiar with writing command line interfaces, implement reading parameters from users using
   built-in `input` function.
   
   Here are example correct invocations of the utilities that should further clarify the idea.
   
   Subscribe to `devices/accelerometer` topic with `qos=2` to the broker listening on localhost at port 1883.
   ```
   mqtt_sub -h localhost -p 1883 -q 2 devices/accelerometer
   ```
  
   Publish message `open` to `home/door` topic to the broker located at 192.168.0.1 listening at port 2137.
   
   ```
   mqtt_pub -h 192.168.0.1 -p 2137 -q 1 home/door open
   ```
2. Write a simple messaging app. The idea is as follows:
   - The messages are published to `message/<username_from>/<username_to>`.
   - When launching an application user should supply his or her username (possibly by command switch) as well as the second
     user's username.
   - Suppose that user chooses `Alice` as her user name and the second user's name is `Bob`. The application should subscribe
     to `message/Bob/Alice` and display all of the incoming messages. At the same time it should be possible to publish messages
     to `message/Alica/Bob` so the other party could receive them.
   
