import yaml
import time
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



CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')




class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communications between the nodes of the blockchain network.
    """

    def __init__(self) -> None:
        self.pubnub                  = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())


    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()


    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """

        self.publish(CHANNELS['BLOCK'], block.to_json())
        




def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo':'bar'})



if __name__ == '__main__':
    main()


