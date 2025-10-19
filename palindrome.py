def is_palindrome(text):
    # Normalize the text (e.g., remove spaces and convert to lowercase)
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    
    # Check if the text equals its reverse
    return clean_text == clean_text[::-1]

# Example Usage
word1 = "level"
word2 = "Hello"
phrase = "A man, a plan, a canal: Panama"

print(f"'{word1}' is palindrome: {is_palindrome(word1)}")      # True
print(f"'{word2}' is palindrome: {is_palindrome(word2)}")      # False
print(f"'{phrase}' is palindrome: {is_palindrome(phrase)}")    # True
