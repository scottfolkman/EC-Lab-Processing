import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic

data_set = {

'IrOx' : {
'Ru' : 0.81,  #measured resistance in ohms
'label' : 'IrO<sub>X</sub>',
'cal' : 0.309,
'mass' : 1.0,
'data_PEIS' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1_C05.mpt',
'data_CV' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1 set1_01_CV_C02.mpt',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1 set1_03_CP_C02.mpt', 
'color_index' : 0,
},

'CoNx' : {
'Ru' : 0.988,  #measured resistance in ohms
'label' : 'CoN<sub>X</sub>',
'cal' : 0.309, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 0.99, #actual mass of catalyst
'data_PEIS' : 'Data_1mg\\2022_01_30 CoNx 1mg ref309_C05.mpt', #file path the slash needs to be '/' rather than the '\' which is automatic
'data_CV' : 'Data_1mg\\2022_01_30 CoNx 1mg ref309_set1_01_CV_C02.mpt',
'data_CA' : 'Data_1mg/2022_01_30 CoNx 1mg ref309_CA_C02.mpt',
'data_CP' : '',
'data_Tafel' : 'Data_1mg/2022_01_30 CoNx 1mg ref309_set1_03_CP_C02.mpt',
'color_index' : 1,
},

'NiNx' : {
'Ru' : 1.15,  #measured resistance in ohms
'cal' : 0.307, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 1.35, #actual mass of catalyst,
'label' : 'NiN<sub>X</sub>',
'data_PEIS' : 'Data_1mg/2023_01_31 NiNx 1 mg 307ref set1_C05.mpt', 
'data_CV' : 'Data_1mg/2023_01_31 NiNx 1 mg 307ref set2_01_CV_C01.mpt',
'data_CA' : 'Data_1mg/2023_01_31 NiNx 1 mg 307ref set2_04_CA_C01.mpt',
'data_CP' : '',
'data_Tafel': 'Data_1mg/2023_01_31 NiNx 1 mg 307ref set2_03_CP_C01.mpt',
'color_index' : 2,
},

'FeNx' : {
'Ru' : 1.43,  #measured resistance in ohms
'label' : 'FeN<sub>X</sub>',
'cal' : 0.309, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 1.09, #actual mass of catalyst
'data_PEIS' : 'Data_1mg/2022_01_27 FeNx 1mg ref309_C05.mpt', 
'data_CV' : 'Data_1mg/2022_01_27 FeNx 1mg ref309_set1_01_CV_C02.mpt',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : 'Data_1mg/2022_01_27 FeNx 1mg ref309_set1_03_CP_C02.mpt',
'color_index' : 3,
},

'NiCoFeOx' : {
'Ru' : 1.60,  #measured resistance in ohms
 #file path the slash needs to be '/' rather than the '\' which is automatic
'label' : 'Ni<sub>60</sub>Co<sub>30</sub>Fe<sub>10</sub>O<sub>X</sub>',
'cal' : 0.309, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 1.12, #actual mass of catalyst
'data_PEIS' : 'Data_1mg/2022_01_27 Ni60Co30Fe10Ox 1mg ref309_C05.mpt',
'data_CV': 'Data_1mg/2022_01_27 Ni60Co30Fe10Ox 1mg ref309__01_CV_C02.mpt',
'data_CA': '',
'data_CP' : '',
'data_Tafel': 'Data_1mg/2022_01_27 Ni60Co30Fe10Ox 1mg ref309__03_CP_C02.mpt',
'color_index' : 4,
},

'Co30Ni60Fe10Nx' : {
'Ru' : 1.16,  #measured resistance in ohms
'label' : 'Co<sub>30</sub>Ni<sub>60</sub>Fe<sub>10</sub>N<sub>X</sub>',
'cal' : 0.309, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 0.97, #actual mass of catalyst
'data_PEIS' : 'Data_1mg/2022_01_25 Co30Ni60Fe10Nx 1mg  ref309 elect1 set_C05.mpt',
'data_CV': 'Data_1mg/2022_01_25 Co30Ni60Fe10Nx 1mg  ref309 elect1 set1_01_CV_C02.mpt',
'data_CA' : '',
'data_CP' : 'Data_1/2022_01_25 Co30Ni60Fe10Nx 1mg  ref309 elect1 cv and bulk_03_CP_C02.mpt',
'data_Tafel': 'Data_1mg/2022_01_25 Co30Ni60Fe10Nx 1mg  ref309 elect1 tafel_C02.mpt',
'color_index' : 5,
},

'Co45Ni45Fe10Nx' : {
'Ru' : 0.90,  #measured resistance in ohms
'label' : 'Co<sub>45</sub>Ni<sub>45</sub>Fe<sub>10</sub>N<sub>X</sub>',
'cal' : 0.309, #calibration of the Hg/HgO electrode vs RHE converting to overpotential vs OER MUST BE UPDATED WHEN USING A DIFFERENT REF ELECTRODE
'mass' : 1.0, #actual mass of catalyst
'data_PEIS' : 'Data_1mg/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_01_PEIS_C05.mpt',
'data_CV' : 'Data_1mg/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_02_CV_C05.mpt',
'data_CA' : 'Data_1mg/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_bulk_C01.mpt',
'data_CP' : '',
'data_Tafel' : 'Data_1mg/2023_01_31_Co45Ni45Fe10Nx 1mg ref309_04_CP_C05.mpt',
'color_index' : 6,
},

'CoNiFeNx 400C 24h' : {
'Ru' : 0.81,  #measured resistance in ohms
'label' : 'CoNiFeNx 400C 24h',
'cal' : 0.309,
'mass' : 1.0,
'data_PEIS' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1_C05.mpt',
'data_CV' : 'Data_Lola\CoNiFeNx_400ºC_24h_13102022\Electrodes_19012023\\2023_01_20_CoNiFeNx_400ºC_24h_electrode1_19012023_1_01_CV_C01.mpr',
'data_CA' : '',
'data_CP' : '',
'data_Tafel' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1 set1_03_CP_C02.mpt', 
'color_index' : 7,
},

}

