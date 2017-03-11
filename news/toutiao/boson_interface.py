##coding=utf-8
__author__ = 'shifeixiang'

import json
import requests
from bs4 import BeautifulSoup


def test_emotion():
    SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
    # 注意：在测试时请更换为您的API Token
    headers = {'X-Token': 'B10dxhtR.13489.BjImZQNV6D6K'}

    s = ['他是个英雄', '美好的世界']
    data = json.dumps(s)
    resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))

    print(resp.text)

def test_emotion():
    word = '和平'
    url = 'https://zh.wikipedia.org/wiki/' + str(word)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html)
    contents = soup.find(id='bodyContent').stripped_strings
    tmp_list = ""
    for content in contents:
        tmp_list  = tmp_list + content

    print tmp_list

def test_keyword():
    KEYWORDS_URL = 'http://api.bosonnlp.com/keywords/analysis'


    text = '''
    安徽商报 合肥网 无线合肥讯 1岁半男婴，腹部膨胀阵疼，无其他过多症状，经省儿童医院医生精确诊断，竟然为罕见的寄生胎，发病几率为五十万分之一。 3月6日，省儿童医院普外二科成功为一名小患儿实施手术，为其摘除了腹中的寄生胎。
配图
一岁半男童经常腹痛
小墨墨(化名)今年1岁6个月大，砀山人。 5个月前，家人发现小墨墨腹部膨胀，随后带他到当地医院就医。由于小墨墨无腹痛，无发热、无呕吐，大小便正常，当地医院考虑，小墨墨可能为“漏斗胸”，未予特殊处理及检查。今年2月28日，小墨墨出现腹痛，但是没有发热、无血便，伴随呕吐。 3月3日，小墨墨的家人带着小墨墨，到安徽省儿童医院就诊。“我们最初在当地县级院做了检查，医生怀疑是疝气。”小墨墨的奶奶说，经过打听，他们听说周口有家疝气专科医院比较好，就带孩子到了周口。后来，麻醉针都打过了，孩子准备做手术之时，医生觉得不对劲，就停了下来。建议到周口另外一家医院做检查。后B超显示，孩子肚子里面有肿块，怀疑是肿瘤，周口当地医院的医生建议，把小孩赶紧送往安徽省儿童医院。
肚子大因有“寄生胎”
“孩子肚里有肿瘤”，一家人都吓蒙了。墨墨的爷爷朱锁银说，孩子自出生到现在，一直很健康，就肚子稍大些，吃饭非常好，长得也比较胖。听到这个消息后，家人一点都不敢耽搁，立即通知远在杭州打工的墨墨父亲赶紧赶回家，带着孩子来到省儿童医院。
在省儿童医院，B超检查显示，小墨墨腹腔内有巨大房囊性包块，右侧精索鞘膜积液，初诊医生考虑，患儿可能肠系膜淋巴管瘤，建议住院进一步治疗。
省儿童医院普外二科副主任未德成介绍，小墨墨入院后，他在检查中发现，小墨墨中上腹可和右侧腹股沟有包块。经过进一步判定，未德成认为，小墨墨腹内可能有寄生胎，建议手术。
手术成功孩子将出院
未德成介绍，此次手术的最大难点在于寄生胎周围的血管供应复杂，寄生胎位于腹膜后，多条重要的动脉血管与正常孩子脏器相连，损伤任何一条都将造成不可估量的后果。经过1个半小时的精细手术，寄生在小墨墨腹内的寄生胎成功取出。寄生胎除头部、心脏未发育完全外，四肢、躯干、骨盆等均隐约可见。目前，小墨墨手术非常成功，寄生胎取出后，一切恢复良好，即将康复出院。
啥叫“寄生胎”？
未德成介绍，寄生胎是指母体内卵裂过程中，受精停止发育而寄生在另一个健康发育的正常体内，是一种罕见的先天性疾病，遗传学上又称“胎内胎”，发病几率为五十万分之一。寄生胎大多在婴幼儿时即被发现，像小墨墨这样，经过一年多才发现，也是不多见的。
    '''
    params = {'top_k': 10}
    data = json.dumps(text)
    headers = {'X-Token': 'B10dxhtR.13489.BjImZQNV6D6K'}
    resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))


    for weight, word in resp.json():
        print(weight, word)


if __name__ == '__main__':
    test_keyword()