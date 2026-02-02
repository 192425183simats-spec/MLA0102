import math
from collections import Counter


def entropy(data):
    labels = [row[-1] for row in data]
    label_counts = Counter(labels)

    ent = 0
    total = len(labels)

    for count in label_counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent



def split_data(data, index, value):
    subset = []
    for row in data:
        if row[index] == value:
            reduced_row = row[:index] + row[index+1:]
            subset.append(reduced_row)
    return subset



def information_gain(data, index):
    total_entropy = entropy(data)

    feature_values = [row[index] for row in data]
    value_counts = Counter(feature_values)

    weighted_entropy = 0
    for value, count in value_counts.items():
        subset = split_data(data, index, value)
        weighted_entropy += (count / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy



def best_feature(data):
    gains = []
    for i in range(len(data[0]) - 1):
        gains.append(information_gain(data, i))
    return gains.index(max(gains))



def build_tree(data, features):
    labels = [row[-1] for row in data]

    # If all labels same → return label
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # If no more features
    if len(data[0]) == 1:
        return Counter(labels).most_common(1)[0][0]

    best = best_feature(data)
    best_feature_name = features[best]

    tree = {best_feature_name: {}}

    feature_values = set(row[best] for row in data)

    for value in feature_values:
        sub_features = features[:best] + features[best+1:]
        subset = split_data(data, best, value)
        tree[best_feature_name][value] = build_tree(subset, sub_features)

    return tree


features = ["Outlook", "Temperature", "Humidity", "Wind"]

data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]


decision_tree = build_tree(data, features)

print("Decision Tree:")
print(decision_tree)
