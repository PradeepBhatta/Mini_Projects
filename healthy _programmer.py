
# Healthy Programmer

from datetime import datetime
from time import time
from pygame import mixer


def musiconloop(file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("= ")
        if a == stopper:
            mixer.music.stop()
            break

def log_water(msg):
        with open("water.txt", "a") as f:
             f.write(f"{msg}{datetime.now()}\n") 


def log_eyes(msg):
        with open("eyes.txt", "a") as f:
             f.write(f"{msg}{datetime.now()}\n") 
def log_ex(msg):
        with open("ex.txt", "a") as f:
             f.write(f"{msg}{datetime.now()}\n") 


if __name__ == '__main__':

    init_water = time()
    init_eyes = time()
    init_ex = time()

    water_time = 25
    eyes_time = 30
    ex_time = 45

    while True :
        if time() - init_water  > water_time:
            print("Water drinking Time. Type 'done' to STOP")
            init_water = time()
            musiconloop("water.mp3", "done")
            log_water(f"Water drank at ")

        if time() - init_eyes  > eyes_time:
            print("Eyes Relaxing Time. Type 'done' to STOP")
            musiconloop("eyes.mp3", "done")
            init_eyes = time()
            log_eyes(f"Eyes relaxed at ")

        if time() - init_ex  > ex_time:
            print("Exercise doing Time. Type 'done' to STOP")
            musiconloop("Physical.mp3", "done")
            init_ex = time()
            log_ex(f"Exercise done at ")

