from unittest import TestCase
from sports_man import SportsMan, Player, Coach


class TestCasesSportsMan(TestCase):
    """Tests the functionality of the base class SportsMan"""

    def test_sportsman_full_name(self):
        """Tests for the output of the fullname method"""
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertTrue(self.sportsman.fullname(), 'Allan Smith')

    def test_pay_raise_is_right(self):
        """Tests for the output of the pay_raise method"""
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertEqual(self.sportsman.pay_raise(), 90000)


class TestCasesPlayer(TestCase):
    """Tests for class Player"""
    def test_player_inherits_from_SportsMan(self):
        """Tests if Player inherits from SportsMan"""
        self.assertTrue(issubclass(Player, SportsMan))

    def test_player_full_name(self):
        """Tests for the output of the fullname method"""
        self.player = Player('Wayne', 'Rooney', 10000, 'Dribble')
        self.assertTrue(self.player.fullname(), 'Wayne Rooney')

    def test_pay_raise_is_right(self):
        """Tests for the output of the pay_rise method"""
        self.player = Player('Wayne', 'Rooney', 100000, '[Dribble, Finesse]')
        self.assertEqual(self.player.pay_raise(), 200000)


class TestCasesCoach(TestCase):
    """Tests for class Coach"""
    def test_player_inherits_from_SportsMan(self):
        self.assertTrue(issubclass(Coach, SportsMan))

    def test_player_full_name(self):
        """Tests for the output of the fullname method"""
        self.coach = Coach('Jose', 'Murhinho', 10000, ['Wayne Rooney', 'Marcus Rashford'])
        self.assertTrue(self.coach.fullname(), 'Jose Murhinho')

    def test_pay_raise_is_right(self):
        """Tests for the output of the pay_raise method"""
        self.coach = Coach('Wayne', 'Rooney', 100000, ['Wayne Rooney', 'Marcus Rashford'])
        self.assertEqual(self.coach.pay_raise(), 240000)

    def test__can_have_no_players(self):
        """Tests for output in case coach has no players"""
        self.coach = Coach('Wayne', 'Rooney', 100000)
        self.assertEqual(self.coach._players, None)