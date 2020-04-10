

import pathlib
import sys


class fileLoader():

    def __init__(self):
        pass

    def loadFiles(self):
        files = []
        outfiles = []
        argLength: int = len(sys.argv)
        for index in range(1, argLength, 1):
            files.append(self.readfile(index))  # load text from files on disk
        return files

    def readfile(self, fileAtIndex):
        try:
            file = open(sys.argv[fileAtIndex], 'r')
            filetext = file.read()
            file.close()
            return filetext
        except:
            print("{} \n\tException:  error loading file {}\n\t"
                  "Application will quit so you can try again!\n{}".format("*" * 72, sys.argv[fileAtIndex], "*" * 72))
            input("press ENTER key to continue quitting\n\n")
            print("Bye!\n\n")
            exit()