import os
import yaml
import pandas as pd

import orca
from urbansim.utils import misc
from urbansim.utils import yamlio

def register_config_injectable_from_yaml(injectable_name, yaml_file):
    @orca.injectable(injectable_name, cache=True)
    def func():
        with open(os.path.join(misc.configs_dir(), yaml_file)) as f:
            config = yaml.load(f)
            return config
    return func

def register_table_from_csv(table_name):
    @orca.table(table_name, cache=True)
    def func(store):
        return pd.read_csv('./data/%s.csv' % table_name)
    return func

# Tables from data-store
for table in ['jobs', 'households', 'persons', 'zones', 'residential_units', 'nodes', 'edges', 
              'annual_household_control_totals', 'annual_household_relocation_rates']:
    register_table_from_csv(table)

# Configs
for yaml_file in ["settings.yaml", "model_structure.yaml"]:
    injectable_name = yaml_file.split('.')[0]
    register_config_injectable_from_yaml(injectable_name, yaml_file)


@orca.injectable('year')
def year():
    default_year = 2010
    try:
        iter_var = orca.get_injectable('iter_var')
        if iter_var is not None:
            return iter_var
        else:
            return default_year
    except:
        return default_year
