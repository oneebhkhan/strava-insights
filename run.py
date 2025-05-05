import requests
import os

def get_athlete_profile(athlete_id: str, token: str) -> dict:
    """
    Fetch the athlete profile from Strava API.

    Args:
        athlete_id (str): The ID of the athlete.
        token (str): The access token for authentication.

    Returns:
        dict: The athlete profile data.
    """
    url = f"https://www.strava.com/api/v3/athlete/activities"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching athlete profile: {response.status_code} - {response.text}")
