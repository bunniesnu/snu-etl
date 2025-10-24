import requests
from .const import HEADERS

def fetch_data(url, x_csrf_token, legacy_normandy_session):
    header = HEADERS.copy()
    header["X-CSRF-Token"] = x_csrf_token
    header["Cookie"] = f"_legacy_normandy_session={legacy_normandy_session}"
    response = requests.get(url, headers=header)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

if __name__ == "__main__":
    import os
    url = "https://myetl.snu.ac.kr/api/v1/dashboard/dashboard_cards"
    x_csrf_token = os.getenv("x_csrf_token")
    legacy_normandy_session = os.getenv("legacy_normandy_session")
    try:
        data = fetch_data(url, x_csrf_token, legacy_normandy_session)
        if data is None:
            raise ValueError("No data returned from fetch_data")
        print("Fetch successful")
    except Exception as e:
        print(f"Error during fetch: {e}")