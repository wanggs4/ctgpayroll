from urllib import request
import re
import json

class Spider():

    url='https://baike.baidu.com/usercenter/userpage?uname=%E7%A2%8E%E6%A2%A6%E5%A4%A7%E9%81%93%E4%B8%9C&from=diff'
    root_pattern='<meta name="Description"([\w\W]*?)<strong>参考文献</strong>'
    name_pattern='</i>([\w\W]*?)</span>'
    number_pattern='<i class="ricon ricon-eye"></i>([\w\W]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url,)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
        print(htmls)

    def __pachong(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for root in root_html:
            name = re.findall(Spider.name_pattern,root)
            number = re.findall(Spider.number_pattern,root)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        print(root_html[0])
        return anchors
        # a =1

    def __refine(self,anchors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l,anchors)

    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            # print(anchor['name'] + '-----'+anchor['number'])
            print('rank' +str(rank + 1)
                  + ':' + anchors[rank]['name']
                  + ':' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors =self.__pachong(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        anchors = self.__show(anchors)


spider = Spider()
spider.go()

