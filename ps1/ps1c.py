def guessRate(begin, end):
    guess = ((begin + end) / 2) / 10000.0
    return guess

def findSaveRate(starting_salary):
    #program constants
    portion_down_payment = 0.25
    total_cost = 1000000
    down = total_cost * portion_down_payment
    r = 0.04
    semi_annual_raise = .07
    months = 36

    #counters, boundaries
    searches = 0
    begin = 0
    end = 10000

    while (end - begin) > 1:
        searches += 1
        current_savings = 0.0
        annual_salary = starting_salary
        currentGuess = guessRate(begin, end)
        month = 1

        while month <= months:
            current_savings *= 1 + (r / 12)
            current_savings += (annual_salary / 12) * currentGuess
            #increases salary semi-annually after every 6th month
            if (not (month % 6)):
                annual_salary *= 1 + semi_annual_raise
            month += 1
        
        costDiff = current_savings - down
        if costDiff > 100:
            end = currentGuess * 10000
        elif costDiff < 0:
            begin = currentGuess * 10000
        else:
            print("Best savings rate:", str(currentGuess))
            print("Steps in bisection search:", str(searches))
            return
    
    #if impossible to save for down payment within 36 months
    print("It is not possible to pay the down payment in three years.")
    

if __name__ == "__main__":
    findSaveRate(float(input("Enter the starting salary: ")))