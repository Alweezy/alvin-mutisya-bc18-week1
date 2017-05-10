from unittest import TestCase
from http_and_web import get_name, search_song


class TestGetName(TestCase):
    """Test the user input to make sure the name meets a certain criteria;
    that it is only a string.
    """
    def test_artist_name_is_not_int(self):
        getname = get_name(20)
        self.assertEqual(getname, 'Enter a valid artist_name: ')

    def test_artist_name_is_not_list(self):
        getname = get_name([])
        self.assertEqual(getname, 'Enter a valid artist_name: ')

    def test_artist_name_is_not_dictionary(self):
        getname = get_name({})
        self.assertEqual(getname, 'Enter a valid artist_name: ')

    def test_artist_name_is_not_set(self):
        getname = get_name(())
        self.assertEqual(getname, 'Enter a valid artist_name: ')

    def test__name_returns_correct_url(self):
        getname = get_name('Rihanna')
        url = ('https://itunes.apple.com/search?term=rihanna&entity=musicVideo', 'Rihanna')
        self.assertTrue(getname, url)

    def test_empty_imput(self):
        getname = get_name('')
        self.assertEqual(getname, 'artist name is a requirement')
