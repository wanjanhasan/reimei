import datetime
    
def completeNameChange():
    return
    
def invalidEntriesCheck(givenEntry, validEntries):
    while (givenEntry not in validEntries):
        print("Please enter a letter from the given list only.")
        givenEntry=input()
    return givenEntry
    
def pastDate():
    date=""
    #need to check if the entered value is a numeral
    while(len(date)!=8):
        year=""
        month=""
        day=""
        while(year==""):
            print("Type the Year:")
            year=input()
            while(len(year)!=4): #Need a check for non-numerals
                print("Type the correct year.")
                year=input()
        while(month==""):
            print("Type the Month number:")
            month=input()
            while(len(month)!=2):
                if(len(month)==1):
                    month="0"+month
                    break
                print("Type the correct month.")
                month=input()
        while(day==""):
            print("Type the Day of the month:")
            day=input()
            while(len(day)!=2):
                if(len(day)==1):
                    day="0"+day
                    break
                print("Type the correct day")
                day=input()
        date=year+month+day
        return date

def twentyFourHoursHour(twelveHoursHour):
    twentyFourHoursHour=None #need to check if the entered value is a numeral
    while (twelveHoursHour<1 or twelveHoursHour>12 or twelveHoursHour==None):
        print("Enter the correct 12 hour time.")
        twelveHoursHour=input()
    print("Was the time:\n[a] before noon (ante meridiem (am))?\n[p] after noon (post meridiem (pm))")
    ampmCheck=invalidEntriesCheck(input(), "ap")
    if(ampmCheck=="p"):
        if(twelveHoursHour==12):
            twentyFourHoursHour=twelveHoursHour   
        else:
            twentyFourHoursHour=twelveHoursHour+12
        twelveHoursHour=input()
    if(ampmCheck=="a"):
        if(twelveHoursHour==12):
            twentyFourHoursHour=twelveHoursHour-12
        else:
            twentyFourHoursHour=twelveHoursHour
    return twentyFourHoursHour
    

def pastTime():
    time=""
    while(len(time)==4 or len(time)==6):
        hour=""
        minute=""
        second=""
        while(hour==""):
            print("What was the hour?")
            hour=input()
            print("Did you give the hour in:\n[a] 24-hour clock?\n\n[b] 12-hour clock?")
            entry=invalidEntriesCheck(input(), "ab")
            if(entry=="b"):
                hour=twentyFourHoursHour(hour)
            print("What was the minute?")
            minute=input()
            print("What was the second?")
            second=input()
    return time

def documentDate(givenDate):
    print(givenDate+"<---Does this date in file name correspond to the actual date of the file open in front of you?\nPress:\n[y] for Yes\n[n] for No")
    entry=invalidEntriesCheck(input(), "yn")
    if(entry=="n"):
        print("Is the document from today?\nPress:\n[y] for Yes\n[n] for No")
        checkIfToday=invalidEntriesCheck(input(), "yn")
        if(checkIfToday=="y"):
            givenDate=datetime.datetime.now()
            givenDate=givenDate.date()
            givenDate=str(givenDate).replace("-", "")
        if(entry=="n"):
            givenDate=pastDate()
    return givenDate

def documentTime(givenTime):
    print(givenTime+"<---Does this time in file name correspond to the actual time of the file open in front of you?\nPress:\n[y] for Yes\n[n] for No")
    entry=invalidEntriesCheck(input(), "yn")
    if(entry=="n"):
        givenTime=pastTime()
        if(len(givenTime)==1):
            givenTime="0"+str(givenTime)
    return givenTime

def documentDateTime():
    print("Enter your file name.")
    fn=input()
    date=None
    time=None
    information=None
    display=None
    validEntries="yn"
    if(fn.count("_")>=0):
        date=documentDate(fn.split("_")[0])
        if(fn.count("_")>=1):
            secondPos=fn.split("_")[1]
            print(secondPos+"<---Does this look like a time to you?\nPress:\n[y] for Yes\n[n] for No")
            entry=invalidEntriesCheck(input(), "yn")
            if(entry=="y"):
                time=documentTime(secondPos)
            if(entry=="n"):
                information=secondPos
        if(fn.count("_")>=2):
            information=fn.split("_")[2]
    print("Date:"+date+"\n"+"Time"+time+"\n"+"Details"+information)
    
def institutionCheck():
    print("Which institution does this file belong to?\nPress:\n[a] for Reimei\n[b] for Home")
    checkIfToday=invalidEntriesCheck(input(), "ab")
    inst=input()
    if(inst=="a"):
        name=reimei(name)
        name+"
    if(inst=="b"):
        name=name+"(Home"
    name=name+return answer
"""    else:
        print("<<<<((((Maybe your file needs a change of name?))))>>>>\nPress Enter to Continue doing so.")
    
       
        
        
        
        
        
        
        
    if(entry=="n"):
        
        display=date
print(display)""" 


"""
"""
documentDateTime()
