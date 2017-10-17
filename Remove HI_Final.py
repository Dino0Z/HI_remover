import glob, os, re, fileinput, time, shutil

a = 0
while True:
    a=0
    print("\
[\"info\" for information]\n\
[\"default\" use current dir]\n\
[\"quit\" to terminate this program]")
    path = raw_input("[enter full path to dir]:")

    if path == "quit":
        print("Exiting...")
        break
    
    elif path == "info":
        print ("\nThis script cleans Hearing Impaired (HI) tags \
from all .srt files in a directory. Backups are made and stored \
in folder \"Original subs\". Type the full path to directory that \
needs HI cleanup. Current directory is used if nothing is \
specified or \"default\" is used.")
        raw_input("Press Enter to continue...")
        print("\n")
        continue
        
    elif path == "" or path == "default":
        path = os.getcwd()
        
    if os.path.isdir(path):
        os.chdir(path)
        orgSubs = path + "/Original subs"
        if not os.path.exists(orgSubs):
            os.makedirs(orgSubs)
        print ("\nStarting to clean...")
        time.sleep(1)
        for file in glob.glob("*.srt"):
            #bakCheck = orgSubs + "/" + file[:-4] + " - Dirty Sub.srt"
            bakCheck = orgSubs + "/" + file
            if not os.path.isfile(bakCheck):
                shutil.copy2(file, bakCheck)
            for line in fileinput.FileInput(file, inplace=1):
                #if re.search(r'(\[|\()(.*?)(\]|\))', line):
                line=re.sub(r'(\[|\()(.*?)(\]|\))', r' ', line.rstrip())
                #if not line == "":
                print line
            a+=1
            print("Cleaned file: " + file)
        print("\nCleaned " + str(a) + " files in total. Also made backups \
of files in folder \"Original subs\"")
        
    else:
        print("\nDirectory doesn't exist")
    
    usrInput = raw_input("More cleaning? [y/n] ").lower()

    if usrInput.strip() == 'y' or usrInput == '':
        pass
    elif usrInput.strip() == 'n':
        print("Exiting...")
        break
    else:
        print ("I'll take that as a no...")
        break

time.sleep(1)
