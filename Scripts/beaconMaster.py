import time
from datetime import datetime
import pickle
import csv
from beacontools import BeaconScanner, IBeaconFilter


def FigureItOut(minor,currentState,currentBeacon,startTime):
    if minor == currentBeacon:
        pass
    else:
        if currentState == 'Sliding':
            endTime = datetime.now()
            totalTime = endTime - datetime.strptime(startTime,'%m/%d/%y %H:%M:%S')
            print('Slide Time: ', str(totalTime))
            outputString = 'notSliding,' + minor + ',0'
            with open('currentState.csv', 'w+') as f:
                f.write(outputString)
            f.close()
        else:
            startingTime = datetime.now()
            outputString = 'Sliding,' + minor + ',' + str(startingTime)
            with open('currentState.csv', 'w+') as f:
                f.write(outputString)
            f.close()

# This function simulates the wristband being on and always looking for signals
def callback(bt_addr, rssi, packet, additional_info):
    rssiScore = rssi
    major = additional_info['major']
    minor = additional_info['minor']
    currentState = ''
    currentBeacon = ''
    startTime = ''
    with open('currentState.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            currentState = row[0]
            currentBeacon = row[1]
            startTime = row[2]
    f.close()
    FigureItOut(minor,currentState,currentBeacon,startTime)


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="636f3f8f-6491-4bee-95f7-d8cc64a863b5")
)
scanner.start()
time.sleep(5)
scanner.stop()







#
# print('begin')
# print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
# print('bt_addr')
# print(bt_addr)
# print(type(bt_addr))
# print('rssi')
# print(rssi)
# print(type(rssi))
# print('packet')
# print(packet)
# for thing in additional_info:
#     print(thing,additional_info[thing],type(thing))
# print('end')
# begin
# <70:cd:9d:aa:2d:e6, -36> IBeaconAdvertisement<tx_power: -59, uuid: 636f3f8f-6491-4bee-95f7-d8cc64a863b5, major: 0, minor: 5> {'major': 0, 'uuid': u'636f3f8f-6491-4bee-95f7-d8cc64a863b5', 'minor': 5}
# bt_addr
# 70:cd:9d:aa:2d:e6
# <type 'unicode'>
# rssi
# -36
# <type 'int'>
# packet
# IBeaconAdvertisement<tx_power: -59, uuid: 636f3f8f-6491-4bee-95f7-d8cc64a863b5, major: 0, minor: 5>
# ('major', 0, <type 'str'>)
# ('uuid', u'636f3f8f-6491-4bee-95f7-d8cc64a863b5', <type 'str'>)
# ('minor', 5, <type 'str'>)
# end
