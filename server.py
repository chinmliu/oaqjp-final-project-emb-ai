''' import all the modules
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows all the score for all emotions
        along with the dominant emotion
    '''

    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominate = response["dominant_emotion"]

    # Check if the label is None, indicating an error or invalid input
    if dominate is None:
        return "Invalid text! Try again!"

    # Return a formatted string with the sentiment label and score
    return (f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, "
        f"'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominate}.")


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
