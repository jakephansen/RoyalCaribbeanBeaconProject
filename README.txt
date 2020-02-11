When I was thinking of a "Data Project" centered around Royal Caribbean, the
possibilities seemed endless. I decided on creating a Beacon-based project,
from looking at the world's tallest waterslide in North America and thinking to
myself, "as a kid I would want to know how fast I went down that slide". From
leaderboards at the bottom of slides that would give kids their times, to the
ability for parents to keep tabs on where their kids are, to enabling network
analysis for data mining purposes, beacons would greatly help Royal Caribbean
to continue advancing the quality of their vacations to their guests.


This project is still under development, but in its current state it simulates
a vacationer going down a slide at CocoCay. To run it, you need a linux device
with pybluez / bluez installed to run the "beaconMaster.py" file in the Scripts
folder. Then, you need two iBeacons within range of the linux device. set the
UUID to '636f3f8f-6491-4bee-95f7-d8cc64a863b5' and choose any two distinct
values for the minor variable. The first one simulates the person starting at
the top of a slide, and the second one will end the timing for it.

setting up iBeacon: - http://www.wadewegner.com/2014/05/create-an-ibeacon-transmitter-with-the-raspberry-pi/
(or you can download an app and do it on your phone)

Still to do:

-Connect to Database
-Create model for determining location of "wristband" based on multiple beacon RSSI values, from data set found in citation from western Michigan
-Create Presentation for how many beacons Royal would need, cost benefit analysis, ROI
-Implement other examples of possible data captures from Royal Caribbean integrating
beacons into their infrastructure.












Dependencies:

pip install psycopg2
pip install configparser
Linux operating system with bluetooth capabilites and Bluez installed
create Database, host it, connect in in database.ini file in Database folder

Citations:
@article{mohammadi2017semi,
author={M. Mohammadi and A. Al-Fuqaha and M. Guizani and J. S. Oh},
journal={IEEE Internet of Things Journal},
title={{Semi-supervised Deep Reinforcement Learning in Support of IoT and Smart City Services}},
year={2017},
pages={1-12},
publisher={IEEE},
doi={10.1109/JIOT.2017.2712560},
ISSN={2327-4662},
}
