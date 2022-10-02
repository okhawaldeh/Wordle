#needed lib: requests, beautifulsoup4, html.parser

#from turtle import clear
import requests
from bs4 import BeautifulSoup

#prints out nice HTMLclea
#print(soup.prettify())

def definition_finder():
    url_wordle = "https://www.tomsguide.com/news/what-is-todays-wordle-answer"

    #calls the requests lib
    resultW = requests.get(url_wordle)

    #make sure wesbite is accessible, should return 200
    #print(result.status_code)

    #creates a var of all the content of the website
    srcW = resultW.content
    #print(src)

    #create a soup object of the source
    soupW = BeautifulSoup(srcW, 'lxml')

    #takes out the links and prints them
    tagsW = soupW.findAll('strong')[1]
    #print(tagsW.string)

    #words =[] #list of the words inside tag strong
    wordle = tagsW.string #the wordle of the day

    #appends the words inside the tag
    #for tag in tagsW.string.split():
    #    words.append(tag)

    #finds the wordle by looking after string "is"
    #for i in range(len(words)):
    #    if(words[i] == "is"):
    #        wordle = words[i + 1]
            
    #print(wordle)

    url_def = "https://www.vocabulary.com/dictionary/" + wordle
    resultD = requests.get(url_def)
    #print(resultD.status_code)

    srcD = resultD.content
    soupD = BeautifulSoup(srcD, 'lxml')

    #finds the specific line using its tag
    tagD = soupD.find_all('div', attrs={'class': 'definition'})
        
    lines =[] #list of the words inside tag strong
    definition = "" #definition string

    #appends the words inside the tag
    for tag in tagD[0].get_text().split():
        lines.append(tag)

    #putting it together in a string
    for i in range(len(lines)):
        if i == 0:
            definition += lines[i]
            definition += ":"
        else:
            definition = definition + " " + lines[i]
    definition+= "."

    return(definition)


def main():
    print(definition_finder())

if __name__ == "__main__":
    main()

