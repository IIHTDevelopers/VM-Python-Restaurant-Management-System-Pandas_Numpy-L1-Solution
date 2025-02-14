from restaurant_manager import RestaurantManager

# Create a restaurant instance
restaurant = RestaurantManager()

# Add some orders
print("Adding orders...")
total1 = restaurant.add_order("John", ["Burger", "Pizza"])
print(f"Order 1 total: ${total1:.2f}")

total2 = restaurant.add_order("Alice", ["Salad", "Ice Cream"])
print(f"Order 2 total: ${total2:.2f}")

# Get revenue stats
stats = restaurant.get_daily_revenue_stats()
print("\nDaily Revenue Statistics:")
for key, value in stats.items():
    print(f"{key.capitalize()}: ${value:.2f}")

# Get sales analysis
print("\nSales Analysis:")
df = restaurant.get_sales_analysis()
print(df)
