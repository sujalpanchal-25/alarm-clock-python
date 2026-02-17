import datetime
import time
import pygame

ct = datetime.datetime.now().strftime("%I:%M:%S %p")

def set_alarm(at):
    print(f"Alarm Set {at}")
    sound_file = "countdown.mp3"
    is_running  = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"Current Time : {current_time}",end="\r")
        
        if current_time == at:
             print("\n")
             print("WAKE UP! 😴")
        
             pygame.mixer.init()
             pygame.mixer.music.load(sound_file)
             pygame.mixer.music.play()
             
             while pygame.mixer.music.get_busy():
                 time.sleep(1)
             
             is_running = False
        
        time.sleep(1)    


print(f"Current Time : {ct}")
at = input("Enter The Alarm Time(HH:MM:SS AM/PM) : ")

set_alarm(at)