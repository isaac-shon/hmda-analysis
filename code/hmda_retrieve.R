library(httr)     # For downloading files
library(zip)      # For unzipping files
library(fs)       # For file system functions

setwd('C:/Users/isaac/Desktop/Projects/hmda-analysis')
# Define the years for which we want to download the data
years <- c(2017)

# Create a loop that downloads and stores the zip files to the data folder
for (year in years) {
  url <- paste0('https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_', year, '_nationwide_all-records_labels.zip')
  
  # Define the file path
  zip_path <- file.path("data/", paste0("hmda_", year, ".zip"))
  
  # Download the zip file
  GET(url, write_disk(zip_path, overwrite = TRUE))
  
  # OPTIONAL: Unzip the file
  # unzip(zip_path, exdir = "data/")
  # 
  # Remove the zip file
  # file_delete(zip_path)
  
  cat("Downloaded", year, "data\n")
}

cat("All files downloaded.\n")
