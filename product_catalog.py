from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[:3])


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference.lower())  # store preferences in lowercase
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
for product in products:
    product["tags"] = set(product["tags"])




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags)  # intersection of sets




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    matches = []
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            matches.append((product["name"], match_count))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches


# TODO: Step 7 - Call your function and print the results
recommended = recommend_products(products, customer_tags)
print("\nRecommended Products:")
for product, count in recommended:
    print(f"- {product} ({count} match(es))")



"""
Design Memo:

This program uses Python lists, sets, and loops to recommend products based on 
customer preferences. Customer preferences are first collected in a list because 
lists allow multiple inputs in order. Then the list is converted to a set to remove 
duplicates and allow for fast set operations.

Each product’s tags are also stored as a set so that the intersection operation (&) 
can quickly find common tags between products and the customer’s preferences. The 
count_matches() function uses this intersection to calculate matches, and 
recommend_products() loops through all products, counting matches and sorting them 
so the highest match products appear first.

For larger datasets (e.g., 1,000+ products), we might switch from simple loops to 
dictionaries for faster lookups, or use databases or machine learning techniques to 
recommend products efficiently. For now, this set-based approach is ideal for a 
small dataset because it is simple, readable, and runs quickly.
"""

