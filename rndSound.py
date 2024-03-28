from pygame import mixer, time
from random import randrange


PAUSE_SHORT = 10 
PAUSE_LONG = 20
QUE_SHORT = 9
QUE_LONG = 20


# loads the mixer in
def setup():
    mixer.init()


def play_start():
    mixer.music.load('./sounds/start.mp3')
    mixer.music.play()
    while mixer.music.get_busy(): 
        time.Clock().tick(10)


def play_stop():
    mixer.music.load('./sounds/stop.mp3')
    mixer.music.play()
    while mixer.music.get_busy(): 
        time.Clock().tick(10)     


def pause(p_time):
    time.wait(p_time * 1000)  # * 100 to convert it to 10 or 20 seconds


def pause_quee(q_type):
    time.wait((randrange(1, q_type, 2) * 1000) * 60)


def settings():
    que_setting = ""
    while(que_setting == ""):
        que_setting = input(" -- Do you want the short or long quee setting (short or long): ").lower()
        if que_setting == "long":
            que_setting = QUE_LONG
        elif que_setting == "short":
            que_setting = QUE_SHORT
        else:
            print(" !! you typed something wrong. Can you retry.")
            que_setting = ""
    pause_setting = 0
    while(pause_setting == 0):
        pause_setting = input(" -- Do you want to pause len to be 1 | 10 seconds or 2 | 20 seconds (1 or 2):")
        if pause_setting == "1": 
            pause_setting = PAUSE_SHORT
        elif pause_setting == 2:
            pause_setting = PAUSE_LONG
        else:
            print(" !! You typed something wrong. Can you retry.")
            pause_setting = 0
    return que_setting, pause_setting


def main(q, p, n) -> None: 
    pause_quee(q)  
    play_start()    
    pause(p)
    play_stop()
    print(f"-{n}-")
    n =+ 1


if __name__ == "__main__":
    setup()
    p_settings = settings()
    sound_delay = 0
    next_sound = 0
    count = 1
    while(True):
        main(p_settings[0], p_settings[1], count)
