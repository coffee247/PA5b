

import math
import operator
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
import logging
import fileLoaderClass

# set up logging
dirpath = pathlib.Path(__file__).parent.absolute()

logging.basicConfig(filename=f'{dirpath}/my-model.txt', filemode='w', format='%(message)s')


class sentimenter():
    bagOfWords = dict()  # unigram table of word frequencies
    corpora = []  # container for each of the loaded files (from disk)

    def __init__(self):
        myFileloader = fileLoaderClass
        self.corpora = myFileloader.loadFiles()  # load files from disk into files array
        a=1



