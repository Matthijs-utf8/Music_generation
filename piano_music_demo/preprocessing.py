import numpy as np
import pandas as pd
from utils import *
# import keras
import matplotlib.pyplot as plt
import os
import pygame
import mido
from tqdm import tqdm

class Data:

    def __init__(self, base_path):

        # Get the class name
        from traceback import extract_stack
        (filename, line_number, function_name, text) = extract_stack()[-2]
        self.name = text[:text.find('=')].strip()

        # Config
        self.base_path = base_path
        self.ticks_per_beat = 480
        self.tempo = int(0.5E6) # [microseconds]
        self.max_sequence_length = int(15E3)

        # get data
        self.get_data()

    def get_data(self):

        # Initialize empty array to store the data in
        self.data = np.zeros(shape=(len(os.listdir(self.base_path)), self.max_sequence_length, 3))

        # Loop through all the midi files
        for n, filename in enumerate(os.listdir(self.base_path)):

            # Read midi file and extract relevant messages (only the "note_on" type messages)
            file = mido.MidiFile(self.base_path + filename, clip=True)
            messages = [msg for msg in file.tracks[1] if msg.type == "note_on"]

            # Loop through all the messages and extract the note, velocity and time from them and store them in the data array
            for i, msg in enumerate(messages[:self.max_sequence_length]):
                self.data[n, i, :] = [msg.note,
                                      msg.velocity,
                                      mido.tick2second(msg.time, tempo=self.tempo, ticks_per_beat=self.ticks_per_beat)]

        # Normalize the data
        self.maxima = np.max(self.data, axis=(0, 1))
        self.data = self.data / self.maxima


# data = Data(base_path="C:\\Users\\matth\\PycharmProjects\\Data_for_all_projects\\Music_generator_project1\\maestro-v3.0.0\\2004\\")
# save_class_as_pickle(data)

