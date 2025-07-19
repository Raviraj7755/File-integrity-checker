import hashlib

def calculate_file_hash(filename):
    hasher = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Change 'sample.txt' to your file name
filename = 'sample.txt'
hash_value = calculate_file_hash(filename)
print(f"The SHA-256 hash of the file is: {hash_value}")

with open('hash.txt', 'w') as h:
    h.write(hash_value)