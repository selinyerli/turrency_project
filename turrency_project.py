import pandas as pd

# Conversion rates
USD_TO_TRY = 35
EUR_TO_TRY = 36.57

# Updated inflation rates (calculated from dataset)
USD_INFLATION_RATE = 0.049  # 4.9%
EUR_INFLATION_RATE = 0.054  # 5.4%

# Activity dataset with duplicates removed
data = [
    # New York - Date-Specific (NBA Games)
    {"Activity": "Utah Jazz at NY Knicks", "Type": "NBA Game", "Category": "High", "Date": "02.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 1995, "City": "New York", "Price (EUR)": None},
    {"Activity": "Utah Jazz at NY Knicks", "Type": "NBA Game", "Category": "Mid", "Date": "02.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 850, "City": "New York", "Price (EUR)": None},
    {"Activity": "Utah Jazz at NY Knicks", "Type": "NBA Game", "Category": "Low", "Date": "02.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 350, "City": "New York", "Price (EUR)": None},

    {"Activity": "Orlando Magic at NY Knicks", "Type": "NBA Game", "Category": "High", "Date": "06.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 1850, "City": "New York", "Price (EUR)": None},
    {"Activity": "Orlando Magic at NY Knicks", "Type": "NBA Game", "Category": "Mid", "Date": "06.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 750, "City": "New York", "Price (EUR)": None},
    {"Activity": "Orlando Magic at NY Knicks", "Type": "NBA Game", "Category": "Low", "Date": "06.01.2025",
     "Location": "Madison Square Garden", "Price (USD)": 300, "City": "New York", "Price (EUR)": None},

    # New York - Date-Specific (Movies)
    {"Activity": "Rabbit Trap", "Type": "Movie", "Category": "High", "Date": "09.01.2025",
     "Location": "Regal Battery Park", "Price (USD)": 30, "City": "New York", "Price (EUR)": None},
    {"Activity": "Rabbit Trap", "Type": "Movie", "Category": "Mid", "Date": "09.01.2025",
     "Location": "Regal Battery Park", "Price (USD)": 20, "City": "New York", "Price (EUR)": None},
    {"Activity": "Rabbit Trap", "Type": "Movie", "Category": "Low", "Date": "09.01.2025",
     "Location": "Regal Battery Park", "Price (USD)": 10, "City": "New York", "Price (EUR)": None},

    # Paris - Date-Specific (Concerts and Football)
    {"Activity": "Paris Saint-Germain vs. Marseille", "Type": "Football Match", "Category": "High", "Date": "02.01.2025",
     "Location": "Parc des Princes", "Price (USD)": None, "City": "Paris", "Price (EUR)": 1200},
    {"Activity": "Beyoncé Renaissance Tour", "Type": "Concert", "Category": "High", "Date": "15.01.2025",
     "Location": "Accor Arena", "Price (USD)": None, "City": "Paris", "Price (EUR)": 950},
    {"Activity": "Ed Sheeran Concert", "Type": "Concert", "Category": "High", "Date": "22.01.2025",
     "Location": "Stade de France", "Price (USD)": None, "City": "Paris", "Price (EUR)": 850},

    # Non-Date-Specific
    {"Activity": "Empire State Building", "Type": "Museum", "Category": "High", "Date": None,
     "Location": "20 W 34th St", "Price (USD)": 146, "City": "New York", "Price (EUR)": None},
]

df_complete_activities = pd.DataFrame(data).drop_duplicates()

# Add food options to the New York non-date-specific activities
food_options = [
    # High
    {"Activity": "Eleven Madison Park", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "11 Madison Ave", "Price (USD)": 100, "City": "New York", "Price (EUR)": None},
    {"Activity": "Jean-Georges", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "1 Central Park W", "Price (USD)": 100, "City": "New York", "Price (EUR)": None},
    {"Activity": "Daniel NYC", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "60 E 65th St", "Price (USD)": 100, "City": "New York", "Price (EUR)": None},

    # Mid
    {"Activity": "Veselka", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "144 2nd Ave", "Price (USD)": 25, "City": "New York", "Price (EUR)": None},
    {"Activity": "In-n-out Burger", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "N/A", "Price (USD)": 23, "City": "New York", "Price (EUR)": None},
    {"Activity": "Levain Bakery", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "351 Amsterdam Ave", "Price (USD)": 7, "City": "New York", "Price (EUR)": None},

    # Low
    {"Activity": "Los Tacos No. 1", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "75 9th Ave", "Price (USD)": 13, "City": "New York", "Price (EUR)": None},
    {"Activity": "Bleecker Street Pizza", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "69 7th Ave S", "Price (USD)": 5, "City": "New York", "Price (EUR)": None},
    {"Activity": "Crumble Cookie", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "1385 Broadway", "Price (USD)": 4, "City": "New York", "Price (EUR)": None},
]

# Additional food options for Paris
paris_food_options = [
    # High
    {"Activity": "Le Jules Verne", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "Eiffel Tower, Champ de Mars", "Price (USD)": 200, "City": "Paris", "Price (EUR)": None},
    {"Activity": "Guy Savoy", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "Monnaie de Paris, 11 Quai de Conti", "Price (USD)": 250, "City": "Paris", "Price (EUR)": None},
    {"Activity": "L'Ambroisie", "Type": "Restaurant", "Category": "High", "Date": None,
     "Location": "9 Place des Vosges", "Price (USD)": 300, "City": "Paris", "Price (EUR)": None},

    # Mid
    {"Activity": "Bouillon Pigalle", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "22 Boulevard de Clichy", "Price (USD)": 50, "City": "Paris", "Price (EUR)": None},
    {"Activity": "Le Petit Cler", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "29 Rue Cler", "Price (USD)": 40, "City": "Paris", "Price (EUR)": None},
    {"Activity": "Chez Janou", "Type": "Restaurant", "Category": "Mid", "Date": None,
     "Location": "2 Rue Roger Verlomme", "Price (USD)": 35, "City": "Paris", "Price (EUR)": None},

    # Low
    {"Activity": "Crepes at Breizh Cafe", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "109 Rue Vieille du Temple", "Price (USD)": 10, "City": "Paris", "Price (EUR)": None},
    {"Activity": "Baguette Sandwich at Local Bakery", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "Various Locations", "Price (USD)": 8, "City": "Paris", "Price (EUR)": None},
    {"Activity": "Falafel at L'As du Fallafel", "Type": "Restaurant", "Category": "Low", "Date": None,
     "Location": "34 Rue des Rosiers", "Price (USD)": 6, "City": "Paris", "Price (EUR)": None},
]

# Convert food options into DataFrames
df_food_options = pd.DataFrame(food_options)
df_paris_food_options = pd.DataFrame(paris_food_options)

# Add the new food options to the main dataset
df_complete_activities = pd.concat([df_complete_activities, df_food_options, df_paris_food_options], ignore_index=True)

# Transportation costs dictionary
transportation_costs = {
    "New York": {"Taxi (per km)": 3, "Metro Pass (daily)": 12, "Bike Rental (hourly)": 10},
    "Paris": {"Taxi (per km)": 2, "Metro Pass (daily)": 10, "Bike Rental (hourly)": 8}
}

def get_transportation_info(city):
    """Display transportation options and costs for the selected city."""
    return transportation_costs.get(city.title(), "No transportation data available.")

def recommend_activities(city, category, start_date, end_date):
    """Recommend activities based on city, category, and travel date range."""
    city = city.title()
    category = category.capitalize()
    
    # Convert dates to datetime objects for comparison
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter date-specific activities within the date range
    date_specific = df_complete_activities[
        (df_complete_activities['City'] == city) &
        (df_complete_activities['Category'] == category) &
        (df_complete_activities['Date'].notna())
    ]
    
    date_specific = date_specific.copy()  # Avoid SettingWithCopyWarning
    date_specific['Date'] = pd.to_datetime(date_specific['Date'], format='%d.%m.%Y')
    date_specific = date_specific[
        (date_specific['Date'] >= start_date) & (date_specific['Date'] <= end_date)
    ]

    # Include non-date-specific activities
    non_date_specific = df_complete_activities[
        (df_complete_activities['City'] == city) &
        (df_complete_activities['Category'] == category) &
        (df_complete_activities['Date'].isna())
    ]

    # Combine results, ensuring all activities are included
    combined_results = pd.concat([date_specific, non_date_specific], ignore_index=True)
    return combined_results

def calculate_predicted_price(price, inflation_rate):
    """Calculate the predicted price based on the inflation rate."""
    if pd.notna(price):
        return price * (1 + inflation_rate)
    return None

def validate_date(date):
    """Validate date format and return as YYYY-MM-DD."""
    try:
        return pd.to_datetime(date, format='%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        return None

# User Interaction
user_city = input("Select a city (New York/Paris): ").strip()
user_category = input("Select your travel standard (High/Mid/Low): ").strip()

# Validate start and end dates
while True:
    user_start_date = validate_date(input("Enter your departure date (DD.MM.YYYY): ").strip())
    user_end_date = validate_date(input("Enter your return date (DD.MM.YYYY): ").strip())
    if user_start_date and user_end_date and user_start_date <= user_end_date:
        break
    print("Invalid date(s) or range. Please enter valid dates in DD.MM.YYYY format.")

# Display Transportation Costs
print(f"\nTransportation Costs in {user_city}:")
transport_info = get_transportation_info(user_city)
if transport_info == "No transportation data available.":
    print(transport_info)
else:
    for mode, cost in transport_info.items():
        print(f"  {mode}: {cost}")

# Get Recommendations
recommendations = recommend_activities(user_city, user_category, user_start_date, user_end_date)

# Add Predicted Prices to Recommendations
recommendations['Predicted Price (USD)'] = recommendations['Price (USD)'].apply(
    lambda x: calculate_predicted_price(x, USD_INFLATION_RATE))
recommendations['Predicted Price (EUR)'] = recommendations['Price (EUR)'].apply(
    lambda x: calculate_predicted_price(x, EUR_INFLATION_RATE))

# Display Recommendations and Calculate Total Cost
if not recommendations.empty:
    print(f"\nRecommended Activities in {user_city} ({user_category.capitalize()} Category) between {user_start_date} and {user_end_date}:")
    print(recommendations[['Activity', 'Type', 'Category', 'Date', 'Location', 
                           'Price (USD)', 'Price (EUR)', 'Predicted Price (USD)', 'Predicted Price (EUR)']])
    
    # Calculate current total costs
    total_cost_usd = recommendations['Price (USD)'].sum(skipna=True)
    total_cost_eur = recommendations['Price (EUR)'].sum(skipna=True)
    total_cost_try = (total_cost_usd * USD_TO_TRY) + (total_cost_eur * EUR_TO_TRY)
    
    # Calculate predicted total costs
    predicted_total_cost_usd = recommendations['Predicted Price (USD)'].sum(skipna=True)
    predicted_total_cost_eur = recommendations['Predicted Price (EUR)'].sum(skipna=True)
    predicted_total_cost_try = (predicted_total_cost_usd * USD_TO_TRY) + (predicted_total_cost_eur * EUR_TO_TRY)
    
    print(f"\nTotal Cost of Selected Activities (Current Prices):")
    if total_cost_usd > 0:
        print(f"  Total Cost in USD: ${total_cost_usd:.2f}")
    if total_cost_eur > 0:
        print(f"  Total Cost in EUR: €{total_cost_eur:.2f}")
    print(f"  Total Cost in TRY: ₺{total_cost_try:.2f}")

    print(f"\nTotal Cost of Selected Activities (Predicted Prices for 2025):")
    if predicted_total_cost_usd > 0:
        print(f"  Predicted Total Cost in USD: ${predicted_total_cost_usd:.2f}")
    if predicted_total_cost_eur > 0:
        print(f"  Predicted Total Cost in EUR: €{predicted_total_cost_eur:.2f}")
    print(f"  Predicted Total Cost in TRY: ₺{predicted_total_cost_try:.2f}")
else:
    print("\nNo activities are available for your selected options.")