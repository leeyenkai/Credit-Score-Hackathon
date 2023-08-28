#SET IN TERMINAL:
#setx COMPUTER_VISION_SUBSCRIPTION_KEY 4f666ad596814a61aa4a420cfad9b190
#setx COMPUTER_VISION_ENDPOINT https://safecreditpolyfintech.cognitiveservices.azure.com/
#RESTART TO TAKE EFFECT

#pip install --upgrade azure-cognitiveservices-vision-computervision
#pip install Pillow
def verifyAPI():
    import json
    import os
    import sys
    import requests
    import time
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    from PIL import Image
    from io import BytesIO

    #USE THIS IF SETERROR IS THROWN:
    #os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY'] = '28636b9eb98942cc95f7c5cbf54bc92c'
    #os.environ['COMPUTER_VISION_ENDPOINT'] = 'https://safecredit.cognitiveservices.azure.com/'

    missing_env = False
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()
    # Add your Computer Vision endpoint to your environment variables.
    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    else:
        print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    else:
        print("From Azure Cogntivie Service, retrieve your endpoint and subscription key.")
        print("\nSet the COMPUTER_VISION_ENDPOINT environment variable, such as \"https://westus2.api.cognitive.microsoft.com\".\n")
        missing_env = True

    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("From Azure Cogntivie Service, retrieve your endpoint and subscription key.")
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable, such as \"1234567890abcdef1234567890abcdef\".\n")
        missing_env = True

    if missing_env:
        print("**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    # Change Image path to your own image
    text_recognition_url = endpoint + "/vision/v3.0/read/analyze"
    image_path = "C:/Users\Vina/Pictures/NRIC.jpg" 
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = requests.post(text_recognition_url, headers=headers, data = image_data)

    response.raise_for_status()

    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        
        time.sleep(1)
        if ("analyzeResult" in analysis):
            poll = False
        if ("status" in analysis and analysis['status'] == 'failed'):
            poll = False

    polygons = []
    if ("analyzeResult" in analysis):
        # Extract the recognized text, with bounding boxes.
        polygons = [(line["boundingBox"], line["text"])
                    for line in analysis["analyzeResult"]["readResults"][0]["lines"]]

    Vname = analysis['analyzeResult']['readResults'][0]['lines'][5]['text']
    Vdob = analysis['analyzeResult']['readResults'][0]['lines'][12]['text']

    # Display the image and overlay it with the extracted text.
    image = Image.open(BytesIO(image_data))
    ax = plt.imshow(image)
    for polygon in polygons:
        vertices = [(polygon[0][i], polygon[0][i+1])
                    for i in range(0, len(polygon[0]), 2)]
        text = polygon[1]
        patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='y')
        ax.axes.add_patch(patch)
        plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top")
    
    if __name__ == '__main__':
        plt.show()
        print(json.dumps(analysis, indent=4))

        print(Vname)
        print(Vdob)
    
    return Vname,Vdob
    
# unit testing    

if __name__ == '__main__':
    verifyAPI()