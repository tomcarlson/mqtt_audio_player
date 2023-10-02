# MQTT Audio Player

This project is an MQTT-based audio player daemon that listens for MQTT messages and plays different audio files when specific conditions are met. It can be used to integrate audio notifications into your home automation or IoT projects.

## Features

- Listens to multiple MQTT topics.
- Plays different audio files for each MQTT topic when a specific condition is met.
- Supports JSON payload for MQTT messages.

## Prerequisites

Before running the MQTT Audio Player, you need to have the following prerequisites installed:

- Python 3.x
- Paho-MQTT library
- Pygame library

You can install the required Python libraries using pip:

```bash
pip install paho-mqtt pygame
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/tomcarlson/mqtt-audio-player.git
cd mqtt-audio-player
```

2. Configure the MQTT broker settings and audio directory by modifying the script as needed. You can set the following variables in the script:

   - `MQTT_BROKER_HOST`: The IP address or hostname of your MQTT broker.
   - `MQTT_BROKER_PORT`: The port of your MQTT broker.
   - `AUDIO_DIRECTORY`: The directory where your audio files are located.
   - `TOPIC_AUDIO_MAPPING`: A dictionary mapping MQTT topics to their associated audio files.

3. Run the MQTT Audio Player script:

```bash
python mqtt_audio_player.py
```

The script will connect to the MQTT broker, listen for messages on the specified topics, and play the corresponding audio files when conditions are met.

## Example Configuration

Here's an example configuration in the script:

```python
# MQTT broker settings
MQTT_BROKER_HOST = "192.168.1.200"
MQTT_BROKER_PORT = 1883

# Define the audio directory
AUDIO_DIRECTORY = ""

# Define MQTT topics without /occupancy and their associated audio files
TOPIC_AUDIO_MAPPING = {
    "zigbee2mqtt/HouseLeft Motion": "Left.mp3",
    "zigbee2mqtt/HouseRight Motion": "Right.mp3",
    "zigbee2mqtt/HouseFront Motion": "Front.mp3",
}
```

In this example, three MQTT topics are defined, and the associated audio files are specified.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is based on the [Paho-MQTT](https://github.com/eclipse/paho.mqtt.python) and [Pygame](https://www.pygame.org/) libraries.

