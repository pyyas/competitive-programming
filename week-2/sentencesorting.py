class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        str1 = ''
        for j in range(len(x)):
            for i in range(len(x)):
                
                index = int(x[i][-1]) - 1
                curr = x[index]
                x[index] = x[i]
                x[i] = curr
            
        for i in range(len(x)):
            x[i] = x[i][:-1]
        for i in x:
            str1 = str1 + ' ' + i
        return str1[1:]