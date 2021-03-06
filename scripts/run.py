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
# for each language! Along with a few subset json files.
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
        getattr(meta_make,graph_obj)()
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

# -------------------------------------------------------------------------------

def get_trees(language):
    '''Get language-specific output trees'''
    tree_graph_objs = os.path.join("./graph_objs", language)  
    tree_published = os.path.join("./published", language)  
    for tree in [tree_graph_objs, tree_published]:
        if not os.path.exists(tree):
            print "[{}]".format(NAME), '... making', tree
            os.makedirs(tree)
        else:
            print "[{}]".format(NAME), '...', tree, 'already exists OK'
    return tree_graph_objs, tree_published


def write_meta(tree, meta_language):
    '''Write meta to <tree>/graph_objs_meta.json'''
    file_meta = os.path.join(tree, "graph_objs_meta.json")
    with open(file_meta, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_meta
        json.dump(meta_language, f, indent=4, sort_keys=False)
    return

def write_keymeta(tree, meta_language):
    '''Write keymeta to <tree>/graph_objs_keymeta.json'''
    _keymeta = []
    for obj, stuff in meta_language.items():
        _keymeta += [(obj, stuff['keymeta'])]
    _keymeta = OrderedDict(_keymeta)
    file_keymeta = os.path.join(tree, "graph_objs_keymeta.json")
    with open(file_keymeta, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_keymeta
        json.dump(_keymeta, f, indent=4, sort_keys=False)
    return

def write_NAME_TO_KEY(tree, meta_language):
    '''
    Write mapping from name of graph object its parent key 
    in graph_objs/<lang>/NAME_TO_KEY.json
    '''
    _NAME_TO_KEY = dict()
    for obj, stuff in meta_language.items():
        _NAME_TO_KEY[stuff['name']] = obj
    file_NAME_TO_KEY = os.path.join(tree, "NAME_TO_KEY.json")
    with open(file_NAME_TO_KEY, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_NAME_TO_KEY
        json.dump(_NAME_TO_KEY, f, indent=4, sort_keys=False)
    return _NAME_TO_KEY


def write_KEY_TO_NAME(tree, meta_language):
    '''
    Write mapping from parent key to name of graph object
    in graph_objs/<lang>/KEY_TO_NAME.json
    '''
    _KEY_TO_NAME = dict()
    for obj, stuff in meta_language.items():
        parent_keys = stuff['parent_keys']
        if parent_keys:
            for parent_key in parent_keys:
                _KEY_TO_NAME[parent_key] = stuff['name']
        else:
            _KEY_TO_NAME[obj] = stuff['name']
    file_KEY_TO_NAME = os.path.join(tree, "KEY_TO_NAME.json")
    with open(file_KEY_TO_NAME, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_KEY_TO_NAME
        json.dump(_KEY_TO_NAME, f, indent=4, sort_keys=False)
    return _KEY_TO_NAME


def write_PARENT_TREE(tree, meta_language):
    '''
    Write parent tree (label by their name) for given key
    in graph_objs/<lang>/KEY_TO_NAME.json
    '''
    _PARENT_TREE = dict()
    for obj, stuff in meta_language.items():
        _PARENT_TREE[obj] = dict()
        for parent_key in stuff['parent_keys']:
            _PARENT_TREE[obj][parent_key] = []
            for _ , _stuff in meta_language.items():
                for k,v in _stuff['keymeta'].items():
                    if parent_key == k:
                        if 'key_type' in v.keys():
                            if v['key_type'] == "object":
                                _PARENT_TREE[obj][parent_key] += [_stuff['name']]
    file_PARENT_TREE = os.path.join(tree, "PARENT_TREE.json")
    with open(file_PARENT_TREE, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_PARENT_TREE
        json.dump(_PARENT_TREE, f, indent=4, sort_keys=False)
    return _PARENT_TREE

def write_OBJ_MAP(tree, meta_language, graph_objs_info_language, tables):
    '''
    Write object map to 'basename' and 'info_key', an input of the
    class factories in the python API
    '''
    _OBJ_MAP = dict()
    for obj, stuff in meta_language.items():
        if stuff['obj_type'] == tables['UL']:
            if obj in graph_objs_info_language['trace']['graph_objs']:
                _base_name = 'PlotlyTrace'
            else:
                _base_name = 'PlotlyDict'
        elif stuff['obj_type'] == tables['OL']:
            _base_name = 'PlotlyList'
        else:
            print "[{}]".format(NAME), 'Weird obj_type at:', obj
            print "[{}]".format(NAME), '... execution stopped'
            sys.exit(0)
        _info_key = obj
        _OBJ_MAP[stuff['name']] = dict(
            base_name=_base_name,
            info_key=_info_key
        )
    file_OBJ_MAP = os.path.join(tree, "OBJ_MAP.json")
    with open(file_OBJ_MAP, 'w') as f:
        print "[{}]".format(NAME), '... writes in', file_OBJ_MAP
        json.dump(_OBJ_MAP, f, indent=4, sort_keys=False)
    return _OBJ_MAP


def write_config(tree, lang, graph_objs_info, meta,
                 KEY_TO_NAME, PARENT_TREE):
    '''
    Write config file for plot.ly/<lang>/reference, 
    patching together table of content and language-specific meta,
    remove graph object with no description from the to be displayed list 
    and the table of content.
    '''
    _INFO = [info 
            for info in graph_objs_info.values() 
            if info['description']]
    _graph_objs_NAME = [KEY_TO_NAME[graph_obj]
                   for __INFO in _INFO 
                   for graph_obj in __INFO['graph_objs']]
    for _i, _info in enumerate(_INFO):
        for _g, graph_obj in enumerate(_info['graph_objs']):
            _meta = meta[graph_obj]
            # - Each graph_obj is labelled by their 'name'
            label = meta[graph_obj]['name']
            # - Replace link addresses to relative
            _link = []
            for link in _meta['links']:
                _link += [link.replace('https://plot.ly','')]
            _meta['links'] = _link
            # - Add parent tree leaves to object meta
            _PARENT_TREE = dict()
            for _k, _vals in PARENT_TREE[graph_obj].items():
                _PARENT_TREE[_k] = []
                for _val in _vals:
                    if _val in _graph_objs_NAME:
                        _PARENT_TREE[_k] += [_val]
            _meta['parent_tree'] = _PARENT_TREE
            # - Add child object to keymeta (if any)
            for _k in _meta['keymeta'].keys():
                if _k in KEY_TO_NAME.keys():
                    _meta['keymeta'][_k]['child_obj'] = KEY_TO_NAME[_k]
            # - Replace ordered dict of keymeta with list of dicts 
            #   (easier to deal with in django)
            _keymeta = []
            for _k, _v in _meta['keymeta'].items():
                _keymeta += [{_k: _v}]
            _meta['keymeta'] = _keymeta
            # Copy resulting _meta in dict linked to 'label'
            _INFO[_i]['graph_objs'][_g] = {label: _meta}
    # Write config!
    _config = _INFO
    file_config = os.path.join(tree, "config.json")
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

        # Make/Check output tree structures
        tree_graph_objs, tree_published = get_trees(language)

        # Make deep copy of language-agnostic meta and graph_objs_info
        meta_language = deepcopy(meta)
        graph_objs_info_language = deepcopy(graph_objs_info)
        
        # Retrieve examples from Examples class
        meta_language = retrieve_examples(meta_language, language)
        
        # Get language tables and format meta respectively to each language
        table = language_table.table[language]
        tables = make_tables(table)
        meta_language = format_meta_vocab(meta_language, tables)

        # Write meta and keymeta
        write_meta(tree_graph_objs, meta_language)
        write_keymeta(tree_graph_objs, meta_language)
        
        # Write NAME_TO_KEY, KEY_TO_NAME, PARENT_TREE
        NAME_TO_KEY = write_NAME_TO_KEY(tree_graph_objs, meta_language)
        KEY_TO_NAME = write_KEY_TO_NAME(tree_graph_objs, meta_language)
        PARENT_TREE = write_PARENT_TREE(tree_graph_objs, meta_language)

        # Write OBJ_MAP (python only)
        if language == 'python':
            OBJ_MAP = write_OBJ_MAP(tree_graph_objs,
                                    meta_language,
                                    graph_objs_info_language, tables)

        # Make\Write meta+toc config file (for plot.ly)
        write_config(tree_published, language, 
                     graph_objs_info_language, 
                     meta_language,
                     KEY_TO_NAME, PARENT_TREE) 

if __name__ == '__main__':
    main()
