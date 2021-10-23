import base64
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function b64 encode data')

    data = req.params.get('data')
    operation = req.params.get('op')


    if (not data) or (not operation):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get('data')

    if data:
        if operation == 'enc':
            message = data
            ascii_bytes = message.encode('ascii')
            base64_encoded = base64.b64encode(ascii_bytes)
            base64_encoded_string = base64_encoded.decode('ascii')
            
            return func.HttpResponse(f"Howdy 🍕! Your encoded data is {base64_encoded_string}!🌟")

        elif operation == 'dec':
            message = data
            ascii_bytes = message.encode('ascii')
            base64_decoded = base64.b64decode(ascii_bytes)
            base64_decoded_string = base64_decoded.decode('ascii')

            return func.HttpResponse(f"Howdy 🍕! Your decoded data is {base64_decoded_string}!🌟")
        
        elif not operation:
            return func.HttpResponse("Set 'op' param value please")

        else:
            return func.HttpResponse(
             "Please ensure that both query parameters are correct",
             status_code=200
            )
    else:
        return func.HttpResponse(
             "Welcome to HTTP triggered Azure function 🍟 for base64 operations. \n\nWhat is Base64 encoding?\nBase64 encoding schemes are commonly used when there is a need to encode binary data that needs to be stored and transferred over media that are designed to deal with ASCII. \n\nHow to use?\nPass a 'data' and an 'op' ( 'enc' for encode / 'dec' for decode ) parameter in the query string.\n\nExample request \nEncoding : https://base64club.azurewebsites.net/api/hellohttp?data=HelloAzure&op=enc\nDecoding : https://base64club.azurewebsites.net/api/hellohttp?data=SGVsbG9BenVyZQ==&op=dec",
             status_code=200
        )
