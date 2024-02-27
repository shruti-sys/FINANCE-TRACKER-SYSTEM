import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdftables_api  # Install this library using pip if not already installed

# PDF to CSV
import tabula
def convert_pdf_to_csv(path_path, csv_output_path):
    df = tabula.read_pdf("test.pdf", pages='all')[0]
    tabula.convert_into("test.pdf", "input.csv", output_format="csv", pages='all')
    print(df)


# Remove Duplicate Rows
def remove_duplicates(input_csv, cleaned_csv):
    df = pd.read_csv(input_csv, header=None)
    df_cleaned = df.drop_duplicates(keep='first')
    df_cleaned.to_csv(cleaned_csv, index=False, header=None)

# Remove Page Numbers
def remove_page_numbers(input_csv, modified_csv):
    df = pd.read_csv(input_csv)
    pattern = 'Page No .: \d+'
    mask = ~df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1)
    df_filtered = df[mask]
    df_filtered.to_csv(modified_csv, index=False)

# Categorize Narration
def categorize_narration(narration):
    # Convert the narration to lowercase for case-insensitive matching
    lower_narration = narration.lower()

    # Define lists of keywords for each category
    food_keywords = ['swiggy', 'milk', 'restaurant', 'zomato', 'mcdonalds', 'snack', 'mcd',
                     'store', 'cafe', 'market', 'dominos', 'pizza', 'dmart', 'super market',
                     'burglars', 'richie rich', 'foods', 'momos', 'biryani', 'mother dairy',
                     'dairy', 'cake', 'burger', 'amul', 'ice cream', 'bakers', 'juice', 'roll',
                     'food', 'blinkit', 'grofers']

    lifestyle_keywords = ['maxfashion', 'tatacliq', 'fabrication', 'derma co', 'dermaco',
                          'statonery', 'stationary', 'amazon', 'flipkart', 'ajio', 'myntra',
                          'stationers', 'meesho', 'puma', 'adidas', 'nike']

    beauty_keywords = ['beauty', 'salon', 'nykaa']

    tech_keywords = ['prepaid', 'apple', 'jio', 'mobility', 'technologi', 'recharge', 'reliance']

    medicine_keywords = ['chemist', 'medical', 'med', 'medicose', 'wellness forever']

    travel_keywords = ['makemytrip', 'railways', 'pvr', 'airport', 'zoomcar', 'car']

    college_keywords = ['bharati vidyapeeth']

    # Check for the presence of keywords and assign the corresponding category
    for keyword_list, category in zip(
            [food_keywords, lifestyle_keywords, beauty_keywords, tech_keywords, medicine_keywords,
             travel_keywords, college_keywords],
            ['food', 'lifestyle', 'beauty', 'tech', 'medicine', 'travel', 'college']):
        for keyword in keyword_list:
            if keyword in lower_narration:
                return category

    # If no keywords match, assign the category as 'other'
    return 'other'
    

# Process Bank Statement
def process_bank_statement(input_csv, output_csv):
    df = pd.read_csv(input_csv, header=None)
    
    # Additional processing steps can be added here if needed
    
    # Apply the categorization function to create a new 'Category' column
    df['Category'] = df[2].apply(categorize_narration)
    
    # Count occurrences of each category and add a new column 'Category_Count'
    category_counts = df['Category'].value_counts()
    df['Category_Count'] = df['Category'].map(category_counts)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(output_csv, index=False)

# Visualize Category Counts
def visualize_category_counts(input_csv):
    df = pd.read_csv(input_csv)
    category_counts = df['Category'].value_counts()
    dict_count = {}
    print("Category_Count:")
    for category, count in category_counts.items():
        print(f"{category.ljust(10)}: {count}")
        dict_count[category] = count
    
    # Convert the dictionary to a DataFrame
    df_count = pd.DataFrame(list(dict_count.items()), columns=['Category', 'Category_Count'])
    
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

# Example Usage
pdf_path = 'test.pdf'  # Replace with your actual PDF file path
csv_output_path = 'input.csv'
cleaned_csv_path = 'cleaned_output.csv'
modified_csv_path = 'modified_output.csv'

# Convert PDF to CSV
convert_pdf_to_csv(pdf_path, csv_output_path)

# Remove Duplicate Rows
remove_duplicates(csv_output_path, cleaned_csv_path)

# Remove Page Numbers
remove_page_numbers(cleaned_csv_path, modified_csv_path)

# Process Bank Statement
process_bank_statement(modified_csv_path, 'final_output.csv')

# Visualize Category Counts
visualize_category_counts('final_output.csv')
