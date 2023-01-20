def count_char_in_string(x,c):
    count_list = [i.count(c) for i in x] #[2 , 3, 1]
    return (count_list)
     
if __name__ == "__main__":
    x = ["abba", "babana", "ann"]
    c = 'a'
    a = count_char_in_string(x,c)
    print(a)