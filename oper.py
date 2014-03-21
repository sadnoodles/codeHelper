# -*- coding: utf-8 -*-
class oper:
    def __init__(self,):
        self.libs=[]
        self.strings=''
        
    def __str__(self):
        return self.render()
        
    def render(self):
        return self.strings
        
    def __add__(self,obj):
        return self.render()+'\n'+obj.render()

        
def main():        
    b=oper()
    b.strings='asd'
    c=oper()
    c.strings='ffasdff'
    print b
    print b+c

if __name__=='__main__':
    main()