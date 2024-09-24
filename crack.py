import random

# Path to bip39.txt file
BIP39_FILE_PATH = 'bip39.txt'

# Read BIP39 words from file
def load_bip39_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# Generate a list of random phrases
def generate_random_phrases(words, num_phrases=5, num_words=12):
    return [' '.join(random.sample(words, num_words)) for _ in range(num_phrases)]

if __name__ == "__main__":
    # Load words and generate 5 random 12-word phrases
    bip39_words = load_bip39_words(BIP39_FILE_PATH)
    phrases = generate_random_phrases(bip39_words)

    # Print each generated phrase
    for idx, phrase in enumerate(phrases, 1):
        print(f"\n\n{phrase}")
