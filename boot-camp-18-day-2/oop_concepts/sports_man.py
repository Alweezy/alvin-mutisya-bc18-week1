class SportsMan(object):
    """This is the parent class, from which other classes inherit """
    pay_raise_index = 1.5

    def __init__(self,  fname, lname, salary):
        """Initializes the parent class, SportsMan"""
        self._fname = fname
        self._lname = lname
        self._salary = salary

    def fullname(self):
        """Returns a sports man's full name"""
        return self._fname + ' ' + self._lname

    def pay_raise(self):
        """Calculates a sports man's salary"""
        self._salary *= self.pay_raise_index
        return self._salary


class Player(SportsMan):
    """This is a child class which inherits from SportsMan"""
    # A specific pay_rise_index for class player
    pay_raise_index = 2.0

    def __init__(self, fname, lname, salary, skillset=None):
        """Initializes class Player"""
        # attributes fname, lname, salary are superclass attributes
        super(Player, self).__init__(fname, lname, salary)
        self._skillset = skillset


class Coach(SportsMan):
    """A second class inheriting from SportsMan"""
    # a specific pay_rise_index for class coach
    pay_raise_index = 2.4

    def __init__(self, fname, lname, salary, players=None):
        """Initializes the class Coach"""
        # attributes fname, lname, salary superclass attributes
        super(Coach, self).__init__(fname, lname, salary)
        if players is None:
            # return an empty list if coach has no players
            self._players = []
        self._players = players