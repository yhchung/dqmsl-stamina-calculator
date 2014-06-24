# Stamina Calulator
#
# 
import datetime

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
now = datetime.datetime.now()
datetime.time(now.hour, now.minute)

targetHour = now.hour + neededHours
targetMinute = now.minute + neededMinutes

if targetMinute >= 60 :
	targetMinute -= 60
	targetHour += 1


print "you can read the needed stamina at " + str(targetHour) + ":" + str(targetMinute)


# you can use XX stamina now

eventTimeMinutes = eventTime * 60
currentTime = now.hour * 60 + now.minute
remainingTime = eventTimeMinutes - currentTime # minutes
extraStamina = currentStamina + int(remainingTime/10) - maxStamina

print "you can use " + str(extraStamina) + " stamina now"



