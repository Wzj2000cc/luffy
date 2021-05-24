import requests
from lxml import etree
import pyttsx3
engine = pyttsx3.init()
import re


url='http://www.duanziwang.com/t/5bCP56yR6K%2Bd.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
response=requests.get(url=url,headers=headers).text
tree=etree.HTML(response)
dl_list=tree.xpath('//div[@class="nr"]/dl')
for dl in dl_list:
    title=dl.xpath('./span/dd/a/strong/text()')[0]
    print(title)
    engine.say(title)
    engine.runAndWait()
    if dl.xpath('./dd/text()')!=[]:
        str=dl.xpath('./dd/text()')[0]
        print(str)
        engine.say(str)
        engine.runAndWait()
    else:
        str_list=dl.xpath('./dd/p[1]/font/text()')
        for str in str_list:
            print(str)
            engine.say(str)
            engine.runAndWait()
        str_list=dl.xpath('./dd/font/p/text()')
        for str in str_list:
            print(str)
            engine.say(str)
            engine.runAndWait()