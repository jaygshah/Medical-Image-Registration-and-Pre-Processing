import pandas as pd
import numpy as np

def remove_same_value_features(df):
    return [e for e in df.columns if df[e].nunique() == 1]

def remove_null_value_features(df):
	return [col for col in df.columns if df[col].isnull().all()]

clinical_data = pd.read_csv ('clinical_data.csv')
print("Original shape: ", clinical_data.shape)
clinical_data = clinical_data[ 
((clinical_data['redcap_event_name'] == 'baseline_arm_2') & pd.isnull(clinical_data['redcap_repeat_instrument'])) |
((clinical_data['redcap_event_name'] == 'baseline_arm_1') & pd.isnull(clinical_data['redcap_repeat_instrument']))
]

same_val_cols = remove_same_value_features(clinical_data)
clinical_data = clinical_data.drop(columns = same_val_cols)
empty_val_cols = remove_null_value_features(clinical_data)
clinical_data = clinical_data.drop(columns = empty_val_cols)


print("Shape after cleaning: ", clinical_data.shape)
clinical_data.to_csv('processed_clinical_data.csv', sep='\t', encoding='utf-8')