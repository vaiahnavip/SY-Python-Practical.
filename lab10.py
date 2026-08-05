
text = input("Enter a paragraph:")

characters = len(text)

spaces = text.count(" ")

words = len(text.split())

vowels = "aeiouAEIOU"
vowel_count = 0

for i in text:
    if i in vowels:
        vowel_count += 1

# Display results
print("\n***** Text Analysis *****")  
print("total characters :", characters)
print("total words      :", words)
print("total spaces     :", spaces)      
print("total vowels     :",vowel_count)

# Demonstrating indexing
if len(text) > 0:
    print("\nFirst Character (Indexing):", text[0])
    print("\nLast Character (Indexing):", text[-1])

# Demonstrating slicing
print("\nFirst 10 Characters (Slicing):", text[:10])
print("\nLast 10 Character (Slicing):", text[-10:])