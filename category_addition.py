import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#CATEGORIES DIVISION

csv_file_path = 'modified_output.csv' 
df = pd.read_csv(csv_file_path)

# Define function to categorize narration based on keywords
def categorize_narration(narration):
    food_keywords = ['SWIGGY', 'MILK', 'RESTAURANT', 'ZOMATO', 'MCDONALDS', 'SNACK', 'MCD',
                     'STORE', 'CAFE', 'MARKET', 'DOMINOS', 'PIZZA', 'DMART', 'SUPER MARKET',
                     'BURGLARS', 'RICHIE RICH', 'FOODS', 'MOMOS', 'BIRYANI', 'MOTHER DAIRY',
                     'DAIRY', 'CAKE', 'BURGER', 'AMUL', 'ICE CREAM', 'BAKERS', 'JUICE', 'ROLL',
                     'FOOD', 'BLINKIT', 'GROFERS']

    lifestyle_keywords = ['MAXFASHION', 'TATACLIQ', 'FABRICATION', 'DERMA CO', 'DERMACO',
                          'STATONERY', 'STATIONARY', 'AMAZON', 'FLIPKART', 'AJIO', 'MYNTRA',
                          'STATIONERS', 'MEESHO', 'PUMA', 'ADIDAS', 'NIKE']

    beauty_keywords = ['BEAUTY', 'SALON', 'NYKAA']

    tech_keywords = ['PREPAID', 'APPLE', 'JIO', 'MOBILITY', 'TECHNOLOGI', 'RECHARGE', 'RELIANCE']

    medicine_keywords = ['CHEMIST', 'MEDICAL', 'MED', 'MEDICOSE', 'WELLNESS FOREVER']

    travel_keywords = ['MAKEMYTRIP', 'RAILWAYS', 'PVR', 'AIRPORT', 'ZOOMCAR', 'CAR']

    college_keywords = ['BHARATI VIDYAPEETH']


    for keyword_list, category in zip(
            [food_keywords, lifestyle_keywords, beauty_keywords, tech_keywords, medicine_keywords,
             travel_keywords, college_keywords],
            ['food', 'lifestyle', 'beauty', 'tech', 'medicine', 'travel', 'college']):
        for keyword in keyword_list:
            if keyword in narration:
                return category

    return 'other'

# Apply the categorization function to create a new 'Category' column
df['Category'] = df['Narration'].apply(categorize_narration)

# Count occurrences of each category and add a new column 'Category_Count'
category_counts = df['Category'].value_counts()
df['Category_Count'] = df['Category'].map(category_counts)

# Sort the DataFrame based on the 'Category' column
df_sorted = df.sort_values(by='Category')

# Save the updated DataFrame back to the CSV file
df.to_csv('modified_output.csv', index=False)  # Replace with your desired output file path

# Display the sorted DataFrame
print(df_sorted[['Date', 'Narration', 'Category']])



#DISPLAY CATEGORY AND THEIR COUNTS

# Specify the path to your CSV file
csv_file_path = 'modified_output.csv'  # Replace with your actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


# Count occurrences of each category and add a new column 'Category_Count'
category_counts = df['Category'].value_counts()

# Display the count of each category
dictCount = {}
print("Category_Count:")
for category, count in category_counts.items():
    print(f"{category.ljust(10)}: {count}")
    dictCount[category] = count


#VISUALIZATION  

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming dictCount is already defined

# Convert the dictionary to a DataFrame
df_count = pd.DataFrame(list(dictCount.items()), columns=['Category', 'Category_Count'])

# Sort the DataFrame by Category_Count in descending order
df_count = df_count.sort_values(by='Category_Count', ascending=False)

# Plot a bar graph
plt.figure(figsize=(12, 8))
sns.barplot(x='Category', y='Category_Count', data=df_count, palette='viridis')
plt.title('Category Count Bar Plot')
plt.xlabel('Category')
plt.ylabel('Category_Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.show()
# Set the y-axis limits (adjust the values as needed)
plt.ylim(0, 1000)




