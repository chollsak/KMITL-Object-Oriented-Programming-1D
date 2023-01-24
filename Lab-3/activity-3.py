
def is_plusone_dictionary(d):
    limit = 2
    previous_value = 1e9
    for key, value in d.items():
        if  previous_value + 1 != key or key + 1 != value :
            limit -= 1
        
        if limit == 0 : 
            return False

        previous_value = value
    
    return True

d = {1 : 2, 3 : 4, 5 : 6}
print(is_plusone_dictionary(d))