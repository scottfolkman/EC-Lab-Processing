import pandas as pd
import numpy as np 
import re
#file path the slash needs to be '/' rather than the '\' which is automatic
data_set = {

'CoNiFeNx 400C 24h' : {
'Ru' : 0.81,  #measured resistance in ohms
'label' : 'CoNiFeNx 400C 24h',
'cal' : 0.309,
'mass' : 1.0,
'data_PEIS' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1_C05.mpt',
'data_CV' : 'Data_Lola\CoNiFeNx_400ºC_24h_13102022\Electrodes_19012023\\2023_01_20_CoNiFeNx_400ºC_24h_electrode1_19012023_1_01_CV_C01.mpt',
'data_CA' : '',
'data_Tafel' : 'Data_1mg/2022_01_26 IrOx 1mg  ref309 elect1 set1_03_CP_C02.mpt', 
},

}

