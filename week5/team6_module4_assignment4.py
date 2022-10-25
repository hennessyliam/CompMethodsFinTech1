# Team 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Oct 6, 2022
#

def compound_interest(principal, time_in_years, rate):
	total_compounded = time_in_years * 12
	for i in range(1, (total_compounded + 1)):
		principal = principal * (1 + (rate / 12))
	return principal


def compound_recursion(principal, time_in_years, rate):
	periods = time_in_years * 12

	def compound_periods(principal, periods):
		if periods == 0:
			return principal
		else:
			principal = principal * (1 + (rate / 12))
			return compound_periods(principal, periods - 1)

	return compound_periods(principal, periods)


# Driver Code:
print(compound_interest(4000, 10, 0.06))
print(compound_recursion(4000, 10, 0.06))


# Team 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Oct 7, 2022

# This program uses recursive function to find the final amount of a compounding interest
# given the principal, years, compounding periods, and rate

def compound_interest(principal, times_in_years, rate):
    # base case
    if times_in_years == 0:
        return principal
    # recur on compounding periods
    else:
        return compound_interest(principal*(1+(rate/12)), ((times_in_years*12)-1)/12, rate)


# Driver Code:
print(compound_interest(4000, 10, 0.06))
