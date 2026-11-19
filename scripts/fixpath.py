import pandas as pd
import os

# 1. Load the data we made in Colab
df = pd.read_csv('mapped_samples.csv')

# 2. Update this to where your samples are on your hard disk
# Example: 'D:/Music/Samples/My_Collection'
LOCAL_ROOT = r'E:\202Samples\OST Audio - Synthwave Drums (WAV)' 

def repair(row):
    # This rebuilds the path using the filename + your local folder
    return os.path.join(LOCAL_ROOT, row['folder'], row['name']).replace("\\", "/")

df['path'] = df.apply(repair, axis=1)

# 3. Save it
df.to_csv('mapped_samples_local.csv', index=False)
print(f"✅ Repaired {len(df)} paths.")
print(f"Sample Check: {df['path'].iloc[0]}")