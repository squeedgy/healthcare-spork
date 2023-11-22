# src/data_preprocessing/preprocess_data.py
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_hospital_data(hospital_data):
    # Perform data cleaning for the Hospital_General_Information.csv
    # Example: Drop unnecessary columns, handle missing values, etc.
    cleaned_hospital_data = hospital_data.drop(columns=['Hospital overall rating footnote', 'MORT Group Footnote', 'Safety Group Footnote', 'READM Group Footnote', 'Pt Exp Group Footnote', 'TE Group Footnote'])
    # Additional cleaning steps...

    return cleaned_hospital_data

def merge_data(hospital_data, neuropsychiatry_data):
    # Merge the hospital and neuropsychiatry data based on a common key, e.g., ZIP Code
    merged_data = pd.merge(hospital_data, neuropsychiatry_data, left_on='ZIP Code', right_on='zip_code', how='inner')
    # Additional merging steps...

    return merged_data

def preprocess_main():
    # Define file paths
    hospital_file_path = 'data/raw/Hospital_General_Information.csv'
    neuropsychiatry_file_path = 'data/raw/Neuropsychiatry.csv'

    # Load data
    hospital_data = load_data(hospital_file_path)
    neuropsychiatry_data = load_data(neuropsychiatry_file_path)

    # Clean data
    cleaned_hospital_data = clean_hospital_data(hospital_data)

    # Merge data
    merged_data = merge_data(cleaned_hospital_data, neuropsychiatry_data)

    # Save the processed data
    merged_data.to_csv('data/processed/processed_data.csv', index=False)

if __name__ == "__main__":
    preprocess_main()
