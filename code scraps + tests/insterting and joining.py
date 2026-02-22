nums = ["1","2","3","4","5","6"]
nums.insert(2, "-")  # puts - at index 2 without replacing
nums.insert(5, "-")  # puts - at index 5 without replacing
print(nums)
jnums = ''.join(nums)  # converts list into one string with nothing between each value
print(jnums)
