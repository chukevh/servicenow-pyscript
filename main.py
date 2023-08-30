import requests

# ServiceNow instance URL and API endpoint for incidents
instance_url = "https://your-instance.service-now.com"
incident_endpoint = "/api/now/table/incident"

# Replace with your ServiceNow credentials
username = "your_username"
password = "your_password"

# Set up the request headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Construct the URL for the incident API
url = instance_url + incident_endpoint

# Perform basic authentication
auth = (username, password)

# Make the API request
response = requests.get(url, headers=headers, auth=auth)

# Check if the request was successful
if response.status_code == 200:
    incidents_data = response.json()
    # Process and use the incidents_data as needed
    for incident in incidents_data['result']:
        print("Incident Number:", incident['number'])
        print("Description:", incident['short_description'])
        print("Priority:", incident['priority'])
        print("State:", incident['state'])
        print("=" * 40)
else:
    print("Error:", response.status_code)
    print("Response:", response.text)