import os
import sys
import requests
from bs4 import BeautifulSoup
from imdb import IMDb


def getFileListFromDir(directory):
    fileList = []
    if os.path.exists(directory):
        print("[getFileListFromDir] Listing files from directory <"+directory+">...")
        for files in os.listdir(directory):
            filePath = os.path.join(directory, files)
            fileList.append(filePath)
        return fileList
    else:
        print("==========>[ERROR][getFileListFromDir] directory <" + directory + "> does not exist !")

def checkPath(inputPath):
    if os.path.exists(inputPath):
        print("[checkPath] Validating input path...")
    else:
        print("==========>[ERROR][checkPath] path <" + inputPath + "> does not exist !")
        print("Aborting...")
        sys.exit(1)
    
def movieRequest(movie,imdb):
    print("[movieRequest] Requesting IMDB API...") 
    return imdb.get_movie(movie)

def removeExtension(movie):
    data = movie.split('.')
    print("[removeExtension] Removing extension...") 
    return data[0]

def transformParenthese(string):
    transform = ''
    print("[transformParenthese] Transforming Parenthese for GET request...")
    for x in string:
        if x == '(':
            x = '%28'
        elif x == ')':
            x = '%29'
        transform += x
    return transform
            
def extractID(link):
    print("[extractID] Extracting movie ID...")
    link = link.replace('/title/tt', '')
    link = link.replace('/', '')
    return link            

def imdbRequest(movie):
    print("[imdbRequest] Sending HTTP request...")
    url = "https://www.imdb.com/find?q="+movie
    response = requests.get(url)
    if response.ok:
        links =[]
        data = BeautifulSoup(response.text, 'lxml')
        tables = data.findAll('table')
        for table in tables:
            a = table.find('a')
            link = a['href']
            links.append(link)
            id = extractID(links[0])
            return id
        else:
            print("==========>[ERROR][imdbRequest] Error when sending request !")
            return None


#code = requests.get(url)

if __name__ == '__main__':
    # check arguments
    if ((len(sys.argv) != 2)):
        print("Error, usage is: python {0} <input_path>".format(sys.argv[0]))
        sys.exit(1)
    else:
        PATH = sys.argv[1]
        checkPath(PATH)
        fileList = getFileListFromDir(PATH)
        
        for file in fileList:
            file = os.path.basename(file)
            # remove extension .xxx
            movie = removeExtension(file)
            print(movie)
            movie = transformParenthese(movie)
            id = imdbRequest(movie)
            
            if id is not None:
                imdb = IMDb()
                response = movieRequest(str(id),imdb)
                #print(sorted(response.keys()))
                print(response.get('genres'))
        