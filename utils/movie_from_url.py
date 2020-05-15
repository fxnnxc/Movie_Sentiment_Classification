from bs4 import BeautifulSoup
import urllib.request as req


def getResponse(url):
    response = req.urlopen(url)
    data = response.read()
    soup = BeautifulSoup(data, "html.parser")
    # print(soup.prettify("utf-8"))
    return soup

def get_movie_name(genre):
    movieList = []

    url = "https://www.imsdb.com/genre/" + genre
    soup = getResponse(url)
    card_list = soup.find_all("a")
    canAppend = False
    for link in card_list:
        text = link.text.strip()

        if "Index" in text:
            canAppend =False
        if canAppend:
            movieList.append(text)
        if "ALL SCRIPTS" in text:
            canAppend =True

    return movieList


def get_movie_script(name):
    name = name.replace(' ', '-') + ".html"
    url = "https://www.imsdb.com/scripts/" + name
    soup = getResponse(url)
    card_list = soup.find("td", {'class': 'scrtext'})

    return card_list


import re

def store_data(genre, MAX):
    movieList = get_movie_name(genre)
    count =0
    for movie in movieList:
        try:
            script = get_movie_script(movie)
        except:
            print(movie, " is not possible May be no script")
        if len(str(script))> 3000:
            movie = re.sub('\W', '_', movie)
            with open('data/'+genre+"_"+movie+".txt", "w", encoding='utf-8') as g:
                g.write(str(script))
                g.close()
                print(genre, movie, " is stored")
                count += 1
        if count >= MAX:
            break


import argparse


def main():
    parser = argparse.ArgumentParser(description='Parser example')
    parser.add_argument('--num_genre', type=int, default=10, help='' )
    parser.add_argument('--num_movie', type=int, default=20, help='' )
    
    config = parser.parse_args()
    Genre = """
    Action	Adventure	Animation
    Comedy	Crime	Drama
    Family	Fantasy	Film-Noir
    Horror	Musical	Mystery
    Romance	Sci-Fi	Short
    Thriller War	Western
    """
    Genre = Genre.strip().split()
    if config.num_genre>len(Genre):
        config.num_genre = len(Genre)
    for genre in Genre[:config.num_genre]:
        store_data(genre,config.num_movie)

import os
if __name__ == "__main__":
    main()
    



