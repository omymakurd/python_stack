class MathDojo:
    def __init__(self):
        self.result=0
    def add(self,num,*nums):
       self.result+= num
       for n in nums:
          self.result+=n
       return self
    def subtrac(self ,num,*nums):
        self.result-=num
        for n in nums:
           self.result-=n
        return self
md =MathDojo()
print(md.add(2).add(2,5,1).subtrac(3,2).result) 
md1=MathDojo()
print(md1.add(5).add(7,8,9).subtrac(6).subtrac(2,3).result) 
md3=MathDojo()
print(md3.add(7).add(10,11,17,18,20).subtrac(6,3,4,2).result)


