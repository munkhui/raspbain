import paho.mqtt.client as mqtt

def on_connect(mqtt_client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("connected succesfully")
        mqtt_client.subscribe('9fmrvy5679/')
    else:
        print("bad connection. Code :", rc)

def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic :{msg.topic} with payload:{str(msg.payload)}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("9fmrvy5679", "2agmoprtvx")

client.connect(
  host = "b37.mqtt.one",
  port = 1883,
  keepalive = 60,
)
client.loop_forever()
