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

# columns = list(clinical_data)
# for i in range(len(columns)):
# 	print("index:", i, columns[i])

cols_to_drop = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 18, 23, 27, 28, 29, 31, 55, 56, 57, 59, 61, 62, 63, 65, 66, 67, 68, 
69, 70, 139, 140, 141, 143, 145, 149, 150, 151, 152, 155, 156, 157, 158, 159, 160,
161, 162, 163, 164, 165, 166, 168, 171, 173, 174, 175, 176, 177, 178, 179, 180, 181, 183, 185, 188, 198,
199, 200, 201, 202, 203, 204, 205, 206, 210, 211, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261,
263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283,
285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298,
300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321,
323, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 343, 344, 345, 346, 347, 348, 349, 350, 351,
353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 378, 
379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 
409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435,
437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 462, 461, 463,
464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489,
491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518,
519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 535]
clinical_data.drop(clinical_data.columns[cols_to_drop], axis=1, inplace=True)

print("Columns selectively dropped: ", len(cols_to_drop))
print("Shape after dropping columns: ", clinical_data.shape)
clinical_data.to_csv('processed_clinical_data.csv', sep='\t', encoding='utf-8')