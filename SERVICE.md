To set up the MQTT audio player script as a daemon using systemd on a Linux system, follow these steps:

1. Create a systemd service unit file for your MQTT audio player. Open a terminal and create a new service unit file:

```bash
sudo nano /etc/systemd/system/mqtt_audio_player.service
```

2. Add the following content to the `mqtt_audio_player.service` file. Make sure to adjust the `ExecStart` and other parameters as needed based on your specific script location and system configuration:

```plaintext
[Unit]
Description=MQTT Audio Player Daemon
After=network.target

[Service]
Type=simple
User=your_username
ExecStart=/usr/bin/python3 /path/to/mqtt_audio_player.py
WorkingDirectory=/path/to/script/directory
Restart=always

[Install]
WantedBy=multi-user.target
```

- Replace `your_username` with your actual username.
- Replace `/path/to/mqtt_audio_player.py` with the full path to your Python script.
- Replace `/path/to/script/directory` with the directory where your Python script is located.

3. Save the file and exit the text editor.

4. Reload the systemd manager configuration to pick up the new service:

```bash
sudo systemctl daemon-reload
```

5. Enable the service to start at boot:

```bash
sudo systemctl enable mqtt_audio_player.service
```

6. Start the MQTT audio player service:

```bash
sudo systemctl start mqtt_audio_player.service
```

7. Check the status of the service to ensure it's running without errors:

```bash
sudo systemctl status mqtt_audio_player.service
```

You should see output indicating that the service is active and running. If there are any issues, you can check the service's logs using `journalctl`:

```bash
sudo journalctl -u mqtt_audio_player.service
```

That's it! Your MQTT audio player script should now run as a daemon using systemd and automatically start at boot. You can stop, start, or restart the service using `systemctl` commands as needed.