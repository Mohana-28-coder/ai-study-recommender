# Simple AI Study Recommender

topics = [
    "calculus",
    "algebra",
    "machine learning",
    "data structures",
    "neural networks",
    "probability"
]

def recommend_topic(user_input):
    recommendations = []
    
    for topic in topics:
        if user_input.lower() in topic:
            recommendations.append(topic)
    
    if not recommendations:
        return ["Try basic mathematics", "Start with fundamentals"]
    
    return recommendations

# Example
user_input = input("Enter a topic: ")
result = recommend_topic(user_input)

print("Recommended topics:")
for r in result:
    print("-", r)
