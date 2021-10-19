import os

try:
    import subprocess
    from colored import fg,bg,attr
    from playsound import playsound
    from gtts import gTTS

    def save_file():
        filename = "sound.mp3"
        tts = gTTS(text="Password found", lang="en")
        tts.save(filename)
        playsound(filename)
        os.remove(filename)


    def printWordlist(file):
        try:
            wordlist = open(file,"r",encoding="ISO-8859-1")
            wordsWordlist = wordlist.read().split("\n")
            print("")
            for i in range(0,1000000):
                try:
                    raw_hash = str(str(str(str(subprocess.check_output(f"echo -n '{wordsWordlist[i]}' | {hashType}sum", shell=True)).replace("-","")).replace("b'","")).replace("\\n'","")).replace(" ","")
                    text = fg("black") + bg("white") + f"     {wordsWordlist[i]}     " + attr(0)
                    print(f"\r-> {text}",end="")
                    if raw_hash == rawHash:
                        text = fg("green") + "Password found! >>" + attr(0)
                        password = fg("black") + bg("yellow") + f"{wordsWordlist[i]}" + attr(0)
                        print("")
                        print(f"{text} {password}")
                        save_file()
                        exit()

                except IndexError:
                    break
                
            text = fg("red") + "Password not found!" + attr(0)
            print("")
            print(text)
            exit()
        except FileNotFoundError:
            print("File not found!")

    hashList = """
md5
sha256
"""

    wordlist_file = input("Enter wordlist path [Exp: /root/Desktop/wordlist.txt]: ")
    while True:
        global hashType
        hashType = input("Enter hash format ['list' show all formats]: ")
        splitted_HashList = hashList.split("\n")
        a = 0
        if hashType == "list":
            print(hashList)
            continue
        for i in range(0,10):
            try:
                if str(hashType) != str(splitted_HashList[i]):
                    a += 1
                    continue
            except IndexError:
                if a > 3:
                    print("Unknown hash format!")
                    exit()
                else:
                    pass
        else:
            break
    rawHash = input("Enter hash string: ")
    printWordlist(wordlist_file)
except ModuleNotFoundError:
    data = input("install requirements (y/n) ")
    if data == "y" or data == "Y":
        os.system("pip install subprocess")
        os.system("pip install gtts")
        os.system("pip install colored")
        os.system("pip install playsound")
    elif data == "n" or data == "N":
        exit()
    else:
        exit()
except KeyboardInterrupt:
    print("\nquit...")
    exit()
