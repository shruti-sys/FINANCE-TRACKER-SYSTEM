
####PDF TO CSV

import pdftables_api 

conversion = pdftables_api.Client('uw4g07tktvsl') 

conversion.csv('test.pdf', 'input')

#######REMOVE HDFC INFO

import pandas as pd

csv_file_path = 'input.csv' 
df = pd.read_csv(csv_file_path, header=None)

df_cleaned = df.drop_duplicates(keep='first')

cleaned_csv_path = 'cleaned_output.csv' 

df_cleaned.to_csv(cleaned_csv_path, index=False, header=None)

print(f"Cleaned CSV file saved to {cleaned_csv_path}.")


#####REMOVE PAGE NUMBERS

import pandas as pd

csv_file_path = 'cleaned_output.csv'  
df = pd.read_csv(csv_file_path)

pattern = 'Page No .: \d+'

mask = ~df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1)

df_filtered = df[mask]


modified_csv_path = 'modified_output.csv'  

df_filtered.to_csv(modified_csv_path, index=False)       
    
print(f"Modified CSV file saved to {modified_csv_path}.")


# Remove All null but Third value line

import pandas as pd

csv_file_path = 'modified_output.csv'  

df = pd.read_csv(csv_file_path, header=None)

condition = df.iloc[:, :2].isnull().all(axis=1) & ~df[2].isnull()

filtered_df = df[~condition]

print("Filtered DataFrame:")
print(filtered_df)

filtered_csv_path = 'filtered_output.csv'  
filtered_df.to_csv(filtered_csv_path, index=False)

print(f"Filtered lines saved to {filtered_csv_path}.")

