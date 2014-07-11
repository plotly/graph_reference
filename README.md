# Plotly Graph Reference

*Welcome to the ultimate reference of Plotly's JSON graph format (graph reference
for short)!*

Graph reference is used:

- in Plotly's API online documentation:
  [Python](https://plot.ly/python/reference/),
  [MATLAB](https://plot.ly/matlab/reference/),
  [R](https://plot.ly/r/reference/), 
  [node.js](https://plot.ly/nodejs/reference/) and
  [Julia](https://plot.ly/julia/reference/),

- in the output of our APIs' help functions.


### Files in this repo:

- `graph_objs_meta.py` : Meta-generating file

- `graph_objs_meta-toc.md` : Table of content for meta-generating file

- `graph_objs_keys.py` : JSON of all Plotly keys

- `graph_objs_meta.json` : JSON of (all) META of all Plotly keys

- `graph_objs_checklist.json` : List of undocumented keys 

- `test_graph_reference.py` : Test script

- `circle.yml` : Tells Circle to run test

- `__init__.py` : to support relative imports


### Philosophy

* All Plotly meta should be generated using a single (Python) file (this is
  `graph_objs_meta.py`). This meta-generating file should be clean and
  well-organized (see `graph_objs_meta-toc.md`).

+ All Plotly keys should be contained in a single JSON file (this is
  `graph_objs_keys.json`).

+ Every Plotly API should have its own meta JSON file, with meta consistent with
  each language's terminology (coming soon).

* A fully described key is an object with the keys: 
  1. `'required'`: Whether the key is required or not to create the chart type,
  1. `'type'`: `'style'`, `'plot_info'`, `'object'` or `'data'` (**Important**),
  1. `'val_types'`: Valid types (e.g. array-like of strings, number: in [0, 1]),
  1. `'description'`: making help helpful!

* There are two additional keys: `'streamable'` and `'examples'`.

* Repetition in the meta-generating file should be kept to a minimum.  More
  precisely, meta for keys that are contained in more than 1 object and they
  show significant similarities, is generated using shortcuts. These
  meta-generating shortcuts come in two flavors:
  1. functions, named `make_<key>` e.g. `make_x`, used when small discrepancies
  occur from object to object,
  1. dictionaries, named `drop_<key>` e.g. `drop_ visisble`, used when the exact
  same meta is used for all objects containing a particular key.
  
### Contributing

1. Clone and/or pull the latest master version: 
```
$ git pull origin master
```

1. Make a new branch (for testing purposes) and checkout: 
```
$ git branch your_branch_name
$ git checkout your_branch_name
```

1. Add and modified keys in `graph_objs_meta.py`, with special attention to
   existing shortcuts (search for key shortcuts with `@key@`).  Update the table
   content in `graph_objs_mets-toc.md` if keys were added or if the order was
   modified.

1. Generate the JSON files:
```
$ python graph_objs_meta.py
```

1. Add, commit and push to online repo:
```
$ git add .
$ git commit 
$ git push origin your_branch_name
```
When you push any branch to the online repo, Nose is going to test the
`test_graph_references.py` file. To see if your push passed, go 
[here](https://circleci.com/gh/plotly/graph_reference)


### Glossary

*

