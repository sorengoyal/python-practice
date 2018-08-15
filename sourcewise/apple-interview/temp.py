mortage_payment = 2200
rent = 1300
income = 1000
monthly_property_tax = 5000/12
monthly_maintenace = 10000/12
net_monthly_payment = mortage_payment+monthly_maintenace+monthly_property_tax - income
total_cost_of_ownership = 0
for i in range(36):
    total_cost_of_ownership += net_monthly_payment

net_money_at_end_of_term = 2200*36 - total_cost_of_ownership
total_rent_paid_for_term = 1300*36
net_benefit = net_money_at_end_of_term + total_rent_paid_for_term
print(total_cost_of_ownership)
print(net_money_at_end_of_term)
print(total_rent_paid_for_term)
print(net_benefit)