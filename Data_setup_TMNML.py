import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'Co50 Ni0 Fe50 300C 2h_elect1': {
'Ru' : 1.12,  #measured resistance in ohms
'label' : 'Co50 Ni0 Fe50 300C 2h_',
'cal' : 0.299, #vs OER
'mass' : 1.13,
'data_PEIS' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect1_1130ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect1_1130ug_299mV_01_CV_C02.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect1_1130ug_299mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect1_1130ug_299mV_04_CP_C02.mpr', 
'fit_min': -4.101,
'fit_max': -2.499,
'color_index' : 0,
},

'Co50 Ni0 Fe50 300C 2h_elect2' : {
'Ru' : 1.03,  #measured resistance in ohms
'label' : 'Co50 Ni0 Fe50 300C 2h',
'cal' : 0.299, #vs OER
'mass' : 0.960,
'data_PEIS' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect2_960ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect2_960ug_299mV_01_CV_C02.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect2_960ug_299mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co50Fe50Nx_2h_300C/2023_03_01_LJ_Co50Fe50Nx_2h_300C_Elect2_960ug_299mV_04_CP_C02.mpr', 
'fit_min': -3.801,
'fit_max': -1.99,
'color_index' : 0,
},

'Co0 Ni50 Fe50 400C 2h' : {
'Ru' : 0.68,  #measured resistance in ohms
'label' : 'Co0 Ni50 Fe50 400C 2h',
'cal' : 0.307, #vs OER
'mass' : 1.10,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Scott/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/Scott/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Scott/2023_02_28_Scott_Co0Ni50Fe50Nx_2h_400C_Elect3_1100ug_307mV_04_CP_C04.mpr',
'fit_min': -4.11,
'fit_max': -2.499, 
'color_index' : 1,
},

'Co25 Ni25 Fe50 600C 2h_elect1' : {
'Ru' : 1.23,  #measured resistance in ohms
'label' : 'Co25 Ni25 Fe50 600C 2h_elect1',
'cal' : 0.299, #vs OER
'mass' : 1.10,
'data_PEIS' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31__LJ_Co25Ni25Fe50Nx_2h_600C_elect1_1100ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect1_1100ug_299mV_1_01_CV_C02.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect1_1100ug_299mV_1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5.01,
'fit_max': -1.99,
'color_index' : 2,
},

'Co25 Ni25 Fe50 600C 2h_elect2' : {
'Ru' : 1.16,  #measured resistance in ohms
'label' : 'Co25 Ni25 Fe50 600C 2h_elect2',
'cal' : 0.299, #vs OER
'mass' : 1.22,
'data_PEIS' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect2_1220ug__299mV_1_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect2_1220ug__299mV_1_01_CV_C02.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect2_1220ug__299mV_1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5.01,
'fit_max': -1.99,
'color_index' : 2,
},

'Co25 Ni25 Fe50 600C 2h_elect3' : {
'Ru' : 1.38,  #measured resistance in ohms
'label' : 'Co25 Ni25 Fe50 600C 2h_elect3',
'cal' : 0.299, #vs OER
'mass' : 0.950,
'data_PEIS' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect3_950ug__299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect3_950ug__299mV_1_01_CV_C02.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co25Ni25Fe50Nx_2h_600C/2023_01_31_LJ_Co25Ni25Fe50Nx_2h_600C_elect3_950ug__299mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : '', 
'fit_min': -5.01,
'fit_max': -1.99,
'color_index' : 2,
},

'Co33 Ni33 Fe33 800C 2h' : {
'Ru' : 0.981,  #measured resistance in ohms
'label' : 'Co33 Ni33 Fe33 800C 2h',
'cal' : 0.307, #vs OER
'mass' : 1.07,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Scott/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Scott/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Scott/2023_02_20_Scott_Co33Ni33Fe33_2h_800C_Elect1_1050ug_307mV_Tafel_C01.mpr', # no problems with current
'fit_min': -4.801,
'fit_max': -2.499,
'color_index' : 3,
},

'Co50 Ni50 Fe0 300C 6h 1' : {
'Ru' :0.978, #measured resistance in ohms
'label' :'Co50 Ni50 Fe0 300C 6h' ,
'cal' :0.304, #vs OER
'mass' :1.12,
'data_PEIS' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect1_1120ug_304mV_DJF3-IGC1_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect1_1120ug_304mV_DJF3-IGC1_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect1_1120ug_304mV_DJF3-IGC1_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect1_1120ug_304mV_DJF3-IGC1_04_CP_C01.mpr',
'fit_min': -5.01,
'fit_max': -2.699,
'color_index' : 4,
},

'Co50 Ni50 Fe0 300C 6h 2' : {
'Ru' :0.675, #measured resistance in ohms
'label' :'Co50 Ni50 Fe0 300C 6h' ,
'cal' :0.304, #vs OER
'mass' :1.15,
'data_PEIS' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect2_1150ug_304mV_DJF3-IGC2_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect2_1150ug_304mV_DJF3-IGC2_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect2_1150ug_304mV_DJF3-IGC2_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_03_03_IG_Co50Ni50Nx_6h_300C_Elect2_1150ug_304mV_DJF3-IGC2_04_CP_C01.mpr',
'fit_min': -5.01,
'fit_max': -2.699,
'color_index' : 4,
},

'Co0 Ni0 Fe100 400C 6h_elect1' : {
'Ru' : 1.05, #measured resistance in ohms
'label' : 'Co0 Ni0 Fe100 400C 6h',
'cal' : 0.299, #vs OER
'mass' : 0.99,
'data_PEIS' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect1_990ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect1_990ug_299mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect1_990ug_299mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect1_990ug_299mV_04_CP_C04.mpr', 
'fit_min': -4.501,
'fit_max': -2.499,
'color_index' : 5,
},

'Co0 Ni0 Fe100 400C 6h_elect3' : {
'Ru' : 1.14, #measured resistance in ohms
'label' : 'Co0 Ni0 Fe100 400C 6h',
'cal' : 0.299, #vs OER
'mass' : 0.94,
'data_PEIS' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect3_940ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect3_940ug_299mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect3_940ug_299mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Fe100Nx_6h_400C/2023_02_24_LJ_FeNx_6h_400C_Elect3_940ug_299mV_04_CP_C04.mpr', 
'fit_min': -4.501,
'fit_max': -2.499,
'color_index' : 5,
},

'Co25 Ni75 Fe0 600C 6h' : {
'Ru' : 0.80, #measured resistance in ohms
'label' : 'Co25 Ni75 Fe0 600C 6h',
'cal' : 0.298, #vs OER
'mass' : 1.970,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Irene/2023_03_08_irene_Co25Ni75Nx_6h_600C_Elect1_1970ug_298mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Irene/2023_03_08_irene_Co25Ni75Nx_6h_600C_Elect1_1970ug_298mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Irene/2023_03_08_irene_Co25Ni75Nx_6h_600C_Elect1_1970ug_298mV_04_CP_C01.mpr', 
'fit_min': -4.301,
'fit_max': -2.499,
'color_index' : 6,
},

'Co25 Ni0 Fe75 800C 6h_Elect2' : {
'Ru' : 0.734, #measured resistance in ohms
'label' : 'Co25 Ni0 Fe75 800C 6h',
'cal' : 0.299, #vs OER
'mass' : 1.001,
'data_PEIS' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect2_1001ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect2_1001ug_299mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect2_1001ug_299mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect2_1001ug_299mV_04_CP_C04.mpr', 
'fit_min': -5.01,
'fit_max': -2.599,
'color_index' : 7,
},

'Co25 Ni0 Fe75 800C 6h_Elect3' : {
'Ru' : 1.07, #measured resistance in ohms
'label' : 'Co25 Ni0 Fe75 800C 6h',
'cal' : 0.299, #vs OER
'mass' : 0.970,
'data_PEIS' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect3_970ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect3_970ug_299mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect3_970ug_299mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co25Fe75Nx_6h_800C/2023_02_22_LJ_Co25Ni0Fe75_6h_800C_Elect3_970ug_299mV_04_CP_C04.mpr', 
'fit_min': -5.01,
'fit_max': -2.599,
'color_index' : 7,
},

'Co25 Ni50 Fe25 300C 12h' : {
'Ru' : 1.07, #measured resistance in ohms
'label' : 'Co25 Ni50 Fe25 300C 12h',
'cal' : 0.299, #vs OER
'mass' : 1.23,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Irene/2023_03_10_irene_C025Ni50Fe25Nx_12h_300C_Elect1_1230ug_298mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Irene/2023_03_10_irene_C025Ni50Fe25Nx_12h_300C_Elect1_1230ug_298mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Irene/2023_03_10_irene_C025Ni50Fe25Nx_12h_300C_Elect1_1230ug_298mV_04_CP_C01.mpr',
'fit_min': -4.1,
'fit_max': -2.799,
'color_index' : 8,
},

'Co100 Ni0 Fe0 400C 12h' : {
'Ru' : 0.807, #measured resistance in ohms
'label' : 'Co100 Ni0 Fe0 400C 12h',
'cal' : 0.298, #vs OER
'mass' : 1.00,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Irene/2023_03_07_irene_Co100Nx_12h_400C_Elect1_1200ug_298mV_01_CV_C02.mpr',
'data_CA' : 'Data for ML/Irene/2023_03_07_irene_Co100Nx_12h_400C_Elect1_1200ug_298mV_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Irene/2023_03_07_irene_Co100Nx_12h_400C_Elect1_1200ug_298mV_04_CP_C02.mpr', 
'fit_min': -4.2601,
'fit_max': -2.499,
'color_index' : 9,
},

'Co0 Ni25 Fe75 600C 12h' : {
'Ru' : 0.881, #measured resistance in ohms
'label' : 'Co0 Ni25 Fe75 600C 12h',
'cal' : 0.307, #vs OER
'mass' : 1.01,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Scott/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_01_CV_C04.mpr',
'data_CA' : 'Data for ML/Scott/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Scott/2023_03_02_Scott_Co0Ni25Fe75Nx_12h_600C_Elect2_1010ug_307mV_04_CP_C04.mpr', 
'fit_min': -5.01,
'fit_max': -3.24,
'color_index' : 10,
},

'Co0 Ni100 Fe0 800C 12h 1' : {
'Ru' :1.15, #measured resistance in ohms
'label' :'Co0 Ni100 Fe0 800C 12h 1' ,
'cal' :0.299, #vs OER
'mass' :0.2,
'data_PEIS' : 'Data for ML/Ilario/2023_02_28_IG_NiNx_12h_800C_Elect1_200ug_299mV_DJF3-IGA1_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_02_28_IG_NiNx_12h_800C_Elect1_200ug_299mV_DJF3-IGA1_01_CV_C02.mpr',
'data_CA' : 'Data for ML/Ilario/2023_02_28_IG_NiNx_12h_800C_Elect1_200ug_299mV_DJF3-IGA1_03_CA_C02.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect1_950ug_304mV_DJF3-IGB1_04_CP_C01.mpr',
'fit_min': -4.401,
'fit_max': -1.99,
'color_index' :11,
},

'Co0 Ni100 Fe0 800C 12h 2' : {
'Ru' :1.4, #measured resistance in ohms
'label' :'Co0 Ni100 Fe0 800C 12h 2' ,
'cal' :0.304, #vs OER
'mass' :0.23,
'data_PEIS' : 'Data for ML/Ilario/2023_03_01_IG_NiNx_12h_800C_Elect2_230ug_304mV_DJF3-IGA2_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_03_01_IG_NiNx_12h_800C_Elect2_230ug_304mV_DJF3-IGA2_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Ilario/2023_03_01_IG_NiNx_12h_800C_Elect2_230ug_304mV_DJF3-IGA2_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_03_01_IG_NiNx_12h_800C_Elect2_230ug_304mV_DJF3-IGA2_04_CP_C01.mpr',
'fit_min': -4.401,
'fit_max': -2.499,
'color_index' :11,
},

'Co0 Ni100 Fe0 800C 12h 4' : {
'Ru' : 1.02, #measured resistance in ohms
'label' :'Co0 Ni100 Fe0 800C 12h 4' ,
'cal' :0.299, #vs OER
'mass' :0.81,
'data_PEIS' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect4_810ug_299mV_DJF3-IGD1_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect4_810ug_299mV_DJF3-IGD1_01_CV_C04.mpr',
'data_CA' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect4_810ug_299mV_DJF3-IGD1_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect4_810ug_299mV_DJF3-IGD1_04_CP_C04.mpr',
'fit_min': -4.01,
'fit_max': -2.99,
'color_index' :11,
},

'Co0 Ni100 Fe0 800C 12h 5' : {
'Ru' : 0.98, #measured resistance in ohms
'label' :'Co0 Ni100 Fe0 800C 12h 5' ,
'cal' :0.299, #vs OER
'mass' :0.49,
'data_PEIS' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect5_490ug_299mV_DJF3-IGD2_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect5_490ug_299mV_DJF3-IGD2_01_CV_C04.mpr',
'data_CA' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect5_490ug_299mV_DJF3-IGD2_03_CA_C04.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_03_10_IG_NiNx_12h_800C_Elect5_490ug_299mV_DJF3-IGD2_04_CP_C04.mpr',
'fit_min': -4.01,
'fit_max': -2.99,
'color_index' :11,
},

'Co75 Ni25 Fe0 300C 24h 1' : {
'Ru' :1.44, #measured resistance in ohms
'label' :'Co75 Ni25 Fe0 300C 24h' ,
'cal' :0.304, #vs OER
'mass' :0.95,
'data_PEIS' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect1_950ug_304mV_DJF3-IGB1_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect1_950ug_304mV_DJF3-IGB1_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect1_950ug_304mV_DJF3-IGB1_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect1_950ug_304mV_DJF3-IGB1_04_CP_C01.mpr',
'fit_min': -5.01,
'fit_max': -2.9,
'color_index' :12,
},

'Co75 Ni25 Fe0 300C 24h 2' : {
'Ru' :1.01, #measured resistance in ohms
'label' :'Co75 Ni25 Fe0 300C 24h' ,
'cal' :0.304, #vs OER
'mass' :0.97,
'data_PEIS' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect2_970ug_304mV_DJF3-IGB2_PEIS_C05.mpr',
'data_CV' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect2_970ug_304mV_DJF3-IGB2_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect2_970ug_304mV_DJF3-IGB2-2ndpart_01_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Ilario/2023_02_28_IG_Co75Ni25Nx_24h_300C_Elect2_970ug_304mV_DJF3-IGB2-2ndpart_02_CP_C01.mpr',
'fit_min': -5.01,
'fit_max': -2.9,
'color_index' :12,
},

'Co50 Ni25 Fe25 400C 24h' : {
'Ru' : 1.22, #measured resistance in ohms
'label' : 'Co50 Ni25 Fe25 400C 24h',
'cal' : 0.307, #vs OER
'mass' : 0.99,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Scott/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Scott/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Scott/2023_03_01_Scott_Co50Ni25Fe25Nx_24h_400C_Elect1_9900ug_307mV_04_CP_C01.mpr', 
'fit_min': -3.701,
'fit_max': -1.99,
'color_index' : 13,
},

'Co0 Ni75 Fe25 600C 24h' : {
'Ru' : 0.72, #measured resistance in ohms
'label' : 'Co0 Ni75 Fe25 600C 24h',
'cal' : 0.298, #vs OER
'mass' : 1.45,
'data_PEIS' : '',
'data_CV' : 'Data for ML/Irene/2023_03_08_irene_Ni75Fe25Nx_24h_600C_Elect1_1450ug_298mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/Irene/2023_03_08_irene_Ni75Fe25Nx_24h_600C_Elect1_1450ug_298mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/Irene/2023_03_08_irene_Ni75Fe25Nx_24h_600C_Elect1_1450ug_298mV_04_CP_C01.mpr', 
'fit_min': -4.701,
'fit_max': -2.699,
'color_index' : 14,
},

'Co75 Ni0 Fe25 800C 24h_Elect1' : {
'Ru' : 1.25, #measured resistance in ohms
'label' : 'Co75 Ni0 Fe25 800C 24h',
'cal' : 0.299, #vs OER
'mass' : 1.13,
'data_PEIS' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect1_1130ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect1_1130ug_299mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect1_1130ug_299mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect1_1130ug_299mV_04_CP_C01.mpr', 
'fit_min': -5.01,
'fit_max': -1.99,
'color_index' : 17,
},

'Co75 Ni0 Fe25 800C 24h_Elect3' : {
'Ru' : 1.47, #measured resistance in ohms
'label' : 'Co75 Ni0 Fe25 800C 24h',
'cal' : 0.299, #vs OER
'mass' : 1.04,
'data_PEIS' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect3_1040ug_299mV_PEIS_C05.mpr',
'data_CV' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect3_1040ug_299mV_01_CV_C01.mpr',
'data_CA' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect3_1040ug_299mV_03_CA_C01.mpr',
'data_CP' : '',
'data_Tafel' : 'Data for ML/LoleJurado/Co75Fe25Nx_24h_800C/2023_03_07_LJ_Co75Fe25Nx_24h_800C_Elect3_1040ug_299mV_04_CP_C01.mpr', 
'fit_min': -3.801,
'fit_max': -1.99,
'color_index' : 17,
},


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
# 'fit_min': -5.01,
# 'fit_max': -1.99,
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
# 'fit_min': -5.01,
# 'fit_max': -1.99,
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
# 'fit_min': -5.01,
# 'fit_max': -1.99,
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
# # 'data_Tafel' : '', 
# 'fit_min': -5.01,
# 'fit_max': -1.99,
# 'color_index' : 19,
# },

}

