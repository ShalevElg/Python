import sys
from collections import Counter

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = file.read().split()
            return Counter(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: N must be an integer.")
        sys.exit(1)

    filename = "text_file.txt"  # ניתן להחליף את שם הקובץ לשם המתאים
    word_count = count_words(filename)

    # מיון המילים לפי מספר המופעים בסדר יורד
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # הדפסת N המילים הנפוצות ביותר
    print(f"Top {n} words:")
    for i in range(min(n, len(sorted_word_count))):
        word, count = sorted_word_count[i]
        print(f"{word}: {count} occurrences")

if __name__ == "__main__":
    main()
