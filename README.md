[English Version of ReadMe](https://github.com/jaaack-wang/ccnc/blob/main/README_EN.md)

## 基本数据 (Basic statistics)
| 姓名数 (names) | 姓的数量 (last names ) | 名的数量 (first names)| 男性数量 (M)| 女性数量 (F) | 未知性别 (Unknown)|
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3658109 | 808 | 710594 | 2054134 | 1509650 | 94325 |

样图：<br><br>
 <img align="center" width='500' height='250' src="https://github.com/jaaack-wang/ccnc/blob/main/sample_img_ch.png">

## 拼音版 (Pinyin Version)
由于源文件比较大，这里提供用于为语料库注音的[源码](https://github.com/jaaack-wang/ccnc/blob/main/Scripts/convert_to_pinyin.py)。运行源码前，你必须首先将[Ch-Last-Names-Dict](https://github.com/jaaack-wang/ccnc/tree/main/Ch-Last-Names-Dict)中的两个json文件下载下来，并与源码放置于同一个文件夹下。或者，你也可以点击[这里](https://drive.google.com/file/d/1Y7INZUv98JFuI09MleZcpiaxqiqTdlUN/view?usp=sharing)下载本语料库的三个版本（纯中文版，两个拼音版，一个有声调，另外一个没有声调)。

拼音版的姓，用我自己制作的中文姓氏注音字典标注的；而名的拼音则直接用[pypinyin](https://github.com/mozillazg/python-pinyin)。分开注音的主要原因是，pypinyin对一些罕见姓氏的注音并不很准确。当然，由于某些姓氏可能有多种读音，完全正确的注音是不可能。

做拼音版的主要想法是，拼音版可以用来做英文文献中中文人名(不包括港澳台，这些地方的中文名转英文的规则不一样。)的实体识别。拼音版的全名中，姓和名都用空格隔开。

## 来源 (Sources)
语料库来自以下两个渠道:
 - [姓名大全](http://www.resgain.net/xmdq.html), 贡献了2513097条语例。[抓取代码/Script](https://github.com/jaaack-wang/ccnc/blob/main/Scripts/namescraping.py)
 - [中文人名语料库](https://github.com/wainshine/Chinese-Names-Corpus), 贡献了1145012条语例。

另外需要注意的是：
- 中文人名语料库的姓名原本不分，这里做了区分。
- 两个来源大约有三十万的重叠语例，都被删减掉了。
- 两个人如果姓名一样，但是性别不一样，在这里也当作两个不同的语例来处理。
- 本语料库的未知性别语例均来自于第二个来源，即中文人名语料库。

## 中文姓氏注音字典 (Romanized Chinese Last Names Dictionary)
中文姓氏拼音字典收集了1606条中文姓氏及其拼音。其中1534条姓氏及其注音抓取自[名霸百家姓](http://bjx.mingba.cn)，剩下的72条则见于本语料库的具体语例，并由我自己手动注音，包括：滕, 刁, 牧, 欧阳, 徐离, 傲, 宾, 博, 采, 恩, 凡, 格, 冠, 好, 昊, 浩, 荷, 恒, 鸿, 湖, 化, 基, 继, 见, 杰, 静, 菊, 俊, 卡, 科, 奎, 立, 丽, 刘付, 绿, 麦, 曼, 美, 梦, 名, 默, 沐, 娜, 乃, 尼, 日, 如, 润, 若, 上, 升, 桃, 天, 拓, 旺, 未, 溪, 夏候, 湘, 晓, 雄, 雅, 岩, 彦, 艳, 依, 远, 悦, 忠, 珠。

中文姓氏博大精深。通过构建这个姓氏注音字典，我第一次了解到有的人姓：第，第一，第三，第四，第五，第六，第七，第八...稍微以某字 + “姓“查了下百度，罕见的姓确实能罕见得超乎想象。

## 训练集/测试集/预测集 (train/dev/test set)
这里提供一段简单的[代码](https://github.com/jaaack-wang/ccnc/blob/main/Scripts/train_dev_test_split.ipynb)将ccnc语料库切分成训练集，测试集和预测集。默认的切分比例为6:2:2，[这个](https://drive.google.com/file/d/1z06MpC1Q0kKjVjCyUtmb2crpSsJ_Tjl4/view)是针对全汉字版的已经切分好的压缩文件。切分两个拼音版的语料库可以如法炮制。
