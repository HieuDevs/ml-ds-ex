# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

from collections import deque, defaultdict

graph = defaultdict(list)


def build_graph(words):
    graph = defaultdict(list)
    for word in words:
        key = word[:2]
        graph[key].append(word)
    return graph


def load_words_and_build_graph(file_path):
    with open(file_path, "r") as file:
        words = {line.strip() for line in file}
    return ([word for word in words if len(word) >= 3], build_graph(words))


def find_shortest_chain(start_word, end_word):
    words, graph = load_words_and_build_graph("Ex1/wordsEn.txt")
    if start_word == end_word:
        return [start_word]
    if end_word not in words:
        return None
    queue = deque([(start_word, [start_word])])
    visited = set()
    print("...Finding the shortest chain...")
    while queue:
        current_word, path = queue.popleft()
        if current_word in visited:
            continue
        visited.add(current_word)

        if current_word == end_word:
            return path

        next_key = current_word[-2:]
        for next_word in graph.get(next_key, []):
            if next_word not in visited:
                queue.append((next_word, path + [next_word]))

    return None


def resolve():
    start_word = input("Enter the first word: ").strip()
    end_word = input("Enter the second word: ").strip()

    chain = find_shortest_chain(start_word, end_word)

    if chain:
        print("The shortest chain is:", " -> ".join(chain))
    else:
        print("No chain is found between the 2 words.")
