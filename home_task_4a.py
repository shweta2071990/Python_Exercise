import random
import string

# ---------------------------
# Helpers (Functional Style)
# ---------------------------

def generate_random_dict(num_keys):
    """Generate one dictionary with random letters and random int values."""
    keys = random.sample(string.ascii_lowercase, num_keys)
    return {k: random.randint(0, 100) for k in keys}


def generate_dict_list():
    """Generate list of random dictionaries (2–10)."""
    num_of_dicts = random.randint(2, 10)
    return [generate_random_dict(random.randint(1, 10)) for _ in range(num_of_dicts)]


def build_key_tracker(dict_list):
    """Track max value and dict index for each key."""
    tracker = {}
    for idx, d in enumerate(dict_list):
        for k, v in d.items():
            if k not in tracker or v > tracker[k][0]:
                tracker[k] = (v, idx + 1)
    return tracker


def count_key_occurrences(dict_list, key):
    """Count how many dicts contain a given key."""
    return sum(1 for d in dict_list if key in d)


def build_final_dict(dict_list, tracker):
    """Build final merged dictionary according to the rules."""
    result = {}
    for k, (value, dict_index) in tracker.items():
        if count_key_occurrences(dict_list, k) > 1:
            result[f"{k}_{dict_index}"] = value
        else:
            result[k] = value
    return result


# ---------------------------
# Main logic
# ---------------------------

def process_dict_homework():
    dict_list = generate_dict_list()
    tracker = build_key_tracker(dict_list)
    final_dict = build_final_dict(dict_list, tracker)
    return dict_list, final_dict


# Run
generated, merged = process_dict_homework()

print("Generated dict list:")
print(generated)
print("\nMerged final dictionary:")
print(merged)