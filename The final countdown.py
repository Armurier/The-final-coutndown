import wave
from time import sleep
def countdown():
    i = 3
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
    sleep(1)
if i == 1:
    print("The Final Countdown !!")
    wave.open('final.wav', 'r')
