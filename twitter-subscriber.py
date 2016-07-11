import tweepy
from database import db_session
from models import Tweet

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = "h0xZXm9tvTlvxB6dE21nSnv7j"
consumer_secret = "lW5TJyn1R0sP0gKbs5TBFLonMPzzp48SGjNXkIVXVXdYo9pOSR"
access_token = "40432028-pWMflsAj7MNRnCdlA94Qm6K4TEdMSAUJIPCjJ3e82"
access_token_secret = "Ujg4lris5jU5HhECH3ojIFuoAzhf7rbUOGjrJ6RfVMz6Y"


class EnigmariusStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        tweet = Tweet(text=status.text)
        db_session.add(tweet)
        session.commit()

    def on_error(self, status):
        print status


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    maticatradio = api.get_user("maticatradio")

    stream = tweepy.Stream(auth=auth, listener=EnigmariusStreamListener())
    stream.filter(follow=[str(maticatradio.id)])
