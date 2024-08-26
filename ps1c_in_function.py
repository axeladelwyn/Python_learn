def part_c(initial_deposit):
	#########################################################################
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	#################################################################################################
	cost_of_house = 800000
	down_payment_percentage = 0.25
	months = 36
	epsilon = 100  # Allowable error margin
	# Calculate the down payment
	down_payment = cost_of_house * down_payment_percentage
	# Bisection search setup
	low = 0.0
	high = 1.0
	steps = 0
	max_steps = 1000
	r = None
	# Check if the initial deposit is already sufficient
	if initial_deposit >= down_payment - epsilon:
	    r = 0.0
	else:
	    def calculate_savings(initial_deposit, r, months):
	        current_savings = initial_deposit
	        monthly_return = r / 12
	        for month in range(1, months + 1):
	            current_savings += current_savings * monthly_return
	        return current_savings
	    # Bisection search
	    while low <= high and steps < max_steps:
	        steps += 1
	        guess = (high + low) / 2.0
	        savings = calculate_savings(initial_deposit, guess, months)
	        
	        if abs(savings - down_payment) <= epsilon:
	            r = guess
	            break
	        elif savings < down_payment:
	            low = guess
	        else:
	            high = guess
	    # If no suitable rate is found
	    if r is None:
	        r = None
	return r, steps