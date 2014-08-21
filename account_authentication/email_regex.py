##coding=utf8
##reference = http://www.crifan.com/python_re_search_vs_re_findall/
import re

regexp=re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}', re.IGNORECASE)
text = 'sanhe@gmail.com wanghui@gmail.com'
print re.findall(regexp, text)