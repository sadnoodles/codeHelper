# -*- coding: utf-8 -*-
'''some function that many modules use.'''
import os
import re
import keyword
def renderfile(obj = None, filename = '', recover = False, ):
    '''
    Function renderfile:  put code into a file
    Argument obj: 
    Argument filename: 
    Argument recover:  recover the file if exists. Default is False.
    '''
    s = '# -*- coding: utf-8 -*-\n'
    s += "'''Add doc here.'''\n"
    s += obj.render()
    space1=' '*obj.space
    #def main
    s += "\ndef main():\n"
    s += (space1 + '\n')
    s += space1 + 'return None\n'
    s += "\nif __name__=='__main__':\n"
    s += (space1+"main()")
    #end
    if not filename:
        raise TypeError, "please give me a filename"
    if not (filename.endswith('.py') or filename.endswith('.pyw')):
        filename += '.py'
    if (not recover) and os.path.exists(filename):
        raise OSError,filename+' already exist.'
        return filename
    open(filename, 'w').write(s)
    return filename
    
def addimport(obj,*name ):
    '''
    Function addimport: 
    Argument name: 
    '''
    if len(name)==1:
        if type(name[0])==str:
            obj.libs.append(name[0])
    else:
        for i in name:
            if type(i)==str:
                obj.libs.append(i)
            else:
                raise TypeError,"names must be string"

def isgoodname(name):
    m=re.match('[a-zA-Z_][0-9a-zA-Z_]*',name)
    if m:
        return name==m.group() and not(name in keyword.kwlist)
    else:
        return False
        
        
def main():
    names=['','1','a','as','_1_','_','1a','Av','a1',
    '__main__','ADDSA','DFGYHUJIKO','f$j','h2h','as/d','a\s','d*',';','abs','if']
    for i in names:
        print "%10s ,%7s"%(i,isgoodname(i))
if __name__=="__main__":
    main()