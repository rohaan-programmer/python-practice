
"""
CS50 Python Practice: List and Dictionary Comprehensions
--------------------------------------------------------
Description:
This script reads text from 'address.txt', counts word frequencies,
and saves/processes the data into 'counts.csv' using dictionary comprehensions.
"""
import csv
import re


def get_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()
        words = re.findall(r"\b[a-z]+\b", text)

    return words


def save_counts(counts):
    with open("counts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])

        for word, count in counts.items():
            writer.writerow([word, count])


def main():
    words = get_words("address.txt")

    counts = {
        word: words.count(word)
        for word in words
    }

    save_counts(counts)


if __name__ == "__main__":
    main()