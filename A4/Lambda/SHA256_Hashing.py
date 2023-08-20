import hashlib
import json
import urllib3


def lambda_handler(event, context):

    # Retrieve the input JSON from the 'input' key
    input_data = event['action']

    course_uri = event['course_uri']
    # Extract the value of the key "value" from the input JSON
    value = event['value']

    # Perform SHA256 hashing
    hashed_value = hashlib.sha256(value.encode('utf-8')).hexdigest()

    # Prepare the response
    response = {
        'banner': "B00936916",
        'result': hashed_value,
        'arn': context.invoked_function_arn,
        'action': 'sha256',
        'value': value
    }

    # Send the POST request to the course_uri
    try:
        http = urllib3.PoolManager()
        headers = {'Content-Type': 'application/json'}
        encoded_response = json.dumps(response).encode('utf-8')
        r = http.request('POST', course_uri, body=encoded_response, headers=headers)
        r_status = r.status
        if r_status == 200:
            return response
        else:
            # Handle the case when the POST request fails
            return {
                'statusCode': r_status,
                'body': f'POST request failed with status code {r_status}'
            }
    except Exception as e:
        # Handle any other exceptions that may occur during the request
        return {
            'statusCode': 500,
            'body': f'Error sending POST request: {str(e)}'
        }