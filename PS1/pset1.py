





'''

def best_saving_rate(annual_starting_salary):

    """
    input annual salary
    output the optimal rate for a 36 month saving plan to save up for a 1000000  house 
    """
    proportion_down_payment = 0.25
    monthly_salary = annual_starting_salary/12
    total_cost = 1000000
    aim_savings = total_cost * proportion_down_payment  
    semi_annual_raise = 0.07
    portion_saved = 0
    r = 0.04
    
    flag = False
    step = 0
    min = 0
    max = 1
    current_savings = 0
    while True:
        portion_saved = (min + max)/2
        for i in range(36):
            current_savings += current_savings*r/12 + monthly_salary*portion_saved
        
            if  i % 6 == 0:
                monthly_salary *= (1+ semi_annual_raise)
        
        if abs(current_savings - aim_savings) < 100:
            break
            
        elif current_savings - aim_savings >100:
            max -= 0.01
            current_savings = 0
            monthly_salary = annual_starting_salary/12
        elif aim_savings - current_savings > 100:
            min += 0.01
            current_savings = 0
            monthly_salary = annual_starting_salary/12
    return portion_saved
        
print(best_saving_rate(150000))
'''
def best_saving_rate(annual_starting_salary):
    """
    input annual salary
    output the optimal rate for a 36-month saving plan to save up for a $1,000,000 house
    """
    proportion_down_payment = 0.25
    monthly_salary = annual_starting_salary / 12
    total_cost = 1000000
    aim_savings = total_cost * proportion_down_payment
    semi_annual_raise = 0.07
    portion_saved = 0
    r = 0.04

    flag = False
    step = 0.01
    min_rate = 0
    max_rate = 1
    current_savings = 0

    while abs(current_savings - aim_savings) > 100:
        portion_saved = (min_rate + max_rate) / 2
        current_savings = 0
        monthly_salary_temp = monthly_salary  # Save the initial monthly salary for each iteration

        for i in range(36):
            current_savings += current_savings * r / 12 + monthly_salary_temp * portion_saved

            if i % 6 == 0:
                monthly_salary_temp *= (1 + semi_annual_raise)

        if current_savings < aim_savings:
            min_rate = portion_saved
        else:
            max_rate = portion_saved

    return portion_saved


print(best_saving_rate(150000))

      
        
   








