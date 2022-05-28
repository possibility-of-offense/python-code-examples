import random
import math

songs = [
    'Song 1',
    'Song 2',
    'Song 3',
    'Song 4'
]

current_song = 'Song 1'

def play_random_song() :
    random_song = math.floor(random.random() * len(songs))
    current_song = songs[random_song]
    return 'You\'re currently listening to the {song}!'.format(song = current_song)

playing_song = play_random_song()
print(playing_song)

def play_song(current_song, directional = 'next') :
    filtered_songs = songs.copy()
    filtered_songs.remove(current_song)
    song = ''

    match directional :
        case 'next':
            random_song = math.floor(random.random() * len(filtered_songs))
            song = songs[random_song]
            return f'The next song is {song}!'
        case 'prev':
            random_song = math.floor(random.random() * len(filtered_songs))
            song = songs[random_song]
            return f'The previous song is {song}!'
        case _ :
            return 'Not valid value'

played_song = play_song(current_song)
print(played_song)