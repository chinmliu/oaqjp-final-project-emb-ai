import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)

        emotion_result = {}
        emotion_result["anger"] = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        emotion_result["disgust"] = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        emotion_result["fear"] = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        emotion_result["joy"] = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        emotion_result["sadness"] = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        max_emotion = max(emotion_result.values())
        for k, v in emotion_result.items():
            if v == max_emotion:
                emotion_result["dominant_emotion"] = k
                break 
    
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    return emotion_result