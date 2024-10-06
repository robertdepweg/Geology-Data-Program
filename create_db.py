# MODULE:  create_db.py                       used by PROJECT:  Geology Project.py
# AUTHOR:  Robert Depweg                    
# DESCRIPTION:  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import sys 

def load_initial_data():  
    ''' reads in data from .csv file, creates + returns 
    dictionary of tuples '''
    try:
        water_supply_db = {}
        with open('PfasMunicipalDrinkingWaterSamplingHexbins.csv', 'r') as infile:
            for i in range(1): # skips the header line
                infile.readline()
            for line in infile: 
                line: str = line.strip('\n')
                fields: list = line.split(',')
                hex_id, system_name, wssn, system_type, sample_date, treatment_status, hfpodra_results, hfpodra_flags, pfbs_results, pfbs_flags, pfhxa_results, pfhxa_flags, pfhxs_results, pfhxs_flags, pfna_results, pfna_flags, pfoa_results, pofa_flags, pfos_results, pfos_flags, pf3ouds11ci_results, pf3ouds11ci_flags, pf3ons9cl_results, pf3ons9cl_flags, adona_results, adona_flags, ftsa42_flags, ftsa62_flags, ftsa82_flags, fosa_results, fosa_flags, netfosar_results, netfosaf_flags, nmefosaa_results, nmefosaa_flags, pfba_flags, pfda_results, pfda_flags, pfdoda_results, pfdoda_flags, pfds_results, pfds_flags, pfhpa_results, pfhpa_flags, pfhps_flags, pfns_flags, pfpea_flags, pfpes_flags, pfteda_results, pfteda_flags, pftrda_results, pftrda_flags, pfunda_results, pfunda_flags, sampling_results = get_conv_fields(fields)
                
                # entry tuple added to dict
                water_supply_db[hex_id] = (system_name, wssn, 
                system_type, sample_date, treatment_status, 
                hfpodra_results, hfpodra_flags, pfbs_results, 
                pfbs_flags, pfhxa_results, pfhxa_flags, pfhxs_results,
                pfhxs_flags, pfna_results, pfna_flags, pfoa_results,
                pofa_flags, pfos_results, pfos_flags, 
                pf3ouds11ci_results, pf3ouds11ci_flags, 
                pf3ons9cl_results, pf3ons9cl_flags, adona_results, 
                adona_flags, ftsa42_flags, ftsa62_flags,
                ftsa82_flags, fosa_results, fosa_flags, 
                netfosar_results, netfosaf_flags, nmefosaa_results,
                nmefosaa_flags, pfba_flags, pfda_results,
                pfda_flags, pfdoda_results, pfdoda_flags, pfds_results, 
                pfds_flags, pfhpa_results, pfhpa_flags,
                pfhps_flags, pfns_flags, pfpea_flags, pfpes_flags, 
                pfteda_results, pfteda_flags, pftrda_results, 
                pftrda_flags, pfunda_results, pfunda_flags, 
                sampling_results)

            print('\nWater database assets have loaded.\n')
            return water_supply_db
    except IOError as err: # exits system if issue with file
        sys.exit(err)
    except Exception as err:
        sys.exit(err)

def get_conv_fields(fields):  
    ''' recieves list of fields, returns each 
    list element as converted variable '''
    try:
        counter = 0

        hex_id: int = int(fields[1])
        system_name: str = fields[2]
        wssn: str = fields[3]
        system_type: str = fields[4]
        sample_date: str = fields[11]
        treatment_status: str = fields[12]

        hfpodra_results: int = result_checker(fields, counter)
        hfpodra_flags: str = flag_checker(fields, counter)
        pfbs_results: int = result_checker(fields, counter)
        pfbs_flags: str = flag_checker(fields, counter)
        pfhxa_results: int = result_checker(fields, counter)
        pfhxa_flags: str = flag_checker(fields, counter)
        pfhxs_results: int = result_checker(fields, counter)
        pfhxs_flags: str = flag_checker(fields, counter)
        pfna_results: int = result_checker(fields, counter)
        pfna_flags: str = flag_checker(fields, counter)
        pfoa_results: int = result_checker(fields, counter)
        pofa_flags: str = flag_checker(fields, counter)
        pfos_results: int = result_checker(fields, counter)
        pfos_flags: str = flag_checker(fields, counter)
        pf3ouds11ci_results: int = result_checker(fields, counter)
        pf3ouds11ci_flags: str = flag_checker(fields, counter)
        pf3ons9cl_results: int = result_checker(fields, counter)
        pf3ons9cl_flags: str = flag_checker(fields, counter)
        adona_results: int = result_checker(fields, counter)
        adona_flags: str = flag_checker(fields, counter)
        ftsa42_flags: str = flag_checker(fields, counter)
        ftsa62_flags: str = flag_checker(fields, counter)
        ftsa82_flags: str = flag_checker(fields, counter)
        fosa_results: int = result_checker(fields, counter)
        fosa_flags: str = flag_checker(fields, counter)   
        netfosar_results: int = result_checker(fields, counter)
        netfosaf_flags: str = flag_checker(fields, counter)
        nmefosaa_results: int = result_checker(fields, counter)   
        nmefosaa_flags: str = flag_checker(fields, counter)
        pfba_flags: str = flag_checker(fields, counter)
        pfda_results: int = result_checker(fields, counter)
        pfda_flags: str = flag_checker(fields, counter)
        pfdoda_results: int = result_checker(fields, counter)
        pfdoda_flags: str = flag_checker(fields, counter)
        pfds_results: int = result_checker(fields, counter)
        pfds_flags: str = flag_checker(fields, counter)
        pfhpa_results: int = result_checker(fields, counter)
        pfhpa_flags: str = flag_checker(fields, counter)
        pfhps_flags: str = flag_checker(fields, counter)
        pfns_flags: str = flag_checker(fields, counter)
        pfpea_flags: str = flag_checker(fields, counter)
        pfpes_flags: str = flag_checker(fields, counter) 
        pfteda_results: int = result_checker(fields, counter)
        pfteda_flags: str = flag_checker(fields, counter)
        pftrda_results: int = result_checker(fields, counter)
        pftrda_flags: str = flag_checker(fields, counter)
        pfunda_results: int = result_checker(fields, counter)
        pfunda_flags: str = flag_checker(fields, counter)
        sampling_results: int = fields[64]

        return hex_id, system_name, wssn, system_type, sample_date, treatment_status, hfpodra_results, hfpodra_flags, pfbs_results, pfbs_flags, pfhxa_results, pfhxa_flags, pfhxs_results, pfhxs_flags, pfna_results, pfna_flags, pfoa_results, pofa_flags, pfos_results, pfos_flags, pf3ouds11ci_results, pf3ouds11ci_flags, pf3ons9cl_results, pf3ons9cl_flags, adona_results, adona_flags, ftsa42_flags, ftsa62_flags, ftsa82_flags, fosa_results, fosa_flags, netfosar_results, netfosaf_flags, nmefosaa_results, nmefosaa_flags, pfba_flags, pfda_results, pfda_flags, pfdoda_results, pfdoda_flags, pfds_results, pfds_flags, pfhpa_results, pfhpa_flags, pfhps_flags, pfns_flags, pfpea_flags, pfpes_flags, pfteda_results, pfteda_flags, pftrda_results, pftrda_flags, pfunda_results, pfunda_flags, sampling_results
    except Exception as exe:
        sys.exit(exe)

def result_checker(fields, counter):
    if fields[18+counter].isnumeric():    
        substance: int = int(fields[18+counter])
    else:
        substance: str = fields[18+counter]
    counter += 1
    return substance

def flag_checker(fields, counter):
    if fields[19+counter].startswith('"') and not fields[20+counter].endswith('"'):
        flag: str = fields[19+counter]+fields[20+counter]
    else: # fields[19+counter].startswith('"') and fields[20+counter].endswith('"')
        flag: str = fields[19+counter]
    counter += 1
    return flag