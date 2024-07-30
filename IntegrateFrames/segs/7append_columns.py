import os
import pandas as pd

# Directory containing the text files
directory = r"G:\.shortcut-targets-by-id\0B8-gGFa6hkR4XzJJMDlqZXVKRk0\ansom\Data\THz 1\Qdots.20240701\Position Test\Pos0\processed\individual"
output = directory + "/combined_data.csv"

# Initialize an empty DataFrame to hold the combined data
combined_df = pd.DataFrame()

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Check if the file is a text file
        filepath = os.path.join(directory, filename)
        
        # Read the file into a DataFrame
        try:
            df = pd.read_csv(filepath, sep=',', header=None)
            
            # Extract the wavelength column (assumed to be the same in all files)
            if combined_df.empty:
                combined_df['Wavelength'] = df[0]
            
            # Extract the second column and name it after the filename (without extension)
            combined_df[filename.split('.')[0]] = df[1]
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Save the combined DataFrame to a CSV file
combined_df.to_csv(output, index=False)
