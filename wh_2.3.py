import chardet
import json
from collections import Counter

files = ('newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json')


for file in files:
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    with open(file, encoding=result['encoding']) as data_file:
        data = json.load(data_file)
        text = data['rss']['channel']['items'][1]['description']
        words = text.split(' ')
        words_short = []
        for word in words:
            if len(word) > 6:
                words_short.append(word)
        words_short.sort()
        count = Counter(words_short)
        print('топ 10 самых часто встречающихся слов длиннее 6 символов:', count.most_common(10))

