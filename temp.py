import pyaudio
import wave
import speech_recognition as sr
from os import path
import re


r = sr.Recognizer()
m = sr.Microphone()

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

###################

try:
    #set threhold level
    with m as source: r.adjust_for_ambient_noise(source)
    # print("dynamic energy ratio {}",r.dynamic_energy_ratio)
    # print("dynamic energy adjacement dampning {}",r.dynamic_energy_adjustment_damping)
    # print("energy threshold{}",r.energy_threshold)
    # print("non speaking duration ", r.non_speaking_duration)
    # print ("pause duration ",r.pause_threshold)
    # print("Set minimum energy threshold to {}".format(r.energy_threshold))

    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

except:
    pass
####################


def analysis():
    x = r.recognize_google(audio)
    print x
    ai = x
    parts = re.split('\s|(?<!\d)[,.](?!\d)', ai)

    l = len(parts)
    #print(l)
    array = [
        ["angry", 'aggressive', 'aggressive', 'annoyed', 'bitter', 'boiling', 'cross', 'enraged', 'fuming', 'hateful'
            , 'hostile', 'incensed','indignant', 'inflamed', 'infuriated','insulting','irritated', 'offensive',
         'provoked'
            , 'resentful', 'sore', 'unpleasant', 'upset', 'worked', 'up',
         'annoyed', 'apathetic', 'bored', 'certain', 'cold', 'crabby', 'cranky', 'critical', 'cross',
         'detached', 'displeased',
         'frustrated', 'impatient', 'indifferent', 'irritated', 'peeved', 'rankled',

         'affronted', 'aggravated', 'angry', 'antagonized', 'arrogant', 'bristling', 'exasperated',
         'incensed', 'indignant', 'inflamed', 'mad', 'offended', 'resentful', 'sarcastic',

         'aggressive', ' sppalled', 'belligerent', 'bitter', 'contemptuous', 'disgusted', 'furious',
         'hateful', 'hostile', 'irate', 'livid', 'menacing', 'outraged', 'ranting', 'raving',
         'seething', 'spiteful', 'vengeful', 'vicious', 'vindictive', 'violent','hate'
         ]

        , ["sad", 'aggressive', 'annoyed', 'bitter', 'boiling', 'cross', 'enraged', 'fuming', 'hateful', 'hostile',
           'incensed'
            , 'indignant', 'inflamed', 'infuriated', 'insulting', 'anguish', 'desolate', 'desperate', 'dismayed',
           'grief', 'grieved'
            , 'lonely', 'mournful', 'pained', 'pessimistic', 'sorrowful', 'tearful', 'unhappy',
           'contemplative', 'disappointed', 'disconnected', 'distracted', 'grounded', 'listless', 'low',
           'regretful', 'steady', 'wistful',

           'dejected', 'discouraged', 'dispirited', 'down', 'downtrodden', 'drained', 'forlorn',
           'gloomy', 'grieving', 'heavy-hearted',
           'melancholy', 'mournful', 'sad', 'sorrowful', 'weepy',

           'anguished', 'bereaved', 'bleak', 'depressed', 'despairing', 'despondent', 'grief-stricken',
           'Heartbroken', 'Hopeless',
           'inconsolable', 'morose']

        , ["happy", 'playful', 'gay', 'joyous', 'lucky', 'fortunate', 'delighted', 'overjoyed', 'gleeful', 'thankful',
           'important'
            , 'festive', 'ecstatic', 'satisfied', 'glad', 'cheerful', 'sunny', 'merry', 'elated', 'jubilant', 'amused',
           'calm', 'encouraged', 'friendly', 'hopeful', 'inspired', 'jovial', 'open', 'peaceful',
           'smiling',

           'cheerful', 'contented', 'delighted', 'excited', 'fulfilled', 'glad', 'gleeful', 'gratified',
           'happy', 'healthy', 'joyful',
           'lively', 'merry', 'optimistic', 'playful', 'pleased', 'proud', 'rejuvenated', 'satisfied',

           'awe-filled', 'blissful', 'ecstatic', 'egocentric', 'elated', 'enthralled', 'euphoric',
           'exhilarated', 'giddy', 'jubilant', 'manic', 'overconfident', 'overjoyed', 'radiant',
           'rapturous', 'self-aggrandized', 'thrilled','love']

        ,
        ["afraid", 'alarmed', 'anxious', 'cowardly', 'doubtful', 'fearful', 'frightened', 'menaced', 'nervous', 'panic'
            , 'quaking', 'restless', 'scared', 'shaky', 'suspicious', 'terrified', 'threatened', 'timid', 'wary',
         'worried', 'alert', 'apprehensive', 'cautious', 'concerned', 'confused', 'curious',
         'disconcerted', 'disoriented',
         'disquieted', 'doubtful', 'edgy', 'fidgety', 'hesitant', 'indecisive', 'insecure',
         'instinctive', 'intuitive', 'leery', 'pensive', 'shy', 'timid',
         'uneasy', 'watchful',

         'afraid', 'alarmed', 'anxious', 'aversive', 'distrustful', 'fearful', 'jumpy', 'nervous',
         'perturbed', 'rattled', 'shaky',
         'startled', 'suspicious', 'unnerved', 'unsettled', 'wary', 'worried',

         'dread', 'horrified', 'panicked', 'paralyzed', 'petrified', 'phobic', 'shocked', 'terrorized']
    ]


    i = 0
    freq = [[None] * 2] * 4

    freq[0][1] = 0
    freq[1][1] = 0
    freq[2][1] = 0
    freq[3][1] = 0

    freq1 = [0, 0, 0, 0]

    #print(freq)
    rows = len(array)
    for row in xrange(rows):
        cols = len(array[row])
        for col in xrange(cols):
            array[row][col].lower()

    while (i < l):
        input = parts[i]
        for row in xrange(rows):
            cols = len(array[row])
            for col in xrange(cols):
                array[row][col].lower()
                if input == array[row][col]:
                    # print(array[row][0])
                    temp = array[row][0]
                    #temp=temp.tolower()
                    #print(temp)
                    if temp == 'angry':
                        freq1[0] = freq1[0] + 1
                    elif temp == "sad":
                        freq1[1] = freq1[1] + 1
                    elif temp == "happy":
                        freq1[2] = freq1[2] + 1
                    elif temp == "afraid":
                        freq1[3] = freq1[3] + 1;
        #print(freq1)
        i = i + 1
    #print(freq1)

    f = 0
    i = 0
    if freq1[0] > f:
        f = freq1[0]

    if freq1[1] > f:
        f = freq1[1]

    if freq1[2] > f:
        f = freq1[2]

    if freq1[3] > f:
        f = freq1[3]

    print("You are:")
    if (f > 0):
        if f == freq1[0]:
            print("angry" + " ")
        if f == freq1[1]:
            print("sad" + " ")
        if f == freq1[2]:
            print("happy" + " ")
        if f == freq1[3]:
            print("afraid" + " ")
    else:
        print("sorry couldnt predict your mood!")


analysis()
