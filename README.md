# Plotly Graph Reference

*Welcome to the ultimate reference of Plotly's JSON graph format!*

Or just graph reference for short.

Graph reference is used:

- in Plotly's API online documentation:
  [Python](https://plot.ly/python/reference/),
  [MATLAB](https://plot.ly/matlab/reference/)
  [R](https://plot.ly/r/reference/),
  [node.js](https://plot.ly/nodejs/reference/) and
  [Julia](https://plot.ly/julia/reference/)

- in the output of our API libraries' help functions e.g.:

```python
from plotly.graph_objs import Scatter
help(Scatter)
```

- and for graph object key validation (currently in the Python API library and
  possibly in Plotly's backend in the future).

### Philosophy

* All Plotly meta -- for all languages -- is generated using a single
  command! <br>That command is `$ make run`.

+ Although graph objects have the same name in all of Plotly's API library,
  each Plotly API library should have its own meta JSON file, with meta consistent with
  each language's terminology. For example, an underlying JSON object is
  called a dictionary in the Python meta and a structure in the MATLAB meta.

+ Repetition is kept to minimum, to avoid typos and stay sane in the process.

### The graph reference structure

For a given graph object (e.g. `'scatter'` or `'layout'`), its corresponding
meta has the following structure:

```json
{
  "<some-graph_obj>": {
    "name": "Name or type of the graph object",
    "obj_type": "object equivalent" or "array equivalent in given language",
    "parent_keys": [
      "list of keys linking this graph objects"
    ],
    "docstring": "some info about the graph object",
    "examples": [
      "list of short code snippet example(s)"
    ],
    "links": [
      "list of URLs to related api docs pages"
    ],
    "keymeta": { 
      "<some-key>": {
         "key_type": "data" or "style" or "plot_info" or "object", 
         "val_types": "what values are expected for this key",
         "required": "whether this key is required to generate a plot",
         "description": "description of this key's functionality",
         "examples": [
           "list of example(s) of how to define key", 
         ]
         "streamable": (optional) "boolean indicating if key is streamable of not"
     },
     "<some-other-key>": {
        ...
     }
    }
  },
  "<some-other-graph-obj>": {
     ...
  }
}
```

#### Remarks:

  + `'key_type'`: must have either `'data'` (the only keys that remain
     after`.get_data()`), `'style'` (keys that are stripped by `.strip_style()`)
     or `'plot_info'` (keys that not affected by `.strip_style()`, i.e.
     *information specific to a given figure or, in other words, information
     that cannot be transplanted to other figures*) or `'object'` (keys that are
     to be linked to another object).


### Files and folders in this repo:

- `README.md` : this file you're reading

- `CONTRIBUTING.md` : info on how to contribute to this repo

- `scripts/` : all scripts and their inputs used to generate the meta files

- `makefile` : set of shortcut to generate the meta

- `graph_objs/` : generated meta

- `published/` : published content for plot.ly

- `test_graph_reference.py` : test script for `nosetest`

- `circle.yml` : tells Circle to run test

### Want to contribute?

See [`CONTRIBUTING.md`](./CONTRIBUTING.md)
