import os
import os.path as op

import subprocess as sp
import shlex

def makepth(plist):
    r = op.splitdrive(os.getcwd())[0] + os.path.sep 
    for p in plist:
        r = op.join(r, p)
    
    return r

def collectDoc(p):
    pist = [op.join(p, i) for i in os.listdir(p) if "doc" in i]
    for ii, pp in enumerate(pist):
        pi = pp.replace(" ", "_")
        if not pi == pp:
            os.rename(pp, pi)
            pist[ii] = pi
    return pist

class Conversion:
    def __init__(self):
        self.pyo = makepth(["Program Files", "LibreOffice", "program", "python.exe "])
        self.uno = makepth(["Users", "Philadelphia", "Anaconda", "envs", "py36", "Scripts", "unoconv "])
        self.convstr = self.pyo + self.uno + "-f html "
        self.panconv = "pandoc -f html -t markdown -o "
    def convertDoc(self, p):
        docs = collectDoc(p)
        for d in docs:
            dd, _ = op.splitext(d) 
            htmldoc = dd+".html "
            mddoc = dd+".md "
            print(self.convstr + d)
            if op.isfile(mddoc):
                continue
            if not op.isfile(htmldoc):
                sp.call(self.convstr + d)
            
            print(self.panconv + mddoc + htmldoc)
            sp.call(self.panconv + mddoc + htmldoc)

    

thispath = op.abspath(op.dirname(__file__))
dlist = sorted([op.join(thispath, d) for d in os.listdir(thispath) if op.isdir(d)])
c = Conversion()
for d in dlist:
    c.convertDoc(d)



