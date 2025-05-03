import pandas as pd
from recommendation_system import IndianTravelRecommender
import time

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(f" {text} ".center(80, "="))
    print("=" * 80)

def print_subheader(text):
    """Print a formatted subheader"""
    print("\n" + "-" * 60)
    print(f" {text} ".center(60, "-"))
    print("-" * 60)

def print_recommendation(rec, rank=None):
    """Print a formatted recommendation"""
    prefix = f"[{rank}] " if rank is not None else ""
    print(f"\n{prefix}✨ {rec['Destination_Name']} ({rec['State']})")
    print(f"   Type: {rec['Type']}")
    print(f"   Best Time: {rec['Best_Time_to_Visit']}")
    if 'Budget_Min' in rec and 'Budget_Max' in rec:
        print(f"   Budget: ₹{rec['Budget_Min']} - ₹{rec['Budget_Max']} per day")
    print(f"   Popularity: {rec['Popularity_Score']}/10")
    if 'Preferences' in rec:
        print(f"   Experience: {rec['Preferences']}")
    if 'Final_Score' in rec:
        match_percentage = int(rec['Final_Score'] * 100)
        print(f"   Match Score: {match_percentage}%")

def main():
    """Main demonstration function"""
    print_header("INDIAN TRAVEL RECOMMENDATION SYSTEM DEMO")
    print("\nInitializing the recommendation system...")
    
    try:
        recommender = IndianTravelRecommender()
        print("✅ Recommendation system initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing the recommender: {e}")
        return
    
    # Demo 1: Preference-based recommendations
    print_subheader("DEMO 1: PREFERENCE-BASED RECOMMENDATIONS")
    preferences = ['Beach', 'Relaxation']
    print(f"Preferences: {', '.join(preferences)}")
    
    print("\nGenerating recommendations...")
    time.sleep(1)  # Simulate processing time
    
    pref_recs = recommender.get_recommendation_by_preferences(preferences)
    
    print(f"\nTop 5 destinations for {', '.join(preferences)}:")
    for i, (_, rec) in enumerate(pref_recs.iterrows()):
        print_recommendation(rec, i+1)
    
    # Demo 2: Demographic-based recommendations
    print_subheader("DEMO 2: DEMOGRAPHIC-BASED RECOMMENDATIONS")
    group_type = "Family"
    num_adults = 2
    num_children = 2
    
    print(f"Group Type: {group_type}")
    print(f"Number of Adults: {num_adults}")
    print(f"Number of Children: {num_children}")
    
    print("\nGenerating recommendations...")
    time.sleep(1)  # Simulate processing time
    
    demo_recs = recommender.get_recommendation_by_demographics(group_type, num_adults, num_children)
    
    print(f"\nTop 5 destinations for {group_type} with {num_adults} adults and {num_children} children:")
    for i, (_, rec) in enumerate(demo_recs.iterrows()):
        print_recommendation(rec, i+1)
    
    # Demo 3: Budget-based recommendations
    print_subheader("DEMO 3: BUDGET-BASED RECOMMENDATIONS")
    min_budget = 1000
    max_budget = 5000
    
    print(f"Budget Range: ₹{min_budget} - ₹{max_budget} per person per day")
    
    print("\nGenerating recommendations...")
    time.sleep(1)  # Simulate processing time
    
    budget_recs = recommender.get_recommendation_by_budget(min_budget, max_budget)
    
    print(f"\nTop 5 destinations within budget range ₹{min_budget} - ₹{max_budget}:")
    for i, (_, rec) in enumerate(budget_recs.iterrows()):
        print_recommendation(rec, i+1)
    
    # Demo 4: Hybrid recommendations
    print_subheader("DEMO 4: HYBRID RECOMMENDATIONS")
    preferences = ['Nature', 'Mountains', 'Adventure']
    group_type = 'Family'
    num_adults = 2
    num_children = 1
    min_budget = 1000
    max_budget = 10000
    current_month = 'October'
    
    print(f"Preferences: {', '.join(preferences)}")
    print(f"Group Type: {group_type}")
    print(f"Number of Adults: {num_adults}")
    print(f"Number of Children: {num_children}")
    print(f"Budget Range: ₹{min_budget} - ₹{max_budget} per person per day")
    print(f"Travel Month: {current_month}")
    
    print("\nGenerating hybrid recommendations...")
    time.sleep(1.5)  # Simulate processing time
    
    hybrid_recs = recommender.get_hybrid_recommendations(
        preferences=preferences,
        group_type=group_type,
        num_adults=num_adults,
        num_children=num_children,
        min_budget=min_budget,
        max_budget=max_budget,
        current_month=current_month
    )
    
    print(f"\nTop 5 personalized recommendations:")
    for i, (_, rec) in enumerate(hybrid_recs.iterrows()):
        print_recommendation(rec, i+1)
    
    # Demo 5: Detailed explanation
    print_subheader("DEMO 5: DETAILED EXPLANATION")
    destination = hybrid_recs.iloc[0]['Destination_Name']
    
    print(f"Getting detailed information about {destination}...")
    time.sleep(1)  # Simulate processing time
    
    explanation = recommender.explain_recommendation(destination)
    print(f"\nDetailed information about {destination}:")
    print(explanation)
    
    # Personalized scenario
    print_subheader("PERSONALIZED SCENARIO")
    print("Let's create a personalized scenario:")
    print("A couple looking for a romantic getaway with relaxation and scenic views")
    print("Budget: ₹5,000 - ₹15,000 per day")
    print("Travel month: February (Valentine's season)")
    
    preferences = ['Romantic', 'Relaxation', 'Scenic']
    group_type = 'Couple'
    num_adults = 2
    num_children = 0
    min_budget = 5000
    max_budget = 15000
    current_month = 'February'
    
    print("\nGenerating personalized recommendations...")
    time.sleep(1.5)  # Simulate processing time
    
    personalized_recs = recommender.get_hybrid_recommendations(
        preferences=preferences,
        group_type=group_type,
        num_adults=num_adults,
        num_children=num_children,
        min_budget=min_budget,
        max_budget=max_budget,
        current_month=current_month
    )
    
    print(f"\nTop 5 romantic destinations for February:")
    for i, (_, rec) in enumerate(personalized_recs.iterrows()):
        print_recommendation(rec, i+1)
    
    print_header("DEMO COMPLETE")
    print("\nThe Indian Travel Recommendation System successfully demonstrated all filtering methods:")
    print("✅ Content-based filtering (matching destinations to preferences)")
    print("✅ Demographic-based filtering (finding suitable destinations for group types)")
    print("✅ Budget-based filtering (recommending destinations within budget constraints)")
    print("✅ Seasonal considerations (suggesting destinations ideal for the travel month)")
    print("✅ Hybrid filtering (combining all approaches for personalized recommendations)")
    print("\nThank you for exploring the recommendation system!")

if __name__ == "__main__":
    main()