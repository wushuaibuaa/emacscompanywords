# -*- coding: utf-8 -*-
import codecs

f = codecs.open("en_cn.txt", 'r', "utf-8")
s = f.readlines()
# print(s)
f.close()

# f = open("company-en-words.el", 'w')
f = codecs.open("company-words-discn.el","w","utf-8")  
f.write("(require 'cl-lib)")
f.write("\n")
f.write("(require 'company)")
f.write("\n\n")
f.write(" (defconst en-words-completions \n '(")

for x in s:
    # print(x)
    mylist = x.split(' ')  #
    # print(mylist)
    mylist[0]  = mylist[0].replace('\"', ' ')
    for i in range(len(mylist)-2):
        mylist[1] += mylist[i+2]
    mylist[1] = mylist[1].strip()
    mylist[1]  = mylist[1].replace('\"', ' ')
    # print(mylist[1])
    f.write('#(\"'  + mylist[0] + '\" ' + '0 1' + '\n' +
         '(:initials \"' +  mylist[1] + '\"))\n')
    
f.write("))\n\n")

f.write(";;add support for fuzzy matching.\n")
f.write("(defun en-words-fuzzy-match (prefix candidate)\n")
f.write("(cl-subsetp (string-to-list prefix)\n")
f.write("(string-to-list candidate)))\n")
f.write("\n")
f.write("\n")
f.write("(defun en-words-annotation  (s)\n")
f.write("(format \" [\%s]\" (get-text-property 0 :initials s)))\n")
f.write("\n")
f.write("(defun company-en-words (command &optional arg &rest ignored)\n")
f.write("(interactive (list 'interactive))\n")
f.write("\n")
f.write("(cl-case command \n")
f.write("(interactive (company-begin-backend 'company-en-words))\n")
f.write("(prefix (company-grab-word))\n")
f.write("(candidates \n")
f.write("(remove-if-not\n")
f.write("(lambda (c) (en-words-fuzzy-match arg c))  \n")
f.write("en-words-completions))\n")
f.write("(annotation (en-words-annotation arg))\n")
f.write("(sorted t)\n")
f.write("(ignore-case 'keep-prefix)\n")
f.write("))\n")
f.write("\n")
f.write("\n")
f.write("(defun company-en-words-enable ()\n")
f.write("(interactive)\n")
f.write("(add-to-list 'company-backends 'company-en-words))\n")
f.write("\n")
f.write("\n")
f.write("(defun company-en-words-disable ()\n")
f.write("(interactive)\n")
f.write("(setq company-backends (remove 'company-en-words company-backends)))\n")
f.write("\n")
f.write("\n")
f.write(";;(add-to-list 'company-backends 'company-en-words)\n")
f.write("\n")
f.write("\n")
f.write("(provide 'company-en-words)\n")


f.close()

