import pandas as pd
import numpy as np

clinical_data = pd.read_csv ('hand_processed_clinical_data.csv')
print("Original shape: ", clinical_data.shape)
clinical_data = clinical_data.fillna(clinical_data.mode().iloc[0])
print("Now shape: ", clinical_data.shape)

race = []
for i in clinical_data.index:
	if clinical_data['race___2'][i] == 1:
		race.append(1)
	if clinical_data['race___3'][i] == 1:
		race.append(2)
	if clinical_data['race___5'][i] == 1:
		race.append(3)
	if clinical_data['race___6'][i] == 1:
		race.append(4)

clinical_data.insert(3, "race", race, True)
clinical_data.drop(columns=['race___2', 'race___3', 'race___5', 'race___6'], axis=1, inplace=True)

clinical_data.to_csv('imputed_hand_processed_clinical_data.csv', index=False)