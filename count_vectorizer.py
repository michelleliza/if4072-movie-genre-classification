def count_vectorizer(all_doc_words):
    bag_of_words = set()
    for doc in all_doc_words:
        for word in doc:
            bag_of_words.add(word)

    bag_of_words = list(bag_of_words)
    bag_of_words.sort()

    vectorize_doc = []
    for doc in all_doc_words:
        temp_vectorize_doc = []
        for word in bag_of_words:
            temp_vectorize_doc.append(doc.count(word))
        vectorize_doc.append(temp_vectorize_doc)

    return vectorize_doc
    
documents = ["It was the best of times best",
"It was the worst of times",
"It was the age of wisdom wisdom",
"It was the age of foolishness"]

all_doc_words = []
for doc in documents:
    all_doc_words.append([w.lower() for w in doc.split(" ")])

vectorize_doc = count_vectorizer(all_doc_words)
print(vectorize_doc)
