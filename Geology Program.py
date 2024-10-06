# PROGRAM:     Per/Polyfluoroalkyl Substances (PFAS) Sampling Data Pie Chart 
# AUTHOR:      Robert Depweg
# DESCRIPTION: Creates a pie chart from the Per/Polyfluoroalkyl Substances (PFAS) sampling effort dataset
# INPUT:       Per/Polyfluoroalkyl Substances (PFAS) sampling effort .csv File
# OUTPUT:      Pie Chart
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import create_db as create 
import db_operations as op # 
import numpy as np # 
import matplotlib.pyplot as plt # 
import sys

def main():
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - CONSTANT DECLARATIONS
    MAX_MIN_CHART: int = 1
    CONTAMINATED_LIST: int = 2
    SUBSTANCE_LIST: int = 3
    TREATMENT_COUNT_LIST: int = 4
    QUIT: int = 5

# - - - - - - - - - - - - - - - - - - - - - - - - - - - VARIABLE INITIALIZATION
    chemicals: dict = {'HFPO-DA':0, 'PFBS':0, 'PFHxA':0, 'PFHxS':0, 'PFNA':0,
                 'PFOA':0, 'PFOS':0, '11Cl-PF3OUdS':0, '9Cl-PF3ONS':0,
                 'ADONA':0, 'NEtFOSAA':0, 'NMeFOSAA':0, 'PFDA':0, 
                 'PFDoA':0, 'PFHpA':0, 'PFTA':0, 'PFTrDA':0, 'PFUnA':0}
    chem_list = [18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 42, 44, 47, 
                 49, 52, 58, 60, 62]
    system_types: list = ['CWS', 'NCWS', 'ASFSTC', 'CHLCMP', 'DAYCARE', 
                    'INDUS', 'MEDCAR', 'MOTEL', 'MUN']
    treatment_statuses: dict = {'raw':0, 'treated':0, 'tested':0, 'mp':0, 
                          'unavailable':0}
  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - INPUT
    sample_data_dict = create.load_initial_data()
    entry = int(user_entry(MAX_MIN_CHART, CONTAMINATED_LIST, 
                       SUBSTANCE_LIST, TREATMENT_COUNT_LIST, QUIT))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -CALCULATIONS
    while entry != QUIT:

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -OUTPUT
        if entry == MAX_MIN_CHART:
            op.max_min_chart(sample_data_dict, chemicals)
        if entry == CONTAMINATED_LIST:
            op.contaminated(sample_data_dict)
        if entry == SUBSTANCE_LIST:
            op.substance(sample_data_dict, chemicals, chem_list)
        else:
            op.treatment_count(sample_data_dict, treatment_statuses)
    print('Shutting down...')
    sys.exit()
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCTIONS
def user_entry(MAX_MIN_CHART, CONTAMINATED_LIST, SUBSTANCE_LIST, TREATMENT_COUNT_LIST, QUIT):
    ''' Obtains the user's choice '''
    print('OPTIONS:')
    print(f'{MAX_MIN_CHART}: Top 5 most and least amounts of chemicals in samples.')
    print(f'{CONTAMINATED_LIST}: Top 5 most and least chemically contaminated towns.')
    print(f'{SUBSTANCE_LIST}: 18 per/polyfluoroalkyl substances ranked from highest to lowest amounts across all samples collected.')
    print(f'{TREATMENT_COUNT_LIST}: A percentage of the overall sample treatment status.')
    print(f'{QUIT}: Quit the program.')
    entry = input('What will you choose? ')
    if not entry.isnumeric():
        raise ValueError
    if int(entry) < 1 or int(entry) > 5:
        raise ValueError
    return entry

# Conditional call to main()
if __name__ == '__main__':
    main()