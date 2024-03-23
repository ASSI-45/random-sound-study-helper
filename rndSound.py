import pygame

# read (other solution): https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame

# loading everthing in the package and the filles through the pkg
def setup():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('./start.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    pygame.mixer.music.load('./sounds/start.mp3')
    pygame.mixer.music.load('./sounds/stop.mp3')


def main() -> None:
    setup()
    print("Running")


if __name__ == "__main__":
    while(True):
        main()

