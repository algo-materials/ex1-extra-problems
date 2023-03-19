# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:17:32 2020

@author: Nathan
"""
import random
import numpy as np

def rc_genprices(size):
    adds = [random.randint(0,4) for i in range(size)]
    if adds[0] == 0:
        adds[0] = 1
    prices = np.cumsum(adds)
    return list(prices)

def fmt_prices(prices):
    size = len(prices)
    print('|length _i_|'+'|'.join(map(str, list(range(1, size+1)))) + '|')
    print('|:---:'*(size+1) + '|')
    print('|price _pi_|' + '|'.join(map(str,prices)) + '|')
    
#fmt_prices(rc_genprices(5))
    
def dp_rc(prices):
    rev = [0] # rev[i] is max rev for piece of size i
    first_cut = [0] # where to make the first cut
    prices = [0] + prices
    size = len(prices)
    for i in range(1, size):
        maxrev = prices[i]
        cut = i
        for j in range(1, i):
            if prices[j] + rev[i-j] > maxrev:
                maxrev = prices[j] + rev[i-j]
                cut = j
        rev.append(maxrev)
        first_cut.append(cut)
    return rev[1:], first_cut[1:]

def fmt_soln(r,s):
    size = len(r)
    print('|length _i_|'+'|'.join(map(str, list(range(1, size+1)))) + '|')
    print('|:---:'*(size+1) + '|')
    print('|revenue _ri_|' + '|'.join(map(str,r)) + '|')
    print('|first cut _si_|' + '|'.join(map(str,s)) + '|')
#fmt_soln(*dp_rc([2,4,7,11,13]))
#fmt_soln(*dp_rc([2, 2, 5, 5, 9]))
#fmt_soln(*dp_rc([4, 8, 11, 15, 15]))
'''
# how to generate a problem and the solution (rod cutting)
prices = rc_genprices(8)
print(prices)
fmt_prices(prices)
print()

fmt_soln(*dp_rc(prices))
'''

def dp_lcs (seq1, seq2):
    rows = 1 + len(seq1)
    cols = 1 + len(seq2)
    C = []
    for r in range(rows):
        C.append([0 for c in range(cols)])
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i-1] == seq2[j-1]:
                C[i][j] = 1 + C[i-1][j-1]
            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])
    return C

def longest_subseq(seq1, seq2, C):
    i = len(C)-1
    j = len(C[0])-1
    seq = []
    while i > 0 and j > 0:
        if C[i][j] == 1 + C[i-1][j-1] and seq1[i-1] == seq2[j-1]:
            seq.append(seq1[i-1])
            i -= 1
            j -= 1
        elif C[i][j] == C[i-1][j]:
            i -= 1
        else: j -= 1
    return seq[::-1]

def fmt_lcs_ans(seq1, seq2, C):
    row_headers = [' ']+[x for x in seq1]
    cols = len(seq2)+1
    print('|||'+'|'.join([x for x in seq2])+'|')
    print('|:---:'*(cols+1) + '|')
    print('|'+'|0'*(cols+1)+'|')
    for i in range(1,len(row_headers)):
        print('|**{}**|'.format(row_headers[i]) + '|'.join(map(str, C[i])) +'|')

#C = dp_lcs('abcdef', 'defabc')
#print(longest_subseq('abcdef', 'defabc', C))
#fmt_lcs_ans('abcdef', 'defabc', C)
def gen_lcs(l):
    alpha = [x for x in 'qwertyuiopasdfghjklzxcvbnm']
    random.shuffle(alpha)
    s1 = alpha[:l]
    s2 = alpha[:l]
    random.shuffle(s2)
    return ''.join(s1), ''.join(s2)

'''
# generate and print a random LCS problem
seq1, seq2 = gen_lcs(6)
C = dp_lcs(seq1, seq2)
print('`{}`, `{}`'.format(seq1, seq2))
print()
fmt_lcs_ans(seq1, seq2, C)
print()
print(longest_subseq(seq1, seq2, C))        
'''
seq1 = 'lollygag'
seq2 = 'brouhaha'
C = dp_lcs(seq1, seq2)
print('`{}`, `{}`'.format(seq1, seq2))
print()
fmt_lcs_ans(seq1, seq2, C)
print()
print(longest_subseq(seq1, seq2, C))

      