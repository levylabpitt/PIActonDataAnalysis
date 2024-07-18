'''
Background Removal Script for QDots Spectra Data

Context:
Within the area of QDs, we move to different positions (Pos1, Pos2, Pos3, etc.) and take a series of frames (1, 2, 3, etc.).
Between each position, we take a background frame (BG1, BG2, BG3, etc.) to remove the background noise.
'''

import os
import re
from tqdm import tqdm

# Specify the directories
posdir = r"G:\.shortcut-targets-by-id\0B8-gGFa6hkR4XzJJMDlqZXVKRk0\ansom\Data\THz 1\Qdots spectra\Position Test\Pos6_14"
bgdir = rf"{posdir}\bg"
outdir = rf"{posdir}\bgremoved"

# Create the output directory if it does not exist
os.makedirs(outdir, exist_ok=True)

# Regular expression pattern to match the filenames
pattern = re.compile(r'Pos(\d+)_(\d+)\.txt')

# List all files in the directory
filenames = os.listdir(posdir)

# Iterate over the filenames and extract the numeric values
for filename in tqdm(filenames, desc="Removing Background"):
    match = pattern.match(filename)
    if match:
        run_id = match.group(1)
        frame_id = match.group(2)
        
        pos_file_path = rf"{posdir}\{filename}"
        bg_file_path = rf"{bgdir}\BG{run_id}_1.txt"
        
        # Check if the background file exists
        if not os.path.exists(bg_file_path):
            print(f"Background file for {filename} not found.")
            continue
        
        with open(pos_file_path, 'r') as f1, open(bg_file_path, 'r') as f2:
            # print(f"Processing file: {filename}")
            
            poslines = f1.readlines()
            bglines = f2.readlines()
            
            # Ensure both files have the same number of lines
            if len(poslines) != len(bglines):
                print(f"File {filename} and its background file have different line counts.")
                continue

            # Process and subtract intensities
            result_lines = [
                f"{poswavelength},{posstripe},{float(posintensity) - float(bgintensity)}\n"
                for posline, bgline in zip(poslines, bglines)
                for poswavelength, posstripe, posintensity in [posline.strip().split(',')]
                for bgwavelength, bgstripe, bgintensity in [bgline.strip().split(',')]
            ]

        # Write the result to the output file
        with open(rf"{outdir}\{filename}", 'w') as f3:
            f3.writelines(result_lines)

print("Background removal complete.")
