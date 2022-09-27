Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>import random,winsound,time

while True:
    t=random.randint(1,100)
    if t>60:
       print("Temperature is high.....",t)
       winsound.PlaySound("Desktop/440.wav", winsound.SND_FILENAME)
    else:
        print("Temperature is normal.....",t)


    time.sleep(1)
