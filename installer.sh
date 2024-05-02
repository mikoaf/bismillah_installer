#!/bin/bash
# Buat folder
mkdir /home/pi/belajar_installer

# Clone git
echo "===========Install git==========="
sudo apt install git -y

git clone -b 'coba' https://github.com/mikoaf/bismillah_installer.git /home/pi/belajar_installer
resp=$?

if [ $resp -eq 0 ]
then
    #Install venv & pip
    echo "===========Install venv & pip==========="
    sudo apt update -y
    sudo apt-get install python3-dev -y
    sudo apt-get install python3-venv -y
    sudo apt-get install python3-pip -y
    sleep 0.5

    #Install nodejs dan pm2
    echo "===========Install node & pm2==========="
    sudo apt-get update
    sudo apt install nodejs -y
    sudo apt install npm -y
    sudo npm install -g n -y
    sudo n latest -y
    sleep 0.5
    sudo npm install -g pm2 -y

    #Set up virtual environment
    echo "===========Set up virtual environment==========="
    python3 -m venv /home/pi/belajar_installer/venv
    . /home/pi/belajar_installer/venv/bin/activate
    if [ $? -eq 0 ]; then
        echo "===========virtual environment berhasil diaktifkan==========="
    else
        echo "===========virtual environment gagal diaktifkan==========="
    fi

    #Install adafruit dht
    echo "===========Install adafruit dht=========="
    python -m pip install --timeout 1000 adafruit-circuitpython-dht
    sudo apt-get install libgpiod2
    sudo apt-get install python3-rpi.gpio

    #Install requirements library
    echo "===========Install requirements library==========="
    python -m pip install -r /home/pi/belajar_installer/requirements.txt

    #Setting pm2
    echo "===========Set up pm2==========="
    sudo pm2 start /home/pi/belajar_installer/main.py -f --interpreter=/home/pi/belajar_installer/venv/bin/python
    sudo pm2 start /home/pi/belajar_installer/publisher.py -f --interpreter=/home/pi/belajar_installer/venv/bin/python
    sudo pm2 startup
    sudo pm2 save

    echo "===========Installation successfully==========="
    sleep 1
    # sudo reboot
else
    echo "===========Installation unsuccesfully==========="
    rm -rf /home/pi/belajar_installer
fi