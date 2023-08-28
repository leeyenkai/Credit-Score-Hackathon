def faceverify():
    import asyncio
    import io
    import glob
    import os
    import sys
    import time
    import uuid
    import requests
    import json
    from urllib.parse import urlparse
    from io import BytesIO
    from PIL import Image, ImageDraw
    from azure.cognitiveservices.vision.face import FaceClient
    from msrest.authentication import CognitiveServicesCredentials
    from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

    KEY = "640c776ecb64483fb7f60d929f1afb7d"
    ENDPOINT = "https://safecredithackathon.cognitiveservices.azure.com/face/v1.0/verify"
    ENDPOINT2 = "https://safecredithackathon.cognitiveservices.azure.com/face/v1.0/detect"

    #face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

        # CHANGE IMAGE PATH TO YOUR OWN USERNAME. 
        # NAME IS CASE SENSITIVE
    image_path1 = "C:/Users/Vina/Pictures/Picture2.jpg"
    image_path2 = "C:/Users/Vina/Pictures/Picture.jpg"

    headers = {'Content-Type': 'application/octet-stream', 
            'Ocp-Apim-Subscription-Key': KEY}
    data1 = open(image_path1, 'rb')
    response = requests.post(ENDPOINT2, headers=headers, data=data1)
    data2 = open(image_path2, 'rb')
    response1 = requests.post(ENDPOINT2, headers=headers, data=data2)

    result = response.json()
    result1 = response1.json()

    faceid1= str(result[0]['faceId'])
    faceid2= str(result1[0]['faceId'])

    headers1 = {'Ocp-Apim-Subscription-Key': KEY}
    body = { 'faceId1': faceid1, 'faceId2': faceid2}
    response3 = requests.post(url = ENDPOINT, headers = headers1, json = body)

    result3 = response3.json()
    identical = result3['isIdentical']
    confidence = result3['confidence']

    if __name__ == '__main__':
            print(faceid1)
            print(faceid2)

            print(identical)
            print(confidence)

            print(json.dumps(result3, indent=4))
    
    return identical, confidence


# Unit testing

if __name__ == '__main__':
    faceverify()