name_age = input("Please enter your name and age:")
for i in range(len(name_age)):
    if name_age[i] in '01023456789':
        name = name_age[: i - 1]
        age = name_age[i - 1 :]
print (name.rstrip() + ', you will be 100 years old in ' + str(100 - int(age)) + ' years.')

        
        

