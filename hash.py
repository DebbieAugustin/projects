import hashlib
import random

def hash_word(word, salt):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Add the salt to the word
    salted_word = word + salt

    # Update the hash object with the salted word's bytes
    sha256_hash.update(salted_word.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_word = sha256_hash.hexdigest()

    return hashed_word

if __name__ == "__main__":
    try:
        input_word = input("Enter a word to hash: ")
        salt = str(random.randint(1, 10000))  # Generate a random salt
        hashed_word = hash_word(input_word, salt)

        print("Salt:", salt)
        print("Hashed word:", hashed_word)
    except Exception as e:
        print("An error occurred:", e)
