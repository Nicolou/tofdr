# Define som useful classes or structures to group some data and treatments
class FlightFeature:
    date = ''
    time = ''
    location = ''
    pilot = ''
    aircraft = ''
    registration = ''
    AirportFrom = ''
    AirportTo = ''
    
    def __str__(self):
        return "Aircraft: %s (%s)\nPilot: %s\nLocation: %s\nDate: %s Time: UTC %s" % (self.aircraft, self.registration, self.pilot, self.location, self.date, self.time)
