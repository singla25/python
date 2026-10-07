# import requests

# def fetch_random_user_freeapi():
#     url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
#     response = requests.get(url)
#     data = response.json()

#     if data["success"] and "data" in data:
#         user_data = data['data']
#         username = user_data["login"]["username"]
#         country = user_data["location"]["country"]
#         return username, country
#     else:
#         raise Exception("Failed to fetch user data")

# def main():
#     try:
#         username, country = fetch_random_user_freeapi()
#         print(f"Username: {username} \nCountry: {country}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()



import requests

API_URL = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_random_user_freeapi():
    """Return a dict of user info, or None if anything goes wrong."""
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError:
        print("Response was not valid JSON.")
        return None

    if not data.get("success"):
        print("API returned an unsuccessful response:", data.get("message"))
        return None

    user = data.get("data")
    if not user:
        print("No user data found in response.")
        return None

    try:
        name = user["name"]
        return {
            "name": f"{name['title']} {name['first']} {name['last']}",
            "username": user["login"]["username"],
            "email": user["email"],
            "country": user["location"]["country"],
            "age": user["dob"]["age"],
            "picture": user["picture"]["large"],
        }
    except (KeyError, TypeError) as e:
        print(f"Unexpected response format, missing field: {e}")
        return None


def main():
    user = fetch_random_user_freeapi()
    if user is None:
        return  # error message already printed

    print("-" * 40)
    print(f"Name     : {user['name']}")
    print(f"Username : {user['username']}")
    print(f"Email    : {user['email']}")
    print(f"Age      : {user['age']}")
    print(f"Country  : {user['country']}")
    print(f"Picture  : {user['picture']}")
    print("-" * 40)


if __name__ == "__main__":
    main()