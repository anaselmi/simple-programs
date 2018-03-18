#July 7, 2017
#Clock that takes time and returns as words

def talking_clock(time):
    
    #Gives us hour and minute as ints
    hour = int(time[0:2])
    minute = int(time[3:])
    minute_tens = int(time[3])
    minute_ones = int(time[4])
    
    if hour >= 12:
        #Gives us our p.m hours in twelve hour time
        hour = hour - 12
        day_or_night = "pm" #Used to tell if am or p.m
    else:
        day_or_night = "am" #used to tell if am or pm

    #Lists used to turn int to word
    hour_list = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    minute_tens_list = ["oh", "ten", "twenty", "thirty", "forty", "fifty"]
    minute_ones_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    minute_teens_list = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    hour_word = hour_list[hour] #Hour in words

    if minute_tens == 0 and minute_ones == 0:
        minute_word = "" #Should be empty if there's no minute at all
    elif minute_tens == 1 and minute_ones != 0:
        minute_word = minute_teens_list[minute_ones] #This is for when minute is in the teens and not ten
    else:
        minute_word = minute_tens_list[minute_tens] + " " + minute_ones_list[minute_ones] + " " #runs in all other scenarios

    print("It's %s %s%s" %(hour_word, minute_word, day_or_night))

talking_clock("24:53")