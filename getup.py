# Motivates the user to get up every once in a while and get ripped
import random
things = ['sit ups', 'leg raises', 'push ups', 'jumping jacks', 'leg circles', 'lunges', 'squats']
print('Get up and do ' + str(random.randint(1, 40)) + ' ' + things[random.randint(0, len(things) - 1)])
input('? ')