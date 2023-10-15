import requests
import json

SERVER_URL = "http://127.0.0.1:5000"

class MyAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_data(self, data):
        url = f"{SERVER_URL}/send_data"
        headers = {'Content-Type': 'application/json'}
        payload = {'api_key': self.api_key, 'data': data}

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                print("Data sent successfully.")
            else:
                print("Error sending data. Status code:", response.status_code)
        except Exception as e:
            print("Error:", str(e))

    def get_data(self, data_key):
        url = f"{SERVER_URL}/send_data/{data_key}"
        headers = {'Content-Type': 'application/json'}
        data = {'api_key': self.api_key}
        try:
            response = requests.get(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                print("Data received successfully.")
                return response.json()  # You might want to return the data instead of just printing
            else:
                print("Error receiving data. Status code:", response.status_code)
        except Exception as e:
            print("Error:", str(e))

    def upload_csv(self, csv_file_path):
        url = f"{SERVER_URL}/upload_csv/{self.api_key}"

        try:
            with open(csv_file_path, 'rb') as csv_file:
                files = {'csv_file': csv_file}
                response = requests.post(url, files=files)

                if response.status_code == 200:
                    print("CSV file uploaded successfully.")
                else:
                    print("Error uploading CSV file. Status code:", response.status_code)
        except IOError as e:
            print("Error reading CSV file:", str(e))
