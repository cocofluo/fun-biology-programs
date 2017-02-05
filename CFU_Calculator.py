#Kelsey Coyne
#A program that calculates the number of colony forming units, based on plated dilutions
#Just for funsies
#And also because I don't like doing math.

#Logic: extrapolate the CFU/ml of original concentration based on the data we have from each dilution
#Then average the CFU/ml.

print 20*'*', 'Welcome to the Colony Forming Units Calculator!', 20*'*'
print ''
print 'This program uses the following steps to determine CFU/ml from serial dilutions and plates: '
print "Each dilution's two plates are averaged, then multiplied by the amount they were diluted by to get the original concentration."
print "If you include data from multiple dilutions, the values will be averaged to determine the final CFU/ml value."
print ''
print 'Please enjoy this program, and remember: Make sure to only enter values that are in an adequate range for calulating Colony Forming Units!'
print 'This is between 20 and 300 units!'
print ''
print ''
print 29*'*', 'COLONY FORMING UNITS CALCULATOR', 29*'*' 
print ''
   
def Plate_Dictionary(any_answer):    
#This dictionary takes in the values and if there is already a key in the dictionary for dilution, averages the two values.
#Because we should probably average the plate values before we do the equation, right?

    ans1 = any_answer.lower()
    any_plate_dict = {}
    while ans1 == 'yes':
        dilution = float(raw_input('Enter dilution of plate: 10^-'))
        CFU = float(raw_input('Enter Colony Forming Units: '))
        if dilution in any_plate_dict:
            CFU1 = any_plate_dict.get(dilution)
            any_plate_dict[dilution] = (CFU1 + CFU)/2
        else:
            any_plate_dict[dilution] = CFU
            print 'New dilution added!'
        ans2 = raw_input('Do you have plates to input? ')
        ans1 = ans2.lower()    
    else:
        print ''
        print "Dilution and CFU values are", any_plate_dict
    return  any_plate_dict 

def Undilute(any_dictionary, dilution):
#This function scales up the CFU to the original concentration.
    CFU = any_dictionary.get(dilution)
    CFU_value = CFU*(10**dilution)
    CFU_per_ml = CFU_value
    return CFU_per_ml    

def Average_Plates(any_CFU_dictionary):
#This function averages the number of CFU among all plates.
    plate_count_list = any_CFU_dictionary.values()
    sum_plates = sum(plate_count_list)
    length_list = len(plate_count_list)
    average_plates = sum_plates/length_list
    return average_plates

def main():
    ans = raw_input('Do you have plates to input? ') 
    plate_dict = Plate_Dictionary(ans)
    CFU_dictionary = {}
    for dilution in plate_dict:
        CFU_value = Undilute(plate_dict, dilution)
        CFU_dictionary[dilution] = CFU_value
    print ''
    print "Each dilution's CFU/ml are: ", CFU_dictionary
    CFU_Average = Average_Plates(CFU_dictionary)
    Rounded_CFU_Average = round(CFU_Average, -((len(str(CFU_Average)))-4))
    print ''
    print 'Averaged CFU/ml is: ', int(Rounded_CFU_Average) 
    print("Or {:.2e}".format(Rounded_CFU_Average))
    return  

main()
    
