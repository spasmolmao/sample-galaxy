import pandas as pd
import os

# 1. Load your Colab CSV
df = pd.read_csv('mapped_samples.csv')

# 2. Define your NEW local base path
# CHANGE THIS to the actual folder on your D: drive
local_base_path =r"E:\202Samples\OST Audio - Synthwave Drums (WAV)" 

# 3. Logic: Keep the filename, but change the folder path
# This assumes the filenames haven't changed!
df['path'] = df['name'].apply(lambda x: os.path.join(local_base_path, x))

# 4. Save it as a LOCAL version
df.to_csv('mapped_samples_local.csv', index=False)
print("✅ Paths updated! Your Galaxy now points to your Hard Disk.")