'''
Author: Zhengxiang (Jack) Wang 
Date: 2021-06-22 
GitHub: https://github.com/jaaack-wang 
About: The current scripts scrapes Chinese Names from http://www.resgain.net/xmdq.html 
'''

import requests
import re
from bs4 import BeautifulSoup as bs
from threading import Thread
from time import time


def getHTML(url, headers=None):
    '''
    Paras:
        url: str --> a url link
        headers: settings for headers in dict format. By default = None.
    Returns: the html content of a url; or False if the url is invalid. 
    '''
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.content
    else:
        print(f'【{url}】 is not working!')
        return False

    
def getMetaData(url, headers=None):
    '''
    Returns the following three lists:
        1. Chinese last names
        2. Counts of different full names associated with the last names
        3. The links to full names associated with the last names
    '''
    html = getHTML(url, headers=headers)
    if html:
        soup = bs(html, 'lxml')
        names = soup.select('body > div.main_ > div > div > div > a')
        lastNames = []
        counts = []
        links = []
        for name in names:
            ln = re.search(r'.+(?=姓名字大全)', name.string)
            lastNames.append(ln.group())
            cts = re.search(r'\d+', name['title']).group()
            counts.append(int(cts))
            links.append('http:' + name['href'])
        return lastNames, counts, links        


def getNameLinksByGender(lname_link):
    '''
    Generates all the possible links to names related to a specific last name by gender.
    It turns out that for each name category, there are at most 18 webpages available even when 
    the number of full names related to a last name is much larger than that. One way to get as 
    many names as possible is thus to get full names by gender. 
    ----------------
    Paras:
        lname_link: a link related to a last name extracted from getMetaData
    Return: two list of links of two genders
    '''
    boy = lname_link.replace('_list', '/boys_{}')
    girl = lname_link.replace('_list', '/girls_{}')
    boy_links = []
    girl_links = []
    for i in range(1, 19):
        boy_links.append(boy.format(i))
        girl_links.append(girl.format(i))

    return boy_links, girl_links
    


def getFullNames(urls, headers=None):
    '''
    Paras: 
        urls: list --> a list of urls
    Returns:
        list --> a list of full names in given webpages.   
    '''
    fullnames = []
    for url in urls:
        html = getHTML(url, headers=headers)
        if html:
            soup = bs(html, 'lxml')
            names = soup.select('body > div.main_ > div > div > div > div')
            fullnames.extend([name.div.string for name in names[:-1]])
            
    return fullnames
    

def getFirstNames(fullName, lastName):
    '''
    Works for names where last name comes first and there is no space
    between the first name and the last name. 
    ----------------
    Paras:
        fullName: str or list
        lastName: str
    ----------------
    Return:
        firstNames: str or list
    '''
    firstName = lambda fullName, lastName: fullName[len(lastName):]
    if isinstance(fullName, list):
        return list(map(firstName, fullName, [lastName] * len(fullName)))
    
    elif isinstance(fullName, str):
        return firstName(fullName, lastName)
    
    else:
        raise ValueError('fullName should be either list or str')


def nameInfoWriter(lname, lname_link, writer, template):
    '''
    Write the following information into a file：
        1. Last Name
        2. First Name
        3. Full Name
        4. Gender
    Paras:
        lname: str --> last name
        lname_link: str --> link related to the last name
        writer: f = open(filename, 'w')
        template: formatted string for writing a file
    '''
    boy_links, girl_links = getNameLinksByGender(lname_link)
    # get male's first names and full names
    boy_fullnames = getFullNames(boy_links)
    boy_firstnames = getFirstNames(boy_fullnames, lname)
    # get female's first names and full names
    girl_fullnames = getFullNames(girl_links)
    girl_firstnames = getFirstNames(girl_fullnames, lname)
    
    # -------writing name info----------
    f = writer
    # writing male's name info
    for i in range(len(boy_fullnames)):
        f.write('\n')
        f.write(template.format(lname, boy_firstnames[i], boy_fullnames[i], 'M'))
    # writing female's name info
    for i in range(len(girl_fullnames)):
        f.write('\n')
        f.write(template.format(lname, girl_firstnames[i], girl_fullnames[i], 'F'))
    print(f'Finish writing name info related to {lname}...')
    
    
def main():
    url = 'http://www.resgain.net/xmdq.html'
    # Get the last names, counts of unique full names related with the last times, and the links
    lastNames, counts, links = getMetaData(url)
    # 中国人名信息库 = Chinese Name Info Corpus
    f = open('中国人名信息库.txt', 'w')
    template = '{}\t{}\t{}\t{}'
    f.write(template.format('姓', '名', '全名', '性别'))
    end_idx = len(lastNames)
    for i in range(0, end_idx, 10):
        # multithreading conducted batch by batch to avoid losing connections 
        threads = []
        for idx in range(i, i + 10 if i+10<=end_idx else end_idx):
            t = Thread(target=nameInfoWriter, args=(lastNames[idx], links[idx], f, template,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    f.close()
##    
    # writing the metadata
    template = '{}\t{}\t{}'
    # 元数据 = metadata
    with open('元数据.txt', 'w') as f:
        f.write(template.format('姓', '姓名数', '链接'))
        for i in range(len(lastNames)):
            f.write('\n')
            f.write(template.format(lastNames[i], counts[i], links[i]))
        f.close()
        

if __name__ == '__main__':
    s = time()
    main()
    e = time()
    print("Total time: " + str(e - s))
