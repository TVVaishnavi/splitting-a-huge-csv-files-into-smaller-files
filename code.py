import os
import pandas as pd
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')


# Define the lists of headers for each category
First_Name = ["First Name", "Name of Representative 1", "If you are planning to bring a friend along, give us their details. (First Name)", "Name (First Name)", "Full Name", "Full Name (can be split into First Name and Last Name)", "Founder details (if includes first name)", "Full Name (Founder 1)", "Full Name (Co-founder 2)(Optional)", "Full Name (Co-founder 3)(Optional)", "First name", "Name", "Name of Co-founder (First Name)", "Founder Details >> Founder 1 >> First Name", "Founder Details >> Founder 2 >> First Name", "Founder Details >> Founder 3 >> First Name", "Founder Details >> Founder 4 >> First Name", "Name of POC 2 (First Name)", "Founder/Co-founder First Name", "Name of the founder/co-founders (if separate fields for first name)", "Name of the POC (First Name)", "Name of POC 2 (First Name)", "Companion Name (First Name)", "Founder details >> Founder 1 >> Name", "Founder details >> Co-founder 1 >> Name"]
Last_Name =["Name of the POC (Last Name)", "Name of POC 2 (Last Name)", "Companion Name (Last Name)", "Founder details >> Founder 1 >> Name.1", "Founder details >> Co-founder 1 >> Name.1", "Founder details >> Co-founder 2 >> Name.1", "Founder details >> Co-founder 3 >> Name.1", "Name of POC 2 (Last Name)", "Founder/Co-founder Last Name", "Name of the founder/co-founders (if separate fields for last name)", "Name of Co-founder (Last Name)", "Founder Details >> Founder 1 >> Last Name", "Founder Details >> Founder 2 >> Last Name", "Founder Details >> Founder 3 >> Last Name", "Founder Details >> Founder 4 >> Last Name", "Last name", "Founder details (if includes last name)", "Name (Last Name)", "Full Name (This could be split into first and last name if needed)", "Last Name", "Name of Representative 2", "If you are planning to bring a friend along, give us their details. (Last Name)"]
Email_id = ["Email", "Founder details >> Co-founder 1 >> Email","Founder details >> Co-founder 6 >> Email", "Founder details >> Co-founder 7 >> Email", "Founder details >> Co-founder 8 >> Email", "Founder details >> Co-founder 9 >> Email",  "Business Email of POC from enterprise", "Business Email.1", "Business Email.2", "Email (Work Id)",  "Official Email Address", "Institutional Email Address", "Founder Email", "Business Email of POC from enterprise", "Business Email ID / வணிக மின்னஞ்சல்", "Email (Work Id)", "Your Business Email Address", "Business Email Address", "Email address (abc@company.com)", "Founder Details >> Founder 1 >> Email", "Business Email Address","Official Email","Official Email ID", "Email id", "Email Address", "Work Email", "Corporate Email", "Business Email Address (Official)", "Work Email", "Work Email Address", "Business Email ID", "Business E-mail ID", "Email", "Email Address","Business Email ID", "Business E-mail ID","Work Email Address", "Email", "Work Email Address", "Business E-mail ID", "Work Email Address", "Business E-mail ID", "Email ID", "Registered Email Address", "Email Address", "Email ID", "Email", "Registered Email Address", "Email Address", "Email Id", "E-mail", "Business Email", "Business Email Address", "Your +1's Email ID"]
Phone_Number = ["Mobile Number of POC from enterprise", "Mobile Number.2", "Phone Number / தொலைபேசி எண் -", "Founder Mobile Number", "Companion Mobile Number", "Mobile Number (Please ensure same Phone Number as Level 1 Application Form)", "Mobile Number of POC from enterprise", "Mobile Number.2", "Phone Number / தொலைபேசி எண்", "Phone Number", "Phone number / தொலைபேசி எண்", "Founder Contact Number", "Phone Number", "Mobile", "WhatsApp Number", "Phone Number (Whatsapp Only!)", "Mobile", "WhatsApp Number", "Phone Number (Whatsapp Only!)", "Contact number", "Phone Number without country code", "Mobile Number", "Business Phone Number", "Mobile", "Contact Number", "Please provide your Phone number if you want us to connect over a call", "Contact number", "Phone Number without country code", "Mobile Number", "Business Phone Number", "Mobile", "Mobile Number.1", "Contact Number", "Business Phone Number", "Phone number", "Mobile", "Contact Number (Applicant)", "Contact Number:", "Whatsapp Number", "Mobile Number", "Phone Number", "Contact Number of Representative 1", "Contact Number of Representative 2"
]
Linkedin = ["LinkedIn", "LinkedIn Profile URL", "LinkedIn Profile Link", "LinkedIn URL", "LinkedIn link", "LinkedIn ID", "LinkedIn Profile Link (Founder 1)", "LinkedIn Profile Link (Co-founder 2)(Optional)", "LinkedIn Profile Link (Co-founder 3)(Optional)", "LinkedIn profile", "LinkedIn URL", "LinkedIn URL", "LinkedIn URL.1", "LinkedIn URL.2", "LinkedIn URL.3", "LinkedIn URL.4", "LinkedIn URL.5", "LinkedIn URL.6", "LinkedIn URL.7", "LinkedIn URL.8", "Your LinkedIn profile", "Your LinkedIn Profile link", "Your Nominee's LinkedIn", "LinkedIn Profile/ LinkedIn விவரம்", "LinkedIn Profile Link", "LinkedIn.1", "Linkedin Profile URL", "LinkedIn", "LinkedIn Profile", "LinkedIn Profile Link", "LinkedIn URL", "LinkedIn link", "LinkedIn ID", "LinkedIn Profile Link (Founder 1)", "LinkedIn Profile Link (Co-founder 2)(Optional)", "LinkedIn Profile Link (Co-founder 3)(Optional)", "Founder's LinkedIn profile", "Founder details >> Founder 1 >> LinkedIn URL", "Founder details >> Co-founder 1 >> LinkedIn URL", "Founder details >> Co-founder 2 >> LinkedIn URL", "LinkedIn URL.1", "LinkedIn URL.2", "LinkedIn URL.3", "LinkedIn URL.4", "LinkedIn URL.5", "LinkedIn URL.6", "LinkedIn URL.7", "LinkedIn URL.8", "Your LinkedIn profile", "Your LinkedIn Profile link", "Your Nominee's LinkedIn", "LinkedIn URL - Founder 1", "LinkedIn URL - Founder 2"]
Company_Name = ["Company/Brand/Institute/School/University/Startup Name", "Organisation Name", "Company Name", "Brand Name", "Name of Startup", "Name of woman founder/co-founder", "School name", "Name of the Company", "Legal/Registered Name of Company", "Company Name (Legal Name as registered with the Government)", "University Name", "Name of the Organisation", "Name of Brand (if different from company name)", "Your Name / Name of the Founders", "Name of the 1st Startup", "Name of the 2nd Startup", "Name of the company", "Name of all the founders", "Name of your brand", "Name of the founder(s)", "Brand/Company Name", "Name of enterprise", "Name of the enterprise", "Company Name/Organisation", "Organisation/Institution/Company", "Organisation Name", "Company Name", "E-mail", "Organisation", "Brand Name", "Name of Startup", "Name of woman founder/co-founder", "School name", "Name of the Company", "Legal/Registered Name of Company", "Company Name (Legal Name as registered with the Government)", "University Name", "Name of the Organisation", "Name of Brand (if different from company name)", "Your Name / Name of the Founders", "Name of the 1st Startup", "Name of the 2nd Startup", "Name of the company", "Name of all the founders", "Name of your brand", "Name of the founder(s)"]                                                                
Company_Website = ["Company Website", "Website", "Website link", "Startup URL", "Links to company website", "Company website", "Company's website link", "Company's website/app link", "Brand Website", "Company URL", "Company Website/App Link", "Website URL", "Company Website", "Website", "Website link", "Startup URL", "Links to company website", "Company website", "Company's website link", "Company's website/app link", "Brand Website", "Website URL"]
Designation =["Designation", "Designation of Representative 1", "Designation of Representative 2", "Role/ Title", "Your Job role", "Job Role", "Job title / role", "Job Role:", "Desgination", "Current Designation", "Designation / பதவி -", "Companion Designation", "Designation (Founder 1)", "Designation (Co-founder 2)(Optional)", "Designation (Co-founder 3)(Optional)", "Role/ Title"]
City = ["City", "City (HQ)", "Location", "City.1", "State/Region", "Location (City)", "City of headquarters / தலைமையகம் நகரம்", "State / Province", "City you prefer to join for Moonshot Day", "City from where the Web3 startup is operating.", "Location (City, State)", "State/ Region"]
Industry = ["Industry", "Sector (Industry)", "Industry Vertical", "Type of company", "Business Type", "Sector", "ustry/Sector", "Industry", "Sector (Industry)", "Industry Vertical", "Type of company", "Business Type", "Sector"]

# Dictionary to hold data for each category

data_dict = {
    "First_Name":[],
    "Last_Name": [],
    "Email_id": [],
    "Phone_Number":[],
    "Linkedin": [],
    "Company_Name":[],
    "Company_Website":[],
    "Designation":[],
    "City":[],
    "Industry":[]
}

head_count = {
    "First_Name":0,
    "Last_Name": 0,
    "Email_id": 0,
    "Phone_Number":0,
    "Linkedin":0,
    "Company_Name":0,
    "Company_Website":0,
    "Designation":0,
    "City":0,
    "Industry":0
}

list_of_columns=[]
count=dict()
# Directory containing the files
path = 'C:/Users/Vaishnavi/OneDrive/Desktop/workspace/csv project/drive file'
files = os.listdir(path)

# Process each file
for s in files:
    subdir_path = os.path.join(path, s)
    if os.path.isdir(subdir_path):
        for track in os.scandir(subdir_path):
            if track.is_file():
                if track.name.endswith('.csv'):
                    df = pd.read_csv(track.path)
                elif track.name.endswith('.xlsx'):
                    df = pd.read_excel(track.path)
                else:
                    continue
                
                columns=df.columns
                for column in columns:
                   list_of_columns.append(column)
                   #if column in data_dict:
                        

#print(list_of_columns)
                # Extract data for each category
                for column in df.columns:
                   if column in First_Name:
                      head_count["First_Name"]+=1
                   elif column in Last_Name:
                       head_count["Last_Name"]+=1
                   elif column in Email_id:
                       head_count["Email_id"]+=1
                   elif column in Phone_Number:
                       head_count["Phone_Number"]+=1
                   elif column in Linkedin:
                       head_count["Linkedin"]+=1
                   elif column in Company_Name:
                       head_count["Company_Name"]+=1
                   elif column in Company_Website:
                       head_count["Company_Website"]+=1
                   elif column in Designation:
                      head_count["Designation"]+=1
                   elif column in City:
                       head_count["City"]+=1
                   elif column in Industry:
                      head_count["Industry"]+=1


                for column in df.columns:
                    if column in First_Name:
                        data_dict["First_Name"].extend(df[column].dropna().tolist())
                    elif column in Last_Name:
                        data_dict["Last_Name"].extend(df[column].dropna().tolist())
                    elif column in Email_id:
                        data_dict["Email_id"].extend(df[column].dropna().tolist())
                    elif column in Phone_Number:
                        data_dict["Phone_Number"].extend(df[column].dropna().tolist())
                    elif column in Linkedin:
                        data_dict["Linkedin"].extend(df[column].dropna().tolist())
                    elif column in Company_Name:
                        data_dict["Company_Name"].extend(df[column].dropna().tolist())
                    elif column in Company_Website:
                        data_dict["Company_Website"].extend(df[column].dropna().tolist())
                    elif column in Designation:
                        data_dict["Designation"].extend(df[column].dropna().tolist())
                    elif column in City:
                        data_dict["City"].extend(df[column].dropna().tolist())
                    elif column in Industry:
                        data_dict["Industry"].extend(df[column].dropna().tolist())
#header=dict()
#for element in list_of_columns:
 #   if element in header:
  #      header[element] += 1
  #  else:
   #     header[element] = 1
#print(header)                        
# Find the maximum length of the lists
max_length = max(len(lst) for lst in data_dict.values())

# Pad shorter lists with NaNs to match the maximum length
for key in data_dict:
   if len(data_dict[key]) < max_length:
       data_dict[key].extend([np.nan] * (max_length - len(data_dict[key])))

# Create a DataFrame from the data dictionary
df_output = pd.DataFrame(data_dict)

# Save the DataFrame to a new CSV file
output_file = 'Extracted_data.csv'
df_output.to_csv(output_file, index=False, encoding='utf-8')

print(f"Data successfully extracted and saved to {output_file}") 
# Check missing data in the extracted lists
#for category in data_dict:
    #missing_count = sum(pd.isna(value) for value in data_dict[category])
    #print(f"Missing values in {category}: {missing_count}")
print(head_count)