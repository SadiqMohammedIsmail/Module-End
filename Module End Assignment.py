"""
Survey Feedback Analyzer
Author: Student
Assignment Solution
"""

# Step 1: Preloaded Feedbacks (Given Data)
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

def clean_text(text):
    """
    Cleans a text string according to Step 3 guidelines:
    - Removes punctuation (., !, ?, ,)
    - Replaces multiple spaces with a single space
    - Removes leading/trailing spaces
    - Converts text to lowercase
    """
    # Convert to lowercase first
    text = text.lower()
    
    # Remove specified punctuation characters
    for punc in ['.', ',', '!', '?']:
        text = text.replace(punc, '')
        
    # Split by spaces and join back using a single space to clean whitespace issues
    words = text.split()
    cleaned_text = ' '.join(words)
    
    return cleaned_text

def count_word_in_feedbacks(word):
    """
    Counts how many feedbacks contain the specific word (case-insensitive).
    """
    target_word = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        # Ensure exact word matching by splitting the cleaned feedback into words
        cleaned_fb = clean_text(fb)
        if target_word in cleaned_fb.split():
            count += 1
    return count

def main():
    print("--- Step 2: Add More Feedbacks ---")
    try:
        num_new = int(input("How many more feedbacks do you want to add? "))
    except ValueError:
        print("Invalid input. Proceeding with 0 additional feedbacks.")
        num_new = 0

    current_s_no = 11
    for i in range(num_new):
        print(f"\nEntering details for feedback #{i+1}:")
        name = input("Enter Name: ")
        fb_text = input("Enter Written Feedback: ")
        try:
            rating = int(input("Enter Rating (1–5): "))
            if rating < 1 or rating > 5:
                print("Rating out of bounds. Defaulting to 3.")
                rating = 3
        except ValueError:
            print("Invalid rating input. Defaulting to 3.")
            rating = 3

        # Append data
        feedback_data['S_No'].append(current_s_no)
        feedback_data['Name'].append(name)
        feedback_data['Feedback'].append(fb_text)
        feedback_data['Rating'].append(rating)
        current_s_no += 1

    print("\n--- Step 3: Text Cleaning ---")
    # Apply cleaning to all feedback entries
    cleaned_feedbacks = [clean_text(fb) for fb in feedback_data['Feedback']]
    feedback_data['Feedback'] = cleaned_feedbacks
    print("Feedback text cleaning complete.")

    print("\n--- Step 4: Word Count Insights ---")
    print(f"Number of feedbacks containing 'good': {count_word_in_feedbacks('good')}")
    print(f"Number of feedbacks containing 'poor': {count_word_in_feedbacks('poor')}")
    print(f"Number of feedbacks containing 'excellent': {count_word_in_feedbacks('excellent')}")

    print("\n--- Step 5: Final Summary & Insights ---")
    print("Cleaned feedback_data Dictionary:")
    print(feedback_data)

    # Average Rating
    total_ratings = sum(feedback_data['Rating'])
    count_ratings = len(feedback_data['Rating'])
    avg_rating = total_ratings / count_ratings if count_ratings > 0 else 0
    print(f"\nAverage Rating: {avg_rating:.2f}")

    # Longest comment (by word count)
    longest_fb = ""
    max_words = -1
    for fb in feedback_data['Feedback']:
        word_count = len(fb.split())
        if word_count > max_words:
            max_words = word_count
            longest_fb = fb
    print(f"Feedback with the longest comment: \"{longest_fb}\" ({max_words} words)")

    # Unique words across all feedbacks
    unique_words = set()
    for fb in feedback_data['Feedback']:
        unique_words.update(fb.split())
    print(f"List of unique words used: {list(unique_words)}")

    print("\n--- (Optional): Sort Feedbacks by Rating ---")
    # Zip elements together, sort by rating descending, and unpack
    zipped_data = zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    )
    sorted_data = sorted(zipped_data, key=lambda x: x[3], reverse=True)

    print(f"{'S_No':<6} | {'Name':<10} | {'Rating':<6} | {'Feedback'}")
    print("-" * 60)
    for row in sorted_data:
        print(f"{row[0]:<6} | {row[1]:<10} | {row[3]:<6} | {row[2]}")

if __name__ == '__main__':
    main()
