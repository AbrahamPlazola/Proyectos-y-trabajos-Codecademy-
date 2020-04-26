from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
    from_lat, from_lon = from_coords
    to_lat, to_lon = to_coords
    
    distance = get_distance(from_lat, from_lon, to_lat, to_lon)

    rate = SHIPPING_PRICES.get(shipping_type)

    price = distance * rate
    return format_price(price)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *driver):
    cheapest_driver = None
    cheapest_driver_price = None

    for i in driver:
        driver_time = i.speed * distance
        price_for_driver = i.salary * driver_time

        if cheapest_driver is None:
            cheapest_driver = i
            cheapest_driver_price = price_for_driver

        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = i
            cheapest_driver_price = price_for_driver
    
    return cheapest_driver_price, cheapest_driver

# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0
    for i, j in trips.items():
        trip_revenue = j.cost - j.driver.cost
        total_money_made += trip_revenue
    return total_money_made
# Test the function by calling 
test_function(calculate_money_made)
