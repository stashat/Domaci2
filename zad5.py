htmlString = '''
<h1 class atributttttybty  >        Stasa Tadic jede hleb   </h1> 
<p> Stasa je uradila domaci </p>

<h1> stasa </h1>
'''
'''if '<h1>' in htmlString:
    start = htmlString.index('<h1>') + len('<h1>')
    end = htmlString.index('</h1>', start)
    print(htmlString[start:end])'''

input_tag = input('Unesite tag: ')
iskorisceni = []
class Get_Html:
    def __init__(self, string, tag):
        self.tag = tag
        self.str = string



    def get_h1(self, tag):
        if self.tag=='h1':
            if '<h1' in self.str :
                start = self.str.index('h1') + self.str.index('>')
                end = self.str.index('</h1', start)
                return self.str[start:end].strip()
        else:
            print('nema h1 taga')

    def get_tag(self):
        tag_start = '<' + self.tag
        tag_end =  '</' + self.tag
        if tag_start in self.str :
            for tag_start in self.str:
                if ( (self.str.index(tag_start) and (self.str.index(tag_end) ) not in iskorisceni:
                    iskorisceni.append(self.str.index(tag_start))
                    iskorisceni.append(self.str.index(tag_end))
                    print(iskorisceni)
                    start = self.str.index(tag_start) + self.str.index('>')
                    print(start)
                    end = self.str.index(tag_end, start)
                    print(end)
                    return self.str[start:end].strip()
        else:
            print('nema taga')

htmlString = Get_Html(htmlString,input_tag)

print(htmlString.get_h1(input_tag))

print(htmlString.get_tag())

