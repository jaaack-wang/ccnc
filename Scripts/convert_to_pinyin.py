'''
Author: Zhengxiang (Jack) Wang 
Date: 2021-06-23 
GitHub: https://github.com/jaaack-wang 
About: Convert the Comprehensive Chinese Name Corpus (CCNC) into 
its pinyin version (with or without tones).
'''


import json
from pypinyin import pinyin, lazy_pinyin


def convert_to_pinyin(filepath, tone=False):
    '''
    Converts and writes the name corpus into a pinyin version of file
    Paras:
        tone: bool, by default = False
    '''
    nameInfo = open(filepath, 'r')
    # skip the header
    next(nameInfo)
    
    if not tone:
        fileName = 'ccnc_pinyin.txt'
        # loading the last names' pinyins
        ln_py = json.load(open('ChineseLastNamesNoTones.json', 'r'))
        # define the pinyin method 
        pyin = lambda string: ''.join(lazy_pinyin(string))
    else:
        fileName = 'ccnc_pinyin_with_tones.txt'
        ln_py = json.load(open('ChineseLastNamesWithTones.json', 'r'))
        pyin = lambda string: ''.join(i[0] for i in pinyin(string))
        
    
    # creating and writing pinyin version of the file
    f = open(fileName, 'w')
    template = '{}\t{}\t{}\t{}'
    f.write(template.format('Last Name', 'First Name', 'Full Name', 'Gender'))
    f.write('\n')
    
    for line in nameInfo:
        line = line.split('\t')
        lastName = line[0]
        firstName = line[1]
        gender = line[-1]
        
        # converting pinyin 
        lastName = ln_py[lastName].replace(' ', '')
        firstName = pyin(firstName)
            
        f.write(template.format(lastName, firstName, lastName + ' ' + firstName, gender))
    
    f.close()
    print(fileName + ' is saved!')
