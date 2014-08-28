import json
import os
import sys
from collections import OrderedDict
from copy import deepcopy

import set_run                     
import language_table              
from meta import MakeMeta         
from meta_examples import MakeExamples 

# -------------------------------------------------------------------------------
#
# Generate 
#
# - `graph_objs_meta.json`, 
# - `graph_objs_keys.json` 
# - `config.json`
#
# for each language!
#
# -------------------------------------------------------------------------------

NAME = "run"  # name of this script

# -------------------------------------------------------------------------------

def get_meta(graph_objs, meta_make):
    '''
    Apply each graph object method to a MetaMake instance, 
    package result in OrderedDict().
    '''
    for graph_obj in graph_objs:
        eval('meta_make.'+graph_obj+'()')
    meta = OrderedDict(meta_make)
    return meta
    
# -------------------------------------------------------------------------------

def retrieve_examples(meta, language):
    '''Retrieve example (language-specific or not) from MakeExamples class'''
    for obj, stuff in meta.items():
        for k1, v1 in stuff.items():
            if isinstance(v1, MakeExamples):
                meta[obj][k1] = getattr(v1, language)
            elif isinstance(v1, list):
                for i_v2, v2 in enumerate(v1):
                    if isinstance(v1, MakeExamples):
                        meta[obj][k1][i_v2] = getattr(v2, language)
            elif isinstance(v1, (OrderedDict, dict)):
                for k2, v2 in v1.items():
                    for k3, v3 in v2.items():
                        if isinstance(v3, MakeExamples):
                            meta[obj][k1][k2][k3] = getattr(v3, language)
    return meta

def format_meta(meta, table):
    '''Format meta to language-specific vocabulary'''
    for obj, stuff in meta.items():
        obj_format = obj.format(**table)
        meta[obj_format] = meta.pop(obj, None)
        for k1, v1 in stuff.items():
            if isinstance(v1, str):
                v1_format = v1.format(**table)
                meta[obj][k1] = v1_format
            elif isinstance(v1, list):
                for i_v2, v2 in enumerate(v1):
                    if isinstance(v2, str):
                        v2_format = v2.format(**table)
                        meta[obj][k1][i_v2] = v2_format
            elif isinstance(v1, (OrderedDict, dict)):
                for k2, v2 in v1.items():
                    for k3, v3 in v2.items():
                        if isinstance(v3, str):
                            v3_format = v3.format(**table)
                            meta[obj][k1][k2][k3] = v3_format
            else:
                print "[{}]".format(NAME), 'Weird meta format at:', obj, k1
                print "      ... meta['']['']: ", v1
                print "[{}]".format(NAME), '... execution stopped'
                sys.exit(0)
    return meta

def get_tree(language):
    '''Get language-specific output tree'''
    tree = os.path.join("./graph_objs",language)  # N.B. from repo parent
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'
    return tree

def write_meta(tree, meta_language):
    '''Write meta to <tree>/graph_objs_meta.json'''
    file_meta = os.path.join(tree, "graph_objs_meta.json")
    with open(file_meta, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_meta
        json.dump(meta_language, f, indent=4, sort_keys=False)
    return

def write_objs_keys(tree, meta_language):
    '''Write keys to <tree>/graph_objs_keys.json'''
    _obj_keys = dict()
    for obj, stuff in meta_language.items():
        _obj_keys[obj] = stuff['keymeta'].keys()
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

    # Get list of languages 
    languages = set_run.languages()

    # Get list of graph objects and graph object info 
    graph_objs_info, graph_objs = set_run.graph_objs()

    # Make instance of MakeMeta object and get graph object meta!
    meta_make = MakeMeta()
    meta = get_meta(graph_objs, meta_make)

    for language in languages:

        # Make deep copy of language-agnostic meta
        meta_language = deepcopy(meta)
        
        # Retrieve examples from Examples class
        meta_language = retrieve_examples(meta_language, language)
        
        # Get language table and format meta respectively to each language
        table = language_table.table[language]
        meta_language = format_meta(meta_language, table)

        # Make/Check output tree structure
        tree = get_tree(language)

        # Write meta, keys and plot.ly config in JSON files
        write_meta(tree, meta_language)
        write_objs_keys(tree, meta_language) 
        write_config(graph_objs_info) 

if __name__ == '__main__':
    main()
