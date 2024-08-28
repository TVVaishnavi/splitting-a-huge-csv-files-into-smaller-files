# splitting-a-huge-csv-files-into-smaller-files

Libraries used :
    1. pandas 
    2. os 
    3. sys 
    4. numpy 
steps :
   As a first step, I showed the path of the CSV files, as the file contains 2 directories
   
   To store the directory path I used the os library
   
   Then inside the first directory, I used a loop to find the file name with the extensions .csv and .xlsx 
   
   using the Pandas library  I made the files to read  took all the headers from the CSV files, and stored them in the array.
   
   Then I made that array as a dictionary where to print all the duplicate headers, from the duplicate header, I manually sorted the header which CSV file was needed and stored each list by categories as a list.
   
   I created  a HashSet to count the header as an integer datatype and how many files it repeated to check the extraction was done without missing data.
   
   with using a loop in the columns where the data frame reads the columns  and finds the counts, the count will be stored as a dictionary as a global set.
    As  i created a set to store the extracted data in the new CSV file, as it will be stored as a header in the CSV file. 
   
 "data_dict"  is the set that I have stored the categorized header name, inside the header name list, is a datatype, which traverses to the output file using the panda's library.

 Final Result:
       As a final result, I have successfully saved the extracted data in the output file.
