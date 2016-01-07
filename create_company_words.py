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

f.write("(defun en-words-fuzzy-match (prefix candidate)\n   (cl-subsetp (string-to-list prefix) \n  (string-to-list candidate)))")

f.write("(defun company-en-words (command &optional arg &rest ignored)\n (interactive (list \'interactive))")

f.write("\n\n")

f.write("(case command \n (interactive (company-begin-backend 'company-en-words)) \n (prefix (company-grab-word)) \n (candidates \n  (remove-if-not \n   (lambda (c) (en-words-fuzzy-match arg c))  \n   en-words-completions))))")

f.write("\n\n")

f.write("(defun company-en-words-enable () \n   (interactive) \n   (add-to-list 'company-backends 'company-en-words))")

f.write("\n\n")

f.write("(defun company-en-words-disable () \n   (interactive) \n   (setq company-backends (remove 'company-en-words company-backends)))")

f.write("\n\n")

f.write(";;(add-to-list 'company-backends 'company-en-words)")

f.close()
