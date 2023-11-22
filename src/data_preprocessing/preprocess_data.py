import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_hospital_data(hospital_data):
    cleaned_hospital_data = hospital_data.drop(columns=['Hospital overall rating footnote', 'MORT Group Footnote', 'Safety Group Footnote', 'READM Group Footnote', 'Pt Exp Group Footnote', 'TE Group Footnote'])

    return cleaned_hospital_data

def merge_data(hospital_data, neuropsychiatry_data):
    merged_data = pd.merge(hospital_data, neuropsychiatry_data, left_on='ZIP Code', right_on='zip_code', how='inner')

    return merged_data

def preprocess_main():
    hospital_file_path = 'data/raw/Hospital_General_Information.csv'
    neuropsychiatry_file_path = 'data/raw/Neuropsychiatry.csv'

    hospital_data = load_data(hospital_file_path)
    neuropsychiatry_data = load_data(neuropsychiatry_file_path)

    cleaned_hospital_data = clean_hospital_data(hospital_data)

    merged_data = merge_data(cleaned_hospital_data, neuropsychiatry_data)

    merged_data.to_csv('data/processed/processed_data.csv', index=False)

if __name__ == "__main__":
    preprocess_main()
