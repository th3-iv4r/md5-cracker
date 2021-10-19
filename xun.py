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
            for i in range(0,1000000):
                try:
                    raw_hash = str(str(str(str(subprocess.check_output(f"echo -n '{wordsWordlist[i]}' | md5sum", shell=True)).replace("-","")).replace("b'","")).replace("\\n'","")).replace(" ","")
                    print("=> {}".format(wordsWordlist[i]))
                    if raw_hash == md5hash:
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
            exit()


    wordlist_file = input("Enter wordlist path [Exp: /root/Desktop/wordlist.txt]: ")
    md5hash = input("Enter md5 hash string [Exp: e10adc3949ba59abbe56e057f20f883e]: ")
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
