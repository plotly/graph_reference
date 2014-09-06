import json
import os
import sys
from collections import OrderedDict
from copy import deepcopy
import inflect

import set_run                     
import language_table              
from meta import MakeMeta         
from meta_examples import MakeExamples 

# -------------------------------------------------------------------------------
#
# Generate 
#
# - `graph_objs_meta.json`
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
    '''Retrieve example (language-specific or not) from MakeExamples instances'''
    for obj, stuff in meta.items():
        for k1, v1 in stuff.items():
            if isinstance(v1, MakeExamples):
                meta[obj][k1] = getattr(v1, language)
            elif isinstance(v1, list):
                for i_v2, v2 in enumerate(v1):
                    if isinstance(v2, MakeExamples):
                        meta[obj][k1][i_v2] = getattr(v2, language)
            elif isinstance(v1, (OrderedDict, dict)):
                for k2, v2 in v1.items():
                    for k3, v3 in v2.items():
                        if isinstance(v3, MakeExamples):
                            meta[obj][k1][k2][k3] = getattr(v3, language)
    return meta

def make_tables(table):
    '''Make indefinite article, plural table complement to vocab table'''
    a_table = A_table = pl_table = dict()
    p = inflect.engine()
    for k,v in table.items():    # make new table using inflect
        a_table['a_'+k] = p.a(v)
        A_table['A_'+k] = p.a(v).capitalize()
        pl_table['pl_'+k] = p.plural(v)
    tables = dict(
        table.items() + a_table.items() + A_table.items() + pl_table.items()
    )
    return tables

def format_meta_vocab(meta, tables):
    '''Format meta to language-specific vocabulary (set in language_table.py)'''
    for obj, stuff in meta.items():
        for k1, v1 in stuff.items():
            if isinstance(v1, str):
                v1_format = v1.format(**tables)
                meta[obj][k1] = v1_format
            elif isinstance(v1, list):
                for i_v2, v2 in enumerate(v1):
                    if isinstance(v2, str):
                        v2_format = v2.format(**tables)
                        meta[obj][k1][i_v2] = v2_format
            elif isinstance(v1, tuple):
                for i_v2, v2 in enumerate(v1[1]):
                    if isinstance(v2, str):
                        v2_format = v2.format(**tables)
                        meta[obj][k1][1][i_v2] = v2_format
            elif isinstance(v1, (OrderedDict, dict)):
                for k2, v2 in v1.items():
                    for k3, v3 in v2.items():
                        if isinstance(v3, str):
                            v3_format = v3.format(**tables)
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

def write_NAME_TO_KEY(tree, meta_language):
    '''
    Write mapping from name of graph object its parent key 
    in graph_objs/python/NAME_TO_KEY.json
    '''
    NAME_TO_KEY = dict()
    for obj, stuff in meta_language.items():
        NAME_TO_KEY[stuff['name']] = obj
    file_NAME_TO_KEY = os.path.join(tree, "NAME_TO_KEY.json")
    with open(file_NAME_TO_KEY, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_NAME_TO_KEY
        json.dump(NAME_TO_KEY, f, indent=4, sort_keys=False)

def write_KEY_TO_NAME(tree, meta_language):
    '''
    Write mapping from parent key to name of graph object
    in graph_objs/python/KEY_TO_NAME.json
    '''
    KEY_TO_NAME = dict()
    for obj, stuff in meta_language.items():
        parent_keys = stuff['parent_keys']
        if parent_keys:
            for parent_key in parent_keys:
                KEY_TO_NAME[parent_key] = stuff['name']
        else:
            KEY_TO_NAME[obj] = stuff['name']
    file_KEY_TO_NAME = os.path.join(tree, "KEY_TO_NAME.json")
    with open(file_KEY_TO_NAME, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_KEY_TO_NAME
        json.dump(KEY_TO_NAME, f, indent=4, sort_keys=False)

def write_config(graph_objs_info):
    '''
    Write config file for plot.ly/<lang>/reference,
    remove graph object with no description from the to be displayed list 
    and the table of content
    '''
    _info = [info 
            for info in graph_objs_info.values() if info['description']]
    _graph_objs = [graph_obj 
                  for __info in _info 
                  for graph_obj in __info['graph_objs']]
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
    graph_objs_info = set_run.graph_objs_info()
    graph_objs = set_run.graph_objs()

    # Make instance of MakeMeta object and get graph object meta!
    meta_make = MakeMeta()
    meta = get_meta(graph_objs, meta_make)

    for language in languages:

        # Make deep copy of language-agnostic meta
        meta_language = deepcopy(meta)
        
        # Retrieve examples from Examples class
        meta_language = retrieve_examples(meta_language, language)
        
        # Get language tables and format meta respectively to each language
        table = language_table.table[language]
        tables = make_tables(table)
        meta_language = format_meta_vocab(meta_language, tables)

        # Make/Check output tree structure
        tree = get_tree(language)

        # Write meta 
        write_meta(tree, meta_language)

        # Write NAME_TO_KEY and KEY_TO_NAME (if 'python')
        if language=='python':
            write_NAME_TO_KEY(tree, meta_language)
            write_KEY_TO_NAME(tree, meta_language)
    
    # Write plot.ly config in JSON files
    write_config(graph_objs_info) 

if __name__ == '__main__':
    main()
