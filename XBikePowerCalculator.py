from AbstractPowerCalculator import AbstractPowerCalculator
_DEBUG=True

class XBikePowerCalculator(AbstractPowerCalculator):
    def __init__(self):
        super(XBikePowerCalculator, self).__init__()
        self.wheel_circumference = 5.0 # default value - can be overridden in config.py

    A = -0.00238126
    B = 0.46587375
    C = 0.03980412
    D = 0.00259981
    # A = 0.019168
    # B = 0.0
    # C = 5.244820
    # D = 0.0

    # from https://kurtkinetic.com/technical-information/kinetic-power-tech/
    # This is a 3rd order polynomial, where
    #  Power = A * v ^ 3 + B * v ^ 2 + C * v + d
    # where v is speed in miles/hour and constants A, B, C & D are as defined above.
    def power_from_speed(self, revs_per_sec):
        if self._DEBUG: print "power_from_speed"

        miles_per_rev = self.wheel_circumference / 1609.34
        mph = revs_per_sec * 3600 * miles_per_rev
        power = self.correction_factor * (self.A * mph * mph * mph +
                                          self.B * mph * mph +
                                          self.C * mph +
                                          self.D)
        return power

    def set_wheel_circumference(self, circumference):
        self.wheel_circumference = circumference
