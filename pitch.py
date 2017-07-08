#!/usr/bin/env python

import os
import signal
import time
from sys import exit
from random import randint

try:
    import pygame
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

import pianohat

SOUNDS = os.path.join(os.path.dirname(__file__), "piano-notes")
ROWSOUND = os.path.join(os.path.dirname(__file__), "right-or-wrong")

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

files = [
    '39187__jobro__piano-ff-040.wav',
    '39188__jobro__piano-ff-041.wav',
    '39189__jobro__piano-ff-042.wav',
    '39190__jobro__piano-ff-043.wav',
    '39191__jobro__piano-ff-044.wav',
    '39193__jobro__piano-ff-045.wav',
    '39194__jobro__piano-ff-046.wav',
    '39195__jobro__piano-ff-047.wav',
    '39196__jobro__piano-ff-048.wav',
    '39197__jobro__piano-ff-049.wav',
    '39198__jobro__piano-ff-050.wav',
    '39199__jobro__piano-ff-051.wav',
    '39200__jobro__piano-ff-052.wav'
    
]

samples = [pygame.mixer.Sound(os.path.join(SOUNDS, sample)) for sample in files]

filerow = [
    'correct.wav',
    'wrong.wav'
]
row = [pygame.mixer.Sound(os.path.join(ROWSOUND, sample)) for sample in filerow]

pianohat.auto_leds(True)

rand = randint(0, 12)
samples[rand].play(loops=0)

def test_note():
    global rand
    time.sleep(3)
    rand = randint(0, 12)
    samples[rand].play(loops=0)

def handle_note(channel, pressed):
    global rand
    if channel < len(samples) and pressed:
        print('Playing Sound: {}'.format(files[channel]))
        print('channel is:', channel)
        samples[channel].play(loops=0)
        time.sleep(1)
        
        if channel == rand:
            row[0].play(loops=0)
        else:
            row[1].play(loops=0)

        test_note()

def handle_instrument(channel, pressed):
    pass


def handle_octave_up(channel, pressed):
    pass


def handle_octave_down(channel, pressed):
    pass

pianohat.on_note(handle_note)
pianohat.on_octave_up(handle_octave_up)
pianohat.on_octave_down(handle_octave_down)
pianohat.on_instrument(handle_instrument)

signal.pause()
