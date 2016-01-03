# coding=gbk
import codecs

f = codecs.open("english-words.txt", 'r')
s = f.readlines()
f.close()

f = open("company-words.el", 'w')
f.write("(require 'cl-lib)")
f.write("\n")
f.write("(require 'company)")
f.write("\n\n")
f.write(" (defconst en-words-completions \n '(")

for x in s:
    # print(x)
    x = x.strip('\n')
    f.write('\"'  + x + '\" ')
    
f.write("))\n\n")

f.write("(defun company-en-words-backend (command &optional arg &rest ignored)\n (interactive (list \'interactive))")

f.write("\n\n")

f.write("(case command \n (interactive (company-begin-backend 'company-en-words-backend)) \n (prefix (company-grab-symbol)) \n (candidates \n  (remove-if-not \n   (lambda (c) (string-prefix-p arg c))  \n   en-words-completions))))")

f.write("\n\n")

f.write("(add-to-list 'company-backends 'company-en-words-backend)")
f.close()
