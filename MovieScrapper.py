import os
import sys
import requests
from bs4 import BeautifulSoup
from imdb import IMDb


def getFileListFromDir(directory):
    fileList = []
    if os.path.exists(directory):
        for files in os.listdir(directory):
            filePath = os.path.join(directory, files)
            fileList.append(filePath)
        return fileList

    else:
        print("==========>[ERROR][getFileListFromDir] directory <" + directory + "> does not exist !")

def checkPath(inputPath):
    if os.path.exists(inputPath):
        return inputPath
    else:
        print("==========>[ERROR][absolutePath] path <" + inputPath + "> does not exist !")
        return None
    
def movieRequest(movie,imdb):
    return imdb.get_movie(movie)

def removeExtension(movie):
    data = movie.split('.')
    return data[0]

def transformParenthese(string):
    transform = ''
    for x in string:
        if x == '(':
            x = '%28'
        elif x == ')':
            x = '%29'
        transform += x
    return transform
            
            

#code = requests.get(url)

if __name__ == '__main__':
    
    #Define var (ONLY THING THAT CAN BE EDITED)

    # check arguments
    if ((len(sys.argv) != 2)):
        print("Error, usage is: python {0} <input_path>".format(sys.argv[0]))
        sys.exit(1)
    else:
        PATH = sys.argv[1]
        # get Files
        if checkPath(PATH) is not None:
            fileList = getFileListFromDir(PATH)
        else:
            print("Aborting...")
            sys.exit(1)
            
        imdb = IMDb()
        for file in fileList:
            file = os.path.basename(file)
            # remove .xxx
            movie = removeExtension(file)
            print(movie)
            transform = transformParenthese(movie)
            url = "https://www.imdb.com/find?q="+transform
            print(url)
            response = requests.get(url)
            if response.ok:
                print(response.text)
                pass
            
            """
            response = movieRequest("0387564",imdb)

            # print the genres of the movie
            print('Genres:')
            for genre in response['genres']:
                print(genre)
            """
        