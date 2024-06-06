from random import choice
def random_generics():
    generics = {
        'Why We Lose ': 'https://www.youtube.com/watch?v=zyXmsVwZqX4&list',
        'C U Again ft. Mikk Mäe': 'https://www.youtube.com/watch?v=NJNp6DnAAIo&list',
        'Say It ': 'https://www.youtube.com/watch?v=80AlC3LaPqQ&list',
        "I'd Love to Change the World ": 'https://www.youtube.com/watch?v=5hEh9LiSzow&list',
        'Alone': 'https://www.youtube.com/watch?v=1-xGerv5FOk&list',
        'Let Me Love You ': 'https://www.youtube.com/watch?v=SMs0GnYze34&list',
        'Here At Last': 'https://www.youtube.com/watch?v=lIsfer_52L4&list',
        'Something Just Like This': 'https://www.youtube.com/watch?v=FM7MFYoylVs&list',
        'Pretty Little Gangster': 'https://www.youtube.com/watch?v=ujgQOosyIYk&list',
        'Prayer In C': 'https://www.youtube.com/watch?v=fiore9Z5iUg&list',
    }
    random_music = choice(list(generics.keys()))
    random_url = generics[random_music]
    return random_url
