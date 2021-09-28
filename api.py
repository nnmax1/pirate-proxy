import feedparser

def TPB_rss(url):
    tpb_data= feedparser.parse(url)
    response = []
    for i in range(0, len(tpb_data.entries)):
        entry = tpb_data.entries[i]
        data = {}
        data['title']=entry.title
        data['link']=entry.guid
        data['magnetLink'] =entry.link
        response.append(data)
        i = i+1
    return response


