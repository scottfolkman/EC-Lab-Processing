import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

# 'Co50 Ni0 Fe50 300C 2h' : {
# 'Ru' : 1.00,  #measured resistance in ohms
# 'label' : 'Co50 Ni0 Fe50 300C 2h',
# 'cal' : 0.307, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 0,
# },

# 'Co0 Ni50 Fe50 400C 2h' : {
# 'Ru' : 0.68,  #measured resistance in ohms
# 'label' : 'Co0 Ni50 Fe50 400C 2h',
# 'cal' : 0.307, #vs OER
# 'mass' : 1.10,
# 'data_PEIS' : '',
# 'data_CV' : 'Data for ML\Scott\/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_01_CV_C04.mpr',
# 'data_CA' : 'Data for ML\Scott\/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_03_CA_C04.mpr',
# 'data_CP' : '',
# 'data_Tafel' : 'Data for ML\Scott\/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_04_CP_C04.mpr', 
# 'color_index' : 1,
# },

# 'Co25 Ni25 Fe50 600C 2h' : {
# 'Ru' : 1.00,  #measured resistance in ohms
# 'label' : 'Co25 Ni25 Fe50 600C 2h',
# 'cal' : 0.307, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 2,
# },

'Co33 Ni33 Fe33 800C 2h' : {
'Ru' : 0.981,  #measured resistance in ohms
'label' : 'Co33 Ni33 Fe33 800C 2h',
'cal' : 0.307, #vs OER
'mass' : 1.07,
'data_PEIS' : '',
'data_CV' : 'Data for ML\Scott\/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML\Scott\/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML\Scott\/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_Tafel_C01.mpr', # no problems with current
'color_index' : 3,
},

# 'Co50 Ni50 Fe0 300C 6h' : {
# 'Ru' : 1.00,  #measured resistance in ohms
# 'label' : 'Co50 Ni50 Fe0 300C 6h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 4,
# },

# 'Co0 Ni0 Fe100 400C 6h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co0 Ni0 Fe100 400C 6h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 5,
# },

# 'Co25 Ni75 Fe0 600C 6h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co25 Ni75 Fe0 600C 6h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 6,
# },

# 'Co25 Ni0 Fe75 800C 6h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co25 Ni0 Fe75 800C 6h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 7,
# },

# 'Co25 Ni50 Fe25 300C 12h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co25 Ni50 Fe25 300C 12h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 8,
# },

# 'Co100 Ni0 Fe0 400C 12h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co100 Ni0 Fe0 400C 12h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 9,
# },

'Co0 Ni25 Fe75 600C 12h' : {
'Ru' : 0.881, #measured resistance in ohms
'label' : 'Co0 Ni25 Fe75 600C 12h',
'cal' : 0.307, #vs OER
'mass' : 1.01,
'data_PEIS' : '',
'data_CV' : 'Data for ML\Scott\/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML\Scott\/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML\Scott\/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_04_CP_C04.mpr', 
'color_index' : 10,
},

# 'Co0 Ni100 Fe0 800C 12h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co0 Ni100 Fe0 800C 12h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 11,
# },

# 'Co75 Ni25 Fe0 300C 24h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co75 Ni25 Fe0 300C 24h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 12,
# },

'Co50 Ni25 Fe25 400C 24h' : {
'Ru' : 1.22, #measured resistance in ohms
'label' : 'Co50 Ni25 Fe25 400C 24h',
'cal' : 0.307, #vs OER
'mass' : 0.99,
'data_PEIS' : '',
'data_CV' : 'Data for ML\Scott\/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML\Scott\/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML\Scott\/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_04_CP_C01.mpr', 
'color_index' : 13,
},

# 'Co0 Ni75 Fe25 600C 24h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co0 Ni75 Fe25 600C 24h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
# 'color_index' : 14,
# },

# 'Co75 Ni0 Fe25 800C 24h' : {
# 'Ru' : 1.00, #measured resistance in ohms
# 'label' : 'Co75 Ni0 Fe25 800C 24h',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.00,
# 'data_PEIS' : '',
# 'data_CV' : '',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : '', 
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
# 'color_index' : 19,
# },


}

