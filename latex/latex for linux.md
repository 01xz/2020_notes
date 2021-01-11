# install latex on ArchLinux

```
sudo pacman -S texlive-core texlive-langchinese texlive-langjapanese texlive-latexextra biber
```

## configuration in VS Code

```
    "editor.wordWrap": "on",
    "latex-workshop.latex.tools": [
    {
        "name": "latexmk",
        "command": "latexmk",
        "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "%DOC%"
        ]
    },
    {
        "name": "xelatex",
        "command": "xelatex",
        "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
        ]
    },
    {
        "name": "pdflatex",
        "command": "pdflatex",
        "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
        ]
    },
    {
        "name": "bibtex",
        "command": "bibtex",
        "args": [
        "%DOCFILE%"
        ]
    }
    ],
    "latex-workshop.latex.recipes": [
    {
        "name": "latexmk",
        "tools": [
        "latexmk"
        ]
    },
    {
        "name": "xelatex -> bibtex -> xelatex*2",
        "tools": [
        "xelatex",
        "bibtex",
        "xelatex",
        "xelatex"
        ]
    },
    {
        "name": "xelatex",
        "tools": [
        "xelatex"
        ]
    },
    {
        "name": "pdflatex -> bibtex -> pdflatex*2",
        "tools": [
        "pdflatex",
        "bibtex",
        "pdflatex",
        "pdflatex"
        ]
    }
    ],
    "latex-workshop.view.pdf.viewer": "browser",
    "files.autoSave": "afterDelay"
```
