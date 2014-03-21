# -*- coding: utf-8 -*-
'''Add doc here.'''
import keyword

from codeclass import pclass
from codefunc import pfunc
from codevalue import pvalue
from common import renderfile,addimport,isgoodname
from oper import oper

class pblock(oper):
    '''Class pclass: this class is use for auto generate code of a class'''
    def __init__(self,space = 4,doc=''):
        oper.__init__(self)
        '''
        Argument space: 4 if not defined
        Argument doc: doc='' if not defined
        '''
        self.libs = []
        self.value_obj = pvalue()
        self.class_list=[]
        self.func_list = []
        self.doc = doc
        self.space = space

    def render(self, ):
        '''
        Function render: 
        '''
        
        space1 = ' ' * self.space
        space2 = ' ' * (2 * self.space)
        s = ''
        for i in self.libs:
            s += 'import %s\n' % i
        objs=[self.value_obj,]+self.func_list+self.class_list
        for i in objs:
            i.space=self.space
            s+=i.render()
        return s
    def show(self, ):
        '''
        Function show: 
        '''
        print self.value_obj
        print self.libs 
        print self.class_list
        print self.func_list 

    def isgoodname(self,name = '', localname= False):
        '''
        Function isgoodname: 
        Argument name: 
        '''
        if isgoodname(name):
            if localname:
                return True
            dict={'func':[f.func_name for f in self.func_list],
                  'class':[c.class_name for c in self.class_list],
                   'value':[v[0] for v in self.value_obj.value_list],
                   }
            for i,j in dict.items():
                if name in j:
                    raise SyntaxError, "Name %s already exist in %s list." %( name,i)
            return True
        else:
            raise SyntaxError, "Bad name:%s" % name
        
    def renderfile(self,filename = '', recover = False, ):
        '''
        Function renderfile:  put code into a file
        Argument filename: 
        Argument recover: recover the file if exists.default is False.
        '''
        return renderfile(self,filename,recover)


    def addfunc(self,pfunc_obj):
        '''
        Function addfunc: 
        Argument name: 
        '''
        if self.isgoodname(pfunc_obj.func_name):
            self.func_list.append(pfunc_obj)
                
    def addvalue(self,name,value):
        '''
        Function addvalue: 
        Argument name: 
        Argument value:
        '''
        if self.isgoodname(name):
            self.value_obj.addvalue(name,value)
    def addvalue_obj(self,value_obj):
        for n,v in value_obj.value_list:
            self.addvalue(n,v)

    def addimport(self,*name ):
        '''
        Function addimport: 
        Argument name: names of module to be imported
        '''
        addimport(self,*name )
    def addobj(self,pobj):
        if isinstance(pobj,pfunc):
            self.addfunc(pobj)
        elif isinstance(pobj,pvalue):
            self.addvalue_obj(pobj)
        elif isinstance(pobj,pclass):
            self.addclass(pobj)
        else:
            raise TypeError,"pobj must be a instance of pvalue, pclass or pfuncs"
            
    def addclass(self,pclass_obj):
        '''
        Function addclass: add class
        Argument pclass_obj: pclass object
        '''
        if self.isgoodname(pclass_obj.class_name):
            self.class_list.append(pclass_obj)
def main():
    node=pclass('node')
    node2=pclass('node2')
    node.addfunc('next')
    node.addvalue('MAX',999)
    # block=pblock(space=2)
    block=pblock()
    block.addvalue('PI',3.1415926)
    block.addvalue('E',2.718281828)
    block.addclass(node)
    block.addclass(node2)
    fun1=pfunc('pi',('x',None))
    fun2=pfunc('decode',('x',None))
    block.addfunc(fun1)
    block.addfunc(fun2)
    print block.render()
    # block.renderfile('test1')

if __name__=='__main__':
    main()