#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    dict = {"January": "01" , "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", 
            "August": "08", "September": "09", "October": "10", "November": "11", "December": "12" }
    
    return dict.get(month)
    

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    user_string = user_string.split()
    user_string[1] = user_string[1].replace(",",'')
    user_string[0] = parse_month(user_string[0])
    if len(user_string[1]) == 1:
        user_string[1] = "0" + user_string[1]
    
    return ("/").join(user_string)
    

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_string = input("Enter a date:")
    print(parse_date(user_string))
    
