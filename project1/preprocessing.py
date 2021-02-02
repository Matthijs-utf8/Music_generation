import numpy as np
import pandas as pd
# import keras
import matplotlib.pyplot as plt
import librosa
import os
import json
import pygame
from mido import MidiFile
import mido

base_path = "C:\\Users\\matth\\PycharmProjects\\Data_for_all_projects\\Music_generator_project1\\maestro-v3.0.0\\2004\\"
test_file = "MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.midi"

# mixer config
freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

def play_music(midi_filename):
  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished


play_music(base_path+test_file)

