# app.py
import requests
import time


def fetch_data(url):
    """Fetch data from an API endpoint."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


def process_items(items):
    """Process items and simulate slow operation."""
    results = []
    for item in items:
        time.sleep(0.5)  # simulate processing delay
        results.append(item.get("name", "unknown").upper())
    return results


def main():
    url = "https://jsonplaceholder.typicode.com/users"
    data = fetch_data(url)
    if data:
        processed = process_items(data)
        print("Processed users:", processed)
    else:
        print("No data to process.")


if __name__ == "__main__":
    main()
