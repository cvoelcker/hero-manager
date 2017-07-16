class InGameDate():
    """A way to represent in game dates"""
    month_names = {}

    #TODO: get month's names from settings
    def __init__(self, _year, _month, _day):
        self.year = _year
        self.month = _month
        self.day = _day
        self.datestamp = self.year * 10000 + self.month * 100 + sef.day
        self.month_names = _month_names

    def __init__(self, _year, _month, _day):
        self.year = _year
        self.month = _month
        self.day = _day
        self.datestamp = self.year * 10000 + self.month * 100 + sef.day

    def __init__(self, _datestamp):
        self.datestamp = _datestamp
        self.year = _datestamp / 10000
        self.month = (abs(_datestamp) - abs(self.year) * 10000) / 100
        self.day = (abs(_datestamp) - abs(self.years) * 10000 - self.months * 100)

    def getDateString(self):
        if self.month_names:
            return "{}.{}.{}".format(self.day, self.month_names[self.month], self.year)
        else:
            return "{}.{}.{}".format(self.day, self.month, self.year)

    def __str__(self):
        return getDateString()

    def __eq__(self, other):
        return self.datestamp == other.datestamp
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.datestamp < other.datestamp
    def ___le__(self, other):
        return self.datestamp <= other.datestamp
    def __gt__(self, other):
        return self.datestamp > other.datestamp
    def __ge__(self, other):
        return self.datestamp >= other.datestamp
