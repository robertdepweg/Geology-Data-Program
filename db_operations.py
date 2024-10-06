# MODULE:  db_operations.py                       used by PROJECT:  Geology Project.py
# AUTHOR:  Robert Depweg                                        
# DESCRIPTION:  User's options for the database are calculated + performed here
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def max_min_chart(sample_data, chemicals, chem_list):
    ''' Top 5 most amount of chemicals in a sample '''
    try:
        counter = 0
        
        user_input = int(input('What sample would you like to see? Please input the samples Hex ID. '))
        if user_input in sample_data.keys():
            for key in chemicals.keys():
                for samples in sample_data:
                    chemicals[key] += sample_data[samples[chem_list[counter]]]
                    counter += 1
            chem_quantity = list(chemicals.values())
            chem_quantity = sorted(chem_quantity)
            print(sorted(chem_quantity[0:5]), sorted(chem_quantity[14:19]))
        else:
            raise ValueError
    except ValueError:
        print(f'Please enter a viable object ID.', end='\n')

def contaminated(sample_data):
    ''' Top 5 most and least chemically contaminated towns '''
    try:
        for keys in sample_data.values():
            for towns in sample_data.keys():
                for samples in sample_data:
                    chemicals[key] += sample_data[samples[chem_list[counter]]]
                    counter += 1
                towns = list(chemicals.values())
                chem_quantity = sorted(chem_quantity)
                print(sorted(chem_quantity[0:5]), sorted(chem_quantity[14:19]))
    except ValueError:
        print(ValueError)

def substance(sample_data, chemicals, chem_list):
    ''' 18 per/polyfluoroalkyl substance results ranked from highest to lowest amounts '''
    sample_counter = 18
    counter = 0
    for samples in sample_data.values():
        if samples[sample_counter] > 0:
            chemicals[counter] += samples[sample_counter]
    chemicals_list = sorted(list(chemicals))
    print(chemicals_list)

def treatment_count(sample_data, treatment_statuses):
    ''' A percentage of the overall sample treatment status '''
    for entries in sample_data.entries():
        for treatments in treatment_statuses.keys():
            if entries == treatments:
                treatment_statuses[entries] += 1
    return treatment_statuses