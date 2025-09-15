import hashlib 

#variable for my input string 
input_string = "hello world"

# Create a SHA-256 hash object and updtate it with the input string
hash_object = hashlib.sha256(input_string.encode('utf-8'))
# Get the hexadecimal representation of the hash7h6
sha256_hash = hash_object.hexdigest()

# Print the hexadecimal representation of the hash
print(f"SHA-256 hash of '{input_string}': {sha256_hash}")
























