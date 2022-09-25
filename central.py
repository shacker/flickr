import sys
import flickrapi
from icecream import ic
import webbrowser

from config import api_key, api_secret, user_id

GROUP_ID = "34427469792@N01"  # For Flickr Central

ans = input(f"This will remove all photos for user {user_id} from group {GROUP_ID}. Continue? ")
if ans not in ["Y", "y"]:
    sys.exit()


flickr = flickrapi.FlickrAPI(api_key, api_secret, format="parsed-json")

# Authorize if needed. Via
# https://stuvel.eu/flickrapi-doc/3-auth.html#non-web-applications
if not flickr.token_valid(perms="write"):

    # Get a request token
    flickr.get_request_token(oauth_callback="oob")

    # Open a browser at the authentication URL.
    authorize_url = flickr.auth_url(perms="write")
    webbrowser.open_new_tab(authorize_url)

    # Get the verifier code from the user.
    verifier = str(input("Verifier code: "))

    # Trade the request token for an access token
    flickr.get_access_token(verifier)


# Get and remove images from the group
results = flickr.groups.pools.getPhotos(GROUP_ID=GROUP_ID, user_id=user_id)
for idx, result in enumerate(results["photos"]["photo"]):

    # Leave the most recent image in place
    if idx == 0:
        continue

    id = result["id"]
    print(f"Removing image {id} - {result['title']}")
    resp = flickr.groups.pools.remove(photo_id=id, GROUP_ID=GROUP_ID)
    ic(resp)
