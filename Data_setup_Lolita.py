import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'Co25Ni25Fe50 600C 2h Elect1' : {
'Ru' : 1.24,  #measured resistance in ohms
'label' : 'Elect1',
'cal' : 0.299, #vs OER
'mass' : 1.1,
'data_PEIS' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode1_30012023_C05.mpr',
'data_CV' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode1_30012023_1_01_CV_C02.mpr',
'data_CA' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode1_30012023_1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 0,
},

'Co25Ni25Fe50 600C 2h Elect2' : {
'Ru' : 1.38,  #measured resistance in ohms
'label' : 'Elect2',
'cal' : 0.299, #vs OER
'mass' : 1.22,
'data_PEIS' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode2_30012023_C05.mpr',
'data_CV' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode2_30012023_1_01_CV_C02.mpr',
'data_CA' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode2_30012023_1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 1,
},

'Co25Ni25Fe50 600C 2h Elect3' : {
'Ru' : 1.1,  #measured resistance in ohms
'label' : 'Elect3',
'cal' : 0.299, #vs OER
'mass' : 0.95,
'data_PEIS' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode3_30012023_C05.mpr',
'data_CV' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode3_30012023_1_01_CV_C02.mpr',
'data_CA' : 'Nitrides\CoNiFeNx_600_2h_30012023/2023_01_31_CoNiFeNx_600ºC_2h_electrode3_30012023_1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'color_index' : 2,
},

}

