import pandas as pd
import spacy

nlp = spacy.load("en_core_web_md")

# Convert file to DataFrame for efficiency.
with open("movies.txt", "r", encoding="utf-8") as f:
    movies_df = pd.DataFrame([line.strip().split(" :") for line in f], columns=["Movies", "Descriptions", "Rating"])

# Filter out stop and punctuation and lemmatise each token.
def preprocess(text):
    return ' '.join([token.lemma_.lower() for token in nlp(text) if not token.is_punct and not token.is_stop])

# Create column to store processed version of descriptions.
movies_df['processed_descrip'] = movies_df['Descriptions'].apply(preprocess)
# Create column to store doc version of pre processed descriptions.
movies_df['doc'] = movies_df["processed_descrip"].apply(lambda sample: nlp(sample))

# Recommendation based on top 5 similarites.
def recommendation(input_descrip, user_age, n_recommendations=5):
    
    # Preprocess and prepare input descriptions.
    input_doc = nlp(preprocess(input_descrip))

    # Calculate similarity.
    movies_df['similarity'] = movies_df['doc'].apply(lambda sample: input_doc.similarity(sample))

    # Filter movies based on user age.
    movies_df['age_sorted'] = movies_df['Rating'].astype(int) <= user_age

    # Filter movies based on age and select top recommendations.
    recommendations = movies_df[movies_df['age_sorted']].nlargest(n=n_recommendations, columns='similarity')

    # Returns based on top 5 highest similarity scores.
    return recommendations[['Movies', 'similarity']]

print(recommendation("Superman", 16))
