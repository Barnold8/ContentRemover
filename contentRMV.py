## Program removes certain chars from file
import sys

def checks(args):

    ERRMESS = "The program expects arguments, you gave none.\n\nUsage [File path] [flag] [chars...chars]"

    if(len(args) < 2):
        print(ERRMESS)
        exit()

    return parseArgs(args)

def parseArgs(args):

    y = 0 # Used to ignore the program name and file path

    flags = []

    for i in range(len(args)):

        if(i > 0):
            if args[i][0] == '-':
                flags.append(args[i])

    return flags

def construct_directory(split_dir,tilde):

    path = ""
    for i in range(len((split_dir))-1):
        if tilde and i == 0:
            path += split_dir[i]
        else:
            path += split_dir[i]
            path += "/"       
    
    return path

def file_process(lines, chars,preserve,newline,PATH):

    newData = []
    newStr = ""
    l = lines
    p = sys.argv[1].split()
    p = p[len(p)-1]
    
    if newline == False:
        
        for i in range(len(l)):
            l[i] = l[i].rstrip("\n")

    for i in range(len(l)):
        newStr = ""
        for j in range(len(l[i])):
            if l[i][j] not in chars:
                newStr += l[i][j]
        newData.append(newStr)
    
    if preserve:
        with open(PATH + "Modified_File","w") as file:
            for dat in newData:
                file.write("%s\n" % dat)
    else:
        with open(p,"w") as file:
            for dat in newData:
                file.write("%s\n" % dat)
    file.close()
    print(newData)
    
def main():

    flags = checks(sys.argv)
    PATH = sys.argv[1].split("/")
    tilde = False
    preserve = False
    newline = False
    char_array = []
    charStr = ""


    ##Flag checks
    if('-T' in flags):
        PATH[0] = "~/"
        tilde = True

    if('-C' in flags):
        for i in range(len(sys.argv)):
            if '-c' == sys.argv[i]:
               charStr = sys.argv[i+1]
               break
        char_array = list(charStr)
    
    else:
        for i in range(len(sys.argv)):
            if i > 1 and sys.argv[i][0] != '-' and len(sys.argv[i]) < 2:
                char_array.append(sys.argv[i])

    if('-P' in flags):
        preserve = True

    if('-N' in flags):
        newline = True

    if('-H' in flags):
        print("\nProgram usage [file path] [flags] [chars]\n\nor\n\nProgram usage [file usage] [-C] [string]")
        print("\n-T : Includes the '~' character at the start of a file path, useful for Linux systems in starting from the 'home' directory\n-C : Allows for the use of a string to represent the ignored chars instead of a set of chars with spaces between them\n-P : Preserves the original file and writes a new file in the same directory\n-N : Keeps all the instances of newlines in the data for processing (leave this if you want to ignore the newlines, each line will still be written as intended)\n-H : Shows this help screen\n")
        exit()

    ###

    print(flags)
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except Exception as e:
        print("Couldnt find the file you were looking for. Write crmv.py -H for help with this program")
        
    file.close()
    
    file_process(lines,char_array,preserve,newline,construct_directory(PATH,tilde))


main()

