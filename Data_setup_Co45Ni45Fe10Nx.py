import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'Co45Ni45Fe10Nx Scott Elect1' : {
'Ru' : 0.90,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Scott Elect1',
'cal' : 0.307, #vs OER
'mass' : 1.0,
'data_PEIS' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_01_PEIS_C05.mpr',
'data_CV' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_02_CV_C05.mpr',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 0,
},

'Co45Ni45Fe10Nx Scott Elect2' : {
'Ru' : 1.58,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Scott Elect2',
'cal' : 0.307, #vs OER
'mass' : 0.97,
'data_PEIS' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 2_PEIS_C05.mpr',
'data_CV' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 2_01_CV_C01.mpr',
'data_CA' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 2_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 1,
},

'Co45Ni45Fe10Nx Scott Elect3' : {
'Ru' : 1.48,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Scott Elect3',
'cal' : 0.307, #vs OER
'mass' : 1.06,
'data_PEIS' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 3_PEIS_C05.mpr',
'data_CV' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 3_01_CV_C01.mpr',
'data_CA' : 'Co45Ni45Fe10Nx 1 mg\Scott\/2023_02_16_Co45Ni45Fe10Nx 1mg ref307_elect 3_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 2,
},

'Co45Ni45Fe10Nx Lola Elect1' : {
'Ru' : 1.24,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Lola Elect1',
'cal' : 0.299, #vs OER
'mass' : 1.1,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 3,
},

'Co45Ni45Fe10Nx Lola Elect2' : {
'Ru' : 1.38,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Lola Elect2',
'cal' : 0.299, #vs OER
'mass' : 1.22,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 4,
},

'Co45Ni45Fe10Nx Lola Elect3' : {
'Ru' : 1.1,  #measured resistance in ohms
'label' : 'Co45Ni45Fe10Nx Lola Elect3',
'cal' : 0.299, #vs OER
'mass' : 0.95,
'data_PEIS' : '',
'data_CV' : '',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : '', 
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
'color_index' : 19,
},


}

