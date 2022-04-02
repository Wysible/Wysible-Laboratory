'''
    @Author: Nishanth
    @Date: 02-04-2022 22:32:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 22:32:00
    @Title: Retrieving top result from google for a search string
'''
from googlesearch import search

def search_result(search_string: str):
    """
        Description:
            Retieves search results for the search string
        
        Parameters:
            Search string as str
        
        Return:
            None
    """
    for j in search(search_string, tld="com", num=10, stop=5, pause=1):
        print(j)


if __name__ == '__main__':
    search_result("lucene")