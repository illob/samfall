import pandas as pd
import re

# Set pandas to display more rows if needed
pd.set_option('display.max_rows', 500)

# Load the CSV file
df = pd.read_csv('', sep=";",low_memory=False)

# Optional: Function to delete rows where 'mark' contains 'gr' (case-sensitive)
def remove_rows_with_gr(df, column='mark', substring='gr'):
    return df[~df[column].str.contains(substring, case=True, na=False)]

# Optional: Function to delete rows where 'mark' contains any number
def remove_rows_with_numbers(df, column='mark'):
    return df[~df[column].str.contains(r'\d+', na=False)]  # Using regex to detect digits

# Optional: Function to remove rows where 'mark' contains a specific substring (case-sensitive)
def remove_rows_with_substring(df, column='mark', substring=''):
    if not substring:  # If no substring is provided, return the original DataFrame
        return df
    return df[~df[column].str.contains(re.escape(substring), case=True, na=False)]    

# Call the optional functions (comment these lines if you don't want to remove the rows)
df = remove_rows_with_gr(df, column='mark', substring='gr')  # Remove rows with 'gr' in 'mark'
df = remove_rows_with_numbers(df, column='mark')  # Remove rows with any number in 'mark'
df = remove_rows_with_substring(df, column='mark', substring='ET')

# Group by 'beygingarmynd' and 'audkenni', and combine 'mark' values
df_combined = df.groupby(['beyg', 'audk'], as_index=False).agg({
    'mark': lambda x: ','.join(x.dropna().unique()),  # Combine unique non-null 'mark' values
    'ord': 'first',       # Retain the first 'ord' value
    'ordfl': 'first',  # Retain the first 'ordflokkur' value
})
# Reorder the columns
df_combined = df_combined[['ord', 'audk', 'ordfl', 'beyg', 'mark']]

# Custom sort key based on Icelandic alphabet order
icelandic_alphabet = "0123456789AÁBCDÐEÉFGHIÍJKLMNÓOÓPQRSTUÚVWXÝYZÞÆÖ"

def icelandic_sort_key(word):
    # Normalize the word to uppercase, map each character to its position in the Icelandic alphabet
    return [icelandic_alphabet.index(c.upper()) if c.upper() in icelandic_alphabet else ord(c) for c in word]

# Sort by the 'ord' column using the custom Icelandic sort key
df_combined = df_combined.sort_values(by='ord', key=lambda col: col.map(icelandic_sort_key))

# Function to remove numbers from text
def remove_numbers(text):
    return re.sub(r'\d+', '', str(text))

# Apply the function to the 'mark' column to remove numbers
#df_combined['mark'] = df_combined['mark'].apply(remove_numbers)

# Print the value counts of the 'mark' column for validation
print(df_combined['mark'].value_counts())

# Save the final DataFrame to a new CSV file
df_combined.to_csv("", sep=";", index=False)
