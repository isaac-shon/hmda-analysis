'''
About: Retrieving HMDA LAR Files from the CFPB

We can directly download relatively recent HMDA records from the CFPB. This will take a while!
As a short side note, this will only work for HMDA records available on the CFPB website (i.e., 2007-2017 records)
In this example, we will retrieve HMDA LAR files for 2015, 2016, and 2017. We will also extract the zip files 
(though this is optional and is meant as an exercise). For more historical HMDA LAR data (i.e., 1981-2006),
see Andrew Forrester's project on openICPSR: https://www.openicpsr.org/openicpsr/project/151921/version/V1/view. 

'''

import os
import requests
import zipfile

os.chdir("C:\\Users\\isaac\\OneDrive\\Desktop\\example_codes\\HMDA")

# We want to first list out the years that we want to extract data
years = [2015, 2016, 2017]

# Create a loop that downloads, unzips, and stores the CSVs to our data folder:
for year in years:
    url = f'https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_{year}_nationwide_all-records_labels.zip'
    response = requests.get(url)
    
    zip_path = os.path.join('data\\', f'hmda_{year}.zip')
    
    with open(zip_path, 'wb') as f:
        f.write(response.content)
        
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('data\\')
        
    os.remove(zip_path)
        
    print(f'Downloaded and unzipped {year} data')
    
print("All files downloaded and unzipped.")



''' 
An alternative method one could use is to use the tidyhome library, which offers a seamless way to retrieve
HMDA data. This library uses the CFPB's Data Browser API and allows users to retrieve certain subsets of the
national LAR files. If you are okay with placing some restrictions on your data, this might be a much
better alternative than downloading the raw files all at once. Consider the following:

%pip install tidyhome
import tidyhome as th

th.get_loans(2019, "dc", th.Action.INCOMPLETE, [th.Race.BLACK, th.Race.WHITE])

'''
