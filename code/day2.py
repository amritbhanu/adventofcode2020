from collections import Counter

def dataPreprocess():
    l = []
    with open("../data/day2.txt") as f:
        for x in f.readlines():
            split_text = x.strip().split(": ")
            left, s = split_text[0], split_text[1]
            split_text = left.split(" ")
            left, ch = split_text[0], split_text[1]
            split_text = left.split("-")
            low, high = int(split_text[0]), int(split_text[1])
            l.append([low, high, ch.lower(), s.lower()])
    return l

def isvalid(low, high, ch, strin):
    dic = Counter(strin)
    if ch in dic and low<=dic[ch] <= high:
        return True
    return False

# l = dataPreprocess()
# valid = 0
# for x in l:
#     if isvalid(x[0], x[1], x[2], x[3]):
#         valid+=1
#
# print(valid)
# print(len(l))

def dataPreprocess1():
    l = []
    with open("../data/day2.txt") as f:
        for x in f.readlines():
            split_text = x.strip().split(": ")
            left, s = split_text[0], split_text[1]
            split_text = left.split(" ")
            left, ch = split_text[0], split_text[1]
            split_text = left.split("-")
            low, high = int(split_text[0])-1, int(split_text[1])-1
            l.append([low, high, ch.lower(), s.lower()])
    return l

def isvalid1(one, two, ch, strin):
    one_flag=False
    two_flag=False
    if 0<=one<len(strin) and strin[one] == ch:
        one_flag=True
    if 0<=two<len(strin) and strin[two] == ch:
        two_flag=True
    return one_flag ^ two_flag

l = dataPreprocess1()
valid = 0
for x in l:
    if isvalid1(x[0], x[1], x[2], x[3]):
        valid+=1

print(valid)
