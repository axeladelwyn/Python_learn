## 6.100A PSet 1: Part A
## Name: Axel
## Time Spent:
## Collaborators: -

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = 112000.0
portion_saved = .17
cost_of_dream_home = 750000.0
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25  # 20% down payment
current_savings = 0.0
annual_return = 0.05  # Annual return on investment
monthly_salary = yearly_salary / 12
monthly_savings = monthly_salary * portion_saved
down_payment = cost_of_dream_home * portion_down_payment
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

# Initialize month counter
months = 0

# Loop until current savings reach the down payment
while current_savings < down_payment:
    # Add monthly savings and investment return
    current_savings += monthly_savings + (current_savings * annual_return / 12)
    months += 1
    
