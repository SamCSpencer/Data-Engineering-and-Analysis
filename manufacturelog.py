# Creates function that checks batch taken as "entry" and checks if
# it is in the proper fromat to be read and then reads it to assign
# the information it carries to a dictionary
def validate_and_extract_log(entry):

    # Intializing counter 0 to keep track of our place in the string
    j = 0
    # Creating list of batches
    batches = []

    # Creating a while loop to detect extra batches and create a new batch
    # j should be one greater than the length of the already read batches 
    # If there is another charchter then it will begin reading it as a new
    # batch and append it to the list of batches.  Therefore j should always
    # indicate the position of the first character in a batch.
    
    while j < len(entry):

        # Checking to make sure the string is sufficiently long enough to
        # Contain a complete batch
        if j+19 >= len(entry):
            return 'invalid'

        # Initialize variables for this batch
        batch_id = ""
        product_code = ""
        quantity = ""
        date = ""
    
        # Checking if first letter of string is B before moving 
        # on to extraction
        if entry[j] == 'B':   
            batch_id = entry[j+1:j+5]
    
            # Check if batch_id is a valid four digit id composed 
            # only of numbers by checking each number individually
            for value in batch_id:
                if value.isdigit() == False:
                    return 'invalid'
                    
            # Checking if sixth digit is an uppercase P
            if entry[j+5] == 'P':
                # Assigning the two characters following P to product code
                product_code = entry[j+6:j+8]
                
                # Checking if the two characte rs following P are uppercase
                # letters
                for char in product_code:
                    if char.isupper() == False:
                        return 'invalid'
                    
            # P Check failed, Ending function and returning 'invalid'
            else:
                return 'invalid'
    
            # Checking if ninth digit is an uppercase Q
            if entry[j+8] == 'Q':
                # Finding the number of digits between Q and D or the
                # first non-digit after D incase the batch is invalid 
                # due to lacking a D
                i = 9
                end_place = 0
                while entry[j+i].isdigit() == True:
                    after_quantity = entry[j+i+1]
                    end_place = j+i
                    i += 1
    
                # Checking to make sure there is at least 1 number after 
                # Q by checking if the while loop at least ran once and was
                # able to assign i to end_place
                if end_place == 0:
                    return 'invalid'
    
                # Checking that the next quantity was D
                if after_quantity == 'D':
                    # reading the quantity value from the entry between
                    # the values after Q and the found location of D
                    quantity = entry[j+9:end_place+1]

                    # Removing any leading 0's
                    quantity = quantity.lstrip('0')
                    
                    
                    # Reading date from the 8 places following D
                    date = entry[end_place+2:end_place+10]

                    # Checking that all values in date are numbers
                    for val in date:
                        if val.isdigit() == False:
                            return 'invalid'

                    # Checking that date has all 8 digits to signify a proper
                    # date
                    if len(date) != 8:
                        return 'invalid'

                    # Checking year, contained in first four characters of date,
                    # is between 2000 and 2099
                    year = int(date[0:4])
                    if 2000 > year or year > 2099:
                        return 'invalid'
                        
                    # Checking if month, contained in the 5th and 6th characters
                    # of date, are between 01 and 12
                    month = int(date[4:6])
                    if 1 > month or month > 12:
                        return 'invalid'

                    # Checking if day, contained in the 7th and 8th characters
                    # of date, are between 01 and 31
                    day = int(date[6:8])
                    if 1 > day or day > 31:
                        return 'invalid'
    
                # D Check failed, Ending function and returning 'invalid'
                else:
                    return 'invalid' 
                    
            # Q Check failed, Ending function and returning 'invalid'
            else:
                return 'invalid'   
    
        else:
            return('invalid')
            
        # Creates batch dictionary using the values we have saved throughout
        # our loop
        batch = {
            'Batch ID': batch_id,
            'Product Code': product_code,
            'Quantity': quantity,
            'Date': date
        }

        # Adding batch from current to the list of batches
        batches.append(batch)

        # Iterating j by the length of the last batch
        j += i+9

    # Checking to make sure the while loop ran at least once and that at least
    # one batch was read.
    if batches == []:
        return 'invalid'

    else:
        return batches
        
