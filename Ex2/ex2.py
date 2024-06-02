# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

import re
import time
from typing import Counter
import numpy as np


def count_words(file_name):
    with open(file_name, "r") as file:
        text = file.read().lower()
        words = re.findall(r"\b\w+\b", text)
        word_counts = Counter(words)
        return word_counts


def print_top_words_without_numpy(word_counts, n=100):
    for word, count in word_counts.most_common(n):
        print(f"{word}: {count}")


def print_top_words_with_numpy(word_counts, n=100):
    words = np.array(list(word_counts.keys()))
    counts = np.array(list(word_counts.values()))
    sorted_indices = np.argsort(counts)[::-1]
    sorted_words = words[sorted_indices]
    sorted_counts = counts[sorted_indices]
    for i in range(min(n, len(sorted_words))):
        print(f"{sorted_words[i]}: {sorted_counts[i]}")


def resolve():
    file_name = "Ex2/story.txt"
    word_counts = count_words(file_name)
    print("-----Welcome to the AI Menu!-----")
    print("1. Run exercise not numpy")
    print("2. Run exercise with numpy")
    print("3. Quit")
    print("-----Welcome to the AI Menu!-----")
    while True:
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
        else:
            start_run_time = time.time()
            if choice == "1":
                print_top_words_without_numpy(word_counts)
                print("Time taken: ", (time.time() - start_run_time) * 1000, "ms")
            elif choice == "2":
                print_top_words_with_numpy(word_counts)
                print("Time taken: ", (time.time() - start_run_time) * 1000, "ms")
            else:
                print("Goodbye!")
                break
