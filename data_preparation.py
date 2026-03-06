import kagglehub
import pandas as pd
import os
import shutil

# Download dataset
path = kagglehub.dataset_download("ravindrasinghrana/job-description-dataset")
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
df = pd.read_csv(os.path.join(path, csv_files[0]))

print(f"Original dataset: {len(df)} rows")

# Step 1: Sample 5000 random rows first (for diversity)
df_sample = df.sample(n=5000, random_state=42)

# Step 2: Keep only needed columns
df_clean = df_sample[['Job Title', 'skills', 'Job Description']].copy()

# Step 3: Rename
df_clean.columns = ['job_title', 'skills', 'full_description']

# Step 4: Create job_description (skills + first 150 chars)
df_clean['job_description'] = (
    df_clean['skills'].astype(str) + ' ' + 
    df_clean['full_description'].astype(str).str[:150]
)

# Step 5: Remove duplicates
df_clean = df_clean.drop_duplicates(subset=['job_title'], keep='first')

print(f"After deduplication: {len(df_clean)} unique job titles")

# Step 6: Take top 500 (or all if less)
df_final = df_clean.head(min(500, len(df_clean)))

# Step 7: Keep only needed columns
df_final = df_final[['job_title', 'job_description']]

print(f"Final dataset: {len(df_final)} rows")
print(f"\nSample rows:")
print(df_final.head(3))

# Step 8: Save
if os.path.exists('data.csv'):
    shutil.copy('data.csv', 'data_backup.csv')
    print("\nOld data.csv backed up")

df_final.to_csv('data.csv', index=False)
print("New data.csv created with real Kaggle data!")