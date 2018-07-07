# Shutdown Switch Orange Pi Zero

Simple script python3 to shutdown orange pi zero to external button

### Requirements

#### Hardware

* Orange Pi Zero
* Resistor 10K
* Button NO

#### Software

* armbian
* Python 3 and PIP

### Prerequisite

Connect resistor between 3.3V (pin 1) and pin select in script. The button is connected between pin select in script and any GND pin. 

### Installation
* Download and install from Github and install pip3
    ```sh
    $ git clone https://github.com/GuillermoElectrico/power-switch-Ozero
	$ sudo apt-get install python3-pip
	$ sudo pip3 install --upgrade OPi.GPIO
    ```
* Edit script and modify InputPin as unused pin in the board

* To run the python script at system startup. Add to following lines to the end of /etc/rc.local but before exit:
    ```sh
    # Start Power Switch Orange Pi Zero
    python3 /home/--user--/power-switch-Ozero/power-switch-Ozero.py 
    ```
