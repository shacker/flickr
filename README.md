# flickr_tools

 Misc personal tools for working with Flickr API. This is purely for personal use and totally unsupported, but help yourself.

## Setup

Not included in this repo but required:

Place a `config.py` in the root of this repo with the following (replacing with your own credentials).

```
api_key = "abc134"
api_secret = "zxy987"
user_id = "1234@N00"
```

## Included

### central.py

The Flickr Central group allows a maximum of 25 images. Once you hit that limit, you cannot add any more images until you remove your old ones. That's possible via the Organizr tool, but I find it easier to just run this script. Be careful - this will remove all of your images from whatever group ID is specified at the top.

