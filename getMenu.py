#import libraries
import urllib.request
from bs4 import BeautifulSoup

def setPageURL():
    # url to get the menu from
    symantecPageURL = 'http://www.aramarkcafe.com/layouts/canary_2015/locationhome.aspx?locationid=3072&pageid=20&stationID=-1'

    # use urllib2 to query the page and return the html
    pageHTML = urllib.request.urlopen(symantecPageURL)

    # parse the html using bs4
    soup = BeautifulSoup(pageHTML, 'html.parser')

    return soup

def getMenuForEachDay(soup):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    foodOnDay = dict.fromkeys(days, 0)

    # get the items for a certain day
    day = 'monday'
    dayColumn = soup.find('div', id=day+'Column')

    for day in foodOnDay:
        foodOnDay[day] = dayColumn

    return foodOnDay


if __name__=="__main__":
    soup = setPageURL()
    allMenus = getMenuForEachDay(soup)
    exitFlag = True
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    while(exitFlag):
        userInput = input("Pick a day of the week or a number 1-5\n").lower()

        if userInput in allMenus:
            print(allMenus[userInput].prettify())
        elif int(userInput) >= 1 and int(userInput) <= 5:
            print(allMenus[days[int(userInput)]].prettify())
        elif userInput.lower() == "exit":
            exitFlag = False
            print("GoodBye!")
        else:
            print("Input invalid, please enter a day of the workweek or a number 1-5")
        
