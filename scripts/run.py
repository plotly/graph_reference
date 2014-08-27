# Import set functions!
import set_run

# Import meta-generating methods!
import meta 

from collections import OrderedDict
import json
import os

# -------------------------------------------------------------------------------
#
# Run all the meta-generating methods of `meta.py` for each language and
# write to a json file.
#
# -------------------------------------------------------------------------------

NAME = "run"  # name of this script


def get_meta(graph_objs, meta_language, language):
    '''Apply each method of MetaMake class to the language-specific instance'''
    for graph_obj in graph_objs:
        eval('meta_language.'+graph_obj+'()')
    print "[{}]".format(NAME), 'Generating meta for {}'.format(language)
    return meta_language
    
# -------------------------------------------------------------------------------

def get_tree(language):
    '''Get language-specific output tree'''
    tree = os.path.join("./graph_objs",language)  # from repo parent
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'
    return tree

def write_meta(tree, meta_language):
    '''Write meta to <tree>/graph_objs_meta.json'''
    meta_to_dump = OrderedDict(meta_language)
    file_meta = os.path.join(tree, "graph_objs_meta.json")
    with open(file_meta, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_meta
        json.dump(meta_to_dump, f, indent=4, sort_keys=False)
    return

def write_objs_keys(tree, meta_language):
    '''Write keys to <tree>/graph_objs_keys.json'''
    meta_to_dump = OrderedDict(meta_language)
    _obj_keys = dict()
    for obj, stuff in meta_to_dump.items():
        _obj_keys[obj] = stuff['meta'].keys()
        _obj_keys[obj].sort()
    file_keys = os.path.join(tree, "graph_objs_keys.json")
    with open(file_keys, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_keys
        json.dump(_obj_keys, f, indent=4, sort_keys=True)

def write_config(graph_objs_info):
    '''
    Write config file for plot.ly/<lang>/reference,
    remove graph object with no description from the to be displayed list 
    and the table of content
    '''
    _info = [info for info in graph_objs_info if info['description']]
    _graph_objs = [name for __info in _info for name in __info['names']]
    _config = dict(
        graph_objs=_graph_objs,
        toc=_info
    )
    file_config = os.path.join("./graph_objs/config.json")
    with open(file_config, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_config
        json.dump(_config, f, indent=4, sort_keys=True)
    return

# -------------------------------------------------------------------------------

def main():

    languages = set_run.languages()
    graph_objs_info, graph_objs = set_run.graph_objs()

    for language in languages:

        meta_language = meta.MakeMeta(language)
        meta_language = get_meta(graph_objs, meta_language, language)

        tree = get_tree(language)
        write_meta(tree, meta_language)
        write_objs_keys(tree, meta_language) 
        write_config(graph_objs_info) 

if __name__ == '__main__':
    main()
