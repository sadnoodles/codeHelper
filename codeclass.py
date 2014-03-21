# -*- coding: utf-8 -*-
'''Add doc here.'''
import keyword

from common import renderfile,addimport,isgoodname
from oper import oper

class pclass(oper):
    '''Class pclass: this class is use for auto generate code of a class'''
    def __init__(self,name = 'NewClass', * argv, ** kwargv):
        oper.__init__(self)
        '''
        Argument name: the class you want.
        argvs is the arguments your class carry in tuple ('value_name', value)
        Argument space: 4 if not defined
        Argument doc: doc='' if not defined
        '''
        self.class_name = name
        self.space = kwargv.get('space',4)
        self.libs = []
        self.init_values = []
        self.func = {}
        self.value = {}
        for i, j in argv:
            if self.isgoodname(i):
                self.init_values.append((i, j))
        self.doc = kwargv.get('doc', '')

    def render(self,IMPORT=True ):
        '''
        Function render: 
        '''
        space1 = ' ' * self.space
        space2 = ' ' * (2 * self.space)
        s = ''
        
        #import libs
        if IMPORT:
            for i in self.libs:
                s += 'import %s\n' % i
        #end
        
        #class define
        s += "\nclass %s:\n" % self.class_name
        s += space1
        s += "'''Class %s: %s'''\n" % (self.class_name, self.doc)
        #end
        
        #__init__ define
        t = space1 + "def __init__(self,"
        for i, j in self.init_values:
            t += (i + ' = ' + repr(j) + ', ')
        t += '):\n'
        s += t
        s += (space2 + "'''\n")
        for i, j in self.init_values:
            s += (space2 + 'Argument ' + i + ': \n')
        s += (space2 + "'''\n")
        #end
        
        #set values
        t = space2 + "self."
        for i, j in self.init_values:
            s += (t + i + ' = ' + i + '\n')
        for i, j in self.value.items():
            s += (t + i + ' = ' + repr(j) + '\n')
        #end
        
        
        #define functions
        t = '\n' + space1 + "def "
        for i, j in self.func.items():
            if j:
                s += (t + i + "(self,")
                for k, v in j:
                    s += (k + " = " + repr(v) + ", ")
                s += "):\n"
                s += (space2 + "'''\n")
                s += "%sFunction %s: \n" % (space2, i)
                for k, v in j:
                    s += (space2 + 'Argument ' + k + ': \n')
            else:
                s += (t + i + "(self, ):\n")
                s += (space2 + "'''\n")
                s += "%sFunction %s: \n" % (space2, i)
            s += (space2 + "'''\n")
            s += (space2 + '\n')
            s += (space2 + 'return None\n')
        #end
        
        # print s
        return s
    def show(self, ):
        '''
        Function show: 
        '''
        print self.init_values
        print self.value
        print self.func

    def isgoodname(self,name = '', localname= False):
        '''
        Function isgoodname: 
        Argument name: 
        '''
        if isgoodname(name):
            if localname:
                return True
            if name in self.func:
                raise SyntaxError, "Name %s already exist in func list." % name
            if name in [x[0] for x in self.init_values]:
                raise SyntaxError, "Name %s already exist in value list." % name
            if name in self.value.keys():
                raise SyntaxError, "Name %s already exist in value list." % name
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


    def addfunc(self,name , *argv):
        '''
        Function addfunc: 
        Argument name: 
        '''
        if self.isgoodname(name):
            self.func[name] = []
            for i, j in argv:
                self.isgoodname(i, localname = True)
                self.func[name].append((i, j))
    def addfunc_obj(self,pfunc_obj):
        '''
        Function addfunc: 
        Argument name: 
        '''
        self.addfunc(pfunc_obj.func_name,*pfunc_obj.init_values)
                
    def addvalue(self,name = '', value = None):
        '''
        Function addvalue: 
        Argument name: 
        '''
        if self.isgoodname(name):
            self.value[name] = value

    def addimport(self,*name ):
        '''
        Function addimport: 
        Argument name: 
        '''
        addimport(self,*name )

def main():
    s = pclass('ppclass', ('name', ''),('space',4), doc = 'this class is use for auto generate code of a class')
    s.addimport('os','keyword')
    
    s.addvalue('value',{})
    s.addvalue('func',{})
    s.addvalue('libs',[])
    s.addvalue('init_values',[])
    
    s.addfunc('show')
    s.addfunc('render')
    s.addfunc('isgoodname',('name',''))
    s.addfunc('addvalue',('name',''))
    s.addfunc('addfunc',('name',''))
    s.addfunc('renderfile',('filename',''),('recover',False))
    
    s.show()
    print s.render()
    
    return None

if __name__=='__main__':
    main()