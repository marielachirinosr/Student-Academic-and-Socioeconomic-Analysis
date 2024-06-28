import pandas as pd

# Load the data

data = pd.read_csv('data.csv', delimiter=';')

# Display the first few rows of the data

#print(data.head())

#Duplicate values

duplicate = data.duplicated()
print("Total number of duplicates values in DataFrame:",duplicate.sum())

# Total number of null values in DataFrame

total_null_count = data.isnull().sum().sum()
print("Total number of null values in DataFrame:", total_null_count)

# Define mappings for categorical values

mappings = {
    'Marital status': {
        1: 'Single', 
        2: 'Married', 
        3: 'Widower', 
        4: 'Divorced', 
        5: 'Facto Union', 
        6: 'Legally Separated'
    },
    'Application mode': {
        1: '1st phase - general contingent',
        2: 'Ordinance No. 612/93',
        5: '1st phase - special contingent (Azores Island)',
        7: 'Holders of other higher courses',
        10: 'Ordinance No. 854-B/99',
        15: 'International student (bachelor)',
        16: '1st phase - special contingent (Madeira Island)',
        17: '2nd phase - general contingent',
        18: '3rd phase - general contingent',
        26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
        27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
        39: 'Over 23 years old',
        42: 'Transfer',
        43: 'Change of course',
        44: 'Technological specialization diploma holders',
        51: 'Change of institution/course',
        53: 'Short cycle diploma holders',
        57: 'Change of institution/course (International)'
    },
    'Course': {
        33: 'Biofuel Production Technologies',
        171: 'Animation and Multimedia Design',
        8014: 'Social Service (evening attendance)',
        9003: 'Agronomy',
        9070: 'Communication Design',
        9085: 'Veterinary Nursing',
        9119: 'Informatics Engineering',
        9130: 'Equinculture',
        9147: 'Management',
        9238: 'Social Service',
        9254: 'Tourism',
        9500: 'Nursing',
        9556: 'Oral Hygiene',
        9670: 'Advertising and Marketing Management',
        9773: 'Journalism and Communication',
        9853: 'Basic Education',
        9991: 'Management (evening attendance)'
    },
    'Daytime/evening attendance	': {
        1: 'Daytime',
        0: 'Evening'
    },
     'Previous qualification': {
        1: 'Secondary education',
        2: "Higher education - bachelor's degree",
        3: "Higher education - degree",
        4: "Higher education - master's",
        5: "Higher education - doctorate",
        6: "Frequency of higher education",
        9: "12th year of schooling - not completed",
        10: "11th year of schooling - not completed",
        12: "Other - 11th year of schooling",
        14: "10th year of schooling",
        15: "10th year of schooling - not completed",
        19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
        38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
        39: "Technological specialization course",
        40: "Higher education - degree (1st cycle)",
        42: "Professional higher technical course",
        43: "Higher education - master (2nd cycle)"
    },
    'Nacionality': {
        1: 'Portuguese',
        2: 'German',
        6: 'Spanish',
        11: 'Italian',
        13: 'Dutch',
        14: 'English',
        17: 'Lithuanian',
        21: 'Angolan',
        22: 'Cape Verdean',
        24: 'Guinean',
        25: 'Mozambican',
        26: 'Santomean',
        32: 'Turkish',
        41: 'Brazilian',
        62: 'Romanian',
        100: 'Moldova (Republic of)',
        101: 'Mexican',
        103: 'Ukrainian',
        105: 'Russian',
        108: 'Cuban',
        109: 'Colombian'
    },
    'Mother\'s qualification': {
        1: 'Secondary Education - 12th Year of Schooling or Eq.',
        2: "Higher Education - Bachelor's Degree",
        3: "Higher Education - Degree",
        4: "Higher Education - Master's",
        5: "Higher Education - Doctorate",
        6: "Frequency of Higher Education",
        9: "12th Year of Schooling - Not Completed",
        10: "11th Year of Schooling - Not Completed",
        11: "7th Year (Old)",
        12: "Other - 11th Year of Schooling",
        14: "10th Year of Schooling",
        18: "General Commerce Course",
        19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        22: "Technical-Professional Course",
        26: "7th Year of Schooling",
        27: "2nd Cycle of the General High School Course",
        29: "9th Year of Schooling - Not Completed",
        30: "8th Year of Schooling",
        34: "Unknown",
        35: "Can't Read or Write",
        36: "Can Read Without Having a 4th Year of Schooling",
        37: "Basic Education 1st Cycle (4th/5th Year) or Equiv.",
        38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        39: "Technological Specialization Course",
        40: "Higher Education - Degree (1st Cycle)",
        41: "Specialized Higher Studies Course",
        42: "Professional Higher Technical Course",
        43: "Higher Education - Master (2nd Cycle)",
        44: "Higher Education - Doctorate (3rd Cycle)"
    },
    'Father\'s qualification': {
        1: 'Secondary Education - 12th Year of Schooling or Eq.',
        2: "Higher Education - Bachelor's Degree",
        3: "Higher Education - Degree",
        4: "Higher Education - Master's",
        5: "Higher Education - Doctorate",
        6: "Frequency of Higher Education",
        9: "12th Year of Schooling - Not Completed",
        10: "11th Year of Schooling - Not Completed",
        11: "7th Year (Old)",
        12: "Other - 11th Year of Schooling",
        13: "2nd Year Complementary High School Course",
        14: "10th Year of Schooling",
        18: "General Commerce Course",
        19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        20: "Complementary High School Course",
        22: "Technical-Professional Course",
        25: "Complementary High School Course - Not Concluded",
        26: "7th Year of Schooling",
        27: "2nd Cycle of the General High School Course",
        29: "9th Year of Schooling - Not Completed",
        30: "8th Year of Schooling",
        31: "General Course of Administration and Commerce",
        33: "Supplementary Accounting and Administration",
        34: "Unknown",
        35: "Can't Read or Write",
        36: "Can Read Without Having a 4th Year of Schooling",
        37: "Basic Education 1st Cycle (4th/5th Year) or Equiv.",
        38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        39: "Technological Specialization Course",
        40: "Higher Education - Degree (1st Cycle)",
        41: "Specialized Higher Studies Course",
        42: "Professional Higher Technical Course",
        43: "Higher Education - Master (2nd Cycle)",
        44: "Higher Education - Doctorate (3rd Cycle)"
},
    'Mother\'s occupation': {
        0: 'Student',
        1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
        2: 'Specialists in Intellectual and Scientific Activities',
        3: 'Intermediate Level Technicians and Professions',
        4: 'Administrative Staff',
        5: 'Personal Services, Security and Safety Workers and Sellers',
        6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
        7: 'Skilled Workers in Industry, Construction and Craftsmen',
        8: 'Installation and Machine Operators and Assembly Workers',
        9: 'Unskilled Workers',
        10: 'Armed Forces Professions',
        90: 'Other Situation',
        99: '(Blank)',
        122: 'Health Professionals',
        123: 'Teachers',
        125: 'Specialists in Information and Communication Technologies (ICT)',
        131: 'Intermediate Level Science and Engineering Technicians and Professions',
        132: 'Technicians and Professionals, of Intermediate Level of Health',
        134: 'Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services',
        141: 'Office Workers, Secretaries in General and Data Processing Operators',
        143: 'Data, Accounting, Statistical, Financial Services and Registry-Related Operators',
        144: 'Other Administrative Support Staff',
        151: 'Personal Service Workers',
        152: 'Sellers',
        153: 'Personal Care Workers and the Like',
        171: 'Skilled Construction Workers and the Like, Except Electricians',
        173: 'Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like',
        175: 'Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts',
        191: 'Cleaning Workers',
        192: 'Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry',
        193: 'Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport',
        194: 'Meal Preparation Assistants'
    },
    'Father\'s occupation': {
        0: 'Student',
        1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Manager',
        2: 'Specialists in Intellectual and Scientific Activities',
        3: 'Intermediate Level Technicians and Professions',
        4: 'Administrative staff',
        5: 'Personal Services, Security and Safety Workers and Sellers',
        6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
        7: 'Skilled Workers in Industry, Construction and Craftsmen',
        8: 'Installation and Machine Operators and Assembly Workers',
        9: 'Unskilled Workers',
        10: 'Armed Forces Professions',
        90: 'Other Situation',
        99: '(blank)', 
        101: 'Armed Forces Officers',
        102: 'Armed Forces Sergeants',
        103: 'Other Armed Forces personnel',
        112: 'Directors of administrative and commercial services',
        114: 'Hotel, catering, trade and other services directors',
        121: 'Specialists in the physical sciences, mathematics, engineering and related techniques',
        122: 'Health professionals',
        123: 'Teachers',
        124: 'Specialists in finance, accounting, administrative organization, public and commercial relations',
        131: 'Intermediate level science and engineering technicians and professions',
        132: 'Technicians and professionals, of intermediate level of health',
        134: 'Intermediate level technicians from legal, social, sports, cultural and similar services',
        135: 'Information and communication technology technicians',
        141: 'Office workers, secretaries in general and data processing operators',
        143: 'Data, accounting, statistical, financial services and registry-related operators',
        144: 'Other administrative support staff',
        151: 'Personal service workers',
        152: 'Sellers',
        153: 'Personal care workers and the like',
        154: 'Protection and security services personnel',
        161: 'Market-oriented farmers and skilled agricultural and animal production workers',
        163: 'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
        171: 'Skilled construction workers and the like, except electricians',
        172: 'Skilled workers in metallurgy, metalworking and similar',
        174: 'Skilled workers in electricity and electronics',
        175: 'Workers in food processing, woodworking, clothing and other industries and crafts',
        181: 'Fixed plant and machine operators',
        182: 'Assembly workers',
        183: 'Vehicle drivers and mobile equipment operators',
        192: 'Unskilled workers in agriculture, animal production, fisheries and forestry',
        193: 'Unskilled workers in extractive industry, construction, manufacturing and transport',
        194: 'Meal preparation assistants',
        195: 'Street vendors (except food) and street service providers'
},
    'Displaced': {
        0: 'No', 
        1: 'Yes'
    },
    'Educational special needs': {
        0: 'No', 
        1: 'Yes'
    },
    'Debtor': {
        0: 'No', 
        1: 'Yes'
    },
    'Tuition fees up to date': {
        0: 'No', 
        1: 'Yes'
    },
    'Gender': {
        0: 'Female', 
        1: 'Male'
    },
    'Scholarship holder': {
        0: 'No', 
        1: 'Yes'
    },
    'International': {
        0: 'No', 
        1: 'Yes'
    }

}

# Replace categorical values

for column, mapping in mappings.items():
    data[column] = data[column].replace(mapping)

print(data)

# Save the cleaned dataset

data.to_csv('cleaned_dataset.csv', index=False)