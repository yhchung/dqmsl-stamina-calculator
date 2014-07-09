# Stamina Calulator
#
# 
import datetime
from datetime import timedelta

maxStamina = 64
minutePerStamina = 10
dayLightSaving = True
timeDiff = 13

currentStamina = input("Enter current stamina: ")
neededStamina = input("Enter stamina needed: ")
eventTime = input("Enter when it needed (ex: enter 16 for 4pm): ")

#input_doubleStamina = input("Double Stamina? (y/n) ")

neededTime = (neededStamina - currentStamina) * minutePerStamina
neededHours = neededTime / 60
neededMinutes = neededTime % 60

# how long does it take
print "---"
print str(neededHours) + " Hours " + str(neededMinutes) + " Minutes needed for " + str(neededStamina) + " stamina"

# you can reach the needed stamina at 
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
now = datetime.datetime.now()
endTime = now + datetime.timedelta(minutes=neededMinutes, hours=neededHours)

print "you can read the needed stamina at " + str(endTime.hour) + ":" + str(endTime.minute)


# you can use XX stamina now
eventTimeMinutes = eventTime * 60
currentTime = now.hour * 60 + now.minute
remainingTime = eventTimeMinutes - currentTime # minutes
extraStamina = currentStamina + int(remainingTime/minutePerStamina) - neededStamina

if extraStamina > 0 : 
	print "you can use " + str(extraStamina) + " stamina now, down to " \
			+ str(currentStamina - extraStamina)
else :
	print "you can't use stamina now"

"""
print "eventTimeMinutes: " + str(eventTimeMinutes)
print "currentTime: " + str(currentTime)
print "remainingTime: " + str(remainingTime)
print "extraStamina: " + str(extraStamina)
"""


