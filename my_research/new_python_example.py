#hello I am example of python 3.9 script
d1 = {"x": 1, "y": 4, "z": 10}
print(f"one dict: {d1}")
d2 = {"a": 7, "b": 9, "x": 5}
print(f"second dict: {d2}")
merged_dict =  d1|d2 #new merging, amazing!
new_f_string = f"there is this amazing new merging d1|d2 and fstrings are also there {merged_dict}"
print(new_f_string) 
