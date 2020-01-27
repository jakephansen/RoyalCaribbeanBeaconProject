import time
from beacontools import BeaconScanner, IBeaconFilter


def callback(bt_addr, rssi, packet, additional_info):
    print('begin')
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    print('bt_addr')
    print(bt_addr)
    print(type(bt_addr))
    print('rssi')
    print(rssi)
    print(type(rssi))
    print('packet')
    print(packet)
    for thing in additional_info:
        print(thing,additional_info[thing],type(thing))
    print('end')


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="636f3f8f-6491-4bee-95f7-d8cc64a863b5")
)
scanner.start()
time.sleep(5)
scanner.stop()






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
