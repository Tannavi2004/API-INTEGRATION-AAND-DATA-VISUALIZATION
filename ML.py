import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# B. Load and Clean Data
print("Loading dataset...")
df = pd.read_csv('spam.csv')
df.columns = ['label', 'message']
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
print("First 5 rows:\n", df.head())

# C. Preprocessing and Splitting
X = df['message']
y = df['label_num']
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# D. Train the Model
model = MultinomialNB()
model.fit(X_train, y_train)

# E. Evaluation
y_pred = model.predict(X_test)
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# F. Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# G. Predict New Messages
sample = ["Win a brand new car!", "Hey, are we still on for lunch?"]
sample_vector = vectorizer.transform(sample)
predictions = model.predict(sample_vector)

print("\nPredictions:")
for msg, label in zip(sample, predictions):
    result = "SPAM" if label == 1 else "HAM"
    print(f"Message: \"{msg}\" => {result}")