import requests


def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data from FreeAPI")


def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Random User's Username: {username}")
        print(f"Random User's Country: {country}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
