# Read number of entries
n = int(input().strip())

# Create phone book dictionary
phone_book = {}

# Read n entries
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    number = entry[1]
    phone_book[name] = number

# Process queries until EOF
while True:
    try:
        query = input().strip()
        if not query:  # Handle empty lines if any
            continue
            
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
