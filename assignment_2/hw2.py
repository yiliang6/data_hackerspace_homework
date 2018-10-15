import requests
import re
import matplotlib.pyplot as plt
#import apikey
import numpy as np


def lyrics_word_count_easy(artist, song, phrase):
    artist_lower = artist.lower()
    song_lower = song.lower()
    frequency_of_phrase = []
    get = requests.get("https://api.lyrics.ovh/v1/" + artist_lower + "/" + song_lower)
    if get.status_code != 200:
        return -1
    lyrics = get.json()["lyrics"]
    frequency_of_phrase = re.findall(phrase, lyrics, re.IGNORECASE)
    return len(frequency_of_phrase)
#print(lyrics_word_count_easy("Rick Astley", "Never Gonna Give You Up", "never"))


def lyrics_word_count(artist, phrase):

    pass

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28.,-22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    #graph everything using matplotlib
    plt.subplot(2, 1, 1).set_title("LineGraph")
    plt.plot(x, y)
    plt.subplot(2, 2, 3).set_title("Histogram")
    plt.hist((x, y))
    plt.subplot(2, 2, 4).set_title("Scatter")
    plt.scatter(x, y)
    return plt.show()
#print(visualize())
