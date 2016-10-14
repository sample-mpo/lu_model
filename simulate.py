import os
import time
import yaml

import orca
from urbansim.utils import misc

import output

################# CONFIG #############################################
def register_config_injectable_from_yaml(injectable_name, yaml_file):
    @orca.injectable(injectable_name, cache=True)
    def func():
        with open(os.path.join(misc.configs_dir(), yaml_file)) as f:
            config = yaml.load(f)
            return config
    return func

for yaml_file in ["settings.yaml", "model_structure.yaml"]:
    injectable_name = yaml_file.split('.')[0]
    register_config_injectable_from_yaml(injectable_name, yaml_file)

settings = orca.get_injectable('settings')
ms = orca.get_injectable('model_structure')

step_sequence = ms['step_sequence']
step_sequence = [step for pair in zip(step_sequence,['sim_progress_by_step']*len(step_sequence)) for step in pair]
print step_sequence

run_id = 1552
orca.add_injectable('run_id', run_id)
forecast_year = 2012
orca.add_injectable('forecast_year', forecast_year)

#log start
output.log_start(run_id, 2010, forecast_year)

################# USER CODE (RUN SIMULATION) #############################################

# Record start time
start_time = time.time()
orca.add_injectable('start_time', start_time)

output.sim_start_status()

for f in settings['orca_registry_modules']:
    exec 'import %s' % f

output.sim_start_status()
 
orca.run(step_sequence, iter_vars = range(2011, forecast_year + 1))

output.sim_end_status()

# Record end time
end_time = time.time()
time_elapsed = end_time - start_time
print 'Simulation duration: %s minutes' % (time_elapsed/60)

#####################################################

#log finish
output.log_finish(run_id, 2010, forecast_year)
