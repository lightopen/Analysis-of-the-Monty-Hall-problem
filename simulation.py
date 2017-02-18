#python3
from random import randint


"""
define three doors
    car = 1
    goat1 = 2
    goat2 = 3
"""

def calculate_once(total, switch, switch_win, stay, stay_win):
    packed = randint(1, 3)

    #car
    if packed == 1:
        """
        packed car:
            If switched, lose! No matter open which one,
            Not switched, win!
        """            
        switched = randint(0, 1)

        if switched:
            switch += 1
        else:            
            stay += 1
            stay_win += 1

    #goat1
    elif packed == 2:
        """
        packed goat1:
            if switched, win.
            not lose.
        """
        switched = randint(0, 1)
        if switched:
            switch += 1
            switch_win += 1
        else:
            stay += 1

    #goat2
    else:
        """
        packed goat2 like goat1
        """
        switched = randint(0, 1)
        if switched:
            switch += 1
            switch_win += 1
        else:
            stay += 1
    
    return total, switch, switch_win, stay, stay_win

def main():   
    total = 100000
    switch = 0
    switch_win = 0
    stay = 0
    stay_win = 0
        
    for x in range(total):
        total, switch, switch_win, stay, stay_win = calculate_once(total, switch, switch_win, stay, stay_win)


    result = "total %d times\n\tswitch %d times\n\t\twin %d times, p = %f\n\tstay %d times\n\t\twin %d times, p = %f" % (total, switch, switch_win, switch_win / switch, stay, stay_win, stay_win / stay) 
    print(result)

if __name__ == "__main__":
    main()
