
# regular expressions 
import re

# load file 
file_to_load = "raw_data/paragraph_2.txt"
file_to_output = "analysis/paragraph_analysis.txt"

# String variable to hold the parag
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string 
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph 
word_split = paragraph.split(" ")
word_count = len(word_split)

# Create a list 
letter_counts = []

# Loop through the word 
for word in word_split:

    # Add letter count list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# split the paragraph based on punctuation
sentence_split = re.split("(?<=[.!?]) +", paragraph)

print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence 
for sentence in sentence_split:

    # Calculate the number of words in each sentence 
    words_per_sentence.append(len(sentence.split(" ")))

# Calculate the avg word count 
avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))

# Paragraph Analysis Output
output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

# Print the results 
print(output)

# Save the results to analysis 
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)
 