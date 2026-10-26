import os
from pathlib import Path
import subprocess
os.chdir('D:\\Reimei\\Copies\\InProcess\\Shiken')
print(os.getcwd())
def imgOpen(imagePath):
    path=Path(imagePath)
    if not path.exists():
        print(f"Error: The file '{imagePath}' does not exist.")
        return
    os.startfile(path)
#The format I require is Date_Time_ID_CopyType(Sub-CopyType)
#date and times should be taken from the photo name
#Date given? If yes, simply add all the below to the oldname. If not, ask for the exam date.
def underscoreRemoval(fileName):
    fileName=fileName[0:len(fileName)-1]
    return fileName

def date():
    date=""
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
        
def paymentMethod():
    print("Select the payment method:")
    print("a. Cash\nb. bKash\nc. UCB\nd. DBBL\ne. ABL\nf. Nagad\ng. Cheque\nh. Rapid Pass\ni. FDR ABL45573\nj. FDR ABL45678\nk. FDR ABL45685\nl. Receivable\nm. Returnable\nn. Piggy Bank\no. Rocket\np. Upay\nq. Hokuyou Ginkou")
    acco=input()
    validLetters="abcdefghijklmnopq"
    while(acco not in validLetters):
        print("Please enter a letter from the given list only.")
        acco=input()
    if(acco=='a'):
        acco="Cash"
    if(acco=='b'):
        acco="bKash"    
    if(acco=='c'):
        acco="UCB"
    if(acco=='d'):
        acco="DBBL"
    if(acco=='e'):
        acco="ABL"
    if(acco=='f'):
        acco="Nagad"
    if(acco=='g'):
        acco="Cheque"
    if(acco=='h'):
        acco="RapidPass"
    if(acco=='i'):
        acco="FDRABL45573"
    if(acco=='j'):
        acco="FDRABL45678"
    if(acco=='k'):
        acco="FDRABL45685"
    if(acco=='l'):
        acco="Receivable"
    if(acco=='m'):
        acco="Returnable"
    if(acco=='n'):
        acco="PiggyBank"
    if(acco=='o'):
        acco="Rocket"
    if(acco=='p'):
        acco="Upay"
    if(acco=='q'):
        acco="Hokuyou"
    return acco

def currency():
    print("a. Taka\nb. Yen\nc. Rupee\nd. Dollar\ne. Hong Kong Dollar\nf. Minutes")
    curren=input()
    validLetters="abcdef"
    while (curren not in validLetters):
        print("Please enter a letter from the given list only.")
        curren=input()
    if(curren=="a"):
        curren="Taka"
    if(curren=="b"):
        curren="Yen"    
    if(curren=="c"):
        curren="Rupee"
    if(curren=="d"):
        curren="Dollar"
    if(curren=="e"):
        curren="HKDollar"
    if(curren=="f"):
        curren="Minutes"
    return curren

def homeAccount():
    print("a. Family\nb. Natsuko\nc. Wanjan\nd. Tushar\ne. Priyanka\nf. Khala\ng. Non-affiliated Party")
    acco=input()
    validLetters="abcdefg"
    while (acco not in validLetters):
        print("Please enter a letter from the given list only.")
        acco=input()
    if(acco=="a"):
        acco="Family"
    if(acco=="b"):
        acco="Natsuko"    
    if(acco=="c"):
        acco="Wanjan"
    if(acco=="d"):
        acco="Tushar"
    if(acco=="e"):
        acco="Priyanka"
    if(acco=="f"):
        acco="Khala"
    if(acco=="g"):
        acco="NonaffiliatedParty"
    return acco
    
def reimeiAccount():
    print("a. Reimei\nb. RILI01\nc. RILI02\nd. RILI03\ne. RILI04\nf. RILI05\ng. RILI06\nh. RILI07\ni. RILI08\nj. Student\nk. Aichi(HR)\nl. Aichi(Officer)\nm. Aichi(MarketingOfficer)\nn. Aichi(Accounts)\no. EWMCH\np. Non-affiliated Party")
    acc=input()
    validLetters="abcdefghijklmnop"
    while (acc not in validLetters):
        print("Please enter a letter from the given list only.")
        acc=input()
    if(acc=="a"):
        acc="Reimei"
    if(acc=="b"):
        acc="RILI01"    
    if(acc=="c"):
        acc="RILI02"
    if(acc=="d"):
        acc="RILI03"
    if(acc=="e"):
        acc="RILI04"
    if(acc=="f"):
        acc="RILI05"
    if(acc=="g"):
        acc="RILI06"
    if(acc=="h"):
        acc="RILI07"
    if(acc=="i"):
        acc="RILI08"
    if(acc=="j"):
        acc="Student"
    if(acc=="k"):
        acc="Aichi(HR)"
    if(acc=="l"):
        acc="Aichi(Officer)"
    if(acc=="m"):
        acc="Aichi(MarketingOfficer)"
    if(acc=="n"):
        acc="Aichi(Accounts)"
    if(acc=="o"):
        acc="EWMCH"
    if(acc=="p"):
        acc="NonaffiliatedParty"
    return acc

def bkash():
    print("Enter the transaction ID (TrXID):")
    trxID=input()
    print("Is this a copy of:\na. Sent?\nb. Received?")
    scType=input()
    while (scType!="a" or scType!="b"):
        print("Please enter a letter from the given list only.")
        scType=input()
    if(scType=="a"):
        scType="(sent)"
    if(scType=="b"):
        scType="(received)"
    sc=trxID+scType
    return sc
    
    
def abl():

def dbbl():

def ucb():

def cheque():
    print()
    print("Enter the cheque number")
    num=input()
    state=""
    while (scType!="a" or scType!="b" or scType!="c"):
        print("Enter the state of the cheque: a. Received\nb. Deposit\nc. Confirmation")
        state=input()
    if(scType=="a")
        state="(received)"
    if(scType=="b")
        state="(deposit)"
    else:
        state="(confirmation)"
    chequeDetails=num+state
    return chequeDetails
    
def managerReceipt():
    with open("managerReceipt.txt", "r", encoding="utf-8") as fileRead:
        firstLine = fileRead.readline()
        lines=fileRead.readlines()
        with open("managerReceipt.txt", "w", encoding="utf-8") as fileWrite:
            fileWrite.writelines(lines[1:])
        return firstLine

def studentReceipt():
    with open("studentReceipt.txt", "r", encoding="utf-8") as fileRead:
        firstLine = fileRead.readline()
        lines=fileRead.readlines()
        with open("studentReceipt.txt", "w", encoding="utf-8") as fileWrite:
            fileWrite.writelines(lines[1:])
        return firstLine

def studentID():
    studentID = ""
    print("Enter the StudentID:")
    studentID=input()
    while len(studentID)!=8:
        print("Enter the correct StudentID:")
        studentID = input()
    return studentID
    
def payer(thisInstitution):
    print("Who paid in this transaction?")
    if(thisInstitution=="reimei"):
        account=reimeiAccount()
    if(thisInstitution=="home"):
        account=homeAccount()
    return account

def payee(thisInstitution):
    print("Who was paid in this transaction?")
    if(thisInstitution=="reimei"):
        account=reimeiAccount()
    if(thisInstitution=="home"):
        account=homeAccount()
    return account

def storeName():
    print("Enter the name of the store:")
    store=input()
    return store
    
def transaction(insti):
    #(Receipt and No Receipts)
    transacFileName="(Transaction)"
    payer=payer(insti)
    payee=payee(insti)
    serial=""
    paymentMethod=paymentMethod()
    currency=currency()
    if(payer=="NonaffiliatedParty" or payee=="NonaffiliatedParty"):
        suff=storeName()
    if(paymentMethod=="bKash"):
        suff=bkash()
    if(payer=="Reimei" or payee=="Reimei"):
        serial=managerReceipt()
        
    if(((payer=="RILI07" or payer=="Aichi(Officer)") and (payee=="Student")) or ((payee=="RILI07" or payee=="Aichi(Officer)") and (payer=="Student"))):
        serial=studentReceipt()
    
    if(payer=="Student" or payee=="Student"):
        sID=studentID()

    transacFileName=transacFileName+")_("+payer+"TO"+payee+"("+paymentMethod+"("+currency")))"+serial()/storeName
    
    
    payee=payee()
    serial/storeName
    transacFileName=transFileName+"(Transaction))_"
    print("Enter the store name:")
    storeName=input()
    transacFileName=transacFileName+storeName
    print("Enter the amount of the transaction:")
    amountSpent=input()
    transacFileName=
    
def lessonNumber(thisLesson):
    if thisLesson<100:
        if thisLesson<10:
            thisLesson = "0"+str(thisLesson)
        thisLesson = "0"+str(thisLesson)
    return thisLesson

def homework(fileName):
    fileName=fileName+"Homework"
    lesson=""
    while lesson.strip()=="":
        print("Enter the Lesson:")
        lesson=input()
    fileName=fileName+"_Lesson"+str(lessonNumber(int(lesson)))
    lesson=""
    noOfAttempts=""
    while noOfAttempts.strip()=="":
        print("Enter the number of questions attempted:")
        noOfAttempts = input()
    fileName=fileName+"["+noOfAttempts+"of"
    noOfAttempts=""
    noOfQuestions=""
    while noOfQuestions.strip()=="":
        print("Enter the total number of questions:")
        noOfQuestions = input()
    fileName=fileName+noOfQuestions+"]"
    noOfQuestions=""
    return fileName

def exam(fileName):
    fileName=fileName+"Exam("
    examType=""
    while examType.strip()=="":
        print("Enter the Exam Type:\n1. Short\n2. Grammar\n3. Oral\n4. Final")
        examType = input()
    if examType=="4":
        fileName=fileName+"Final("
        subExamType=""
        while subExamType.strip()=="":
            print("Enter the Sub-Exam Type:\n1. Kanji&Vocabulary\n2. Grammar\n3. Oral\n4. Reexam")
            subExamType = input()
        if subExamType=="1":
            fileName=fileName+"Kanji&Vocabulary)"
        if subExamType=="2":
            fileName=fileName+"Grammar)"
        if subExamType=="3":
            fileName=fileName+"Oral)"
        if subExamType=="4":
            fileName=fileName+"Reexam)"    
        subExamType=""
        fileName=fileName+")"
    else:
        if examType=="1":
            fileName=fileName+"Short("
            subExamType=""
            while subExamType.strip()=="":
                print("Enter the Sub-Exam Type:\n1. Hiragana\n2. Number\n3. Katakana\n4. Vocabulary&Sentence\n5. Sentence\n6. Kanji")
                subExamType = input()
            if subExamType=="1":
                subExamType=""
                fileName=fileName+"Hiragana)"
            if subExamType=="2":
                subExamType=""
                fileName=fileName+"Number)"
            if subExamType=="3":
                subExamType=""
                fileName=fileName+"Katakana)"
            if subExamType=="4":
                fileName=fileName+"Vocabulary&Sentence)"
            if subExamType=="5":
                fileName=fileName+"Sentence)"
            if subExamType=="6":
                subExamType=""
                fileName=fileName+"Kanji)"
                fileName=fileName+"_"
                while subExamType.strip()=="":
                    print("Enter the Kanji Exam type:\n1. Kanji 1-20\n2. Kanji 1-40\n3. Kanji 1-60\n4. Kanji 1-80\n5. Kanji 1-107\n6. Kanji 1-127 (Lesson 1)\n7. Kanji 1-147 (Lesson 2)\n8. Kanji 1-167 (Lesson 3)\n9. Kanji 1-187 (Lesson 4)\n10. Kanji 1-207 (Lesson 5)\n11. Kanji 1-207(Review)\n12. Kanji 1-227 (Lesson 6)\n13. Kanji 1-247 (Lesson 7)\n14. Kanji 1-267 (Lesson 8)\n15. Kanji 1-287 (Lesson 9)\n16. Kanji 1-307 (Lesson 10)\n17. Kanji 1-307(Review)\n18. Kanji 1-327 (Lesson 11)\n19. Kanji 1-347 (Lesson 12)\n20. Kanji 1-367 (Lesson 13)\n21. Kanji 1-387 (Lesson 14)\n22. Kanji 1-407 (Lesson 15)\n23. Kanji 1-407(Review)")
                    subExamType=input()
                if subExamType=="1":
                    fileName=fileName+"00001to00020"
                if subExamType=="2":
                    fileName=fileName+"00001to00040"
                if subExamType=="3":
                    fileName=fileName+"00001to00060"
                if subExamType=="4":
                    fileName=fileName+"00001to00080"
                if subExamType=="5":
                    fileName=fileName+"00001to000107"
                if subExamType=="6":
                    fileName=fileName+"00001to00127"
                if subExamType=="7":
                    fileName=fileName+"00001to00147"
                if subExamType=="8":
                    fileName=fileName+"00001to00167"
                if subExamType=="9":
                    fileName=fileName+"00001to00187"
                if subExamType=="10":
                    fileName=fileName+"00001to00207"
                if subExamType=="11":
                    fileName=fileName+"00001to00207(Review)"
                if subExamType=="12":
                    fileName=fileName+"00001to00227"
                if subExamType=="13":
                    fileName=fileName+"00001to00247"
                if subExamType=="14":
                    fileName=fileName+"00001to00267"
                if subExamType=="15":
                    fileName=fileName+"00001to00287"
                if subExamType=="16":
                    fileName=fileName+"00001to00307"
                if subExamType=="17":
                    fileName=fileName+"00001to00307(Review)"
                if subExamType=="18":
                    fileName=fileName+"00001to00327"
                if subExamType=="19":
                    fileName=fileName+"00001to00347"
                if subExamType=="20":
                    fileName=fileName+"00001to00367"
                if subExamType=="21":
                    fileName=fileName+"00001to00387"
                if subExamType=="22":
                    fileName=fileName+"00001to00407"
                if subExamType=="23":
                    fileName=fileName+"00001to00407(Review)"
                subExamType=""
            name=name+")"
            if subExamType=="4" or subExamType=="5":
                subExamType=""
                fileName=fileName+"_Lesson"
                lesson=""
                while lesson.strip()=="":
                    print("Enter the Lesson:")
                    lesson=input()
                if "&" not in lesson:
                    fileName=fileName+str(lessonNumber(int(lesson)))
                else:
                    fileName=fileName+str(lessonNumber(int(lesson.split("&")[0])))+"&"+str(lessonNumber(int(lesson.split("&")[1])))
                lesson=""                      
        if examType=="2":
            fileName=fileName+"Grammar)"
            subExamType=""
            while subExamType.strip()=="":
                print("Enter the Sub-Exam Type:\n1. After Lesson 3\n2. After Lesson 7\n3. After Lesson 13\n4. After Lesson 16\n5. After Lesson 19\n6. After Lesson 23\n7. After Lesson 30\n8. After Lesson 35\n9. After Lesson 40\n10. After Lesson 45")
                subExamType = input()        
            if subExamType=="1":
                fileName=fileName+"_Lesson003from001"
            if subExamType=="2":
                fileName=fileName+"_Lesson007from001"
            if subExamType=="3":
                fileName=fileName+"_Lesson013from001"
            if subExamType=="4":
                fileName=fileName+"_Lesson016from001"
            if subExamType=="5":
                fileName=fileName+"_Lesson019from001"
            if subExamType=="6":
                fileName=fileName+"_Lesson023from001"
            if subExamType=="7":
                fileName=fileName+"_Lesson030from026"
            if subExamType=="8":
                fileName=fileName+"_Lesson035from026"
            if subExamType=="9":
                fileName=fileName+"_Lesson040from026"
            if subExamType=="10":
                fileName=fileName+"_Lesson045from026"
            subExamType=""
        if examType=="3":
            name=name+"Oral)"
            subExamType=""
            while subExamType.strip()=="":
                print("Enter the Sub-Exam Type:\n1. After Lesson 7\n2. After Lesson 13\n3. After Lesson 19\n4. After Lesson 35\n5. After Lesson 40\n6. After Lesson 45")
                subExamType = input()        
            if subExamType=="1":
                name=name+"_Lesson007from001"
            if subExamType=="2":
                name=name+"_Lesson0013from001"
            if subExamType=="3":
                name=name+"_Lesson019from001"
            if subExamType=="4":
                name=name+"_Lesson035from001"
            if subExamType=="5":
                name=name+"_Lesson040from001"
            if subExamType=="6":
                name=name+"_Lesson045from001"
            subExamType=""
        examType=""
    marks=""
    while marks.strip()=="":
        print("Enter the obtained marks:")
        marks=input()
    fileName=fileName+"["+marks+"of"
    marks=""
    while marks.strip()=="":
        print("Enter the total marks:")
        marks=input()
    fileName=fileName+marks+"]"
    return fileName

def home(fileName)
    #activities: 1. Transaction (Receipt and No Receipts) 2. Arts (a. Priyanka's, b. Tushar's, c. Natsuko's, d. Wanjan's)
    
def reimei(fileName):
    fileName=fileName+"(Reimei"
        print("What is the file of?\n1. Transaction\n2. Copy\n3. StudentRecord")
        fileContent=input()
        if(fileContent==1):
            fileName=fileName+transaction("reimei")
        if(fileContent==3):
            fileName=fileName+"(StudentRecord))_"
        if(fileContent==2):
            fileName=fileName+"(Copy))_"
            studentID = studentID()
        fileName=fileName+studentID+"_"
        studentID = ""
        if "JP" in name:
            copyType=""
            while copyType.strip()=="":
                print("Enter the Copy Type:\n1. Exam\n2. HW\n3. Random")
                copyType = input()
            if copyType=="1":
                fileName=exam(fileName)    
            if copyType=="2":
                fileName=homework(fileName)
             
            #Still Remaining: if copyType=="3":
            copyType=""
return fileName


"""def institution():
    institution=""
    print("Enter the institution which the transaction is for:\n1. Home\n2. Reimei")
    inst=input()
    if(inst==1):
        institution=
    if(inst==2):
        institution="(Reimei)"
    return institution"""

for count, file in enumerate(os.listdir()):
    oldName, ext = os.path.splitext(file)
    imgOpen(file)
    print(oldName\n"Is the date (and time) for the occurrance given/accurate? (Press:\n1. Any key if True.\n2. n if False\nand then press Enter")
    letter = input()
    if(letter == 'n'):
        oldName=date()
    print(oldName\n"Is there an _ at the end?\nPress:\n1. n if False\n2. Any key if True.\nand then press Enter")
    letter = input()
    if(letter!="n"):
        oldName=underscoreRemoval(oldName)
    name=oldName
    
    
    newNameWithoutExtension = name
    newNameWithExtension = f'{newNameWithoutExtension}{ext}'
    print(newNameWithExtension)
    subprocess.run(["taskkill", "/f", "/im", "Microsoft.Photos.exe"], capture_output=True)
    subprocess.run(["taskkill", "/f", "/im", "FoxitPDFReader.exe"], capture_output=True)
    print("Press Enter if the renaming is okay or n if it is not okay")
    letter = input()
    if(letter == ''):
       os.rename(file, newNameWithExtension)
    count=count+1