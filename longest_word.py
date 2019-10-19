def longest_word(url):

    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    final = []
    bigger = 0
    with open("words", "r") as f:
        c = f.readlines()
        c = [s.strip() for s in c]
        c = set(c)
        for i in html.split():
            if i in c:
                if len(i) == bigger:
                    bigger = len(i)
                    final.append(i)
                elif len(i) > bigger:
                    bigger = len(i)
                    final = [i]
    for i in list(set(final)):
        return i