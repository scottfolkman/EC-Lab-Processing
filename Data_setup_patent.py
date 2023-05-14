import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'IrOx_' : {
'Ru' : 1.0,  #measured resistance in ohms
'label' : 'IrO<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 0.810,
'data_PEIS' : 'Data_FirstPaper 350 mV\/2023_03_07_Scott_IrOx_Elect2_810ug_307mV_PEIS_C05.mpr',
'data_CV' : 'Data_FirstPaper/2022_01_26 IrOx 1mg  ref309 elect1 set1_01_CV_C02.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_07_Scott_IrOx_Elect2_810ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper2\/2023_02_22_Scott_IrOx_Elect3_1160ug_307mV_04_CP_C01.mpr', 
'fit_min': -4,
'fit_max': -1.9,
'color_index' : 0,
'line_style': 'lines',
'x_pos': '0.82',
'y_pos': '0.85',

},

# 'Ni60Co30Fe10Ox_' : {
# 'Ru' : 1.00,  #measured resistance in ohms
# 'label' : 'Ni<sub>60</sub>Co<sub>30</sub>Fe<sub>10</sub>O<sub>x</sub>',
# 'cal' : 0.307, #vs OER
# 'mass' : 1.04,
# 'data_PEIS' : '',
# 'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_08_Scott_NiCoFeOx_Elect1_1040ug_307mV_350mVCA_01_CV_C04.mpr',
# 'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_08_Scott_NiCoFeOx_Elect1_1040ug_307mV_350mVCA_03_CA_C04.mpr',
# 'data_CP' : '',
# 'data_Tafel' : 'Data_FirstPaper\/2022_01_27 Ni60Co30Fe10Ox 1mg ref309__03_CP_C02.mpr', 
# 'fit_min': -4.3,
# 'fit_max': -3.25,
# 'color_index' : 1,
# 'line_style': 'lines',
# 'x_pos': '0.5',
# 'y_pos': '0.5',
# },

'FeNx_' : {
'Ru' : 1.10,  #measured resistance in ohms
'label' : 'FeN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.11,
'data_PEIS' : '',
'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_08_Scott_FeNx_Elect2_1100ug_307mV_350mVCA_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_08_Scott_FeNx_Elect2_1100ug_307mV_350mVCA_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper\/2022_01_27 FeNx 1mg ref309_set1_03_CP_C02.mpr', 
'fit_min': -4.8,
'fit_max': -3.1,
'color_index' : 3,
'line_style': 'lines',
'x_pos': '0.95',
'y_pos': '0.1',
},

'CoNx_' : {
'Ru' : 0.88,  #measured resistance in ohms
'label' : 'CoN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.05,
'data_PEIS' : '',
'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_CoNx_Elect2_1050ug_307mV_350mvCA_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_CoNx_Elect2_1050ug_307mV_350mvCA_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper\/2022_01_30 CoNx 1mg ref309_set1_03_CP_C02.mpr', 
'fit_min': -3.8,
'fit_max': -2.8,
'color_index' : 4,
'line_style': 'lines',
'x_pos': '0.95',
'y_pos': '0.22',
},

'NiNx_' : {
'Ru' : 0.73, #measured resistance in ohms
'label' : 'NiN<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.28,
'data_PEIS' : '',
'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_NiNx_Elect2_1280ug_307mV_350mVCA_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_NiNx_Elect2_1280ug_307mV_350mVCA_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_NiNx_Elect2_1280ug_307mV_350mVCA_04_CP_C04.mpr', 
'fit_min': -5.1,
'fit_max': -3.5,
'color_index' : 5,
'line_style': 'lines',
'x_pos': '1.0',
'y_pos': '0.02',
},

'Co57Ni14Fe29Nx_' : {
'Ru' : 0.736,  #measured resistance in ohms
'label' : 'Co<sub>57</sub>Ni<sub>14</sub>Fe<sub>29</sub>N<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.07,
'data_PEIS' : '',
'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_Co57Ni14Fe29Nx_6h_425C_Elect11_1070ug_307mV_350mVCA_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_Co57Ni14Fe29Nx_6h_425C_Elect11_1070ug_307mV_350mVCA_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper 350 mV\/2023_03_09_Scott_Co57Ni14Fe29Nx_6h_425C_Elect11_1070ug_307mV_350mVCA_04_CP_C04.mpr',
'fit_min': -3.6,
'fit_max': -2, 
'color_index' : 2,
'line_style': 'lines',
'x_pos': '0.5',
'y_pos': '0.95',
},

'Co45Ni45Fe10Nx' : {
'Ru' : 1.03, #measured resistance in ohms
'label' : 'Co<sub>45</sub>Ni<sub>45</sub>Fe<sub>10</sub>N<sub>x</sub>',
'cal' : 0.307, #vs OER
'mass' : 1.08,
'data_PEIS' : '',
'data_CV' : 'Data_FirstPaper 350 mV\/2023_03_07_Scott_Co45Ni45Fe10Nx_6h_425C_Elect1_1080ug_307mV_350mVCA_01_CV_C04.mpr',
'data_CA' : 'Data_FirstPaper 350 mV\/2023_03_07_Scott_Co45Ni45Fe10Nx_6h_425C_Elect1_1080ug_307mV_350mVCA_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data_FirstPaper 350 mV\/2023_03_07_Scott_Co45Ni45Fe10Nx_6h_425C_Elect1_1080ug_307mV_350mVCA_04_CP_C04.mpr', 
'fit_min': -3.6,
'fit_max': -2,
'color_index' : 6,
'line_style': 'lines',
'x_pos': '1.02',
'y_pos': '0.62',
},

# 'Co57Ni14Fe29Nx' : {
# 'Ru' : 0.98, #measured resistance in ohms
# 'label' : 'Co<sub>57</sub>Ni<sub>14</sub>Fe<sub>29</sub>N<sub>x</sub>',
# 'cal' : 0.299, #vs OER
# 'mass' : 1.13,
# 'data_PEIS' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_PEIS_C05.mpr',
# 'data_CV' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_01_CV_C04.mpr',
# 'data_CA' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_03_CA_C04.mpr',
# 'data_CP' : '',
# 'data_Tafel' : 'Data_FirstPaper2\/2023_03_02_Scott_Co57Ni14Fe29Nx_6h_425C_Elect1_1130ug_307mV_04_CP_C04.mpr', 
# 'color_index' : 7,
# },

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

