# import library used to query wikipedia
import urllib

# specify wikipedia url
wiki="https://en.wikipedia.org/wiki/2017%E2%80%9318_Premier_League"

from bs4 import BeautifulSoup
soup = BeautifulSoup(wiki, 'html.parser')















#import the Beautiful soup functions to parse the data returned from the website
#from bs4 import BeautifulSoup



#Query the website and return the html to the variable 'page'
#page = urllib.urlopen(wiki)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
#soup = BeautifulSoup(page)

#print(soup.prettify())
