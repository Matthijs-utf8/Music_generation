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

        self.data = np.zeros(shape=(len(os.listdir(self.base_path)), self.max_sequence_length, 3))

        for n, filename in enumerate(os.listdir(self.base_path)):

            file = mido.MidiFile(self.base_path + filename, clip=True)
            messages = [msg for msg in file.tracks[1] if msg.type == "note_on"]

            for i, msg in enumerate(messages[:self.max_sequence_length]):
                if msg.type == "note_on" or msg.type == "note_off":
                    self.data[n, i, :] = [msg.note,
                                          msg.velocity,
                                          mido.tick2second(msg.time, tempo=self.tempo, ticks_per_beat=self.ticks_per_beat)]
                else:
                    continue

        self.maxima = np.max(self.data, axis=(0, 1))
        self.data = self.data / self.maxima


# data = Data(base_path="C:\\Users\\matth\\PycharmProjects\\Data_for_all_projects\\Music_generator_project1\\maestro-v3.0.0\\2004\\")
# save_class_as_pickle(data)

