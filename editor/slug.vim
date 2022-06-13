    " Vim syntax file
    " Language: Slug

    " Usage Instructions
" Put this file in .vim/syntax/slug.vim
" and add in your .vimrc file the next line:
" autocmd BufRead,BufNewFile *.slug set filetype=slug

if exists("b:current_syntax")
  finish
endif

set iskeyword=a-z,A-Z,-,*,_,!,@
" Language keywords
syntax keyword slugKeywords put write as if else while do end call use job
" String literals
syntax region slugString start=/\v"/ skip=/\v\\./ end=/\v"/ contains=slugEscapes

" Char literals
syntax region slugChar start=/\v'/ skip=/\v\\./ end=/\v'/ contains=slugEscapes

" Escape literals \n, \r, ....
syntax match slugEscapes display contained "\\[nr\"']"

" Number literals
syntax region slugNumber start=/\s\d/ skip=/\d/ end=/\s/

" Type names the compiler recognizes
" syntax keyword slugTypeNames put
" Set highlights
" highlight default link porthTodos Todo
highlight default link slugKeywords Keyword
" highlight default link porthCommentLine Comment
highlight default link slugString String
highlight default link slugNumber Number
" highlight default link slugTypeNames Type
highlight default link slugChar Character
highlight default link slugEscapes SpecialChar

let b:current_syntax = "slug"

