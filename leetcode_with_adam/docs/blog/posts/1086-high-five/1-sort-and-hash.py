class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        hashtable = {}

        for item in items:
            if item[0] not in hashtable:
                hashtable[item[0]] = []
            # append value
            hashtable[item[0]].append(item[1])

        # python dict remains insertion order, sort it based on id
        sort_hashtable= dict(sorted(hashtable.items(), key=lambda item: item[0])) 

        # result List
        res = []
        
        # 现在我们有所有学生的数据in hash
        for key,values in sort_hashtable.items():
            # sort this student's score
            values.sort(reverse = True)

            sum = 0

            counter = 0
            for i in range(len(values)):
                sum += values[i]
                counter += 1
                
                if counter == 5: break
            
            sum = sum//counter

            res.append([key,sum])
        
        return res


            

