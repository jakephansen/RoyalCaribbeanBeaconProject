When I was thinking of a "Data Project" centered around Royal Caribbean, the
possibilities seemed endless. I decided on creating a Beacon-based project,
from looking at the world's tallest waterslide in North America and thinking to
myself, "as a kid I would want to know how fast I went down that slide". From
leaderboards at the bottom of slides that would give kids their times, to the
ability for parents to keep tabs on where their kids are, to enabling network
analysis for data mining purposes, beacons would greatly help Royal Caribbean
to continue advancing the quality of their vacations to their guests.



Part 1: Created Raspberry Pi Beacon
- install Raspbian Software
- pull this repo
- run the 'python Beacon_Go'


Part 2: Create Postgres DB on local machine
- run command "python DB_Begin"


Part 3: Connect App to Beacon
- run command "Python Begin Beacon Search"


Part 4: Populate Database
- run command "Python Run DatabasePopulation"


Part 5: Run Analysis
- Using the populated Data, Creates Metrics




Dependencies:

pip install psycopg2
pip install configparser
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
