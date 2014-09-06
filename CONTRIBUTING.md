# How to contribute?

For most cases, it is as easy as changing the value of the right key and running
`$ make run`. 


### What inside `scripts/` ?

- `set_run.py` : input languages and graph objects 
- `language_table.py` : input language vocabulary table
- `meta.py` : meta-generating functions for each graph object
- `meta_shortcuts.py` : meta-generating shortcuts
- `meta_examples.py` : examples (or code snippets) 
- `run.py` : generate, format and write meta for all languages


### More philosophy ...

Repetition in meta-generating files should be kept to a minimum.  

More precisely, key meta that are contained in more than one graph object and
that show significant similarities, are generated using shortcuts. All
shortcuts methods are labelled as `@key@` in `meta_shortcuts.py` making
navigation between objects, keys and shortcuts a breeze.  

In addition, language-specific vocabulary is inserted using Python `.format()`
method for string. Insert `{TERM}` in accordance with language table defined in
`language_table.py` and the its variations (i.e. indefinite articles, plurals
etc.) built in `run.py`.


### Common cases

Before each case, make sure to pull the latest master and check out to a new
branch.

#### Case A: Modify meta of an existing graph object

- Open `meta.py` and search for `@<graph-object>@`. This will take you to the
   meta-generating method for this particular graph object.

If the meta field in question is set in `meta.py` (i.e. without a shortcut),
modify it, save `meta.py`, run `$ make run` and you are done!

- If the meta field is generated using a shortcut, open `meta_shortcuts.py` and
   search for `@<graph-object-field>@`. This will take you to the meta-generating
   shortcut method for this particular key.

Modify it, save `meta_shortcuts.py`, run `$ make run` and you are done!
 
#### Case B: Add new key

1. Determine whether this new key has an equivalent for other graph object. You
   can easily do so by searching for `'<key>'` in `meta.py` or `@<key>@` in
   `meta_shortcuts.py`.

If so, link this key in `meta.py` to the appropriate `make` method and modify
the this `make` method accordingly ...

- if you are making a new shortcut function use `output` (see `@output@` to
   format the meta dictionary,
   
(more step-by-step info coming soon ...),

#### Case C: Add new graph objects

(coming soon) 

#### Case D: Add/Modify language vocabulary table

After all cases, commit the changes and make a PR to the online repo.


### Testing

When you push any branch to the online repo, Nose is going to test the
`test_graph_references.py` file. 

To see if your push passed, go
[here](https://circleci.com/gh/plotly/graph_reference).


### Updating the online reference pages

Pull the latest master version of `streambed/` and check out to a new branch.
Then,

- run `$ make push-to-streambed` in `graph_reference`

and you are done!


### Updating the Python API

(need to update this section)

1. The `graph_reference` submodule in the
   [Python-API](https://github.com/plotly/python-api) needs to be updated and
   tests need to pass

1. The [Python-API](https://github.com/plotly/python-api) needs to be pushed to
   pip,

1. Our backend's
   [`requirements.txt`](https://github.com/plotly/streambed/blob/master/requirements.txt)
   needs to be updated with the new version of the Python-API.


### Seeing something not quite right?

Please create a new task on the Asana
[project](https://app.asana.com/0/14961561647922/14961561647922).

You can also comment in the `scripts/` files using the following terminology:

- `#Q`: in `graph_objs_meta.py` these comments refer to questions about Plotly's
  functionality.

- `#TODO`: in `graph_objs_meta.py` these comments refer to tasks that remain
  to be completed.

- Artifact (or `#ARTIFACT`): Artifact keys are keys that not intended for API
  use (i.e. meant for GUI use), but that must remain part of graph reference to 
  ensure reproducibility. Artifact keys should be placed last in each graph
  objects. 

- Obsolete: Obsolete keys are keys no longer relevant in both from the APIs and
  the GUI. Obsolete keys must be dropped from graph reference.
