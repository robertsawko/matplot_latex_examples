# What is this?

This is an example use of python matpltolib together with xetex. 

What you're getting out of it is:
 * fonts are consistently matched with document font
 * you can use LaTeX symbols in your figure labels

# Prerequsites

 * `python2-matplotlib`
 * `python2-numpy`
 * `xelatex`

# How to use
If you wish to compile you need to

 1. Create the figures.
 1. Compile the document

```bash
cd graphics
python2 bessel.py
python2 laminar.py
# go back and compile the main document
cd ../
xelatex example.tex
```
