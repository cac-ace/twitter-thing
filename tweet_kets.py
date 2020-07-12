
#!/usr/bin/env python
import sys
from twython import Twython

photoFilePath = "/home/pi/Pictures/one.jpg"
photo = open(photoFilePath, 'rb')
tweetStr = "A cat photo!"
apiKey = 'enter apiKey here'
apiSecret = 'enter apiSecret here'
accessToken = 'enter accessToken here'
accessTokenSecret = 'enter accessTokenSecret here'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status_with_media(media=photo,status=tweetStr)
print "tweeted: "+tweetStr
