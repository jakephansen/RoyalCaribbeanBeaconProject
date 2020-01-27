#Authored by Jake Hansen, Jan 2020 in preparation of intervew with Royal Caribbean

class Wristband:
    def __init__(self, ID, Age, Latitude, Longitude, nearestBeacon):
        self.ID = ID
        self.Age = Age
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.nearestBeacon = nearestBeacon

class Vacationer:
    def __init__(self, ID, Name, Age, Height, Family, Role):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.Family = Family
        self.Role = Role

class Beacon:
    def __init__(self, ID, Latitude, Longitude, Height, Boat, Island, Section, Number, Name):
        self.ID = ID
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Height = Height
        self.Boat = Boat
        self.Island = Island
        self.Section = Section
        self.Number = Number
        self.Name = Name

class Movement:
    def __init__(self,PreviousBeacon,CurrentBeacon,Wristband,Time):
        self.PreviousBeacon = PreviousBeacon
        self.CurrentBeacon = CurrentBeacon
        self.Wristband = Wristband
        self.Time = Time






print("Hello")
