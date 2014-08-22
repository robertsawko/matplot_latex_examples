let g:Tex_UseMakefile=0
let g:tex_flavor='latex'
let g:Tex_DefaultTargetFormat='pdf'
let g:Tex_MultipleCompileFormats='pdf'
let g:Tex_CompileRule_pdf='xelatex -interaction=nonstopmode $*'

"this is just a matter of taste but LaTeX looks good with some indentation:
"
set sw=2
set textwidth=80
set spell

"TIP: if you write your labels as label{fig:something, then you may press
"Ctrl+n and you will automatically scroll.
set iskeyword+=

"Don't need to open any of these files ever
set wildignore+=*.aux,*.bbl,*.log,*.out
