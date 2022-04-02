'''
    @Author: Nishanth
    @Date: 02-04-2022 22:32:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 22:32:00
    @Title: Retrieving top result from google for a search string
'''
from googlesearch import search

def search_result(search_string: str) -> list:
    """
        Description:
            Retieves search results for the search string
        
        Parameters:
            Search string as str
        
        Return:
            Top 3 results as list
    """
    links = []
    for j in search(search_string, tld="com", num=10, stop=5, pause=0.0005):
        print(j)
        links.append(j)
    
    print("Top 3 links:")
    print(links[0]+'\n'+links[1]+'\n'+links[2])
    return links[0:3]

if __name__ == '__main__':
    search_result("lucene")