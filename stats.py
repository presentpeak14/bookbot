def word_count(book_text):
    words = book_text.split()
    num_words = (len(words))
    return num_words

def char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts



def sort_on(counts):
    return counts["num"]
    
def sort_dict(counts):
    list_counts = []
    for key, value in counts.items():
        list_counts.append({"char":key, "num": value})
    list_counts.sort(reverse=True, key=sort_on)
    return list_counts