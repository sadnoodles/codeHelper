# -*- coding: utf-8 -*-
'''Add doc here.'''
import keyword
from common import renderfile,addimport,isgoodname
from oper import oper

class pvalue(oper):
    '''Class pvalue: '''
    def __init__(self,space = 4):
        oper.__init__(self)
        '''
        '''
        self.space=space
        self.libs = []
        self.value_list = []

    def addvalue(self,name = '', value = None):
        '''
        Function addvalue: 
        Argument name: 
        '''
        if self.isgoodname(name):
            self.value_list.append((name, value))
    def isgoodname(self,name = '', localname= False):
        '''
        Function isgoodname: 
        Argument name: 
        '''
        if isgoodname(name):
            if localname:
                return True
            if name in [v[0] for v in self.value_list]:
                raise SyntaxError, "Name %s already exist in value list." % name
            return True
        else:
            raise SyntaxError, "Bad name:%s" % name

    def renderfile(self,filename = '', recover = False, ):
        '''
        Function renderfile: 
        Argument filename: 
        Argument recover: 
        '''
        return renderfile(self,filename,recover)

    def render(self, IMPORT=True):
        '''
        Function render: 
        '''
        space1 = ' ' * self.space
        s = ''
        
        #import libs
        if IMPORT:
            for i in self.libs:
                s += 'import %s\n' % i
        
        for i,j in self.value_list:
            s += (i+" = "+repr(j)+'\n')
        return s
    def addimport(self,*name ):
        '''
        Function addimport: 
        Argument name: 
        '''
        addimport(self,*name )

def main():
    
    v=pvalue()
    for i in range(100,130):
        v.addvalue('WX_%s'%(i-100),i)
    v.addimport('WX')
    print v.render()

if __name__=='__main__':
    main()