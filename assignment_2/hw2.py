import requests
import re
import matplotlib.pyplot as plt
#import apikey
import numpy as np


def lyrics_word_count_easy(artist, song, phrase):
    artist_lower = artist.lower()
    song_lower = song.lower()
    count = []
    get = requests.get("https://api.lyrics.ovh/v1/" + artist_lower + "/" + song_lower)
    if get.status_code != 200:
        return -1
    lyrics = get.json()["lyrics"]
    count = re.findall(phrase, lyrics, re.IGNORECASE)
    return len(count)

print(lyrics_word_count_easy("Rick Astley", "Never Gonna Give You Up", "never"))


def lyrics_word_count(artist, phrase):
    
    pass

def visualize():
    pass
