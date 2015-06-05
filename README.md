Remote Scan is a simple webapp written in Python3 and Flask, with the help of
which you can access a scanner connected either to your network or directly to
the PC. You must run the app on the PC from which you want to send the scan
command and on which you want to get the scanned images.
The app will be accessible from any device connected to the local network.

Requirments:
- Linux based OS
- Python 3
- Flask
- scanimage (`sudo apt-get install scanimage` on Debian based systems)

Instructions:
- Make sure all the dependencies are satisfied
- Open a terminal and run `scanimage --list` to get a list of the available
  scanners.
<img src="http://i.imgur.com/VUF9zwa.png">
- Copy the name of the desired device(without quotes). In my case:
  *hpaio:/net/Deskjet_3050_J610_series?zc=HP0BF9DD*
- Open *scanconf.conf* and paste your copied device name right next to the
  *device-name* entry
- Edit the output-dir in *scanconf.conf* to match your desired output directory
  for the scanned images
- Optionally: edit the resolution and color of the scan
<img src="http://i.imgur.com/rgVP5qV.png">
- You're done! Make sure your scanner is online and run `python3 main.py`
  A server will be created on the local network at port 5000. To access the
  webapp from any other device you have to know the local IP of your computer
  and enter that IP in the web browser from which you wish to connect, followed
  by the port number: *5000*
    Ex: http://192.164.0.1:5000
