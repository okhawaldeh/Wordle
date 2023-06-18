#needed lib: requests, beautifulsoup4, html.parser

#from turtle import clear
import requests
from bs4 import BeautifulSoup

#prints out nice HTMLclea
#print(soup.prettify())

def definition_finder():
    
    ####################finding the wordle####################
    url_wordle = "https://www.tomsguide.com/news/what-is-todays-wordle-answer"
    # url_wordle = "https://word.tips/todays-wordle-answer/"

    #calls the requests lib
    resultW = requests.get(url_wordle)

    #make sure wesbite is accessible, should return 200
    # print(resultW.status_code) 

    #creates a var of all the content of the website
    srcW = resultW.content
    #print(src)

    #create a soup object of the source
    soupW = BeautifulSoup(srcW,'html.parser')

    #find the strong tags and take the last one in the list
    tags = soupW.find_all('strong')
    tag = tags[len(tags)-1]
    
    #extract the wordle of the tag
    wordle = ""
    for i in tag:
        if i.isupper():
            wordle = wordle + i

    # print(wordle)

    ####################finding the definition####################
    url_def = "https://www.merriam-webster.com/dictionary/" + wordle
    resultD = requests.get(url_def)
    # print(resultD.status_code)

    srcD = resultD.content
    soupD = BeautifulSoup(srcD,'html.parser')

    # finds the specific line using its tag
    tagD = soupD.find("span", {"class": "dtText"}).get_text()

    # taking what we need from the string
    definition = tagD[2:len(tagD)]
    # print(definition)
    
    return(definition)

if __name__ == "__main__":
    print(definition_finder())
    # definition_finder()