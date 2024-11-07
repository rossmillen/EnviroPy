# EnviroPy
This is the base code for using a Raspberry Pi with Enviro Plus hat for monitoring and logging gas level data. 

### Raspberry Pi Setup
Ensure your Raspberry Pi is running Pi OS Bookworm (Debian 12.0) or later. Ensure your OS is up to date by running the following commands:
```bash
    sudo apt update
    sudo apt upgrade
```

Next, open a new terminal and then type the following:
```bash
    git clone https://github.com/pimoroni/enviroplus-python
    cd enviroplus-python
    ./install.sh
```

Once that is done, reboot your Raspberry Pi.
```bash
    sudo systemctl reboot
```

The EnviroPlus-Python repository contains a selection of example pieces of code to demonstrate the function of each sensor on the EnviroPlus sensor board. 
