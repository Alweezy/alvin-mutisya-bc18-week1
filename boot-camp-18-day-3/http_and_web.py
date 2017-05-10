def get_name(artist_name):
    """this function takes the name of artist whose music we want to look for in itunes
    :param artist_name:
    :return: complete_url, name
    """
    if isinstance(artist_name, str):
        name = '' + artist_name
        name = ''.join(name.split())
    else:
        return 'Enter a valid artist_name: '
    if name:
        base_url = 'https://itunes.apple.com/search?term={}&entity=musicVideo'
        artist = name.lower()
        complete_url = base_url.format(artist)
        return complete_url, name
    return 'artist name is a requirement'


def search_song(get_url):
    """
    Use url to perform search and return a list of songs
    :param get_url:
    :return: songs
    """
    import requests
    url, name = get_name(get_url)
    if url:
        response = requests.get(url)
        results = response.json()['results']
        print("{:<15} {:<60} {:<5} {:>20} {:>15}".format("ArtistName",
                                                   "TrackName", "Price",
                                                   "Explicitness", "Kind"))
        print("{:<15} {:<60} {:<5} {:>20} {:>15}".format("**********",
                                                   "*********", "*****",
                                                   "************", "****"))
        for song in results:
            artist = song['artistName']
            artist = ''.join(artist.split())
            if artist == name:
                print("{:<15} {:<60} {:<5} {:>20} {:>15}"
                      .format(song['artistName'], song["trackName"],
                              song["collectionPrice"], song["trackExplicitness"],
                              song["kind"]))
        return '        *************************************************'

print(search_song('Kanye West'))