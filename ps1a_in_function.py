def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    
	return months