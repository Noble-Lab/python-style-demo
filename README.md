# A simple example for organizing data analyses with Python.

This repository is intended to provide some basic guidance on how to structure
your repositories and code when using Python and Jupyter notebooks for your
data analysis projects. It uses Bill's [guide to organizing computational
biology
projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424).

## Contents 
- A toy Python module ([`src/bin/analysis.py`](src/bin/analysis.py)). This file
  contains a couple simple functions and demonstrates how to write Python code
  that can be used as both an imported module and a command line program. It
  also shows how to integrate simple unit tests into the same file. 
  
- A Jupyter notebook
  ([`results/wfondrie/2021-07-14_demo-notebook/demo-notebook.ipynb`](results/wfondrie/2021-07-14_demo-notebook/demo-notebook.ipynb)).
  This notebook demonstrates how you can use your own Python modules in a
  Jupyter notebook.


## Tips for using this repository

- The `src/bin/analysis.py` not only has example functions, but also describes
  how to write documentation alognside the code.
  
- Run the tests (you'll need `pytest` installed either with pip or conda):
  ```bash
  pytest bin/analysis.py
  ```
  
## Contributing

Feel free to open pull requests if you think the repository can be improved!
