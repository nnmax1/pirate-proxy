import feedparser

def rssParse(url):
    rss_data= feedparser.parse(url)
    response = []
    for i in range(0, len(rss_data.entries)):
        entry = rss_data.entries[i]
        data = {}
        data['title']=entry.title
        data['link'] =entry.link
        response.append(data)
        i = i+1
    return response





