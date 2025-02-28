import pandas as pd
import numpy as np 
import re
# File path: the slash needs to be '/' rather than '\' which is automatic.
# The label is used in the figure legends to make subscripts: <sub>x</sub>.

data_set = {

    'Step to 0 V' : {
        'Ru' : 0.00,  # measured resistance in ohms
        'label' : '0.0 V',
        'cal' : 0.00, # vs OER; normalize it yourself
        'mass' : 1.00,
        'data_PEIS' : '',
        'data_CV' : '',
        'data_CA' : 'Data/2025-02-10 exp 2 potential step 0 v_C05.mpr',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 0,
    },

    '2' : {
        'Ru' : 0.00,
        'label' : '0.1 V',
        'cal' : 0.00,
        'mass' : 1.00,
        'data_PEIS' : '',
        'data_CV' : '',
        'data_CA' : 'Data/2025-02-10 exp 3 potential step 0,1 V_C05.mpr',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 1,
    },

    '3' : {
        'Ru' : 0.00,
        'label' : '3',
        'cal' : 0.00,
        'mass' : 1.00,
        'data_PEIS' : '',
        'data_CV' : '',
        'data_CA' : 'Data/2025-02-10 exp 4 potential step -0,5 V_C05.mpt',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 2,
    },

    '4' : {
        'Ru' : 0.00,
        'label' : '4',
        'cal' : 0.00,
        'mass' : 1.00,  
        'data_PEIS' : '',
        'data_CV' : 'Data/2025-02-10 exp 5 CV 10mvs_C05.mpt',
        'data_CA' : '',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 3,
    },

    '5' : {
        'Ru' : 0.00,
        'label' : '5',
        'cal' : 0.00,
        'mass' : 1.00,
        'data_PEIS' : '',
        'data_CV' : 'Data/2025-02-10 exp 6 CV 20mvs_C05.mpr',
        'data_CA' : '',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 4,
    },

    '6' : {
        'Ru' : 0.00,
        'label' : '6',
        'cal' : 0.00,
        'mass' : 1.00,
        'data_PEIS' : 'Data/2025-02-10 exp 12 EIS_C05.mpr',
        'data_CV' : '',
        'data_CA' : '',
        'data_CP' : '',
        'data_Tafel' : '', 
        'fit_min': -5,
        'fit_max': -1,
        'color_index' : 5,
    },

    '7' : {
        'Ru' : 0.00,
        'label' : '7',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '8',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '9',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '10',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '11',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '12',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '13',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '14',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '15',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '16',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '17',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '18',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '19',
        'cal' : 0.00,
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
        'Ru' : 0.00,
        'label' : '20',
        'cal' : 0.00,
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
