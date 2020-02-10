#encoding:utf-8

import string
import random

def creat_code(num):
    '创建一个随机len(num)个数的激活码'
    temp_code = ''
    if isinstance(num,int):
        for n in range(num):
            temp_code += random.choice(string.digits+string.ascii_letters)
        return temp_code
    else:
        print('{} is not a digit!'.format(num))

def creat_code_libary(n,num):
    '创建一个n个激活码的仓库,激活码长度为num'
    codelist = []
    if isinstance(n,int):
        for each in range(n):
            temp_code = creat_code(num)
            codelist.append(temp_code)
        return codelist
    else:
        print('{} is not a digit!'.format(n))

def iscode(code,codelibary):
    '判断输入的激活码是否存在'
    if code in codelibary:
        print('激活码存在，验证成功！')
    else:
        print('激活码不存在，验证失败！')

if __name__ == '__main__':
    code_len = 16
    codelibary_len = 30
    codelibary=creat_code_libary(codelibary_len,code_len)
    one_code = creat_code(code_len)
    iscode(one_code,codelibary)