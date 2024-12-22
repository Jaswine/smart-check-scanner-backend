
def process_recommendations(text):
    recommendations = text.split('*')

    formatted_recommendations = ""
    for recommendation in recommendations:
        recommendation = recommendation.strip()
        if recommendation:
            if ':' in recommendation:
                formatted_recommendation = f"<p><b>{recommendation}</b></p>"
                formatted_recommendations += formatted_recommendation
            else:
                formatted_recommendation = f"<p>{recommendation}</p>"
                formatted_recommendations += formatted_recommendation

    formatted_recommendations = hashteg_recommendations(formatted_recommendations)

    return formatted_recommendations

def hashteg_recommendations(text):
    recommendations = text.split('##')

    formatted_recommendations = ""
    for recommendation in recommendations:
        recommendation = recommendation.strip()
        if recommendation:
            formatted_recommendation = f"<div>{recommendation}</div>"
            formatted_recommendations += formatted_recommendation

    return formatted_recommendations