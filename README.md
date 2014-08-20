# What is this?

This is an example use of python matpltolib together with xetex. 

What you're getting out of it is:
 * fonts are consistently matched with document font
 * you can use LaTeX symbols in your figure labels

# Prerequsites

# How to use
If you wish to compile you need to

 1. Create the figures.
 1. Compile the document

To create the figures `cd` into the directory graphs and make the figures using
python2 or associated Makefile.

Then cd back to the tex directory and run
```
xelatex example.tex
```
