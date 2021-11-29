import yaml
# pip install pubnub==4.1.6

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


with open("backend/config.yml", "r") as stream:
    try:
        yaml_dict = yaml.safe_load(stream)
        publish_key     = str(yaml_dict['publish_key'])
        subscribe_key   = str(yaml_dict['subscribe_key'])
        print(subscribe_key)
        print(publish_key)
    except yaml.YAMLError as exc:
        print(exc)


pnconfig                = PNConfiguration()
pnconfig.subscribe_key  = subscribe_key
pnconfig.publish_key    = publish_key
pubnub                  = PubNub(pnconfig)


TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message object: {message_object}')


pubnub.add_listener(Listener())

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({'foo':'bar'}).sync()


if __name__ == '__main__':
    main()


