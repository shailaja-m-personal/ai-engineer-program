# Main Program
# Create a list of customer names 
list_cust = ["Andy", "Bob", "Charles", "David", "Joe", "Jessy"]

# Store each customer's order details (customer name, product, price, category) as tuples inside a list 
tp_cust_orders = [
                     ("Andy", "Laptop", 800, "Electronics"),
                     ("Andy", "Earpods", 100, "Electronics"),
                     ("Bob", "Shoes", 30, "Clothing"),
                     ("Bob", "Jeans", 10, "Clothing"),
                     ("Charles", "Microwave", 60, "Home Essentials"),
                     ("Charles", "Smartwatch", 30, "Electronics"),
                     ("David", "Smartphone", 900, "Electronics"),
                     ("David", "Jacket", 100, "Clothing"),
                     ("Joe", "Shoes", 200, "Clothing"),
                     ("Joe", "Guitar", 500, "Electronics"),
                     ("Joe", "Smartphone", 1500, "Electronics"),
                     ("Jessy", "Ipad", 800, "Electronics"),
                     ("Jessy", "Bicycle", 300, "Home Essentials"),
                     ("Jessy", "Keyboard", 1000, "Electronics")
                  ]


# Use a dictionary where keys are customer names and values are lists of ordered products 
# function to display customers and their orders
def cust_orders():
    dict_cust_products = {}

    for order in tp_cust_orders:
        customer = order[0]
        product = order[1]

        if customer in dict_cust_products:
            dict_cust_products[customer].append(product)
        else:
            dict_cust_products[customer] = [product]

    print(dict_cust_products)   


# • Use a dictionary to map each product to its respective category 
# function 
def get_prod_categories():
    dict_prod_category = {}

    for order in tp_cust_orders:
        product = order[1]
        category = order[3]

        if category in dict_prod_category:
            if product not in dict_prod_category[category]:
                dict_prod_category[category].append(product)
        else:
            dict_prod_category[category] = [product]

    print(dict_prod_category)

# • Create a set of unique product categories 
# function to create a set of unique product categories 
def get_unique_categories():
    st_unique_categories = set()

    for order in tp_cust_orders:
        category = order[3]
        st_unique_categories.add(category)

    print(st_unique_categories)

# 3. Analyze customer orders 
# • Use a loop to calculate the total amount each customer spends 
# • If the total purchase value is above $100, classify the customer as a high-value buyer 
# • If it is between $50 and $100, classify the customer as a moderate buyer 
# • If it is below $50, classify them as a low-value buyer 
def analyze_cust_orders():
    dict_result = {}
    for cust_list in tp_cust_orders:
      if cust_list[0] in dict_result:
         dict_result[cust_list[0]] += cust_list[2]
      else:
         dict_result[cust_list[0]] = cust_list[2]
    
    # print(dict_result)

    for key, value in dict_result.items():
        if value > 100:
            print(key, "is a high-value buyer")
        elif 50 <= value <= 100 :
            print(key, "is a moderate buyer")
        else:
            print(key, "is a low-value buyer")

# • Calculate the total revenue per product category and store it in a dictionary 
# function
def revenue_by_category():
    dict_category_revenue = {}
    for order in tp_cust_orders:
        price = order[2]
        category = order[3]
        
        if category in dict_category_revenue:
            dict_category_revenue[category] += price
        else:
            dict_category_revenue[category] = price
    print(dict_category_revenue)   

# • Extract unique products from all orders using a set 
# function
def get_unique_product():
    unique_products = set()
    
    for order in tp_cust_orders:
        product = order[1]
        unique_products.add(product)
        
    print(unique_products)

# • Use a list comprehension to find all customers who purchased electronics 
def get_electronics_customers():
    
    list_electronics_customers = list(set(
        [order[0] for order in tp_cust_orders if order[3] == "Electronics"]))
    
    print(list_electronics_customers)

# • Identify the top three highest-spending customers using sorting 
def get_top_customers():
    set_customer_spending = {}
    
    for order in tp_cust_orders:
        customer = order[0]
        price = order[2]
        
        if customer in set_customer_spending:
            set_customer_spending[customer] += price
        else:
            set_customer_spending[customer] = price
    list_customer_spending = list(set_customer_spending.items())
    # print(list_customer_spending)
    
    def get_spending(customer):
        return customer[1]
    
    list_customer_spending.sort(key=get_spending, reverse=True)
    # print(list_customer_spending)
    
    print(list_customer_spending[:3])

# • Print a summary of each customer’s total spending and their classification 

def get_customer_classification():
    customer_spending = {}

    # Calculate total spending
    for order in tp_cust_orders:
        customer = order[0]
        price = order[2]

        if customer in customer_spending:
            customer_spending[customer] += price
        else:
            customer_spending[customer] = price 
    # print(customer_spending)
    # Print summary and classification
    for customer, total in customer_spending.items():
        if total > 1000:
            classification = "High-value buyer"

        elif 500 <= total <= 1000:
            classification = "Moderate buyer"

        else:
            classification = "Low-value buyer"

        print(customer, "-", total, "-", classification)

# • Use set operations to find customers who purchased from multiple categories 
# function 
def get_customer_categories():
    customer_categories = {}

    for order in tp_cust_orders:
        customer = order[0]
        category = order[3]

        if customer in customer_categories:
            customer_categories[customer].add(category)
        else:
            customer_categories[customer] = {category}

    # print(customer_categories)
    # print('Customers who purchased from multiple categories:')
    for customer, categories in customer_categories.items():
        if len(categories) > 1:
            print( customer, categories)

# • Identify common customers who bought both electronics and clothing 
# function
def get_common_customers():
    electronics = set()
    clothing = set()

    for order in tp_cust_orders:
        customer = order[0]
        category = order[3]

        if category == "Electronics":
            electronics.add(customer)

        elif category == "Clothing":
            clothing.add(customer)

    common_customers = electronics.intersection(clothing)

    print(common_customers)

#----------------------------------------------------------------
print('List of customers: \n', list_cust, '\n')

print('Tuple to display customers and their orders: \n', tp_cust_orders, '\n')

#function calling to display customer orders
print('\n Display customers and their orders: \n')
cust_orders(), '\n'

#function calling to display products and their categories defined in a dictionary
print('\n Display products and their categories from dictionary: \n')
get_prod_categories(), '\n'

#function calling to display a set of unique product categories 
print('\n Display a set of unique product categories : \n')
get_unique_categories(), '\n'

#function calling to analyze the customer orders
print('\n Analyze the customers based on their spends : \n')
analyze_cust_orders()

#function calling to calculate the total revenue per product category and store it in a dictionary 
print('\n Display the total revenue per product category : \n')
revenue_by_category()

#function calling to extract unique products from all orders using a set  
print('\n Display unique products from all orders : \n')
get_unique_product()

#function calling to find all customers who purchased electronics from list comprehension  
print('\n Display all customers who purchased electronics : \n')
get_electronics_customers()

#function calling to get top three highest-spending customers  
print('\n The top three highest-spending customers : \n')
get_top_customers()

#function calling to customer classification
print('\n Classify the customers based on their total spends : \n')
get_customer_classification()

#function calling to get the customers who purchased from multiple categories
print('\n Customers who purchased from multiple categories : \n')
get_customer_categories()

#function calling to get the customers who purchased both electronics and clothing
print('\n Customers who purchased both electronics and clothing : \n')
get_common_customers()