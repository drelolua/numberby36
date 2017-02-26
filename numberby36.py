# -*-coding:utf-8-*-
"""
自定义进制
Description:
    定义一个36进制的计数系统
Author:cui shichuan cuisc13@gmail.com
Versions:
    Created by cui on 2016-12-10
"""
import re
ndict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nlen = len(ndict)
# x:整数
#返回: 字符串
def tostr36(x):
    try:
        int(x)
    except:
        x=0
    if x<0:
        x=-x
    if x==0:
        return "0"
    s = ""
    while x>= nlen:
        x1 = x%nlen
        s = ndict[x1]+s
        x = x//nlen
    if x>0:
        s = ndict[x]+s
    return s
# s:36进制字符串
# 返回: 整数
def toint(s):
    x = 0
    s = str(s).strip()
    pattern = re.compile(r'.*[^0-9A-Z].*') # 找出不合法的字符
    assert re.match(pattern, s) is None, 'The string "%s" is not a number of 36 number system.' % s
    if s == '':
        return x
    for y in s:
        k = ndict.index(y)
        if k>=0:
            x=x*nlen+k
    return x
#自增 默认为自增1，可以传入n，实现incr_by
# 自减不另建方法，传入负数，如自减1，则
#       incr(s, -1)
#s:36位的字符串
#返回：36位字符串
def incr(s, n=1):
    num =  toint(s)
    num += n
    return tostr36(num)
