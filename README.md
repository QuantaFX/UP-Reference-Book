
# UP-Reference-Book

University of the Philippines Baguio - Competitive programming reference book
## Code Structure

```
UP-Reference-Book/
├── _code/
├── _docs/
├── code/
│   ├── 01_Data_Structures/
│   │   └── segment_tree.py
│   ├── 02_Graphs/
│   │   └── dijkstra.py
│   └── 03_Mathematics/
│       └── sieve.py
├── tex/
│   ├── 01_Data_Structures.tex
│   ├── 02_Graphs.tex
│   └── 03_Mathematics.tex
├── structure/
│   ├── 01_Data_structures.md
│   ├── 02_Graphs.md
│   └── 03_Mathematics.md
└── build.py
├── notebook.tex
├── notebook.pdf
└── generate_tex.py
└── preprocess.py
```
## Installation

### Python 
Python 3.x: Ensure Python is added to your system PATH.
```
    https://www.python.org/downloads/
```
Pygments: The Python syntax highlighter.

```bash
    pip install Pygments
```

### LaTeX Distribution

Windows: MiKTeX
```bash
    https://miktex.org/download
```

Linux/Mac: TeX Live
```bash
    sudo apt install texlive-full
```

## How to Build

Windows & Linux: Run `build.py`

```DOS
    python build.py
```
## How to Contribute

1. Write your optimized Python algorithm and save it in the appropriate `code/`
subdirectory (`code/03_Math/sieve.py`).
2. Open the corresponding `.md` file in the `structure/` folder (`structure/03_Math.md`).
3. Add a section in the `.md` file: 
```
Data Structures 
    segment_tree.py 
    union_find.py
```
4. Rebuild the project.
## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

