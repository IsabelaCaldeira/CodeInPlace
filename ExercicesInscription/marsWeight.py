
MARS_EQUIVALENT = 0.3783

def main():
    
    #We get the earth weight from the user
    earth_weight_str = input('Enter the weight on earth: ')
    
    #Let's cast the variable, it's not a spell! We are just changing the variable type!!
    earth_weight_float = float(earth_weight_str)
    
    #Now we can finally calculate mars_weight!
    mars_weight = earth_weight_float * MARS_EQUIVALENT
    
    #Casting the mars_weight into a str
    print('Here is the value of the equivalent weight in Mars: ' + str(mars_weight) + 'kg')
    
if __name__ == '__main__':
    main()
    