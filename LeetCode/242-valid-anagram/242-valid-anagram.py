
s = 'anagram'

hashtable = {}

# 
for i in range(len(s)):
    # 判断是否在里面
    if s[i] in hashtable.keys():
        hashtable[s[i]] += 1
    else:
        hashtable[s[i]] = 1
        
        
print(hashtable)

for item in hashtable:
    print(hashtable[item])