import os
import sys
import json
import argparse
import re

FILENAME = r'tmp'
dic = {}
token_freq = []



def token_count(n=2, cutoff=20):
    token_sum = 0
    f_file = open(FILENAME)
    for line in f_file:
        line_str = line.strip().lower()
        line_list = re.split(" |!|\?|,|\.|/|;", line_str)
        if n == 1:
            for word in line_list:
                dic[word] = dic.get(word, 0) + 1
                token_sum = token_sum + 1
        elif n == 2:
            i = 0
            # word_list = []
            for word in line_list:
                if i == 0:
                    i = i + 1
                    continue
                tmp_str = line_list[i - 1] + ' ' + line_list[i]
                token_sum = token_sum + 1
                # word_list.append(tmp_str)
                i = i + 1
            dic[tmp_str] = dic.get(tmp_str, 0) + 1
    token_freq = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    i = 0
    loc = -1
    for word, freq in token_freq:
        if freq < cutoff:
            loc = i
            break
        sys.stdout.write(word + '\t' + str(freq) + '\n')
        i = i + 1
    sys.stderr.write('total' + '\t' + str(token_sum) + '\n')
    del token_freq[loc:]
    #print(token_freq)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='token count', 
        usage='''
        ./token_freq.py -n 1/2 -c 5
        ''', formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('-n',type=int, help='json field', default=1)
    parser.add_argument('-c',type=int, help='json field', default=5)
    args = parser.parse_args()
    token_count(args.n, args.c)
