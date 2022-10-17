from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

pizzas_made = 0

while pizza_orders and employees:
    current_pizza_order = pizza_orders[0]
    current_employee = employees[-1]

    if current_pizza_order <= 0 or current_pizza_order > 10:
        pizza_orders.popleft()
        continue

    if current_pizza_order <= current_employee:
        pizzas_made += current_pizza_order
        pizza_orders.popleft()
        employees.pop()
    else:
        pizzas_made += current_employee
        order_transition = current_pizza_order - current_employee
        if order_transition > 0:
            pizza_orders[0] = order_transition
        else:
            pizza_orders.popleft()
        employees.pop()

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
