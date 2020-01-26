import pymongo
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
    wpm = {'wpm': get_wpm()}
    
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    database = client['tamuhack']
    collection = database['speed']

    collection.insert_one(wpm)


# def check_word(word):
#     client = pymongo.MongoClient('mongodb://localhost:27017/')
#     database = client['tamuhack']
#     collection = database['avoid']

#     with open('pipeline/avoid.json') as file_in:
#         avoid = json.load(file_in)

#     if word in avoid:
#         collection.insert_one({'avoid': word})


def update_speech():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    database = client['tamuhack']
    collection = database['speech']

    temp = list(collection.find().sort('_id', -1).limit(max_words))
    
    words = []
    times = []

    for dic in temp:
        words.append(dic['word'])
        times.append(dic['time'])

    # for word in words:
    #     check_word(word)
    
    for time in times:
        add_time(time)