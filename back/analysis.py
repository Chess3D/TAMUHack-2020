import json


max_words = 10
word_times = []


def add_time(time):
    if(len(word_times) >= max_words):
        word_times.pop(0)
    
    word_times.append(time)


def get_wpm():
    print(word_times)
    time_delta = word_times[-1] - word_times[0]
    wpm = len(word_times) / time_delta
    wpm *= 60

    return wpm


def write_wpm():
    wpm = get_wpm()
    
    with open('pipeline/wpm.json', 'w') as file_out:
        json.dump(wpm, file_out)


def okay_word(word):
    with open('pipeline/avoid.json') as file_in:
        avoid = json.load(file_in)

    return word not in avoid