class SportsMan(object):
    """This is the parent class, from which other classes inherit """
    pay_raise_index = 1.5

    def __init__(self,  fname, lname, salary):
        self._fname = fname
        self._lname = lname
        self._salary = salary

    def fullname(self):
        return self._fname + ' ' + self._lname

    def pay_raise(self):
        self._salary *= self.pay_raise_index
        return self._salary


class Player(SportsMan):
    """This is a child class which inherits from SportsMan"""
    pay_raise_index = 2.0

    def __init__(self, fname, lname, salary, skillset=None):
        super(Player, self).__init__(fname, lname, salary)
        self._skillset = skillset


class Coach(SportsMan):
    """A second class inheriting from SportsMan"""
    pay_raise_index = 2.4

    def __init__(self, fname, lname, salary, players=None):
        super(Coach, self).__init__(fname, lname, salary)
        if players is None:
            self._players = []
        self._players = players