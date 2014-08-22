# What is this?

This document contains a few examples of using matplotlib in a LaTeX document.

What are the benefits of doing it this way:
 * fonts are consistently matched with document font,
 * you can use LaTeX symbols in your figure labels,
 * python can iterate over many folders potentially recreating many figures in a
   single command,
 * TrueType font, if you use xelatex.

# Prerequsites

 * `python2-matplotlib`
 * `python2-numpy`
 * `xelatex`
 * The following LaTeX packages
  * amsfonts 
  * amsmath
  * fontspec for TrueType fonts
  * hyperref
  * pgf
 * Biber for bibliography support (not using Bibtex!)

# How to use
If you wish to compile you need to

 1. Create the figures.
 1. Compile the document

```bash
# to compile figures
cd graphics
python2 bessel.py
python2 laminar.py
# go back and compile the main document
cd ../
xelatex example.tex
# to get bibliography
biber example.tex
# to finish off
xelatex example.tex
```

Use GitBash if you're under Windows.

If you do not want to have TrueType fonts simply comment out font specification
in example.tex.

## Comments, questions and improvements

Feel free to leave them in Issues section.
