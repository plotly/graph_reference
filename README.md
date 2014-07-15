# Plotly Graph Reference

*Welcome to the ultimate reference of Plotly's JSON graph format!*

Or just graph reference for short.

Graph reference is used:

- in Plotly's API online documentation:
  [Python](https://plot.ly/python/reference/),
  [MATLAB](https://plot.ly/matlab/reference/),
  [R](https://plot.ly/r/reference/), 
  [node.js](https://plot.ly/nodejs/reference/) and
  [Julia](https://plot.ly/julia/reference/),

- in the output of our APIs' help functions.


### Files in this repo:

- `graph_objs_meta.py` : Meta-generating script

- `graph_objs_meta-toc.md` : Table of content for meta-generating file

- `graph_objs_keys.py` : JSON of all Plotly keys

- `graph_objs_meta.json` : JSON of (all) META of all Plotly keys

- `graph_objs_checklist.json` : List of undocumented keys 

- `test_graph_reference.py` : Test script

- `circle.yml` : Tells Circle to run test

- `__init__.py` : to support relative imports


### Philosophy

* All Plotly meta should be generated using a single (Python) file (this is
  `graph_objs_meta.py`). This meta-generating script should be clean and
  well-organized (see `graph_objs_meta-toc.md`).

+ All Plotly keys should be contained in a single JSON file (this is
  `graph_objs_keys.json`).

+ Every Plotly API should have its own meta JSON file, with meta consistent with
  each language's terminology (coming soon).

* A fully described key is an object with the keys: 
  1. `'required'`: whether the key is required or not to create the chart type,
  1. `'type'`: **IMPORTANT** `'data'` (the only keys that remain after
  `.get_data()`), `'style'` (is stripped by `.strip_style()`), `'plot_info'` (not
  affected by `.strip_style()`, i.e. keys that may have an important effect on
  the information presented in the figure), or `'object'` (when key is to be linked to
  another object),
  1. `'val_types'`: valid types (e.g. array-like of strings, number: in [0, 1]),
  1. `'description'`: making help helpful!

* Additionally, there are two optional keys: 

  1. `'streamable'`: whether not this key can be streamed using the Streaming
     API,
  1. `'examples'`: list of examples of accepted values for this key.

* Repetition in the meta-generating file should be kept to a minimum.  More
  precisely, meta for keys that are contained in more than 1 object and that
  show significant similarities, is generated using shortcuts. In
  `graph_objs_meta.py`, the meta-generating shortcuts come in two flavors:
  1. functions, named `make_<key>` e.g. `make_x`, used when small discrepancies
  occur from object to object.
  1. dictionaries, named `drop_<key>` e.g. `drop_ visisble`, used when the exact
  same meta is used for all objects containing a particular key.

  Regardless of flavor, all shortcuts are labelled as `@key@` in
  `graph_objs_meta.py` making navigation between objects, keys and shortcuts a
  breeze.
  
### Contributing

Clone and/or pull the latest master version: 
```
$ git pull origin master
```

Make a new branch (for testing purposes) and checkout: 
```
$ git branch your_branch_name
$ git checkout your_branch_name
```

Add and modified keys in `graph_objs_meta.py`:

1. with special attention to existing shortcuts (search for key shortcuts with
   `@key@`),
1. if you are making a new shortcut function use `output` (see `@output@` to
   format the meta dictionary,
1. (more step-by-step info coming soon ...),
1. update the table content in `graph_objs_mets-toc.md` if keys were added or if
   the order was modified.

Generate the JSON files:
```
$ python graph_objs_meta.py
```

Add, commit and push to online repo:
```
$ git add .
$ git commit 
$ git push origin your_branch_name
```
When you push any branch to the online repo, Nose is going to test the
`test_graph_references.py` file. To see if your push passed, go 
[here](https://circleci.com/gh/plotly/graph_reference).

Then, to see the changes made in Plotly's API online documentation:

1. the `graph_reference` submodule in the
   [Python-API](https://github.com/plotly/python-api) needs to be updated and
   tests need to pass,
1. the [Python-API](https://github.com/plotly/python-api) needs to be pushed to
   pip,
1. our backend's `requirements.txt` needs to be updated with the new version of
   the Python-API.

### Glossary

* `#Q`: in `graph_objs_meta.py` these comments refer to questions about Plotly's
  functionality.
* `#TODO!`: in `graph_objs_meta.py` these comments refer to tasks that remain
  to be completed.
* Artifact (or `#ARTIFACT`): Artifact keys are keys that not intended for API
  use (i.e. meant for GUI use), but that must remain part of graph reference to 
  ensure reproducibility. Artifact keys should be placed last in each graph
  objects. 
* Obsolete: Obsolete keys are keys no longer relevant in both from the APIs and
  the GUI. Obsolete keys must be dropped from graph reference.
