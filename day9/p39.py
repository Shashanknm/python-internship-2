'''
Best Grade:
Andrew has a string N consisting of lowercase English letters representing respective
grades of N students in his class. His grade is at Pth index. He can swap any two adjacent grades.

Your task is to help Andrew find and return a string value, representing maximized grade
by bringing lexicographically smallest character on the Pth index after doing at most K swaps

Sample Input:
abcdefg
3
2

Sample Output:
a
'''
s = input()
p = int(input())
k = int(input())
s1 = list(s)
s = 0
e = len(s1)
mini = 999
if abs(p-k-1)>=0:
    s = abs(p-k-1)
if p+k<len(s1):
    e = p+k
print(s,e)
for i in range(s,e):
    mini = min(ord(s1[i]),mini)
    
store = s1[p-1]
s1[p-1] = s1[s1.index(chr(mini))]
s1[s1.index(chr(mini))] = store
print(mini)
print(''.join(s1))
'''
Output:
abcdefg
3
2
0 5
97
cbadefg
'''
