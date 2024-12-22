def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive_ratings = sum(1 for rating in ratings if rating == 4 or rating == 5)
    positive_percentage = (positive_ratings / len(ratings)) * 100
    return f"Positive Feedback Percentage: {positive_percentage:.2f}%"
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback_percentage(ratings))
