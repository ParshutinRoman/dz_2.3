

import chardet
import json
from pprint import pprint
from collections import Counter
path = "/Users/admin/Desktop/netology/PY/dz_2.3"
files = (('newsafr.txt', 'newsafr.json'), ('newscy.txt', 'newscy.json'), ('newsfr.txt', 'newsfr.json'),
         ('newsit.txt', 'newsit.json'))

for file in files:
    with open(file[0], 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    with open(file[1], encoding=result['encoding']) as data_file:
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

