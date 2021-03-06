# --- learn_tutorial/ makefile ---

# Set (relative or absolute) path to streambed
streambed_path="../streambed"

# Set (relative or absolute) path to python-api
python_api_path="../python-api"

# -------------------------------------------------------------------------------

# Make graph object meta for all languages!
run:
	@ipython scripts/run.py

# Push graph object meta to streambed
push-to-streambed:
	@rm -rf $(streambed_path)/shelly/templates/api_docs/includes/reference/*
	@cp -R ./published/* $(streambed_path)/shelly/templates/api_docs/includes/reference/

# Push to graph object meta to python-api (for testing)
push-to-python-api:
	@rm -rf ${python_api_path}/plotly/graph_reference/*
	@cp ./graph_objs/python/graph_objs_meta.json $(python_api_path)/plotly/graph_reference/
	@cp ./graph_objs/python/KEY_TO_NAME.json $(python_api_path)/plotly/graph_reference/
	@cp ./graph_objs/python/NAME_TO_KEY.json $(python_api_path)/plotly/graph_reference/
	@cp ./graph_objs/python/OBJ_MAP.json $(python_api_path)/plotly/graph_reference/




#push-to-virtualenv:
		
