# Original text
text = """  
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# -------------------------------
# 1️⃣ NORMALIZE CASE
# -------------------------------
# Split text into sentences using ".", "!", "?"
sentences = text.split(".")
clean_sentences = []

for s in sentences:
    s = s.strip()
    if s:
        s = s.lower()                      # all lowercase first
        s = s[0].upper() + s[1:]           # sentence case
        clean_sentences.append(s + ".")    # add period back

# Join cleaned sentences into a paragraph
normalized_text = " ".join(clean_sentences)

# -------------------------------
# 2️⃣ FIX "iz" ONLY WHEN WRONG
# -------------------------------
# Rule: replace " iz " with " is "
normalized_text = normalized_text.replace(" iz ", " is ")

# -------------------------------
# 3️⃣ CREATE SENTENCE WITH LAST WORDS
# -------------------------------
sentences2 = normalized_text.split(".")
last_words = []

for s in sentences2:
    s = s.strip()
    if s:
        words = s.split()
        last_words.append(words[-1])

new_sentence = " ".join(last_words).capitalize() + "."

# Add new sentence to the paragraph
final_text = normalized_text + " " + new_sentence

# -------------------------------
# 4️⃣ COUNT ALL WHITESPACES
# -------------------------------
whitespace_count = 0
for ch in text:
    if ch.isspace():
        whitespace_count += 1

# -------------------------------
# OUTPUT
# -------------------------------
print("Final Text:\n")
print(final_text)
print("\nTotal whitespace characters:", whitespace_count)