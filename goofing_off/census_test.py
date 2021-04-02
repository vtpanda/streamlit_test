import pandas as pd

values = pd.read_csv('goofing_off/data/ACS_16_1YR_S2301_with_ann.csv')
metadata = pd.read_csv('goofing_off/data/ACS_16_1YR_S2301_metadata.csv')

values = pd.melt(values, id_vars=['GEO.id', 'GEO.id2', 'GEO.display-label'], value_name="Measure", var_name="Variable")

values = pd.merge(values, metadata, left_on=['Variable'], right_on=['GEO.id'], how='left', sort=False, suffixes=('_x', '_y'), validate="m:1")

values = values.drop(columns=['GEO.id_y'])

values = values.add(values['Id'].str.split(pat=';', n=3, expand=True))