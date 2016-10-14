import numpy as np
import pandas as pd

import orca

import datasources

@orca.column('households', 'age_cat', cache=True)
def age_cat(households):
    return 1*(households.age_of_head<=35) + 2*(households.age_of_head>35)*(households.age_of_head<=60) + 3*(households.age_of_head>60)

@orca.column('households', 'hhsize3plus', cache=True)
def hhsize3plus(households):
    return (households.persons>2).astype('int32')

@orca.column('households', 'hhsize2', cache=True)
def hhsize2(households):
    return (households.persons==2).astype('int32')

@orca.column('households', 'young', cache=True)
def young(households):
    return (households.age_cat==1).astype('int32')

@orca.column('households', 'middle_age', cache=True)
def middle_age(households):
    return (households.age_cat==2).astype('int32')

@orca.column('households', 'old', cache=True)
def old(households):
    return (households.age_cat==3).astype('int32')

@orca.column('households', 'with_child', cache=True)
def with_child(households):
    return (households.children>0).astype('int32')

@orca.column('households', 'with_car', cache=True)
def with_car(households):
    return (households.cars>0).astype('int32')

@orca.column('households', 'income_quartile', cache=True)
def income_quartile(households):
    s = pd.Series(pd.qcut(households.income, 4, labels=False),
                  index=households.index)
    s = s.add(1)
    return s
