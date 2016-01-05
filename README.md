# emacs company mode English words compelete

## Description
A lisp file using company-mode to complete english words.

It defines a words constant list by 'defconst'. 
And define a company backend to complete English words.
It only using company mode.
Do not require ispell or orther program.

## Useage

Put company-words.el file in a path you like, for example "~/Dropbox/Emacs/".

Add the below command in your .emacs file to load it.

(load "~/Dropbox/Emacs/company-words")

It will be enabled in all mode.

## Attached files

English-words.txt: the file includes over 72,000 English words. 
It is not required for emacs. Just for reference.

create_company_words.py: a python file to generate the "company-words.el" file from "English-words.txt" file. It is not requried for emacs. Just for reference.
