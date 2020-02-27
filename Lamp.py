import paho.mqtt.client as mqtt
def on_message (client, userdata, msg):
    print(str(msg.payload))
def on_connect (client, userdata, flags, rc):
    client.subscribe("immortal_flower")

class Lamp:    
    def __init__(self, broker_address, topic):
        self.ligth = False
        self.topic = topic
        self.system_of_control = mqtt.Client("Lamp") 
        self.system_of_control.on_message=on_message 
        self.system_of_control.on_connect = on_connect
        self.system_of_control.username_pw_set("njelhmbg","FrWodAgwXZSu")
        self.system_of_control.connect(broker_address, 16008,60)
    def on(self):
        self.ligth = True
        self.system_of_control.publish(self.topic,"Lamp is ON")
        #print("Сообщение отправлено")
    def off(self):
        self.ligth = False
        self.system_of_control.publish(self.topic,"Lamp is OFF")
        #print("Сообщение отправлено")
    def check(self):
        if(self.ligth):
            return "ON"
        else:
            return "OFF"
