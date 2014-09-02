import json

# -------------------------------------------------------------------------------
#
# Each dictionary is represented with KEYS and VALS i.e. dict(KEY=VAL),
# to avoid confusion with graph objs key, keymeta, etc ...
#
# -------------------------------------------------------------------------------

# Only need to test one output file (they all have the same keys)
with open('./graph_objs/python/graph_objs_meta.json') as f:
    META = json.load(f)

# -------------------------------------------------------------------------------

graph_obj_meta_KEYS = [
    'name',
    'obj_type',
    'parent_keys',
    'docstring',
    'examples',
    'links',
    'keymeta'
]

graph_obj_key_KEYS = [
    'key_type',
    'required',
    'val_types',
    'description',
    'examples',
    'streamable'
]

graph_obj_key_type_VALS = [
    'data', 
    'plot_info',
    'style',
    'object'
]

# -------------------------------------------------------------------------------

def test_meta_KEYS():
    print "\n\ntesting if graph objs KEYS are in graph_objs_meta_KEYS\n"
    checks = True
    for graph_obj, graph_obj_meta in META.items():
        for graph_obj_meta_KEY in graph_obj_meta.keys():
            if graph_obj_meta_KEY not in graph_obj_meta_KEYS:
                checks = False
                print (
                    "You have a graph_obj_meta_KEY ('{}') not part "
                    "graph_obj_meta_KEYS at: {}"
                ).format(graph_obj_meta_KEY, graph_obj)
        for graph_obj_meta_KEY in graph_obj_meta_KEYS:
            if graph_obj_meta_KEY not in graph_obj_meta.keys():
                checks = False
                print (
                    "You are missing the '{}' graph_obj_meta_KEY at: {} "
                ).format(graph_obj_meta_KEY, graph_obj)
    if not checks:
        raise Exception

def test_key_KEYS():
    print "\n\ntesting if graph objs key KEYS are graph_objs_key_KEYS\n"
    checks = True
    for graph_obj, graph_obj_meta in META.items():
        if graph_obj != 'trace':
            KEYMETA = graph_obj_meta['keymeta']
            for graph_obj_key, graph_obj_keymeta in KEYMETA.items():
                for graph_obj_key_KEY in graph_obj_keymeta.keys():
                    if graph_obj_key_KEY not in graph_obj_key_KEYS:
                        checks = False
                        print (
                            "You have a graph_obj_key_KEY ('{}')"
                            "not part graph_obj_key_KEYS at: {}.{}", 
                        ).format(graph_obj_key_KEY, graph_obj, graph_obj_key)
                for graph_obj_key_KEY in graph_obj_key_KEYS[0:-2]:
                    if graph_obj_key_KEY not in graph_obj_keymeta.keys():
                        checks = False
                        print (
                            "You are missing the '{}' graph_obj_key_KEY "
                            "at: {}.{}"
                        ).format(graph_obj_key_KEY, graph_obj, graph_obj_key),
    if not checks:
        raise Exception

def test_key_type_VALS():
    print "\n\ntesting if graph objs key 'type' VALS are graph_objs_key_type_VALS\n"
    checks = True
    for graph_obj, graph_obj_meta in META.items():
        if graph_obj != 'trace':
            KEYMETA = graph_obj_meta['keymeta']
            for graph_obj_key, graph_obj_keymeta in KEYMETA.items():
                for graph_obj_key_KEY, graph_obj_key_VAL in graph_obj_keymeta.items():
                    if graph_obj_key_KEY == 'type':
                        if graph_obj_key_VAL not in graph_obj_key_type_VALS:
                            checks = False
                            print (
                                "You have a graph_obj_key_type_VAL ('{}') not part "
                                'graph_obj_key_type_VALS at: {}.{}.{}'
                            ).format(graph_obj_key_VAL, graph_obj, graph_obj_key,'type')
    if not checks:
        raise Exception
