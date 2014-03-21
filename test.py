# -*- coding: utf-8 -*-
from codeblock import *
def main():
    b=pblock()
    
    fun1=pfunc('quit')
    fun2=pfunc('Hello',('world',42))
    fun3=pfunc('mutilArgvs',('name',''),
                            ('color',(0,255,255)),
                            ('size',[20,20]),
                            ('parent',None),
                            ('good',True))
    fun3.addimport('os')
    fun3.addimport('sys','time','math')
    print fun3.render()
    print '-'*20
    
    b.addfunc(fun1)
    b.addfunc(fun2)
    b.addfunc(fun3)
    b.addvalue('G',9.8)
    
    v=pvalue()
    v.addvalue('HIGHT',100)
    v.addvalue('WEIGHT',60)
    b.addvalue_obj(v)
    print v
    print '-'*20
    
    ball=pclass('Ball',('size',20),('color','#336699'),doc='A ball')
    ball.addfunc('spin',('angel',90))
    ball.addvalue('speed',10)
    
    print ball.render()
    print '-'*20
    
    #or 
    # for i in  [fun1,fun2,fun3,v,ball]:
        # b.addobj(i)
    
    b.addclass(ball)
    import copy
    ball2=copy.deepcopy(ball)
    ball2.class_name='Ball2'
    ball2.addfunc_obj(fun3)
    b.addclass(ball2)
    
    b.addimport('copy')
    
    print b.render()
    print '-'*20
if __name__=='__main__':
    main()