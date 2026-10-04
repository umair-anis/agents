from crewai.tools import tool
import os
import requests


@tool("Send a push notification using Pushover")
def send_push_notification(message: str) -> str:
    """
    Use this tool to send push notification to a user.
    Args:
        message (str): The message to send as a push notification.

    Returns:
        str: Status of the push notification.
    Send a push notification using Pushover
    """

    pushover_user = os.getenv("PUSHOVER_USER")
    pushover_token = os.getenv("PUSHOVER_TOKEN")
    pushover_url = "https://api.pushover.net/1/messages.json"
    payload = {
        "token": pushover_token,
        "user": pushover_user,
        "message": message
    }
    response = requests.post(pushover_url, data=payload)
    if response.status_code == 200:
        return "Notification sent successfully"
    else:
        return f"Failed to send notification: {response.text}"  
    

