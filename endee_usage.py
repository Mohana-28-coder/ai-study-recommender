# Simulated Endee Usage Example

# Sample dataset (topics)
topics = [
    "calculus", "algebra", "machine learning",
    "data structures", "neural networks", "probability"
]

# Simulate storing in Endee (vector DB)
database = {}

def store_in_endee(topic):
    # Fake embedding (for demo)
    embedding = [ord(c) for c in topic]
    database[topic] = embedding

def search_in_endee(query):
    results = []
    for topic in database:
        if query.lower() in topic:
            results.append(topic)
    return results

# Store topics
for t in topics:
    store_in_endee(t)

# Search
query = input("Enter topic: ")
results = search_in_endee(query)

print("Results from Endee:")
for r in results:
    print("-", r)
