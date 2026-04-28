# print("Twinkle Twinkle, Little Star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky\nTwinkle Twinkle Little Star\nHow I wonder what you are!")

# print(''' Twinkle Twinkle, Little Star
#       How I wonder what you are
#       Up above the world so high
#       Like a diamond in the sky
#       Twinkle Twinkle Little Star
#       How I wonder what you are! ''')


import pyttsx3
engine = pyttsx3.init()

engine.say("I will speak this text")
engine.runAndWait()
