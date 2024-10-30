# HMDA LAR Data Retrieval and Analysis

Since its passage as federal law in 1975, the Home Mortgage Disclosure Act (HMDA) requires most mortgage lenders to report detailed information about their lending practices to ensure transparency in the home mortgage markets. This project retrieves HMDA Loan Application Register (LAR) files and performs simple exploratory analysis to identify patterns on lending activity, geographic trends, and borrower demographics for a small cross section of the data. 

In the ```code``` folder, the script ```hmda_retrieve.py``` retrieves HMDA LAR datasets from the Consumer Financial Protection Bureau and stores them in the ```data``` folder. Similarly, the ```hmda_retrieve.R``` script does the same, but using R. We will also extract the zip files, though this is meant as an optional exercise. In most cases it is better to call large datasets through some other mechanism that doesn't require local storage (e.g., calling via API, SQL Database, etc.).

For more historical HMDA LAR data (i.e., 1981-2006), see Andrew Forrester's work [here](https://github.com/acforrester/HMDA.Historical). This is an incredible project that retrieves historical HMDA LAR files from the National Archives, which is also available for download [on openICPSR](https://www.openicpsr.org/openicpsr/project/151921/version/V1/view). 
