# -------------------------------------------------------------
# TASK-1
#--------------------------------------------------------------
# 1. Store customer orders 
# • Create a list of customer names 
# • Store each customer's order details (customer name, product, price, category) as tuples inside a list 
# • Use a dictionary where keys are customer names and values are lists of ordered products 
#---------------------------------------------------------------
# Create a list of customer names 
#---------------------------------------------------------------
list_cust = ["Andy", "Bob", "Charles", "David", "Joe", "Jessy"]
# print(type(list_cust))
# print(list_cust)
#---------------------------------------------------------------
#Store each customer's order details (customer name, product, price, category) as tuples inside a list 
#---------------------------------------------------------------
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
# print(type(tp_cust_orders))
# print(tp_cust_orders)
#---------------------------------------------------------------
#Use a dictionary where keys are customer names and values are lists of ordered products 
#---------------------------------------------------------------
dict_cust_products = {}

for order in tp_cust_orders:
    customer = order[0]
    product = order[1]

    if customer in dict_cust_products:
        dict_cust_products[customer].append(product)
    else:
        dict_cust_products[customer] = [product]

# print(type(dict_cust_products))
# print(dict_cust_products)
#----------------------------------------------------------------
# TASK-2
#----------------------------------------------------------------
# 2. Classify products by category 
# • Use a dictionary to map each product to its respective category 
# • Create a set of unique product categories 
# • Display all available product categories 

# • Use a dictionary to map each product to its respective category 
dict_prod_category = {
                        "Electronics" : ["Laptop", "Earpods", "Smartwatch", "Smartphone", "Guitar", "Ipad"],
                        "Clothing" : ["Shoes", "Jeans", "Jacket", "Dress"],
                        "Home Essentials" : ["Microwave", "Bicycle"],
                        "Produce" : ["Vegetables", "Fruits"],
                        "Grocery" : ["Pulses", "Spices"]
                     }
# print(type(dict_prod_category))
# print(dict_prod_category)
# print(dict_prod_category.keys())
# print(dict_prod_category.values())
# print(dict_prod_category.items())

# • Create a set of unique product categories 
st_prod_categories = {"Electronics", "Clothing", "Home Essentials", "Produce", "Grocery", "Sports"}

# • Display all available product categories 
# print(type(st_prod_categories))
# print(st_prod_categories)

# TASK-3
# 3. Analyze customer orders 
# • Use a loop to calculate the total amount each customer spends 
# • If the total purchase value is above $100, classify the customer as a high-value buyer 
# • If it is between $50 and $100, classify the customer as a moderate buyer 
# • If it is below $50, classify them as a low-value buyer 
# print(tp_cust_orders)
dict_result = {}
def analyze_cust_orders():
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

analyze_cust_orders()
# print(tp_cust_orders)
# print(tp_cust_orders[0][0])
# ----------------------------------------------
# 4. Generate business insights 
# • Calculate the total revenue per product category and store it in a dictionary 
# • Extract unique products from all orders using a set 
# • Use a list comprehension to find all customers who purchased electronics 
# • Identify the top three highest-spending customers using sorting 
# -------------------------------------------------------
# • Calculate the total revenue per product category and store it in a dictionary 
dict_category_revenue = {}
def revenue_by_category():
   for order in tp_cust_orders:
      price = order[2]
      category = order[3]

      if category in dict_category_revenue:
         dict_category_revenue[category] += price
      else:
         dict_category_revenue[category] = price
   # print(dict_category_revenue)   
revenue_by_category()

# • Extract unique products from all orders using a set 
def get_unique_product():
   unique_products = set()

   for order in tp_cust_orders:
      product = order[1]
      unique_products.add(product)

   # print(unique_products)

get_unique_product()

# • Use a list comprehension to find all customers who purchased electronics 
def get_electronics_customers():
   list_electronics_customers = list(set(
    [order[0] for order in tp_cust_orders if order[3] == "Electronics"]
   ))
   # print(list_electronics_customers)

get_electronics_customers()

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

   def get_spending(customer):
    return customer[1]

   list_customer_spending.sort(key=get_spending, reverse=True)

   # print(list_customer_spending[:3])

get_top_customers()

# 5. Organize and display data 
# • Print a summary of each customer’s total spending and their classification 
# • Use set operations to find customers who purchased from multiple categories 
# • Identify common customers who bought both electronics and clothing 

# • Print a summary of each customer’s total spending and their classification 
customer_spending = {}

# Calculate total spending
for order in tp_cust_orders:
    customer = order[0]
    price = order[2]

    if customer in customer_spending:
        customer_spending[customer] += price
    else:
        customer_spending[customer] = price 
print(customer_spending)
# Print summary and classification
for customer, total in customer_spending.items():
    if total > 1000:
        classification = "High-value buyer"

    elif 500 <= total <= 1000:
        classification = "Moderate buyer"

    else:
        classification = "Low-value buyer"

   #  print(customer, "-", total, "-", classification)
# • Use set operations to find customers who purchased from multiple categories 
customer_categories = {}

for order in tp_cust_orders:
    customer = order[0]
    category = order[3]

    if customer in customer_categories:
        customer_categories[customer].add(category)
    else:
        customer_categories[customer] = {category}

print(customer_categories)
print('Customers who purchased from more than one category:')
for customer, categories in customer_categories.items():
    if len(categories) > 1:
        print( customer, categories)

# • Identify common customers who bought both electronics and clothing 
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

print("Customers who bought both electronics and clothing:", common_customers)