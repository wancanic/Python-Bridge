# @Time    : 2019/4/20 1:07
# @Author  : Noah
# @File    : regular_expression.py
# @Software: PyCharm
# @description: re module
import re

#######################################################################
#  .         =>          匹配除换行符之外的所有字符

#  \         =>          作用消除一个字符的特殊功能

#  [a-z]     =>          其中 - 表示字符选择的范围

#  {3}       =>          匹配字符个数

#  ()        =>          表示分组

#  ^         =>          匹配字符串开始位置，而在 [^a-z] 中 ^ 表示取反

#  $         =>          匹配字符串结束位置

#  |         =>          作用类似逻辑或操作

#  表示重复的元字符：
#               * => {0,}
#               + => {1,}
#               ? => {0,1}

# 贪婪 (在符合的条件下会尽量多的匹配) 和 非贪婪 (添加 ?)

# 反斜杠 + 普通字符 = 特殊字符：
#               \b 匹配单词边界                       |   \B

#               \d 匹配Unicode中定义数字字符           |   \D

#               \s 匹配任何空白字符：                  |   \S

#                           \t 表示tab键（制表键）
#                           \n 表示换行符
#                           \r 表示回车
#                           \f 表示换行符
#                           \v 表示垂直的tab键

#               \w 匹配Unicode中定义的单词字符         |  \W

#################################################################################
# 正则表达式标志的位置

#  'A' => 'ASCII'       =>      只能匹配ASCII字符

#  'S' => 'DOTALL'      =>      使 . 可以匹配任何字符并且包括换行符

#  'I' => 'IGNORECASE'  =>      匹配时不区分大小写

#  'L' => 'LOCALE'      =>      使用\w \W \b \B匹配时依赖当前的语言环境

#  'M' => 'MULTILINE'   =>      使 ^ 和 $ 可以匹配每一行的行首或者结尾位置

#  'X' => 'VERBOSE'     =>      使正则表达式写得更好看和更有条理
#                       =>      character = re.compile("""
#  &[ # ]
#  (
#       0[0-7]+
#       |[0-9]+
#       |x[0-9a-fA-F]+
#  );
#  """, re.VERBOSE)

#  'S' => 'Scanner',

#  'T' => 'TEMPLATE',

#  'U' => 'UNICODE',

#  'DEBUG'          =>          显示有关已编译表达式的调试信息

#################################################################################
#  'compile', => 编译正则表达式模式，返回一个对象的模式
pattern = re.compile('\d')

#  'findall',
p = re.findall(pattern, '1a2b3c4d5e')
print(p)  # => ['1', '2', '3', '4', '5']

#  'finditer',  =>  搜索string返回顺序访问每一个匹配结果<Match对象>的迭代器
p = re.finditer(r'\d+', '12 drumm44ers drumming, 11 ... 10 ...')
for i in p:
    print(i)
    print(i.group())
    print(i.span())

#  'fullmatch', =>  如果整个字符串匹配正则表达式模式，则返回一个match对象否则None
p = re.fullmatch(r'\d+', '123456789z')
print(p)  # => None

#  'match',     =>  如果在字符串的开头的零个或更多字符匹配正则表达式模式
p = re.match('http', 'http://www.python.org')
print(p)

#  'purge',     =>  清除正则表达式缓存

#  'search',    =>  扫描字符串寻找的第一个由该正则表达式模式产生匹配的位置
p = re.search('(?<=abc)def', 'abcdef')
print(p.group(0))

#  'split',     =>  按照能够匹配的子串将string分割后返回列表
p = re.split('(\W+)', '...words, words...')
print(p)

#  'sre_compile',
#  'sre_parse',

#  'sub',
text = "JGood is a handsome boy, he is cool, clever, and so on..."
p = re.sub(r'\s+', '-', text)
print(p)  # => JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...

#  'subn',      =>  返回替换次数
p = re.subn('[1-2]', 'A', '123456abcdef')
print(p)  # => ('AA3456abcdef', 2)

#################################################################################
# match object对象方法：
#         group() 返回被 RE 匹配的字符串
#         start() 返回匹配开始的位置
#         end() 返回匹配结束的位置
#         span() 返回一个元组包含匹配 (开始, 结束) 的位置
#         group() 返回re整体匹配的字符串，可以一次输入多个组号对应组号匹配的字符串

#################################################################################
# [0-255] => r'[0-1]\d\d|2[0-4]|25[0-5]'

# email   => ^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$

# phone   => ^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$

# 域名    => [a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?

#################################################################################
