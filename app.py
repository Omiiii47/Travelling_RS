import pandas as pd
import numpy as np
import streamlit as st
from recommendation_system import IndianTravelRecommender

def main():
    """Main function to run the Streamlit app"""
    st.set_page_config(page_title="Smart Destiny", layout="wide")
    
    st.title("Smart Destiny")
    st.markdown("""
    Find your perfect Indian travel destination based on your preferences and needs.
    This hybrid recommendation system combines content-based, demographic, and popularity-based filtering.
    """)
    
    # Initialize the recommender
    try:
        recommender = IndianTravelRecommender('expanded_indian_destinations.csv')
        
    except Exception as e:
        st.error(f"Error initializing the recommender: {e}")
        return
    
    # Sidebar for inputs
    st.sidebar.header("Your Travel Preferences")
    
    # Travel preferences
    st.sidebar.subheader("What are you looking for?")
    all_preferences = recommender.unique_preferences
    selected_preferences = st.sidebar.multiselect(
        "Select preferences (e.g., Beach, Adventure, Culture):", 
        options=all_preferences,
        default=["Nature", "Relaxation"]
    )
    
    # Group type
    st.sidebar.subheader("Travel Group")
    group_type = st.sidebar.selectbox(
        "Select your travel group type:",
        options=["Family", "Solo", "Couple", "Senior", "Friends"],
        index=0
    )
    
    # Number of travelers
    col1, col2 = st.sidebar.columns(2)
    num_adults = col1.number_input("Number of adults:", min_value=1, max_value=10, value=2)
    num_children = col2.number_input("Number of children:", min_value=0, max_value=10, value=0)
    
    # Budget
    st.sidebar.subheader("Budget (per person per day)")
    col1, col2 = st.sidebar.columns(2)
    min_budget = col1.number_input("Minimum (₹):", min_value=500, max_value=20000, value=1000, step=500)
    max_budget = col2.number_input("Maximum (₹):", min_value=1000, max_value=30000, value=10000, step=1000)
    
    # Month of travel
    st.sidebar.subheader("When are you planning to travel?")
    current_month = st.sidebar.selectbox(
        "Select month of travel:",
        options=["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"],
        index=5  # Default to June
    )
    
    # Number of recommendations
    num_recommendations = st.sidebar.slider(
        "Number of recommendations:", 
        min_value=3, 
        max_value=10, 
        value=5
    )
    
    # Generate button
    generate_btn = st.sidebar.button("Generate Recommendations 🔍", type="primary")
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["📊 Recommendations", "🧭 Explore Destinations", "ℹ️ About"])
    
    with tab1:
        if generate_btn:
            if not selected_preferences:
                st.warning("⚠️ Please select at least one preference to get recommendations.")
            else:
                with st.spinner("Generating personalized recommendations..."):
                    # Get hybrid recommendations
                    recommendations = recommender.get_hybrid_recommendations(
                        preferences=selected_preferences,
                        group_type=group_type,
                        num_adults=num_adults,
                        num_children=num_children,
                        min_budget=min_budget,
                        max_budget=max_budget,
                        current_month=current_month,
                        top_n=num_recommendations
                    )
                    
                    # Display recommendations
                    st.subheader("Your Personalized Recommendations")
                    
                    # Create metrics for top recommendation
                    if not recommendations.empty:
                        top_rec = recommendations.iloc[0]
                        col1, col2, col3, col4 = st.columns(4)
                        col1.metric("Top Recommendation", top_rec['Destination_Name'])
                        col2.metric("State", top_rec['State'])
                        col3.metric("Type", top_rec['Type'])
                        col4.metric("Popularity", f"{top_rec['Popularity_Score']}/10")
                        
                        # Create expandable sections for each recommendation
                        for i, (_, rec) in enumerate(recommendations.iterrows()):
                            with st.expander(f"{i+1}. {rec['Destination_Name']} ({rec['State']})"):
                                col1, col2 = st.columns([2, 1])
                                
                                with col1:
                                    st.markdown(f"**Type:** {rec['Type']}")
                                    st.markdown(f"**Best Time to Visit:** {rec['Best_Time_to_Visit']}")
                                    st.markdown(f"**Experience:** {rec['Preferences']}")
                                    st.markdown(f"**Budget Range:** ₹{rec['Budget_Min']} - ₹{rec['Budget_Max']} per day")
                                    
                                with col2:
                                    # Display match score
                                    match_percentage = int(rec['Final_Score'] * 100)
                                    st.markdown(f"**Match Score:** {match_percentage}%")
                                    
                                    # Create a circular progress indicator
                                    html_code = f"""
                                    <div style="margin: 0 auto; width: 100px; height: 100px; position: relative;">
                                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
                                                  border-radius: 50%; background: conic-gradient(#4CAF50 {match_percentage}%, 
                                                  #f3f3f3 {match_percentage}%); text-align: center; line-height: 100px;">
                                            <span style="font-size: 20px; font-weight: bold;">{match_percentage}%</span>
                                        </div>
                                    </div>
                                    """
                                    st.markdown(html_code, unsafe_allow_html=True)
                                
                                # Add detailed explanation
                                st.markdown("### Why this destination?")
                                explanation = recommender.explain_recommendation(rec['Destination_Name'])
                                st.text(explanation)
                    else:
                        st.warning("No recommendations found that match your criteria. Try adjusting your preferences.")
        else:
            
            
            # Display some example destinations as cards
            st.subheader("Popular Indian Destinations")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                ### Goa
                **Famous for:** Beaches, Nightlife, Portuguese heritage  
                **Best time:** October-March
                """)
            
            with col2:
                st.markdown("""
                ### Manali
                **Famous for:** Mountains, Adventure, Scenic beauty  
                **Best time:** December-February
                """)
                
            with col3:
                st.markdown("""
                ### Jaipur
                **Famous for:** Palaces, Culture, Architecture  
                **Best time:** October-March
                """)
    
    with tab2:
        st.subheader("Explore All Destinations")
        
        # Get all destinations data
        all_destinations = pd.read_csv('expanded_indian_destinations.csv')
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            destination_type = st.multiselect(
                "Filter by type:",
                options=all_destinations['Type'].unique(),
                default=[]
            )
        
        with col2:
            state_filter = st.multiselect(
                "Filter by state:",
                options=all_destinations['State'].unique(),
                default=[]
            )
            
        with col3:
            sort_by = st.selectbox(
                "Sort by:",
                options=["Popularity", "Name", "Budget (Low to High)", "Budget (High to Low)"],
                index=0
            )
            
        # Apply filters
        filtered_df = all_destinations
        
        if destination_type:
            filtered_df = filtered_df[filtered_df['Type'].isin(destination_type)]
            
        if state_filter:
            filtered_df = filtered_df[filtered_df['State'].isin(state_filter)]
            
        # Apply sorting
        if sort_by == "Popularity":
            filtered_df = filtered_df.sort_values('Popularity_Score', ascending=False)
        elif sort_by == "Name":
            filtered_df = filtered_df.sort_values('Destination_Name')
        elif sort_by == "Budget (Low to High)":
            filtered_df = filtered_df.sort_values('Budget_Min')
        elif sort_by == "Budget (High to Low)":
            filtered_df = filtered_df.sort_values('Budget_Min', ascending=False)
            
        # Display filtered destinations
        st.write(f"Showing {len(filtered_df)} destinations")
        
        # Display as grid
        for i in range(0, len(filtered_df), 3):
            cols = st.columns(3)
            for j in range(3):
                if i+j < len(filtered_df):
                    dest = filtered_df.iloc[i+j]
                    with cols[j]:
                        st.markdown(f"### {dest['Destination_Name']}")
                        st.markdown(f"**State:** {dest['State']}")
                        st.markdown(f"**Type:** {dest['Type']}")
                        st.markdown(f"**Best Time:** {dest['Best_Time_to_Visit']}")
                        st.markdown(f"**Budget:** ₹{dest['Budget_Min']} - ₹{dest['Budget_Max']}")
                        st.markdown(f"**Popularity:** {dest['Popularity_Score']}/10")
                        
                        # Create a unique key for each details container
                        details_key = f"details_{dest['Destination_Name']}"
                        
                        # Create a unique key for each button
                        if st.button(f"Show Details", key=f"btn_{i}_{j}"):
                            st.session_state[details_key] = True
                        
                        # Show details if the state is True
                        if details_key in st.session_state and st.session_state[details_key]:
                            with st.expander(f"Details for {dest['Destination_Name']}", expanded=True):
                                explanation = recommender.explain_recommendation(dest['Destination_Name'])
                                st.write(explanation)
                                if st.button("Close", key=f"close_{i}_{j}"):
                                    st.session_state[details_key] = False
                                    st.rerun()  # Updated from experimental_rerun() to rerun()
    
    with tab3:
        st.subheader("About this Recommender")
        st.markdown("""
        This Indian Travel Destination Recommender uses a hybrid recommendation system to suggest travel destinations 
        across India based on your personal preferences, group type, budget, and travel dates.
        
        ### How it works
        
        The recommendation engine combines multiple filtering strategies:
        
        1. **Content-based filtering**: Matches destinations to your selected preferences (e.g., Beach, Adventure, Culture)
        2. **Demographic filtering**: Considers your travel group composition (families, solo travelers, couples, etc.)
        3. **Budget filtering**: Filters destinations that fit within your specified budget range
        4. **Seasonal filtering**: Considers the best time to visit each destination based on your travel month
        5. **Popularity-based filtering**: Incorporates destination popularity as a factor in recommendations
        
        If a family has more than three children, the system adjusts the scores of various destinations to better match family preferences:
        Family-friendly destinations like Beaches, Theme Parks, and Wildlife parks are given a 30% boost in their score. This makes them more likely to be recommended because they are generally more suitable and enjoyable for larger families with kids.
                    
        ### Dataset
        
        The system uses a curated dataset of 30 popular Indian destinations with information on:
        - Location and type (Beach, Hill Station, Heritage, etc.)
        - Typical experiences and activities
        - Best seasons to visit
        - Budget ranges
        - Suitability for different traveler demographics
        - Popularity scores
        
        ### Credits
        OM          
        MINAL            
        NEHA
        """)

if __name__ == "__main__":
    main()