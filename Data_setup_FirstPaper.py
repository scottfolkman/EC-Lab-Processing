import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'IrOx_elect3' : {
'Ru' : 0.797,  #measured resistance in ohms
'label' : 'IrO<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.16,
'data_PEIS' : 'Data_FirstPaper2\/2023_02_22_Scott_IrOx_Elect3_1160ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper2\/2023_02_22_Scott_IrOx_Elect3_1160ug_307mV_01_CV_C01.mpr',
'data_CA' : 'Data_FirstPaper2\/2023_02_22_Scott_IrOx_Elect3_1160ug_307mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_02_22_Scott_IrOx_Elect3_1160ug_307mV_04_CP_C01.mpr', 
'color_index' : 0,
},

# 'Ni60Co30Fe10Ox_elect2' : {
# 'Ru' : 1.14,  #measured resistance in ohms
# 'label' : 'Ni<sub>60</sub>Co<sub>30</sub>Fe<sub>10</sub>O<sub>x</sub>',
# 'cal' : 0.307, #vs OER
# 'mass' : 1.10,
# 'data_PEIS' : 'Data_FirstPaper2\/2023_02_23_Scott_Ni60Co30Fe10Ox_Elect2_1100ug_307mV_PEIS_C05.mpr',
# 'data_CV' : 'Data_FirstPaper2\/2023_02_23_Scott_Ni60Co30Fe10Ox_Elect2_1100ug_307mV_01_CV_C04.mpr',
# 'data_CA' : '',
# 'data_CP' : '',
# 'data_Tafel' : 'Data_FirstPaper2\/2023_02_23_Scott_Ni60Co30Fe10Ox_Elect2_1100ug_307mV_04_CP_C04.mpr', 
# 'color_index' : 1,
# },

'FeNx_3' : {
'Ru' : 1.00,  #measured resistance in ohms
'label' : 'FeN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 0.93,
'data_PEIS' : 'Data_FirstPaper2\/2023_02_23_Scott_FeNx_Elect3_930ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper2\/2023_02_23_Scott_FeNx_Elect3_930ug_307mV_01_CV_C02.mpr',
'data_CA' : 'Data_FirstPaper2\/2023_02_23_Scott_FeNx_Elect3_930ug_307mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_02_23_Scott_FeNx_Elect3_930ug_307mV_04_CP_C02.mpr', 
'color_index' : 3,
},

'CoNx_3' : {
'Ru' : 1.51,  #measured resistance in ohms
'label' : 'CoN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.00,
'data_PEIS' : 'Data_FirstPaper2\/2023_02_23_Scott_CoNx_Elect3_1000ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper2\/2023_02_23_Scott_CoNx_Elect3_1000ug_307mV_01_CV_C02.mpr',
'data_CA' : 'Data_FirstPaper2\/2023_02_23_Scott_CoNx_Elect3_1000ug_307mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_02_23_Scott_CoNx_Elect3_1000ug_307mV_04_CP_C02.mpr', 
'color_index' : 4,
},

'NiNx_3' : {
'Ru' : 1.10, #measured resistance in ohms
'label' : 'NiN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.14,
'data_PEIS' : 'Data_FirstPaper2\/2023_02_23_Scott_NiNx_Elect3_1140ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper2\/2023_02_23_Scott_NiNx_Elect3_1140ug_307mV_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper2\/2023_02_23_Scott_NiNx_Elect3_1140ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_02_23_Scott_NiNx_Elect3_1140ug_307mV_04_CP_C04.mpr', 
'color_index' : 5,
},

# 'Co30Ni60Fe10Nx_3' : {
# 'Ru' : 0.77,  #measured resistance in ohms
# 'label' : 'Co<sub>30</sub>Ni<sub>60</sub>Fe<sub>10</sub>N<sub>x</sub>',
# 'cal' : 0.307, #vs OER
# 'mass' : 0.94,
# 'data_PEIS' : 'Data_FirstPaper2\/2023_02_28_Scott_Co30Ni60Fe10Nx_Elect3_940ug_307mV_PEIS_C05.mpr',
# 'data_CV' : 'Data_FirstPaper2\/2023_02_28_Scott_Co30Ni60Fe10Nx_Elect3_940ug_307mV_01_CV_C04.mpr',
# 'data_CA' : 'Data_FirstPaper2\/2023_02_28_Scott_Co30Ni60Fe10Nx_Elect3_940ug_307mV_03_CA_C04.mpr',
# 'data_CP' : '',
# 'data_Tafel' : 'Data_FirstPaper2\/2023_02_28_Scott_Co30Ni60Fe10Nx_Elect3_940ug_307mV_04_CP_C04.mpr', 
# 'color_index' : 2,
# },

'Co45Ni45Fe10Nx' : {
'Ru' : 1.00, #measured resistance in ohms
'label' : 'Co<sub>45</sub>Ni<sub>45</sub>Fe<sub>10</sub>N<sub>x</sub>',
'cal' : 0.299, #vs OER
'mass' : 1.00,
'data_PEIS' : 'Data_FirstPaper\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_01_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_02_CV_C05.mpr',
'data_CA' : 'Data_FirstPaper\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_bulk_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper\/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_04_CP_C05.mpr', 
'color_index' : 6,
},

'Co57Ni14Fe29Nx' : {
'Ru' : 0.98, #measured resistance in ohms
'label' : 'Co<sub>57</sub>Ni<sub>14</sub>Fe<sub>29</sub>N<sub>x</sub>',
'cal' : 0.299, #vs OER
'mass' : 1.13,
'data_PEIS' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_04_CP_C04.mpr', 
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

