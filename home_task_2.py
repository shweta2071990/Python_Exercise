import random
import string

# Generate a list of random number (2–10) of dictionaries
dict_list = []  # list to store all generated dictionaries

# Choose random number of dictionaries
num_of_dicts = random.randint(2, 10)

for _ in range(num_of_dicts):
    # Random number of keys for each dict (1–10 letters)
    num_keys = random.randint(1, 10)
    
    # Randomly pick keys from alphabet without repetition
    keys = random.sample(string.ascii_lowercase, num_keys)
    
    # Create dict with random values (0–100)
    d = {k: random.randint(0, 100) for k in keys}
    
    dict_list.append(d)

print("Generated dicts:")
print(dict_list)

# Merge all dictionaries into one final result
result = {}  # final merged dictionary
key_tracker = {}  # to track max value and source dict index for each key

# Iterate through all dictionaries with index
for idx, d in enumerate(dict_list):
    for k, v in d.items():
        if k not in key_tracker:
            # First time seeing this key → record value and dict index
            key_tracker[k] = (v, idx + 1)  # store (value, dict_number)
        else:
            # Key exists → check if current value is greater than stored value
            if v > key_tracker[k][0]:
                key_tracker[k] = (v, idx + 1)

# Build final dictionary with renamed keys where duplicates existed
for k, (value, dict_index) in key_tracker.items():
    # Check how many dictionaries contain this key
    occurrences = sum(1 for d in dict_list if k in d)
    
    # If key appears in more than one dict → rename with dict index
    if occurrences > 1:
        result[f"{k}_{dict_index}"] = value
    else:
        result[k] = value

print("\nFinal merged dictionary:")
print(result)