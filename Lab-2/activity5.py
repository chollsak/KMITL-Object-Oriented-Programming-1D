def is_alpha(char):
    if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z"):
        return True
    else:
        return False

def only_english(string1):
    s_list = [char for char in string1 if is_alpha(char)]
    new_str = "".join(map(str,s_list))
    return (new_str)

eng = only_english("haสวัสดีครับha123")
print(eng)