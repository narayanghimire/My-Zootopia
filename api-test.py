import requests

# Your API key
api_key = 'v/YVo/vVlM0tlv9Gvq8pRA==JpfSpoX6EqKRqFIH'

# Define the URL you want to request
url = 'https://api.api-ninjas.com/v1/animals?name=cheetah'  # Replace 'example' with the specific endpoint you want to access

# Define the headers with the API key
headers = {
    'X-Api-Key': api_key
}

# Send the GET request
response = requests.get(url, headers=headers)

# Print the HTML or JSON response
print(response.text)  # Use response.json() if you expect JSON data
