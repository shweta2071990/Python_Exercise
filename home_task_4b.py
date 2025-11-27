def split_sentences(text):
    """Split text into sentences using '.'."""
    parts = text.split(".")
    return [p.strip() for p in parts if p.strip()]


def normalize_sentence_case(sentence):
    """Convert to sentence case."""
    sentence = sentence.lower()
    return sentence[0].upper() + sentence[1:]


def normalize_text(sentences):
    """Normalize all sentences."""
    return [normalize_sentence_case(s) + "." for s in sentences]


def fix_iz(text):
    """Fix ' iz ' → ' is ' only when lowercase."""
    return text.replace(" iz ", " is ")


def get_last_words(sentences):
    """Extract last word of every sentence."""
    last_words = []
    for s in sentences:
        words = s.split()
        last_words.append(words[-1].rstrip("."))
    return last_words


def build_new_sentence(last_words):
    """Build new sentence from last words."""
    return (" ".join(last_words)).capitalize() + "."


def count_whitespaces(text):
    """Count ALL whitespace characters."""
    return sum(1 for ch in text if ch.isspace())


# ---------------------------
# Main logic
# ---------------------------

def process_string_homework(text):
    sentences = split_sentences(text)
    normalized = normalize_text(sentences)
    
    normalized_text = " ".join(normalized)
    corrected_text = fix_iz(normalized_text)
    
    final_sentences = split_sentences(corrected_text)
    last_words = get_last_words(final_sentences)
    new_sentence = build_new_sentence(last_words)
    
    final_paragraph = corrected_text + " " + new_sentence
    whitespace_total = count_whitespaces(text)
    
    return final_paragraph, whitespace_total


# Run
text = """  
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

final_text, whitespaces = process_string_homework(text)

print("Final processed text:\n")
print(final_text)
print("\nWhitespace count:", whitespaces)