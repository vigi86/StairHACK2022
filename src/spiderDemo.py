import spider

#print(getSoupPerUrl(url))
url = 'https://www.cbsnews.com/health/'

# how to use getRelevantUrls
interestedIn = ["facebook"]
notInterestedIn = ["twitter"]

relevantUrls = spider.getRelevantUrls(spider.getSoupPerUrl(url), interestedIn, notInterestedIn)
for relevantUrl in relevantUrls:
    print(relevantUrl)