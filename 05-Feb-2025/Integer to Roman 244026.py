# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        x=[1000,500,100,50,10,5,1]
        link={1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        tmp=[]
        ans=''
        while(num):
            p=str(num)[0]
            # print(p != '4' and p != '9')
            if(p != '4' and p != '9'):
                for j in range(len(x)):
                    if(num >= x[j]):
                        tmp.append(x[j])
                        num-=x[j]
                        break
            else:
                # print("num",num)
                for j in range(len(x)):
                    if(num >= x[j]):
                        if(p=='9'):
                            tmp.append(x[j+1])
                            tmp.append(x[j-1])
                        else:
                            tmp.append(x[j])
                            tmp.append(x[j-1])
                        num-=tmp[-1]-tmp[-2]
                        break
        for i in tmp:
            ans+=link[i]

        return ans
