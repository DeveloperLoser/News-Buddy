from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='232c2cbfd9f84018abcce502d1dc640e')

def getSources():
    sources = newsapi.get_sources()
    savedsources = open("sources.txt", 'w')
    savedsources.writelines(sources)

if __name__ == "__main__":
    getSources()