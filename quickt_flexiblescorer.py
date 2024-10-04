import pandas as pd
import matplotlib.pyplot as plt
from flexible_scorer import FlexibleScorer

if __name__ == "__main__":
    # Specify the criteria for scoring, such as "difficulty"
    criteria = "difficulty"
    scorer = FlexibleScorer(criteria)

    # Load the words CSV file
    words_df = pd.read_csv('./words.csv')

    # Extract words and definitions
    words = words_df['word']
    definitions = words_df['definition']

    # Initialize a list to store the scores
    scores = []

    # Iterate through each word and its corresponding definition
    for word, definition in zip(words, definitions):
        # Pass both word and definition to the scorer
        score = scorer.score(word, definition)  # Modify the scorer to accept both parameters
        scores.append((word, score))  # Append the word and its score as a tuple

    # Sort the words by their difficulty score (highest to lowest)
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Convert the sorted scores into a DataFrame
    df = pd.DataFrame(scores, columns=['Word', 'Difficulty'])

    # Plot the results using matplotlib
    plt.figure(figsize=(10, 6))
    plt.barh(df['Word'][:30], df['Difficulty'][:30], color='skyblue')  # Plot top 30 words for clarity
    plt.xlabel('Difficulty')
    plt.ylabel('Word')
    plt.title('Top 30 Words by Difficulty (With Definitions)')
    plt.gca().invert_yaxis()  # Invert y-axis to have highest difficulty on top
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig('word_difficulty_plot_with_definitions.png')

    # Show the plot
    plt.show()

    # Optionally, save the sorted results to a CSV file
    df.to_csv('sorted_words_by_difficulty_with_definitions.csv', index=False)

    # You can print the DataFrame to check the result
    print(df.head())

