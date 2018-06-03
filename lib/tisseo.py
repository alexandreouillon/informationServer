import feedparser
from bs4 import BeautifulSoup

class TisseoRSS():
    def __init__(self):
        self.tisseoRSS = feedparser.parse('https://www.tisseo.fr/infos-reseau/feed')
        
    def get_guid(self, id):
        return str(self.tisseoRSS.entries[id].guid).split(" ")[0]

    def get_title(self, id):
        return self.tisseoRSS.entries[id].title

    def get_description(self,id):
        description = str(self.tisseoRSS.entries[id].description)
        description = description.replace("<br />","\n")
        return description
    
    def printLastInformation(self):
        print(self.get_title(0), self.get_description(0))


