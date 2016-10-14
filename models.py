import os
import time
import numpy as np
import pandas as pd

import orca
import pandana as pdna
from urbansim.models import transition
from urbansim.models import relocation
from urbansim.developer import developer
from urbansim.models import RegressionModel
from urbansim.models import MNLDiscreteChoiceModel

import datasources
import variables

@orca.step('relocation_model')
def relocation_model():
    time.sleep(2)
    
@orca.step('transition_model')
def transition_model():
    time.sleep(2)
    
@orca.step('location_choice_model')
def transition_model():
    time.sleep(2)
    
@orca.step('real_estate_price_model')
def transition_model():
    time.sleep(2)
    
@orca.step('real_estate_price_model')
def transition_model():
    time.sleep(2)

@orca.step('real_estate_supply_model')
def transition_model():
    time.sleep(2)

