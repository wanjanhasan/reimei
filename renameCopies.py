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
def lessonNumber(thisLesson):
    if thisLesson<100:
        if thisLesson<10:
            thisLesson = "0"+str(thisLesson)
        thisLesson = "0"+str(thisLesson)
    return thisLesson

for count, file in enumerate(os.listdir()):
    print(file)
    imgOpen(file)
    oldName, ext = os.path.splitext(file)
    studentID = ""
    while studentID.strip()=="":
        print("Enter the StudentID:")
        studentID = input()
    name=studentID+"_"
    studentID = ""
    if "JP" in name:
        copyType=""
        while copyType.strip()=="":
            print("Enter the Copy Type:\n1. Exam\n2. HW\n3. Random")
            copyType = input()
        if copyType=="1":
            name=name+"Exam("
            examType=""
            while examType.strip()=="":
                print("Enter the Exam Type:\n1. Short\n2. Grammar\n3. Oral\n4. Final")
                examType = input()
            if examType=="4":
                name=name+"Final("
                subExamType=""
                while subExamType.strip()=="":
                    print("Enter the Sub-Exam Type:\n1. Kanji&Vocabulary\n2. Grammar\n3. Oral\n4. Reexam")
                    subExamType = input()
                if subExamType=="1":
                    name=name+"Kanji&Vocabulary)"
                if subExamType=="2":
                    name=name+"Grammar)"
                if subExamType=="3":
                    name=name+"Oral)"
                if subExamType=="4":
                    name=name+"Reexam)"    
                subExamType=""
                name=name+")"
            else:
                if examType=="1":
                    name=name+"Short("
                    subExamType=""
                    while subExamType.strip()=="":
                        print("Enter the Sub-Exam Type:\n1. Hiragana\n2. Number\n3. Katakana\n4. Vocabulary&Sentence\n5. Sentence\n6. Kanji")
                        subExamType = input()
                    if subExamType=="1":
                        subExamType=""
                        name=name+"Hiragana)"
                    if subExamType=="2":
                        subExamType=""
                        name=name+"Number)"
                    if subExamType=="3":
                        subExamType=""
                        name=name+"Katakana)"
                    if subExamType=="4":
                        name=name+"Vocabulary&Sentence)"
                    if subExamType=="5":
                        name=name+"Sentence)"
                    if subExamType=="6":
                        subExamType=""
                        name=name+"Kanji)"
                        name=name+"_"
                        subExamType=""
                        while subExamType.strip()=="":
                            print("Enter the Kanji Exam type:\n1. Kanji 1-20\n2. Kanji 1-40\n3. Kanji 1-60\n4. Kanji 1-80\n5. Kanji 1-107\n6. Kanji 1-127 (Lesson 1)\n7. Kanji 1-147 (Lesson 2)\n8. Kanji 1-167 (Lesson 3)\n9. Kanji 1-187 (Lesson 4)\n10. Kanji 1-207 (Lesson 5)\n11. Kanji 1-207(Review)\n12. Kanji 1-227 (Lesson 6)\n13. Kanji 1-247 (Lesson 7)\n14. Kanji 1-267 (Lesson 8)\n15. Kanji 1-287 (Lesson 9)\n16. Kanji 1-307 (Lesson 10)\n17. Kanji 1-307(Review)\n18. Kanji 1-327 (Lesson 11)\n19. Kanji 1-347 (Lesson 12)\n20. Kanji 1-367 (Lesson 13)\n21. Kanji 1-387 (Lesson 14)\n22. Kanji 1-407 (Lesson 15)\n23. Kanji 1-407(Review)")
                            subExamType=input()
                        if subExamType=="1":
                            name=name+"00001to00020"
                        if subExamType=="2":
                            name=name+"00001to00040"
                        if subExamType=="3":
                            name=name+"00001to00060"
                        if subExamType=="4":
                            name=name+"00001to00080"
                        if subExamType=="5":
                            name=name+"00001to000107"
                        if subExamType=="6":
                            name=name+"00001to00127"
                        if subExamType=="7":
                            name=name+"00001to00147"
                        if subExamType=="8":
                            name=name+"00001to00167"
                        if subExamType=="9":
                            name=name+"00001to00187"
                        if subExamType=="10":
                            name=name+"00001to00207"
                        if subExamType=="11":
                            name=name+"00001to00207(Review)"
                        if subExamType=="12":
                            name=name+"00001to00227"
                        if subExamType=="13":
                            name=name+"00001to00247"
                        if subExamType=="14":
                            name=name+"00001to00267"
                        if subExamType=="15":
                            name=name+"00001to00287"
                        if subExamType=="16":
                            name=name+"00001to00307"
                        if subExamType=="17":
                            name=name+"00001to00307(Review)"
                        if subExamType=="18":
                            name=name+"00001to00327"
                        if subExamType=="19":
                            name=name+"00001to00347"
                        if subExamType=="20":
                            name=name+"00001to00367"
                        if subExamType=="21":
                            name=name+"00001to00387"
                        if subExamType=="22":
                            name=name+"00001to00407"
                        if subExamType=="23":
                            name=name+"00001to00407(Review)"
                        subExamType=""
                    name=name+")"
                    if subExamType=="4" or subExamType=="5":
                        subExamType=""
                        name=name+"_Lesson"
                        lesson=""
                        while lesson.strip()=="":
                            print("Enter the Lesson:")
                            lesson=input()
                        if "&" not in lesson:
                            name=name+str(lessonNumber(int(lesson)))
                        else:
                            name=name+str(lessonNumber(int(lesson.split("&")[0])))+"&"+str(lessonNumber(int(lesson.split("&")[1])))
                        lesson=""                      
                if examType=="2":
                    name=name+"Grammar)"
                    subExamType=""
                    while subExamType.strip()=="":
                        print("Enter the Sub-Exam Type:\n1. After Lesson 3\n2. After Lesson 7\n3. After Lesson 13\n4. After Lesson 16\n5. After Lesson 19\n6. After Lesson 23\n7. After Lesson 30\n8. After Lesson 35\n9. After Lesson 40\n10. After Lesson 45")
                        subExamType = input()        
                    if subExamType=="1":
                        name=name+"_Lesson003from001"
                    if subExamType=="2":
                        name=name+"_Lesson007from001"
                    if subExamType=="3":
                        name=name+"_Lesson013from001"
                    if subExamType=="4":
                        name=name+"_Lesson016from001"
                    if subExamType=="5":
                        name=name+"_Lesson019from001"
                    if subExamType=="6":
                        name=name+"_Lesson023from001"
                    if subExamType=="7":
                        name=name+"_Lesson030from026"
                    if subExamType=="8":
                        name=name+"_Lesson035from026"
                    if subExamType=="9":
                        name=name+"_Lesson040from026"
                    if subExamType=="10":
                        name=name+"_Lesson045from026"
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
            name=name+"["+marks+"]"
            marks=""
        if copyType=="2":
            name=name+"Homework"
            lesson=""
            while lesson.strip()=="":
                print("Enter the Lesson:")
                lesson=input()
            name=name+"_Lesson"+str(lessonNumber(int(lesson)))
            lesson=""
            noOfAttempts=""
            while noOfAttempts.strip()=="":
                print("Enter the number of questions attempted:")
                noOfAttempts = input()
            name=name+"["+noOfAttempts+"/"
            noOfAttempts=""
            noOfQuestions=""
            while noOfQuestions.strip()=="":
                print("Enter the total number of questions:")
                noOfQuestions = input()
            name=name+noOfQuestions+"]"
            noOfQuestions=""
        #Still Remaining: if copyType=="3":
        copyType=""
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