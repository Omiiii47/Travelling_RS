import pandas as pd
import numpy as np

# Create a comprehensive dataset of Indian travel destinations (over 100 destinations)
destinations_data = {
    'Destination_Name': [
        # Original 30 destinations
        'Goa', 'Jaipur', 'Manali', 'Varanasi', 'Agra', 'Rishikesh', 
        'Darjeeling', 'Amritsar', 'Kodaikanal', 'Mumbai', 'Udaipur', 
        'Leh', 'Andaman Islands', 'Munnar', 'Delhi', 'Hampi', 
        'Shimla', 'Ooty', 'Ranthambore', 'Kolkata', 'Mysore',
        'Pondicherry', 'Coorg', 'Alleppey', 'Nainital', 'Kaziranga',
        'Khajuraho', 'Pushkar', 'Gokarna', 'Mahabalipuram',
        
        # Additional 73 destinations to reach 103 total
        'Ajanta & Ellora Caves', 'Alibaug', 'Aurangabad', 'Badami', 'Bangalore', 
        'Bharatpur', 'Bhubaneswar', 'Bikaner', 'Bir Billing', 'Chandigarh', 
        'Chennai', 'Cherrapunji', 'Chikmagalur', 'Chitrakoot', 'Coonoor', 
        'Corbett National Park', 'Dalhousie', 'Daman & Diu', 'Dhanaulti', 'Dharamshala', 
        'Dudhsagar Falls', 'Dwarka', 'Gangtok', 'Gulmarg', 'Guruvayur', 
        'Gwalior', 'Haridwar', 'Hyderabad', 'Jaisalmer', 'Jibhi', 
        'Jodhpur', 'Kanchipuram', 'Kanha National Park', 'Kannur', 'Kanyakumari', 
        'Kasauli', 'Kausani', 'Kochi', 'Konark', 'Kovalam', 
        'Kukke Subramanya', 'Kullu', 'Kumarakom', 'Kutch', 'Lonavala', 
        'Lucknow', 'Madurai', 'Mahabaleshwar', 'Mathura', 'Matheran', 
        'McLeod Ganj', 'Mussoorie', 'Nagapattinam', 'Nashik', 'Panchgani', 
        'Patiala', 'Patnitop', 'Pelling', 'Puri', 'Rameshwaram', 
        'Sawai Madhopur', 'Shillong', 'Shirdi', 'Srinagar', 'Tawang', 
        'Thiruvananthapuram', 'Tirupati', 'Udagamandalam', 'Ujjain', 'Vaishno Devi', 
        'Varkala', 'Visakhapatnam', 'Vrindavan', 'Wayanad'
    ],
    'State': [
        # Original 30 states
        'Goa', 'Rajasthan', 'Himachal Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttarakhand',
        'West Bengal', 'Punjab', 'Tamil Nadu', 'Maharashtra', 'Rajasthan',
        'Ladakh', 'Andaman & Nicobar', 'Kerala', 'Delhi', 'Karnataka',
        'Himachal Pradesh', 'Tamil Nadu', 'Rajasthan', 'West Bengal', 'Karnataka',
        'Puducherry', 'Karnataka', 'Kerala', 'Uttarakhand', 'Assam',
        'Madhya Pradesh', 'Rajasthan', 'Karnataka', 'Tamil Nadu',
        
        # Additional 73 states
        'Maharashtra', 'Maharashtra', 'Maharashtra', 'Karnataka', 'Karnataka', 
        'Rajasthan', 'Odisha', 'Rajasthan', 'Himachal Pradesh', 'Chandigarh', 
        'Tamil Nadu', 'Meghalaya', 'Karnataka', 'Uttar Pradesh', 'Tamil Nadu', 
        'Uttarakhand', 'Himachal Pradesh', 'Daman & Diu', 'Uttarakhand', 'Himachal Pradesh', 
        'Goa', 'Gujarat', 'Sikkim', 'Jammu & Kashmir', 'Kerala', 
        'Madhya Pradesh', 'Uttarakhand', 'Telangana', 'Rajasthan', 'Himachal Pradesh', 
        'Rajasthan', 'Tamil Nadu', 'Madhya Pradesh', 'Kerala', 'Tamil Nadu', 
        'Himachal Pradesh', 'Uttarakhand', 'Kerala', 'Odisha', 'Kerala', 
        'Karnataka', 'Himachal Pradesh', 'Kerala', 'Gujarat', 'Maharashtra', 
        'Uttar Pradesh', 'Tamil Nadu', 'Maharashtra', 'Uttar Pradesh', 'Maharashtra', 
        'Himachal Pradesh', 'Uttarakhand', 'Tamil Nadu', 'Maharashtra', 'Maharashtra', 
        'Punjab', 'Jammu & Kashmir', 'Sikkim', 'Odisha', 'Tamil Nadu', 
        'Rajasthan', 'Meghalaya', 'Maharashtra', 'Jammu & Kashmir', 'Arunachal Pradesh', 
        'Kerala', 'Andhra Pradesh', 'Tamil Nadu', 'Madhya Pradesh', 'Jammu & Kashmir', 
        'Kerala', 'Andhra Pradesh', 'Uttar Pradesh', 'Kerala'
    ],
    'Type': [
        # Original 30 types
        'Beach', 'Heritage', 'Hill Station', 'Religious', 'Heritage', 'Adventure',
        'Hill Station', 'Religious', 'Hill Station', 'Metro', 'Heritage',
        'Adventure', 'Beach', 'Hill Station', 'Metro', 'Heritage',
        'Hill Station', 'Hill Station', 'Wildlife', 'Metro', 'Heritage',
        'Beach', 'Hill Station', 'Backwaters', 'Hill Station', 'Wildlife',
        'Heritage', 'Religious', 'Beach', 'Heritage',
        
        # Additional 73 types
        'Heritage', 'Beach', 'Heritage', 'Heritage', 'Metro', 
        'Wildlife', 'Heritage', 'Heritage', 'Adventure', 'Metro', 
        'Metro', 'Hill Station', 'Hill Station', 'Religious', 'Hill Station', 
        'Wildlife', 'Hill Station', 'Beach', 'Hill Station', 'Hill Station', 
        'Waterfall', 'Religious', 'Hill Station', 'Hill Station', 'Religious', 
        'Heritage', 'Religious', 'Metro', 'Desert', 'Hill Station', 
        'Heritage', 'Religious', 'Wildlife', 'Beach', 'Beach', 
        'Hill Station', 'Hill Station', 'Beach', 'Heritage', 'Beach', 
        'Religious', 'Hill Station', 'Backwaters', 'Desert', 'Hill Station', 
        'Heritage', 'Religious', 'Hill Station', 'Religious', 'Hill Station', 
        'Hill Station', 'Hill Station', 'Religious', 'Religious', 'Hill Station', 
        'Heritage', 'Hill Station', 'Hill Station', 'Religious', 'Religious', 
        'Wildlife', 'Hill Station', 'Religious', 'Hill Station', 'Hill Station', 
        'Beach', 'Religious', 'Hill Station', 'Religious', 'Religious', 
        'Beach', 'Beach', 'Religious', 'Hill Station'
    ],
    'Best_Time_to_Visit': [
        # Original 30 best times
        'October-March', 'October-March', 'December-February', 'October-March', 'October-March', 'September-June',
        'March-June', 'October-March', 'September-May', 'October-March', 'September-March',
        'April-June', 'November-April', 'September-March', 'October-March', 'October-March',
        'March-June', 'October-June', 'October-June', 'October-March', 'September-March',
        'October-March', 'October-May', 'September-March', 'March-June', 'November-April',
        'September-March', 'November-March', 'October-March', 'October-March',
        
        # Additional 73 best times
        'September-March', 'October-May', 'September-March', 'October-March', 'October-March', 
        'October-March', 'October-March', 'October-March', 'March-June', 'September-March', 
        'October-March', 'September-May', 'October-May', 'October-March', 'October-June', 
        'November-June', 'March-June', 'October-May', 'March-June', 'March-June', 
        'October-May', 'October-March', 'March-June', 'December-February', 'October-March', 
        'October-March', 'October-March', 'October-March', 'October-March', 'March-June', 
        'October-March', 'October-March', 'October-June', 'October-March', 'October-March', 
        'March-June', 'March-June', 'October-March', 'October-March', 'October-March', 
        'October-March', 'March-June', 'September-March', 'October-March', 'October-March', 
        'October-March', 'October-March', 'October-March', 'October-March', 'October-March', 
        'March-June', 'March-June', 'October-March', 'October-March', 'October-March', 
        'October-March', 'March-June', 'March-June', 'October-March', 'October-March', 
        'October-June', 'March-June', 'October-March', 'April-October', 'March-October', 
        'October-March', 'October-March', 'October-June', 'October-March', 'March-June', 
        'September-March', 'October-March', 'October-March', 'October-May'
    ],
}

# Create preference categories as multi-label data
# Each destination can have multiple preferences
preferences = {
    # Original 30 destinations
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
    'Mahabalipuram': ['Beach', 'History', 'Architecture', 'Culture', 'Relaxation'],
    
    # Additional 73 destinations
    'Ajanta & Ellora Caves': ['History', 'Architecture', 'Culture', 'Photography', 'Art'],
    'Alibaug': ['Beach', 'Relaxation', 'Weekend Getaway', 'Water Sports', 'Nature'],
    'Aurangabad': ['History', 'Architecture', 'Culture', 'Food', 'Shopping'],
    'Badami': ['History', 'Architecture', 'Culture', 'Photography', 'Nature'],
    'Bangalore': ['Urban', 'Technology', 'Food', 'Shopping', 'Nightlife'],
    'Bharatpur': ['Wildlife', 'Nature', 'Photography', 'Bird Watching', 'History'],
    'Bhubaneswar': ['History', 'Architecture', 'Culture', 'Religious', 'Food'],
    'Bikaner': ['Heritage', 'Desert', 'Food', 'Architecture', 'Culture'],
    'Bir Billing': ['Adventure', 'Paragliding', 'Nature', 'Relaxation', 'Mountains'],
    'Chandigarh': ['Urban', 'Architecture', 'Gardens', 'Shopping', 'Food'],
    'Chennai': ['Culture', 'Food', 'Beach', 'Architecture', 'Shopping'],
    'Cherrapunji': ['Nature', 'Waterfalls', 'Scenic', 'Adventure', 'Monsoon'],
    'Chikmagalur': ['Nature', 'Coffee', 'Mountains', 'Relaxation', 'Hiking'],
    'Chitrakoot': ['Religious', 'Nature', 'Spiritual', 'History', 'Scenic'],
    'Coonoor': ['Nature', 'Tea', 'Mountains', 'Relaxation', 'Scenic'],
    'Corbett National Park': ['Wildlife', 'Nature', 'Adventure', 'Safari', 'Photography'],
    'Dalhousie': ['Nature', 'Mountains', 'Colonial', 'Relaxation', 'Scenic'],
    'Daman & Diu': ['Beach', 'History', 'Portuguese', 'Relaxation', 'Seafood'],
    'Dhanaulti': ['Nature', 'Mountains', 'Tranquility', 'Offbeat', 'Relaxation'],
    'Dharamshala': ['Mountains', 'Buddhism', 'Nature', 'Culture', 'Spirituality'],
    'Dudhsagar Falls': ['Nature', 'Waterfalls', 'Adventure', 'Trekking', 'Photography'],
    'Dwarka': ['Religious', 'History', 'Spiritual', 'Culture', 'Beach'],
    'Gangtok': ['Mountains', 'Nature', 'Culture', 'Adventure', 'Buddhism'],
    'Gulmarg': ['Mountains', 'Snow', 'Skiing', 'Nature', 'Adventure'],
    'Guruvayur': ['Religious', 'Spiritual', 'Culture', 'Architecture', 'History'],
    'Gwalior': ['History', 'Architecture', 'Culture', 'Music', 'Heritage'],
    'Haridwar': ['Religious', 'Spiritual', 'Culture', 'Yoga', 'Nature'],
    'Hyderabad': ['Culture', 'Food', 'History', 'Architecture', 'Shopping'],
    'Jaisalmer': ['Desert', 'Culture', 'Architecture', 'History', 'Adventure'],
    'Jibhi': ['Nature', 'Offbeat', 'Mountains', 'Tranquility', 'Hiking'],
    'Jodhpur': ['History', 'Architecture', 'Culture', 'Shopping', 'Food'],
    'Kanchipuram': ['Religious', 'Temples', 'Culture', 'Silk', 'History'],
    'Kanha National Park': ['Wildlife', 'Nature', 'Safari', 'Photography', 'Adventure'],
    'Kannur': ['Beach', 'Culture', 'Theyyam', 'Food', 'Nature'],
    'Kanyakumari': ['Beach', 'Pilgrimage', 'Sunrise', 'Culture', 'History'],
    'Kasauli': ['Nature', 'Mountains', 'Relaxation', 'Colonial', 'Scenic'],
    'Kausani': ['Nature', 'Mountains', 'Relaxation', 'Scenic', 'Tranquility'],
    'Kochi': ['Culture', 'History', 'Food', 'Beach', 'Art'],
    'Konark': ['Architecture', 'History', 'Beach', 'Culture', 'Art'],
    'Kovalam': ['Beach', 'Ayurveda', 'Relaxation', 'Water Sports', 'Seafood'],
    'Kukke Subramanya': ['Religious', 'Spiritual', 'Nature', 'Culture', 'Pilgrimage'],
    'Kullu': ['Nature', 'Adventure', 'Mountains', 'Culture', 'Shopping'],
    'Kumarakom': ['Backwaters', 'Nature', 'Relaxation', 'Birds', 'Ayurveda'],
    'Kutch': ['Desert', 'Culture', 'Handicrafts', 'Wildlife', 'Photography'],
    'Lonavala': ['Mountains', 'Monsoon', 'Relaxation', 'Nature', 'Weekend Getaway'],
    'Lucknow': ['Culture', 'Food', 'History', 'Architecture', 'Shopping'],
    'Madurai': ['Religious', 'Culture', 'History', 'Architecture', 'Food'],
    'Mahabaleshwar': ['Nature', 'Mountains', 'Strawberries', 'Relaxation', 'Scenic'],
    'Mathura': ['Religious', 'History', 'Culture', 'Spiritual', 'Food'],
    'Matheran': ['Nature', 'Mountains', 'No Vehicles', 'Relaxation', 'Scenic'],
    'McLeod Ganj': ['Buddhism', 'Mountains', 'Culture', 'Relaxation', 'Adventure'],
    'Mussoorie': ['Mountains', 'Nature', 'Colonial', 'Relaxation', 'Scenic'],
    'Nagapattinam': ['Religious', 'Beach', 'Pilgrimage', 'History', 'Culture'],
    'Nashik': ['Religious', 'Vineyards', 'Culture', 'Nature', 'Food'],
    'Panchgani': ['Nature', 'Mountains', 'Relaxation', 'Scenic', 'Strawberries'],
    'Patiala': ['Culture', 'History', 'Food', 'Shopping', 'Architecture'],
    'Patnitop': ['Mountains', 'Snow', 'Nature', 'Adventure', 'Relaxation'],
    'Pelling': ['Mountains', 'Nature', 'Buddhism', 'Scenic', 'Relaxation'],
    'Puri': ['Religious', 'Beach', 'Culture', 'Food', 'Festivals'],
    'Rameshwaram': ['Religious', 'Beach', 'Pilgrimage', 'History', 'Culture'],
    'Sawai Madhopur': ['Wildlife', 'Safari', 'Nature', 'Photography', 'Adventure'],
    'Shillong': ['Mountains', 'Nature', 'Music', 'Culture', 'Waterfalls'],
    'Shirdi': ['Religious', 'Spiritual', 'Pilgrimage', 'Culture', 'Peace'],
    'Srinagar': ['Lakes', 'Mountains', 'Nature', 'Houseboats', 'Gardens'],
    'Tawang': ['Buddhism', 'Mountains', 'Nature', 'Culture', 'Scenic'],
    'Thiruvananthapuram': ['Beach', 'Culture', 'Food', 'Architecture', 'Art'],
    'Tirupati': ['Religious', 'Spiritual', 'Pilgrimage', 'Architecture', 'Culture'],
    'Udagamandalam': ['Nature', 'Mountains', 'Tea', 'Colonial', 'Relaxation'],
    'Ujjain': ['Religious', 'Spiritual', 'History', 'Culture', 'Architecture'],
    'Vaishno Devi': ['Religious', 'Pilgrimage', 'Spiritual', 'Mountains', 'Adventure'],
    'Varkala': ['Beach', 'Cliffs', 'Relaxation', 'Yoga', 'Ayurveda'],
    'Visakhapatnam': ['Beach', 'Port', 'Nature', 'Culture', 'Food'],
    'Vrindavan': ['Religious', 'Spiritual', 'Culture', 'History', 'Music'],
    'Wayanad': ['Nature', 'Wildlife', 'Mountains', 'Adventure', 'Relaxation']
}

# Demographic suitability
# Scale: 1-5, where 5 means most suitable
demographic_suitability = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Family_Friendly': [
        # Original 30 ratings
        5, 5, 4, 3, 5, 3, 4, 5, 5, 4, 5, 3, 4, 5, 4, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 3, 4, 4, 3, 5,
        
        # Additional 73 ratings
        4, 5, 4, 4, 5, 5, 4, 4, 3, 5, 5, 3, 4, 4, 5, 4, 4, 5, 4, 4, 
        3, 5, 4, 3, 5, 5, 5, 5, 4, 3, 5, 5, 4, 4, 5, 
        5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 
        3, 4, 5, 5, 5, 5, 3, 3, 5, 5, 4, 4, 5, 3, 3, 
        5, 5, 5, 5, 4, 4, 5, 5, 4
    ],
    'Solo_Travel': [
        # Original 30 ratings
        4, 4, 4, 5, 4, 5, 5, 4, 3, 5, 4, 5, 3, 4, 5, 5, 4, 4, 3, 5, 4, 5, 5, 4, 4, 4, 4, 5, 5, 4,
        
        # Additional 73 ratings
        4, 4, 4, 5, 5, 3, 4, 4, 5, 4, 4, 5, 5, 3, 4, 3, 4, 3, 5, 5, 
        4, 3, 5, 5, 3, 4, 4, 5, 4, 5, 4, 3, 3, 5, 4, 
        5, 5, 5, 4, 4, 3, 4, 3, 4, 4, 4, 3, 5, 3, 5, 
        5, 5, 3, 4, 5, 4, 5, 5, 3, 3, 3, 5, 3, 5, 5, 
        4, 3, 4, 3, 3, 5, 4, 3, 5
    ],
    
    'Couple_Friendly': [
        # Original 30 ratings
        5, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 4, 4, 5, 5, 4, 4, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5,
        
        # Additional 73 ratings
        4, 5, 4, 4, 5, 3, 4, 5, 4, 5, 5, 4, 5, 3, 5, 3, 5, 5, 5, 4, 
        5, 4, 5, 5, 3, 4, 4, 5, 5, 5, 5, 3, 3, 5, 5, 
        5, 5, 5, 4, 5, 3, 5, 5, 4, 5, 4, 4, 5, 4, 5, 
        5, 5, 3, 4, 5, 4, 4, 5, 3, 4, 4, 5, 3, 5, 4, 
        5, 3, 5, 3, 3, 5, 5, 3, 5
    ],
    'Senior_Friendly': [
        # Original 30 ratings
        4, 4, 3, 3, 4, 2, 3, 4, 4, 3, 4, 2, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4, 3, 5, 4, 2, 3, 3, 3, 4,
        
        # Additional 73 ratings
        3, 4, 4, 3, 4, 4, 4, 3, 2, 4, 4, 2, 3, 3, 4, 3, 3, 4, 3, 3, 
        2, 4, 3, 2, 4, 4, 4, 4, 3, 2, 3, 4, 3, 3, 4, 
        4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 4, 3, 4, 4, 4, 
        2, 3, 3, 4, 4, 4, 2, 2, 4, 3, 3, 3, 4, 2, 2, 
        4, 4, 4, 4, 3, 3, 4, 3, 3
    ],
    'Budget_Traveler': [
        # Original 30 ratings
        3, 4, 4, 5, 3, 5, 4, 5, 4, 3, 3, 3, 3, 4, 4, 5, 3, 4, 3, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4,
        
        # Additional 73 ratings
        4, 4, 4, 5, 3, 4, 4, 4, 5, 4, 3, 5, 4, 5, 4, 3, 4, 4, 5, 4, 
        4, 5, 4, 4, 5, 4, 5, 3, 4, 5, 4, 5, 3, 5, 4, 
        4, 5, 3, 5, 4, 5, 4, 3, 5, 4, 3, 4, 4, 5, 5, 
        4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3, 4, 5, 5, 5, 
        4, 5, 3, 5, 5, 5, 3, 5, 4
    ],
    'Luxury_Traveler': [
        # Original 30 ratings
        5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 5,
        
        # Additional 73 ratings
        4, 5, 5, 3, 5, 4, 4, 5, 3, 5, 5, 3, 5, 3, 5, 5, 5, 4, 3, 5, 
        3, 4, 5, 5, 4, 5, 4, 5, 5, 3, 5, 4, 5, 4, 4, 
        5, 4, 5, 4, 5, 3, 5, 5, 4, 5, 5, 5, 5, 4, 4, 
        5, 5, 4, 4, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 4, 
        5, 4, 5, 4, 3, 4, 5, 3, 5
    ]
}

# Popularity score (1-10)
popularity = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Popularity_Score': [
        # Original 30 scores
        9, 9, 8, 8, 10, 7, 7, 8, 6, 9, 8, 8, 7, 7, 9, 6, 8, 7, 7, 8, 7, 6, 6, 8, 7, 6, 6, 7, 6, 7,
        
        # Additional 73 scores
        7, 6, 7, 5, 9, 6, 7, 7, 6, 8, 8, 6, 6, 5, 6, 7, 7, 5, 5, 8, 
        6, 6, 8, 8, 6, 7, 8, 9, 8, 5, 8, 6, 7, 5, 7, 
        6, 5, 8, 6, 7, 5, 7, 7, 7, 7, 7, 7, 7, 7, 6, 
        7, 7, 5, 7, 6, 6, 5, 7, 7, 7, 6, 7, 7, 8, 6, 
        7, 7, 6, 7, 8, 6, 7, 6, 7
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
df = destinations_df.merge(demo_df, on='Destination_Name')
df = df.merge(popularity_df, on='Destination_Name')

# Calculate budget estimations (per day per person in INR)
# These are rough estimates for accommodation, food, and local travel
budget_range = {
    'Destination_Name': destinations_data['Destination_Name'],
    'Budget_Min': [
        # Original 30 min budgets
        2000, 1500, 1200, 800, 1500, 800, 1200, 1000, 1200, 2000, 1800, 2000, 2500, 1500, 1800, 800, 1500, 1200, 2500, 1500, 1200, 1500, 1500, 1800, 1200, 2000, 1000, 800, 1000, 1200,
        
        # Additional 73 min budgets
        1000, 1500, 1200, 800, 2000, 1500, 1200, 1200, 1000, 1800, 2000, 1000, 1200, 800, 1200, 2000, 1200, 1500, 800, 1200,
        1200, 1000, 1500, 2000, 1000, 1200, 1000, 1800, 1500, 800, 1500, 1000, 2000, 1200, 1200,
        1000, 800, 1800, 1000, 1500, 800, 1200, 1800, 1200, 1500, 1500, 1200, 1500, 1000, 1500,
        1000, 1200, 1000, 1200, 1500, 1200, 1500, 1200, 1000, 1200, 2000, 1200, 1000, 1800, 1000,
        1500, 1200, 1500, 1000, 1200, 1500, 1500, 800, 1200
    ],
    'Budget_Max': [
        # Original 30 max budgets
        20000, 15000, 12000, 8000, 15000, 10000, 10000, 10000, 12000, 25000, 20000, 15000, 18000, 12000, 20000, 5000, 15000, 12000, 20000, 18000, 12000, 15000, 15000, 20000, 12000, 12000, 8000, 8000, 8000, 10000,
        
        # Additional 73 max budgets
        8000, 15000, 12000, 6000, 25000, 10000, 10000, 12000, 10000, 20000, 20000, 8000, 12000, 6000, 12000, 15000, 12000, 12000, 6000, 15000,
        10000, 8000, 15000, 18000, 8000, 10000, 8000, 20000, 15000, 8000, 15000, 8000, 15000, 10000, 10000,
        10000, 6000, 18000, 8000, 15000, 6000, 12000, 18000, 10000, 15000, 15000, 10000, 15000, 8000, 15000,
        8000, 12000, 8000, 10000, 15000, 10000, 12000, 12000, 8000, 10000, 15000, 12000, 8000, 15000, 10000,
        12000, 10000, 12000, 8000, 10000, 15000, 15000, 6000, 12000
    ]
}

budget_df = pd.DataFrame(budget_range)
df = df.merge(budget_df, on='Destination_Name')

# Display the first few rows of the dataset
print(df.head())

# Save to CSV
df.to_csv('expanded_indian_destinations.csv', index=False)

print(f"Expanded dataset created with {len(df)} destinations")