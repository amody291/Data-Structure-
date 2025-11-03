# Linear Search Program

def linear_search(arr, key):
    """
    Performs linear search on the list `arr` to find `key`.
    Returns True if key is found, False otherwise.
    """
    for index, value in enumerate(arr):
        if value == key:
            return index  # return index of found key
    return -1  # key not found


# Main program
try:
    array = list(map(int, input("Enter the numbers (space-separated): ").split()))
    key = int(input("Enter the key to search for: "))

    result = linear_search(array, key)

    if result != -1:
        print(f"✅ Key {key} exists at index {result}.")
    else:
        print(f"❌ Key {key} does not exist in the list.")

except ValueError:
    print("⚠️ Invalid input! Please enter integers only.")
