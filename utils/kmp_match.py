#coding:utf-8
"""
@file:      kmp
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/22 0:58
@description:
            --
"""

def kmp_match(text, pattern):
    def init_prefix_table(word):
        prefix_count = 0
        prefix_table = [0]*len(word)
        # start from the 2nd character
        for i in range(1, len(word)):
            if word[i] == word[prefix_count]:
                prefix_count+=1
            else:
                prefix_count = 0
            prefix_table[i] = prefix_count
        return prefix_table

    prefix_table = init_prefix_table(pattern)
    pattern_index = 0
    for text_index, text_ch in enumerate(text):
        while pattern_index > 0 and text_ch != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index-1]

        if text_ch == pattern[pattern_index]:
            if pattern_index == len(pattern)-1:
                return text_index-pattern_index
            pattern_index+=1

    return -1

if __name__ == '__main__':
   res=kmp_match(str(12313),str(1231))
   if res ==0 :
    print(res)