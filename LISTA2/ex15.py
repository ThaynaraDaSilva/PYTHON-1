#-------------------------------------------------------------------------------
# program outputs date and time from system
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------
from datetime import datetime # library
today = datetime.now() #gets the date and time from library
# conditions checks which month is being output to change from number to name of month
if today.month == 1:
    month = ("January")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 2:
    month = ("February")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 3:
    month = ("March")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 4:
    month = ("April")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 5:
    month = ("May")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 6:
    month = ("June")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 7:
    month = ("July")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 8:
    month = ("August")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 9:
    month = ("September")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 10:
    month = ("October")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 11:
    month = ("November")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))
elif today.month == 12:
    month = ("December")
    print("{}/ {} / {} - {}:{} ".format(today.day, month, today.year, today.hour, today.minute))