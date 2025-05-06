import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

class IndianTravelRecommender:
    """
    Hybrid travel recommendation system for Indian destinations
    Combines content-based, popularity-based, and demographic filtering
    """
    def __init__(self, data_path='expanded_indian_destinations.csv'):
        """Initialize with the dataset"""
        self.df = pd.read_csv(data_path)
        self.prepare_data()
        
    def prepare_data(self):
        """Prepare and preprocess the data"""
        # Extract unique preference keywords
        all_preferences = []
        for prefs in self.df['Preferences'].str.split(', '):
            all_preferences.extend(prefs)
        self.unique_preferences = list(set(all_preferences))
        
        # Create one-hot encoding for preferences
        for pref in self.unique_preferences:
            self.df[f'pref_{pref}'] = self.df['Preferences'].apply(lambda x: 1 if pref in x else 0)
        
        # Create one-hot encoding for types
        self.df = pd.concat([self.df, pd.get_dummies(self.df['Type'], prefix='type')], axis=1)
        
        # Normalize popularity score
        scaler = MinMaxScaler()
        self.df['Normalized_Popularity'] = scaler.fit_transform(self.df[['Popularity_Score']])
        
    def get_recommendation_by_preferences(self, preferences, top_n=5):
        """
        Content-based filtering based on user preferences
        
        Args:
            preferences: List of preference keywords (e.g., ['Beach', 'Adventure'])
            top_n: Number of recommendations to return
            
        Returns:
            DataFrame of recommended destinations
        """
        # Create user preference vector
        user_preferences = np.zeros(len(self.unique_preferences))
        for i, pref in enumerate(self.unique_preferences):
            if pref in preferences:
                user_preferences[i] = 1
                
        # Calculate similarity between user preferences and destinations
        destination_preferences = self.df[[f'pref_{pref}' for pref in self.unique_preferences]].values
        similarities = []
        
        for dest_prefs in destination_preferences:
            # Calculate cosine similarity
            if np.sum(dest_prefs) > 0 and np.sum(user_preferences) > 0:
                sim = np.dot(dest_prefs, user_preferences) / (np.linalg.norm(dest_prefs) * np.linalg.norm(user_preferences))
            else:
                sim = 0
            similarities.append(sim)
            
        self.df['Preference_Similarity'] = similarities
        
        # Return top results
        result = self.df.sort_values('Preference_Similarity', ascending=False).head(top_n)
        return result[['Destination_Name', 'State', 'Type', 'Best_Time_to_Visit', 'Preferences', 
                     'Popularity_Score', 'Budget_Min', 'Budget_Max']]
    
    def get_recommendation_by_demographics(self, group_type, num_adults=1, num_children=0, top_n=5):
        """
        Demographic-based filtering based on travel group
        
        Args:
            group_type: Type of travel group ('Family', 'Solo', 'Couple', 'Senior')
            num_adults: Number of adults in the group
            num_children: Number of children in the group
            top_n: Number of recommendations to return
            
        Returns:
            DataFrame of recommended destinations
        """
        if group_type == 'Family':
            # For families, prioritize family-friendly places
            self.df['Demo_Score'] = self.df['Family_Friendly']
        elif group_type == 'Solo':
            # For solo travelers
            self.df['Demo_Score'] = self.df['Solo_Travel']
        elif group_type == 'Couple':
            # For couples
            self.df['Demo_Score'] = self.df['Couple_Friendly']
        elif group_type == 'Senior':
            # For senior travelers
            self.df['Demo_Score'] = self.df['Senior_Friendly']
        else:
            # Default scoring
            self.df['Demo_Score'] = (self.df['Family_Friendly'] + self.df['Solo_Travel'] + 
                                  self.df['Couple_Friendly'] + self.df['Senior_Friendly']) / 4
            
        # Adjust for group size
        total_people = num_adults + num_children
        if total_people > 4:
            # Larger groups might prefer certain destinations
            # Boost family-friendly places for larger groups
            self.df['Demo_Score'] = self.df['Demo_Score'] * (self.df['Family_Friendly'] / 3)
            
        # Return top results
        result = self.df.sort_values('Demo_Score', ascending=False).head(top_n)
        return result[['Destination_Name', 'State', 'Type', 'Best_Time_to_Visit', 'Preferences', 
                     'Demo_Score', 'Popularity_Score', 'Budget_Min', 'Budget_Max']]
    
    def get_recommendation_by_budget(self, min_budget=0, max_budget=float('inf'), top_n=5):
        """
        Budget-based filtering
        
        Args:
            min_budget: Minimum budget per person per day (INR)
            max_budget: Maximum budget per person per day (INR)
            top_n: Number of recommendations to return
            
        Returns:
            DataFrame of recommended destinations within budget range
        """
        # Filter destinations within budget range
        budget_filter = (self.df['Budget_Min'] >= min_budget) & (self.df['Budget_Max'] <= max_budget)
        
        if budget_filter.sum() == 0:
            # If no exact matches, find closest matches
            self.df['Budget_Fit'] = 1 / (1 + abs(self.df['Budget_Min'] - min_budget) + abs(self.df['Budget_Max'] - max_budget))
            result = self.df.sort_values('Budget_Fit', ascending=False).head(top_n)
        else:
            # Sort by popularity within budget constraints
            result = self.df[budget_filter].sort_values('Popularity_Score', ascending=False).head(top_n)
            
        return result[['Destination_Name', 'State', 'Type', 'Best_Time_to_Visit', 
                       'Preferences', 'Budget_Min', 'Budget_Max', 'Popularity_Score']]
    
    def get_hybrid_recommendations(self, preferences, group_type='Family', num_adults=1, 
                                  num_children=0, min_budget=0, max_budget=float('inf'), 
                                  current_month=None, top_n=5):
        """
        Hybrid recommendation combining content, demographic, and popularity-based filtering
        
        Args:
            preferences: List of preference keywords
            group_type: Type of travel group
            num_adults: Number of adults
            num_children: Number of children
            min_budget: Minimum budget per person per day
            max_budget: Maximum budget per person per day
            current_month: Current month to consider seasonality (optional)
            top_n: Number of recommendations to return
            
        Returns:
            DataFrame of recommended destinations
        """
        # Calculate preference similarity
        user_preferences = np.zeros(len(self.unique_preferences))
        for i, pref in enumerate(self.unique_preferences):
            if pref in preferences:
                user_preferences[i] = 1
                
        destination_preferences = self.df[[f'pref_{pref}' for pref in self.unique_preferences]].values
        similarities = []
        
        for dest_prefs in destination_preferences:
            if np.sum(dest_prefs) > 0 and np.sum(user_preferences) > 0:
                sim = np.dot(dest_prefs, user_preferences) / (np.linalg.norm(dest_prefs) * np.linalg.norm(user_preferences))
            else:
                sim = 0
            similarities.append(sim)
            
        self.df['Preference_Similarity'] = similarities
        
        # Calculate demographic score
        if group_type == 'Family':
            self.df['Demo_Score'] = self.df['Family_Friendly']
        elif group_type == 'Solo':
            self.df['Demo_Score'] = self.df['Solo_Travel']
        elif group_type == 'Couple':
            self.df['Demo_Score'] = self.df['Couple_Friendly']
        elif group_type == 'Senior':
            self.df['Demo_Score'] = self.df['Senior_Friendly']
        else:
            self.df['Demo_Score'] = (self.df['Family_Friendly'] + self.df['Solo_Travel'] + 
                                  self.df['Couple_Friendly'] + self.df['Senior_Friendly']) / 4
        
        # Adjust for group size
        total_people = num_adults + num_children
        if total_people > 4:
            self.df['Demo_Score'] = self.df['Demo_Score'] * (self.df['Family_Friendly'] / 3)
        
        # Calculate budget fit
        budget_filter = (self.df['Budget_Min'] >= min_budget) & (self.df['Budget_Max'] <= max_budget)
        if budget_filter.sum() == 0:
            self.df['Budget_Fit'] = 1 / (1 + abs(self.df['Budget_Min'] - min_budget) + abs(self.df['Budget_Max'] - max_budget))
        else:
            self.df['Budget_Fit'] = budget_filter.astype(float)
        
        # Consider seasonality if month is provided
        if current_month:
            months_map = {
                'January': ['December-February', 'October-March', 'September-March', 'November-March', 'November-April'],
                'February': ['December-February', 'October-March', 'September-March', 'November-March', 'November-April'],
                'March': ['October-March', 'March-June', 'September-March', 'November-March', 'September-May', 'September-June', 'November-April'],
                'April': ['March-June', 'April-June', 'September-May', 'November-April', 'September-June'],
                'May': ['March-June', 'April-June', 'September-May', 'September-June'],
                'June': ['March-June', 'April-June', 'September-June', 'October-June'],
                'July': [],  # Monsoon in most parts
                'August': [],  # Monsoon in most parts
                'September': ['September-March', 'September-May', 'September-June', 'October-June'],
                'October': ['October-March', 'September-March', 'October-June', 'October-May'],
                'November': ['October-March', 'September-March', 'November-March', 'November-April', 'October-June', 'October-May'],
                'December': ['December-February', 'October-March', 'September-March', 'November-March', 'November-April']
            }
            
            if current_month in months_map:
                self.df['Season_Match'] = self.df['Best_Time_to_Visit'].apply(lambda x: 1.0 if x in months_map[current_month] else 0.3)
            else:
                self.df['Season_Match'] = 1.0
        else:
            self.df['Season_Match'] = 1.0
            
        # Calculate final score (weighted average)
        self.df['Final_Score'] = (
            0.35 * self.df['Preference_Similarity'] + 
            0.25 * (self.df['Demo_Score'] / 5) +  # Normalize to 0-1
            0.20 * self.df['Normalized_Popularity'] +
            0.10 * self.df['Budget_Fit'] +
            0.10 * self.df['Season_Match']
        )
        
        # Add group size adjustment
        total_travelers = num_adults + num_children
        
        # Adjust scores based on group size
        # if total_travelers > 6:
        #     # Penalize destinations not suitable for large groups
        #     self.df['Final_Score'] = self.df.apply(
        #         lambda x: x['Final_Score'] * 0.7 if x['Type'] in ['Wildlife', 'Adventure'] else x['Final_Score'],
        #         axis=1
        #     )
        
        if num_children > 3:
            # Boost family-friendly destinations
            self.df['Final_Score'] = self.df.apply(
                lambda x: x['Final_Score'] * 1.3 if x['Type'] in ['Beach', 'Theme Park', 'Wildlife'] else x['Final_Score'],
                axis=1
            )
            # Penalize adventure destinations with young children
            self.df['Final_Score'] = self.df.apply(
                lambda x: x['Final_Score'] * 0.6 if x['Type'] in ['Adventure', 'Trekking' , 'Mountains'] and num_children < 12 else x['Final_Score'],
                axis=1
            )
        
        # Adjust budget per total travelers
        per_person_min = min_budget * (num_adults + (num_children * 0.5))  # Children counted as 0.5 for budget
        per_person_max = max_budget * (num_adults + (num_children * 0.5))
        
        # Filter based on adjusted budget
        recommendations = self.df[
            (self.df['Budget_Min'] <= per_person_max) & 
            (self.df['Budget_Max'] >= per_person_min)
        ]
        
        # Sort by final score and return top_n recommendations
        recommendations = recommendations.sort_values('Final_Score', ascending=False).head(top_n)
        
        return recommendations
    
    def explain_recommendation(self, destination_name):
        """
        Explain why a particular destination is recommended
        
        Args:
            destination_name: Name of the destination
            
        Returns:
            String explanation
        """
        if destination_name not in self.df['Destination_Name'].values:
            return f"Destination '{destination_name}' not found in the database."
            
        dest_data = self.df[self.df['Destination_Name'] == destination_name].iloc[0]
        
        explanation = f"About {destination_name}:\n"
        explanation += f"- Located in: {dest_data['State']}\n"
        explanation += f"- Type: {dest_data['Type']}\n"
        explanation += f"- Best time to visit: {dest_data['Best_Time_to_Visit']}\n"
        explanation += f"- Popularity: {dest_data['Popularity_Score']}/10\n"
        explanation += f"- Budget range: ₹{dest_data['Budget_Min']}-{dest_data['Budget_Max']} per day\n"
        explanation += f"- Experience offerings: {dest_data['Preferences']}\n"
        
        explanation += "\nDemographic suitability (rated 1-5):\n"
        explanation += f"- Family-friendly: {dest_data['Family_Friendly']}/5\n"
        explanation += f"- Solo travel: {dest_data['Solo_Travel']}/5\n"
        explanation += f"- Couple-friendly: {dest_data['Couple_Friendly']}/5\n"
        explanation += f"- Senior-friendly: {dest_data['Senior_Friendly']}/5\n"
        
        return explanation


# Example of how to use the recommender
if __name__ == "__main__":
    # Initialize the recommender
    recommender = IndianTravelRecommender()
    
    # Example 1: Get recommendations based on preferences
    print("\n=== Recommendations based on preferences ===")
    pref_recs = recommender.get_recommendation_by_preferences(['Beach', 'Relaxation'])
    print(pref_recs)
    
    # Example 2: Get recommendations based on demographics
    print("\n=== Recommendations for a family ===")
    demo_recs = recommender.get_recommendation_by_demographics('Family', num_adults=2, num_children=2)
    print(demo_recs)
    
    # Example 3: Get recommendations based on budget
    print("\n=== Recommendations within budget range ===")
    budget_recs = recommender.get_recommendation_by_budget(min_budget=1000, max_budget=5000)
    print(budget_recs)
    
    # Example 4: Get hybrid recommendations
    print("\n=== Hybrid recommendations ===")
    hybrid_recs = recommender.get_hybrid_recommendations(
        preferences=['Nature', 'Mountains', 'Adventure'],
        group_type='Family',
        num_adults=2,
        num_children=1,
        min_budget=1000,
        max_budget=10000,
        current_month='October',
        top_n=5
    )
    print(hybrid_recs)
    
    # Example 5: Explain a recommendation
    print("\n=== Explanation for Manali ===")
    explanation = recommender.explain_recommendation('Manali')
    print(explanation)