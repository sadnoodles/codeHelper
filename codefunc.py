# -*- coding: utf-8 -*-
'''Add doc here.'''
import keyword
from common import renderfile,addimport,isgoodname
from oper import oper
class pfunc(oper):
    '''Class pfunc: this class is use for auto generate code of a function'''
    def __init__(self,name = '', * argv, ** kwargv):
        oper.__init__(self)
        '''
        Argument name: 
        Argument space: 
        Argument doc: 
        '''
        if self.isgoodname(name):
            self.func_name = name
        self.space = kwargv.get('space', 4)
        self.init_values = []
        self.local_value ={}
        self.libs = []
        for i, j in argv:
            if self.isgoodname(i):
                self.init_values.append((i, j))
        self.doc = kwargv.get('doc','')

    def renderfile(self,filename = '', recover = False, ):
        '''
        Function renderfile: put code into a file
        Argument filename: 
        Argument recover: recover the file if exists.default is False.
        '''
        return renderfile(self,filename,recover)
        
    def isgoodname(self,name):
        if isgoodname(name):
            return True
        else:
            raise SyntaxError, "Bad name:%s" % name
            
    def addimport(self,*name ):
        '''
        Function addimport: 
        Argument name: 
        '''
        addimport(self,*name)

    def render(self, IMPORT=True,):
        '''
        Function render: 
        '''
        s=''
        space1=''
        space2=' '*self.space
        
        #import libs
        if IMPORT:
            for i in self.libs:
                s += 'import %s\n' % i
        #end
        t = space1 + "\ndef "
        i=self.func_name
        if self.init_values:
            s += (t + i + "(self,")
            for k, v in self.init_values:
                s += (k + " = " + repr(v) + ", ")
            s += "):\n"
            s += (space2 + "'''\n")
            s += "%sFunction %s: \n" % (space2, i)
            for k, v in self.init_values:
                s += (space2 + 'Argument ' + k +': \n')
        else:
            s += (t + i + "(self, ):\n")
            s += (space2 + "'''\n")
            s += "%sFunction %s: \n" % (space2, i)
        s += (space2 + "'''\n")
        s += (space2 + '\n')
        s += (space2 + 'return None\n')
        return s

def main():
    f=pfunc('renderfile',('obj',None),('filename',''),('recover',False))
    f.addimport('os',)
    print f.render()
    print f.renderfile('renderfile')
    return None

if __name__=='__main__':
    main()