#!/bin/bash
echo "Install git"
sudo apt install git -y

git clone "link github" "direktori tujuan"
resp=$?

if [$resp -eq 0]
then
    #Install venv & pip
    echo "Install venv & pip"
    sudo apt update -y
    # sudo apt install python3-dev -y
    sudo apt install python3-venv -y
    sudo apt install python3-pip -y
    sleep 0.5

    #Install nodejs dan pm2
    echo "Install node & pm2"
    sudo apt install nodejs -y
    sudo apt install npm -y
    npm install -g n -y
    n latest -y
    sleep 0.5
    npm install -g pm2 -y

    #Install requirements library
    echo "Install requirements library"
    pip install -r "direktori di raspi"

    #Setting pm2
    sudo pm2 start "direktori file json di raspi" #atau mau di run dua2nya manual
    sudo pm2 startup
    sudo pm2 save

    echo "Installation successfully"