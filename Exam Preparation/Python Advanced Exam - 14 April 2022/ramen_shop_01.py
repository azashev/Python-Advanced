from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen and customers:
    bowl_of_ramen = bowls_of_ramen[-1]
    customer = customers[0]

    if bowl_of_ramen == customer:
        bowls_of_ramen.pop()
        customers.popleft()
    elif customer < bowl_of_ramen:
        bowls_of_ramen[-1] -= customer
        customers.popleft()
    elif customer > bowl_of_ramen:
        customers[0] -= bowl_of_ramen
        bowls_of_ramen.pop()

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")


# You will be given two sequences of integers representing bowls of ramen and customers.
# Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer.
# Try to serve every customer with ramen until we have no more ramen or customers left:
# • Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next
#   bowl of ramen and the next customer.
# • Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the
#   value of that customer and remove the customer.
#   Then try to match the same bowl of ramen (which has been decreased) with the next customer.
# • Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with
#   the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with
#   the next bowl of ramen.
#
#
# Input:
# • On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a
#   comma ", "
# • On the second line, you will receive integers representing the customers, separated by a single space and a
#   comma ", "
#
# Output:
# • If all customers are served, print: "Great job! You served all the customers."
#   - Print all of the left ramen bowls (if any) separated by comma and space in the format:
#   "Bowls of ramen left: {bowls of ramen left}"
# • Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
#   - Print all customers left separated by comma and space in the format "Customers left: {customers left}"
#
#
#
# Tests
#
# Input:
# 14, 25, 37, 43, 19
# 58, 23, 37
#
# Expected output:
# Great job! You served all the customers
# Bowls of ramen left: 14, 6
#
#
#
# Input:
# 30, 13, 45
# 70, 25, 55, 15
#
# Expected output:
# Out of ramen! You didn't manage to serve all customers.
# Customers left: 7, 55, 15
#
#
#
# Input:
# 30, 25
# 20, 35
#
# Expected output:
# Great job! You served all the customers.
