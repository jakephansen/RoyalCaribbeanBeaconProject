import csv
import pickle

class LabeledRow:
    def __init__(self,location,date,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13):
        self.location = location
        self.date = date
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13

class UnlabeledRow:
    def __init__(self,location,date,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13):
        self.location = location
        self.date = date
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13


inputFileLabeled = '../input/iBeacon_RSSI_Labeled.csv'
inputFileUnlabeled = '../input/iBeacon_RSSI_Unlabeled.csv'
labeledRows = []
counter1 = 0
with open (inputFileLabeled, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        counter1 += 1
        location = row[0]
        date = row[1]
        b1 = row[2]
        b2 = row[3]
        b3 = row[4]
        b4 = row[5]
        b5 = row[6]
        b6 = row[7]
        b7 = row[8]
        b8 = row[9]
        b9 = row[10]
        b10 = row[11]
        b11 = row[12]
        b12 = row[13]
        b13 = row[14]
        newRow = LabeledRow(location,date,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13)
        labeledRows.append(newRow)
f.close()

unlabeledRows = []
counter2 = 0
with open (inputFileUnlabeled, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        counter2 += 1
        location = row[0]
        date = row[1]
        b1 = row[2]
        b2 = row[3]
        b3 = row[4]
        b4 = row[5]
        b5 = row[6]
        b6 = row[7]
        b7 = row[8]
        b8 = row[9]
        b9 = row[10]
        b10 = row[11]
        b11 = row[12]
        b12 = row[13]
        b13 = row[14]
        newRow = UnlabeledRow(location,date,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13)
        labeledRows.append(newRow)
f.close()
print("LabeledRows: ", counter1)



print("UnlabeledRows: ", counter2)
