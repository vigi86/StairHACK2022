import spider

#print(getSoupPerUrl(url))
# TODO: feed with correct urls
url = 'https://www.cbsnews.com/health/'

# how to use getRelevantUrls
interestedIn = ["cbsnews"]
notInterestedIn = ["twitter"]

relevantUrls = spider.getRelevantUrls(spider.getSoupPerUrl(url), interestedIn, notInterestedIn)
for relevantUrl in relevantUrls:
    print(relevantUrl)