htmlString1 = '''<article id="animals">

        <h1 class="main-heading">Nature's Wonders</h1>
        <p>In this article we discuss animals.</p>

        <section id="birds">
                <h2 class="favourite">Birds</h2>
                <p>
                        Forest is a wonderful place to see birds.
                </p>
        </section>

        <section id="butterflies">
                <h2>Butterflies</h2>
                <p>
                    Butterflies possess some of the most striking colour
                    displays from nature.
                </p>
        </section>

</article>'''


def getTagContentF(HTMLstring, HTMLtag):
    HTMLfound_l = []
    HTMLlist = HTMLstring.splitlines()
    HTMLlist = list(map(str.lstrip, HTMLlist))
    HTMLlist = list(map(str.rstrip, HTMLlist))
    ostatak = ''.join(HTMLlist)
    print(ostatak)
    kraj = False
    while not kraj:
        try:
            start = ostatak.index('<' + HTMLtag)
            end = ostatak.index('</' + HTMLtag + '>')
            HTMLfound = ostatak[start:end]
            start1 = HTMLfound.index('>')+1
            HTMLfound = HTMLfound[start1:]
            HTMLfound_l.append(HTMLfound)
            ostatak = ostatak[end + 3 + len(HTMLtag):]
        except ValueError:
            kraj = True
    return HTMLfound_l

input_tag = input('Unesite tag: ')
print(getTagContentF(htmlString1, input_tag))
