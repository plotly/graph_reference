# --- learn_tutorial/ makefile ---

# Set (relative or absolute) path to streambed
streambed_path="../streambed"

# -------------------------------------------------------------------------------

# Make graph object meta for all languages!
run:
	@ipython scripts/run.py

# Push graph object meta to streambed
push-to-streambed:
	@rm -rf $(streambed_path)/shelly/templates/api_docs/includes/reference/*
	@cp -R ./graph_objs/* $(streambed_path)/shelly/templates/api_docs/includes/reference/

#push-to-virtualenv:
		
