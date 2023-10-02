import paho.mqtt.client as mqtt
import os

# Suppress Pygame support message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import json

# Define the audio directory
AUDIO_DIRECTORY = ""

# MQTT broker settings
MQTT_BROKER_HOST = "192.168.1.200"
MQTT_BROKER_PORT = 1883

# Define MQTT topics without /occupancy and their associated audio files
TOPIC_AUDIO_MAPPING = {
    "zigbee2mqtt/HouseLeft Motion": "Left.mp3",
    "zigbee2mqtt/HouseRight Motion": "Right.mp3",
    "zigbee2mqtt/HouseFront Motion": "Front.mp3",
}

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Dictionary to store the state of each topic
topic_states = {topic: False for topic in TOPIC_AUDIO_MAPPING.keys()}

# Callback when MQTT message is received
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    
    if topic in TOPIC_AUDIO_MAPPING:
        try:
            payload_json = json.loads(payload)
            if payload_json["occupancy"] is True and not topic_states[topic]:
                play_audio(TOPIC_AUDIO_MAPPING[topic])
                topic_states[topic] = True
            elif payload_json["occupancy"] is not True:
                topic_states[topic] = False
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON payload: {e}")
        except KeyError:
            print("Payload does not contain 'occupancy' field")

# Function to play audio
def play_audio(audio_file):
    try:
        audio_path = os.path.join(AUDIO_DIRECTORY, audio_file)
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.wait()
    except pygame.error as e:
        print(f"Error playing audio: {e}")

# Initialize MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

# Subscribe to the MQTT topics
for topic in TOPIC_AUDIO_MAPPING.keys():
    client.subscribe(topic, qos=0)

# Start the MQTT loop
client.loop_forever()
