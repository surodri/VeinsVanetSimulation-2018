# VeinsVanetSimulation-2018
## Tech Stack :

* Debian GNU/Linux 9 (stretch) 64-bit
* Omnetpp-5.2.1
* Sumo 0.30
* Instant Veins 4.6
* Catch (Unit Testing Framework)

## Veins Vanet Simulation
Using standards Mac 1609.4 and IEEE 80211p

## Directory content
- vanets/ - Is subclassing from veins framework + some recordings for collisions and channel utilization
- veins/ - Open source vehicular networks framework with some added logging for debugging

Original veins found here. 
https://github.com/sommer/veins.git



## Procedures 👍

## Run simulation
Go inside simulation folder

`$ cd vanets/`

### Run sumo socket
Open terminal window

`$ ./sumo-launchd.py -vv -c sumo-gui`

### Run omnetpp simulation
Go to omnetpp IDE (eclipse)

Select the file [/vanets/src/omnetpp.ini]

- Click green button with arrow at the top to run
- On the pop up window, Select the config file to run. The description is on title
- Click run button on top left corner (NOTE: It is usually faster)
- Stop simulation
- Click on stop button
- Click the button with the flag to conclude simulation
- Clicking the flag will finish the simulation and generate the result files under
/vanets/src/results/

## Test Framework Setup:
#### Install Catch: 



Download catch 
```
$ cd vanets/test/Catch2/
$ git clone https://github.com/catchorg/Catch2.git
$ cd Catch2
$ cmake -Bbuild -H. -DBUILD_TESTING=OFF
$ sudo cmake --build build/ --target install

```

#### Run tests:

```$ cd vanet/test/```

Compile
`$ g++ -std=c++11 -Wall -Icatch2/catch.h -I../src/ChannelService.h -o ChannelServiceTest ChannelServiceTest.cc && ChannelServiceTest --success`

Run
```$ <To add>```

### Install cmake: 
https://cmake.org/install/
 
