import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {


'IrOx5' : {
'label' : 'IrO<sub>x</sub>',
'data_PEIS' : 'Data_AEMEL\/2023-06-06 IrOx stefano control\EXP5 PEIS  tafel steps post overnight_01_PEIS_C01.mpr',
'data' : 'Data_AEMEL\/2023-05-16 New Cell IrOx Nafion\EXP 5 CP 24h 5amp_C01.mpr', 
'color_index' : 0,
},

'NiCoFeOx5' : {
'label' : 'NiCoFeO<sub>x</sub>',
'data_PEIS' : 'Data_AEMEL\/2023-05-23 New Cell NiCoFeOx Nafion\EXP 4 PEIS PEIS CA 3h Tafel CP overnight_02_PEIS_C01.mpr',
'data' : 'Data_AEMEL\/2023-05-23 New Cell NiCoFeOx Nafion\EXP 4 PEIS PEIS CA 3h Tafel CP overnight_09_CP_C01.mpr',
'color_index' : 1,
},


'Co57Ni14Fe29Nx5' : {
'label' : 'Co<sub>57</sub>Ni<sub>14</sub>Fe<sub>29</sub>N<sub>x</sub>',
'data_PEIS' : 'Data_AEMEL\/2023-05-17 New Cell Co57Ni14Fe29Nx Nafion\EXP 7 PEIS 18V_C01.mpr',
'data' : 'Data_AEMEL\/2023-05-17 New Cell Co57Ni14Fe29Nx Nafion\EXP 5 CP 24h 5A_C01.mpr',
'color_index' : 2,
},


'Co45Ni45Fe10Nx5' : {
'label' : 'Co<sub>45</sub>Ni<sub>45</sub>Fe<sub>10</sub>N<sub>x</sub>',
'data_PEIS' : 'Data_AEMEL\/2023-05-18 New Cell Co45Ni45Fe10Nx Nafion\EXP 4 PEIS CA Tafel steps CA overnight_02_PEIS_C01.mpr',
'data' : 'Data_AEMEL\/2023-05-18 New Cell Co45Ni45Fe10Nx Nafion\EXP 4 PEIS CA Tafel steps CA overnight_09_CP_C01.mpr',
'color_index' : 6,
},
# '5' : {
# 'Ru' : 1.00,  #measured resistance in ohms
# 'label' : '5',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 4,
# },

# '6' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '6',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 5,
# },

# '7' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '7',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 6,
# },

# '8' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '8',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 7,
# },

# '9' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '9',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '',
# 'fit_min': -5,
# 'fit_max': -1, 
# 'color_index' : 8,
# },

# '10' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '10',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 9,
# },

# '11' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '11',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 10,
# },

# '12' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '12',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 11,
# },

# '13' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '13',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 12,
# },

# '14' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '14',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 13,
# },

# '15' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '15',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 14,
# },

# '16' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '16',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 15,
# },

# '17' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '17',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 16,
# },

# '18' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '18',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 17,
# },

# '19' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '19',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 18,
# },

# '20' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : '20',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'fit_min': -5,
# 'fit_max': -1,
# 'color_index' : 19,
# },


}

