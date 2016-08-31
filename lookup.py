def add_to_index(index,keyword,url):
    # format of index has been altered to include the count of urls: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls == entry[1]:
                    return
                entry[1].append([url,0])
                return
        index.append([keyword,[url, 0]])

def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] += 1

def lookup(index,keyword):
    output = []
    for entry in index:
        if entry[0] == keyword:
            output.append([entry[1]])
            return

def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])

