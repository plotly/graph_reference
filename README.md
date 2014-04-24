The ultimate reference of Plotly's JSON graph format.

Used as the help reference in [Plotly-Python library](https://github.com/plotly/python-api) and in [Plotly's web documentation](https://plot.ly/api/rest).

#### Format

A fully described `key` is an object with the keys: `val_types`, `required`, `type`, `description`. 
- `val_types`: Valid types (e.g. `array_like of strings`, `number: in [0, 1]`)
- `required`: Whether the key is required or not to create the chart type
- `type`: `style` | `plot_info` | `object` | `data`
- `description`: Self explanatory 

#### Contributing
1 - Add and modifie keys in the `graph_objs_meta.py` file.  There are a bunch of shortcuts in that file, so you might have to hunt around a bit to check if something was already defined or not.

2 - Generate JSON and commit and push
```bash
$ make push
```
This will generate the JSON files automatically, commit, and push to the repo.
