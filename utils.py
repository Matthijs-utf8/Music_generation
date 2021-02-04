
import pygame
import pickle
import os


def play_music(midi_filename):

  # mixer config
  freq = 44100  # audio CD quality
  bitsize = -16  # unsigned 16 bit
  channels = 2  # 1 is mono, 2 is stereo
  buffer = 1024  # number of samples
  pygame.mixer.init(freq, bitsize, channels, buffer)

  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished



def load_pickle(class_name):
    with open(class_name + '.pkl', 'rb') as f:
        A = pickle.load(f)
        f.close()
    return A

def save_class_as_pickle(Obj):
    if hasattr(Obj, "name"):
        with open(Obj.name + '.pkl', 'wb') as f:
            pickle.dump(Obj, f)
            f.close()
    else:
        name_taken = True
        number = 0
        while name_taken:
            name = "unnamed{}.pkl".format(number)
            if name in os.listdir():
                continue
            else:
                with open(name, 'wb') as f:
                    pickle.dump(Obj, f)
                    f.close()
                name_taken = False