import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'Co57Ni14Fe29Nx' : {
'Ru' : 0.98, #measured resistance in ohms
'label' : 'Co<sub>57</sub>Ni<sub>14</sub>Fe<sub>29</sub>N<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : 'Data from NMSU/2024-01-22 Co57Ni14Fe29Nx electrolysis 1A cm2_C05.mpr',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 2,
},

'2' : {
'Ru' : 1.00,  #measured resistance in ohms
'label' : '2',
'cal' : 0.307, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : 'Data from NMSU/2024-02-12 Co57Ni14Fe10Nx cont_C05.mpr',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 1,
},

'3' : {
'Ru' : 1.00,  #measured resistance in ohms
'label' : '3',
'cal' : 0.307, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 2,
},

'4' : {
'Ru' : 1.24,  #measured resistance in ohms
'label' : '4',
'cal' : 0.299, #vs OER
'mass' : 1.1,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 3,
},

'5' : {
'Ru' : 1.00,  #measured resistance in ohms
'label' : '5',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 4,
},

'6' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '6',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 5,
},

'7' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '7',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 6,
},

'8' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '8',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 7,
},

'9' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '9',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '',
'fit_min': -5,
'fit_max': -1, 
'color_index' : 8,
},

'10' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '10',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 9,
},

'11' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '11',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 10,
},

'12' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '12',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 11,
},

'13' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '13',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 12,
},

'14' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '14',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 13,
},

'15' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '15',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 14,
},

'16' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '16',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 15,
},

'17' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '17',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 16,
},

'18' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '18',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 17,
},

'19' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '19',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 18,
},

'20' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : '20',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5,
'fit_max': -1,
'color_index' : 19,
},


}

