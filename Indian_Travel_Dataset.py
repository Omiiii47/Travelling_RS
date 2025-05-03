import pandas as pd
import numpy as np

# Create a comprehensive dataset of Indian travel destinations
destinations_data = {
    'Destination_Name': [
        'Goa', 'Jaipur', 'Manali', 'Varanasi', 'Agra', 'Rishikesh', 
        'Darjeeling', 'Amritsar', 'Kodaikanal', 'Mumbai', 'Udaipur', 
        'Leh', 'Andaman Islands', 'Munnar', 'Delhi', 'Hampi', 
        'Shimla', 'Ooty', 'Ranthambore', 'Kolkata', 'Mysore',
        'Pondicherry', 'Coorg', 'Alleppey', 'Nainital', 'Kaziranga',
        'Khajuraho', 'Pushkar', 'Gokarna', 'Mahabalipuram'
    ],
    'State': [
        'Goa', 'Rajasthan', 'Himachal Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttarakhand',
        'West Bengal', 'Punjab', 'Tamil Nadu', 'Maharashtra', 'Rajasthan',
        'Ladakh', 'Andaman & Nicobar', 'Kerala', 'Delhi', 'Karnataka',
        'Himachal Pradesh', 'Tamil Nadu', 'Rajasthan', 'West Bengal', 'Karnataka',
        'Puducherry', 'Karnataka', 'Kerala', 'Uttarakhand', 'Assam',
        'Madhya Pradesh', 'Rajasthan', 'Karnataka', 'Tamil Nadu'
    ],
    'Type': [
        'Beach', 'Heritage', 'Hill Station', 'Religious', 'Heritage', 'Adventure',
        'Hill Station', 'Religious', 'Hill Station', 'Metro', 'Heritage',
        'Adventure', 'Beach', 'Hill Station', 'Metro', 'Heritage',
        'Hill Station', 'Hill Station', 'Wildlife', 'Metro', 'Heritage',
        'Beach', 'Hill Station', 'Backwaters', 'Hill Station', 'Wildlife',
        'Heritage', 'Religious', 'Beach', 'Heritage'
    ],
    'Best_Time_to_Visit': [
        'October-March', 'October-March', 'December-February', 'October-March', 'October-March', 'September-June',
        'March-June', 'October-March', 'September-May', 'October-March', 'September-March',
        'April-June', 'November-April', 'September-March', 'October-March', 'October-March',
        'March-June', 'October-June', 'October-June', 'October-March', 'September-March',
        'October-March', 'October-May', 'September-March', 'March-June', 'November-April',
        'September-March', 'November-March', 'October-March', 'October-March'
    ],
}

# Create preference categories as multi-label data
# Each destination can have multiple preferences
preferences = {
    'Goa': ['Beach', 'Nightlife', 'Relaxation', 'Culture', 'Food'],
    'Jaipur': ['Culture', 'History', 'Architecture', 'Shopping', 'Food'],
    'Manali': ['Nature', 'Adventure', 'Mountains', 'Relaxation', 'Romantic'],
    'Varanasi': ['Religious', 'Culture', 'History', 'Spiritual', 'Architecture'],
    'Agra': ['History', 'Architecture', 'Culture', 'Romantic', 'Photography'],
    'Rishikesh': ['Adventure', 'Spiritual', 'Nature', 'Yoga', 'Relaxation'],
    'Darjeeling': ['Nature', 'Mountains', 'Tea', 'Scenic', 'Relaxation'],
    'Amritsar': ['Religious', 'Culture', 'Food', 'History', 'Architecture'],
    'Kodaikanal': ['Nature', 'Mountains', 'Relaxation', 'Scenic', 'Romantic'],
    'Mumbai': ['Urban', 'Culture', 'Food', 'Shopping', 'Nightlife'],
    'Udaipur': ['Culture', 'Romantic', 'Architecture', 'Lakes', 'History'],
    'Leh': ['Adventure', 'Mountains', 'Nature', 'Photography', 'Culture'],
    'Andaman Islands': ['Beach', 'Nature', 'Water Sports', 'Relaxation', 'Photography'],
    'Munnar': ['Nature', 'Tea', 'Mountains', 'Scenic', 'Relaxation'],
    'Delhi': ['History', 'Culture', 'Food', 'Shopping', 'Urban'],
    'Hampi': ['History', 'Architecture', 'Culture', 'Photography', 'Nature'],
    'Shimla': ['Mountains', 'Colonial', 'Nature', 'Relaxation', 'Romantic'],
    'Ooty': ['Nature', 'Mountains', 'Scenic', 'Relaxation', 'Colonial'],
    'Ranthambore': ['Wildlife', 'Nature', 'Photography', 'Safari', 'Adventure'],
    'Kolkata': ['Culture', 'Food', 'History', 'Architecture', 'Literature'],
    'Mysore': ['History', 'Architecture', 'Culture', 'Food', 'Art'],
    'Pondicherry': ['Beach', 'Colonial', 'Culture', 'Food', 'Relaxation'],
    'Coorg': ['Nature', 'Coffee', 'Relaxation', 'Mountains', 'Scenic'],
    'Alleppey': ['Backwaters', 'Nature', 'Relaxation', 'Scenic', 'Culture'],
    'Nainital': ['Lakes', 'Mountains', 'Nature', 'Relaxation', 'Boating'],
    'Kaziranga': ['Wildlife', 'Nature', 'Safari', 'Photography', 'Adventure'],
    'Khajuraho': ['Architecture', 'History', 'Art', 'Culture', 'Photography'],
    'Pushkar': ['Religious', 'Culture', 'Desert', 'Spiritual', 'Photography'],
    'Gokarna': ['Beach', 'Relaxation', 'Spiritual', 'Nature', 'Offbeat'],
    'Mahabalipuram': ['Beach', 'History', 'Architecture', 'Culture', 'Relaxation']
}

# Demographic suitability
# Scale: 1-5, where 5 means most suitable
demographic_suitability = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Family_Friendly': [
        5, 5, 4, 3, 5, 3, 4, 5, 5, 4, 5, 3, 4, 5, 4, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 3, 4, 4, 3, 5
    ],
    'Solo_Travel': [
        4, 4, 4, 5, 4, 5, 5, 4, 3, 5, 4, 5, 3, 4, 5, 5, 4, 4, 3, 5, 4, 5, 5, 4, 4, 4, 4, 5, 5, 4
    ],
    'Couple_Friendly': [
        5, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 4, 4, 5, 5, 4, 4, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5
    ],
    'Senior_Friendly': [
        4, 4, 3, 3, 4, 2, 3, 4, 4, 3, 4, 2, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4, 3, 5, 4, 2, 3, 3, 3, 4
    ],
    'Budget_Traveler': [
        3, 4, 4, 5, 3, 5, 4, 5, 4, 3, 3, 3, 3, 4, 4, 5, 3, 4, 3, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4
    ],
    'Luxury_Traveler': [
        5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 5
    ]
}

# Popularity score (1-10)
popularity = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Popularity_Score': [
        9, 9, 8, 8, 10, 7, 7, 8, 6, 9, 8, 8, 7, 7, 9, 6, 8, 7, 7, 8, 7, 6, 6, 8, 7, 6, 6, 7, 6, 7
    ]
}

# Convert to dataframes
destinations_df = pd.DataFrame(destinations_data)
demo_df = pd.DataFrame(demographic_suitability)
popularity_df = pd.DataFrame(popularity)

# Convert preferences to a format suitable for the dataframe
preferences_list = []
for dest in destinations_data['Destination_Name']:
    preferences_list.append(', '.join(preferences[dest]))

destinations_df['Preferences'] = preferences_list

# Merge all dataframes
df = destinations_df.merge(demo_df, on='Destination_Name')
df = df.merge(popularity_df, on='Destination_Name')

# Calculate budget estimations (per day per person in INR)
# These are rough estimates for accommodation, food, and local travel
budget_range = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Budget_Min': [
        2000, 1500, 1200, 800, 1500, 800, 1200, 1000, 1200, 2000, 1800, 2000, 2500, 1500, 1800, 800, 1500, 1200, 2500, 1500, 1200, 1500, 1500, 1800, 1200, 2000, 1000, 800, 1000, 1200
    ],
    'Budget_Max': [
        20000, 15000, 12000, 8000, 15000, 10000, 10000, 10000, 12000, 25000, 20000, 15000, 18000, 12000, 20000, 5000, 15000, 12000, 20000, 18000, 12000, 15000, 15000, 20000, 12000, 12000, 8000, 8000, 8000, 10000
    ]
}

budget_df = pd.DataFrame(budget_range)
df = df.merge(budget_df, on='Destination_Name')

# Display the first few rows of the dataset
print(df.head())

# Save to CSV
df.to_csv('indian_destinations.csv', index=False)

print(f"Dataset created with {len(df)} destinations")