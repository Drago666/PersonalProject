# Python code to find the URL from an input string

def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read()
    except:
        return ""
#The get_page function takes a url and converts it to HTML

import re

def find_url(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]
# Python code to find the URL from an input string




#def get_next_target(page):
#    start_link = page.index('<a href=')
#    if start_link == -1:
#        return None, 0
#    start_quote = page.index('"', start_link)
#    end_quote = page.index('"', start_quote + 1)
#    url = page[start_quote + 1:end_quote]
#    return url, end_quote

#get next target works given a list
def get_next_target(page):
    pageLength=len(page)
    if pageLength>0:

        return page[0],1
    return None, 0
#Union works
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#get all links does not work
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

#TBD
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    crawledLength=len(crawled)
    while tocrawl:
        page = tocrawl.pop()
        if crawledLength>10:
            break
        if page not in crawled:
            union(tocrawl, get_all_links(find_url(str(get_page(page)))))
            crawled.append(page)
    # import pandas as pd
    import pandas as pd

    # Calling DataFrame constructor on list
    df = pd.DataFrame(crawled, columns=["Links:"])
    column=df.to_string(index=False)
    return column


#Testing:

hyperlink=input("Which page would you like to crawl?")
#hyperlink="https://udacity.github.io/cs101x/index.html"
print(

)
#listed_Links=(find_url(str(get_page(hyperlink))))

print(crawl_web(hyperlink))
