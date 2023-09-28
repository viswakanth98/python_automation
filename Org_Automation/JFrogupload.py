import requests

def JFrogupload():
    #Define the URL, file path and authentication
    url = "http://100.25.146.180:8082/ui/repos/tree/General/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    file_path= "/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = "admin"
    password = "Welcome@2024"
    
    # Send the put request
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password))
        
    #check the response status code
    if response.status_code ==201:
        print("PUT response was successful")
    else:
        print("PUT request failed with status code {response.status_code}")
        print("Response Content: ")
        print(response.text)
