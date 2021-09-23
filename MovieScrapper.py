import os
import sys
import requests
from bs4 import BeautifulSoup
from imdb import IMDb
import random
import string
import shutil

def getFileListFromDir(directory):
    fileList = []
    if os.path.exists(directory):
        if DEBUG : print("[getFileListFromDir] Listing files from directory <"+directory+">...")
        for files in os.listdir(directory):
            filePath = os.path.join(directory, files)
            fileList.append(filePath)
        return fileList
    else:
        print("==========>[ERROR][getFileListFromDir] directory <" + directory + "> does not exist !")

def checkPath(inputPath):
    if os.path.exists(inputPath):
        if DEBUG :print("[checkPath] Validating input path...")
    else:
        print("==========>[ERROR][checkPath] path <" + inputPath + "> does not exist !")
        print("Aborting...")
        sys.exit(1)
    
def movieRequest(movie,imdb):
    if DEBUG :print("[movieRequest] Requesting IMDB API...") 
    return imdb.get_movie(movie)

def removeExtension(movie):
    data = movie.split('.')
    if DEBUG :print("[removeExtension] Removing extension...") 
    return data[0]
       
def extractID(link):
    if DEBUG :print("[extractID] Extracting movie ID...")
    link = link.replace('/title/tt', '')
    link = link.replace('/', '')
    return link            

def imdbRequest(movie):
    if DEBUG :print("[imdbRequest] Sending HTTP request...")
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

def cleanSubdirectory(directory):
    if DEBUG :print("[cleanSubdirectory] Removing files in \""+directory+"\" directory...")
    if os.path.exists(directory):
        for files in os.listdir(directory):
            os.remove(os.path.join(directory, files))
    else:
        try:
            os.mkdir(directory)
        except Exception:
            print("==========>[ERROR] [cleanSubdirectory] Could not create " + directory + " subdirectory !")

def concatJSON(jsonPath, outputDirectory, outputFile):
    
    if len(jsonPath) < 2:
        print("==========>[ERROR][concatJSON] Not enough JSON file to concat ! Aborting...")
        sys.exit(1)
    
    if DEBUG :print("[concatJSON] Concatenation of all generated JSON files...")
    outputPath = os.path.join(outputDirectory,outputFile)
    with open(outputPath,"a") as jsonOutput:
        jsonOutput.write("{\n")        
        for jsonFile in jsonPath[:-1]:
            with open(jsonFile,"r") as jsonInput:
                for line in jsonInput:
                    jsonOutput.write(line)
                jsonOutput.write(",\n")
        
        for jsonFile in jsonPath[-1:]:
            with open(jsonFile,"r") as jsonInput:
                for line in jsonInput:
                    jsonOutput.write(line)
                jsonOutput.write("\n")

        jsonOutput.write("}")            

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def movefileToCurrentDirectory(sourceDirectory,sourcefile,destinationDirectory,destinationFile):
    inputPath = os.path.join(sourceDirectory,sourcefile)
    outputPath = os.path.join(destinationDirectory,destinationFile)
    if DEBUG: print("[movefileToCurrentDirectory] Moving "+inputPath+" to "+outputPath+" ...")
    if os.path.exists(inputPath):
        if os.path.exists(outputPath):
            os.remove(outputPath)
            if DEBUG: print("[movefileToCurrentDirectory] "+outputPath+" already exist, removing it before moving new one...")
        shutil.move(os.path.join(sourceDirectory,sourcefile),os.path.join(os.getcwd(),destinationFile))
    else:
        print("==========>[ERROR][movefileToCurrentDirectory] file <" + inputPath + "> does not exist !")    

def getFileListFromDir(directory):
    jsonList = []
    if os.path.exists(directory):
        for files in os.listdir(directory):
            filePath = os.path.join(directory, files)
            jsonList.append(filePath)
        return jsonList

    else:
        print("==========>[ERROR][getFileListFromDir] directory <" + directory + "> does not exist !")

def clear(*directories):
    toClear =  [x for x in directories]
    print("[clear] Cleaning directories..." )
    for y in toClear:    
        if os.path.exists(y):
            for files in os.listdir(y):
                os.remove(os.path.join(y, files))
            os.rmdir(y)
        else:
            print("==========>[ERROR][clear] directory <" + y + "> does not exist !")

def retrieveMovieData(outputPath,movie):    
    with open(outputPath, "w") as f_out:
        try:
            f_out.write(response['title']+'\n')
            f_out.write(str(response['year'])+'\n')
            f_out.write(response['cover url']+'\n')
            f_out.write(response['full-size cover url']+'\n')
            f_out.write(response['kind']+'\n')
                        
            for genre in response['genres']:
                f_out.write(genre + '|')
            f_out.write('\n')
                        
            f_out.write(str(response['rating'])+'\n')
                        
            for director in response['director']:
                f_out.write(director['name']+ '|')
            f_out.write('\n')
                        
            for writer in response['writer']:
                f_out.write(writer['name']+ '|')
            f_out.write('\n')
                        
            for cast in response['cast']:
                f_out.write(cast['name'] + '|')
            f_out.write('\n')
        except:
            print("==========>[WARNING][XXXXXXXXXXXXXXX] Required field is missing ! \""+movie+"\" scrapping is aborted. Continue...")
            f_out.close()
            os.remove(outputPath)

def createJSON(outputDirectory, file):
    if DEBUG: print("[createJSON] generating \""+file+"\" JSON file ...")
    if os.path.exists(outputDirectory):
        with open(file) as f_in:
           
            name = f_in.readline()
            year = f_in.readline()
            url = f_in.readline()
            bigurl = f_in.readline()
            kind = f_in.readline()
            
            genre = [x for x in f_in.readline().split('|') if x != '\n']
            rating = f_in.readline()
            director = [x for x in f_in.readline().split('|') if x != '\n']
            writer = [x for x in f_in.readline().split('|') if x != '\n']
            cast = [x for x in f_in.readline().split('|') if x != '\n']
            outputPath = os.path.join(outputDirectory,file)
            with open(outputPath) as f_out:
                f_out.write('{\n')
                f_out.write("\"name\" : {\n")
                f_out.write("},\n")
                f_out.write("\"year\" : {\n")
                f_out.write("},\n")
                f_out.write("\"name\" : {\n")
                f_out.write("},\n")   # to continue...................................
                f_out.write("\"year\" : {\n")
                f_out.write("},\n")
                f_out.write("\"name\" : {\n")
                f_out.write("},\n")
                f_out.write("\"year\" : {\n")
                f_out.write("},\n")
                
                # to continue...................................            
            
    else:
        print("==========>[ERROR][createJSON] directory <" + outputDirectory + "> does not exist !")
        print("Aborting...")
        sys.exit(1)

if __name__ == '__main__':
    #==========================================
    #Define var (ONLY THING THAT CAN BE EDITED)
    DEBUG = False
    TEMP_DIR = "tmp"
    JSON_DIR = "json"
    JSON_FILE = "output.json"
    OUTPUT_DIR = "output"
    #==========================================
    
    # check arguments
    if ((len(sys.argv) != 2)):
        print("Error, usage is: python {0} <input_path>".format(sys.argv[0]))
        sys.exit(1)
    else:
        PATH = sys.argv[1]
        checkPath(PATH)
        fileList = getFileListFromDir(PATH)
        cleanSubdirectory(TEMP_DIR)
        for file in fileList:
            file = os.path.basename(file)
            # remove extension .xxx
            movie = removeExtension(file)
            id = imdbRequest(movie)
            
            if id is not None:
                tmp_file = get_random_string(16)
                outputPath = os.path.join(TEMP_DIR,tmp_file)
                imdb = IMDb()
                response = imdb.get_movie(str(id))
                #tags = [ 'title', 'year', 'cover url','full-size cover url','kind', 'genres','plot', 'plot outline','synopsis', 'rating','director', 'writer','cast']
                retrieveMovieData(outputPath,movie)

        
        fileList = getFileListFromDir(TEMP_DIR)
        cleanSubdirectory(JSON_DIR)
        for file in fileList:
            createJSON(JSON_DIR,file) # to continue...................................
        fileList = getFileListFromDir(JSON_DIR)
        #concatJSON(fileList,OUTPUT_DIR,JSON_FILE)
        #movefileToCurrentDirectory(OUTPUT_DIR,JSON_FILE,os.getcwd(),JSON_FILE)
        #clear(TEMP_DIR,JSON_DIR,OUTPUT_DIR)                           
            
                        



