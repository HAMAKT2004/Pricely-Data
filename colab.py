import requests

def run_colab():
    notebook_url = "https://colab.research.google.com/drive/YOUR_NOTEBOOK_ID"
    response = requests.get(notebook_url)

    if response.status_code == 200:
        print("✅ Colab Notebook Triggered Successfully!")
    else:
        print(f"❌ Failed to Trigger Notebook. Status Code: {response.status_code}")

run_colab()
