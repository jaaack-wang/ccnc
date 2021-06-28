[中文版见这里](https://github.com/jaaack-wang/ccnc/blob/main/README.md) 

## Basic statistics
| # of names | # of last names ) | # of first names)| # of M| # of F | # of Unknown gender|
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3658109 | 808 | 710594 | 2054134 | 1509650 | 94325 |

sample image (pinyin version)：<br><br>
 <img align="center" width='500' height='250' src="https://github.com/jaaack-wang/ccnc/blob/main/sample_img_en.png">

## Pinyin Version
Due to the large size of the original files, this repository does not store any Pinyin version of the corpus (CCNC). You can click 
[here](https://drive.google.com/file/d/1Y7INZUv98JFuI09MleZcpiaxqiqTdlUN/view) to download the three versions of CCNC (Chinese, Pinyin with tones & Pinyin without tones) in a zip file. 


## Sources
CCNC is compiled from the following two sources:
 - [姓名大全](http://www.resgain.net/xmdq.html), which provides 2513097 examples. [ Scraping Script](https://github.com/jaaack-wang/ccnc/blob/main/Scripts/namescraping.py)
 - [中文人名语料库](https://github.com/wainshine/Chinese-Names-Corpus), which provides 1145012 examples.

Things to note：
- 中文人名语料库 does not differentiate between last names and first names, but CCNC does. 
- There were about 300k overlapping examples that have been filtered. 
- However, if a same name is shared among different genders, the name will be deemed as unique for each gender. 
- All the names with unknown genders come from 中文人名语料库. 

## Romanized Chinese Last Names Dictionary (i.e., Ch-Last-Names-Dict)
The dictionary collects 1606 Chinese last names along with their Pinyins and 1534 of them were scraped from [名霸百家姓](http://bjx.mingba.cn)，
the other 72 rare last names come from the corpus and were annotated with Pinyin by myself. These self-annotated last names include: 滕, 刁, 牧, 欧阳, 徐离, 傲, 宾, 博, 采, 恩, 凡, 格, 冠, 好, 昊, 浩, 荷, 恒, 鸿, 湖, 化, 基, 继, 见, 杰, 静, 菊, 俊, 卡, 科, 奎, 立, 丽, 刘付, 绿, 麦, 曼, 美, 梦, 名, 默, 沐, 娜, 乃, 尼, 日, 如, 润, 若, 上, 升, 桃, 天, 拓, 旺, 未, 溪, 夏候, 湘, 晓, 雄, 雅, 岩, 彦, 艳, 依, 远, 悦, 忠, 珠。
## Train/dev/test set
Here is a simple [script](https://github.com/jaaack-wang/ccnc/blob/main/Scripts/train_dev_test_split.ipynb) to split CCNC into train, dev and test sets. The default splitting ratio is 6:2:2，and this is the split CCNC compressed in [a sample zip file] (https://drive.google.com/file/d/1z06MpC1Q0kKjVjCyUtmb2crpSsJ_Tjl4/view) for the pure Chinese version. You can also apply the script to the Pinyin versions and get similar results.  
