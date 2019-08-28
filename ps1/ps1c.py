def guessRate(begin, end):
    #finds midpoint of the given search range and returns it as a decimal
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

    #search counter, search boundaries
    searches = 0
    begin = 0
    end = 10000

    #continue until there are no more valid save rate guesses.
    while (end - begin) > 1:
        searches += 1
        currentGuess = guessRate(begin, end)

        #reinitialize variables for new iteration
        current_savings = 0.0
        month = 1
        annual_salary = starting_salary

        while month <= months:
            current_savings *= 1 + (r / 12)
            current_savings += (annual_salary / 12) * currentGuess
            
            #increases salary semi-annually after every 6th month
            if (not (month % 6)):
                annual_salary *= 1 + semi_annual_raise
            month += 1
        
        #checks if savings are within 100 dollars of required down payment
        costDiff = current_savings - down

        #updates upper/lower bounds
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