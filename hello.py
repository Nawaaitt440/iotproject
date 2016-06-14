
import sys
import crypto
from pubnub import Pubnub

pubnub = Pubnub(publish_key = 'pub-c-156a6d5f-22bd-848d-b5b4d4b36695', subcribe_key = 'sub-c-f762fb78-2724-lle4-a4df-02ee2ddab7fe')
channel = 'hello-pi'

data = { 
		'username' : 'Your name',
		'message'  : 'Hello world from Pi!'
}

def callback(m):
	print(m)

	pubnub.publish(channel, data, callback = callback, error=callback)
