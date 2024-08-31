## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = 110000
portion_saved = .15
cost_of_dream_home = 750000
semi_annual_raise = .03

yearly_salary = 350000
portion_saved = .3
cost_of_dream_home = 10000000
semi_annual_raise = .05
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25  # 25% down payment
current_savings = 0.0
annual_return = 0.05  # Annual return on investment
monthly_salary = yearly_salary / 12
down_payment = cost_of_dream_home * portion_down_payment
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

months = 0

# Loop until current savings reach the down payment
while current_savings < down_payment:
    # Add monthly savings and investment return
    current_savings += monthly_salary * portion_saved + (current_savings * annual_return / 12)
    months += 1
    #for every six months we added the semi-annual salary increase 
    if months % 6 == 0:
        # added the salary increase
        monthly_salary += monthly_salary * semi_annual_raise
    