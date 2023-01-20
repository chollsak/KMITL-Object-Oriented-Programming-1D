
def delete_minus(x):
    newlist = [[i for i in line if i >= 0] for line in x]
    return (newlist)

if __name__ == "__main__":
    x = [[1, -3, 2],[-8, 5],[-1, -4, -3]] 
    newlist = delete_minus(x)
    print(newlist)