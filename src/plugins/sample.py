from plugins.utils import request_util
from slackbot.bot import respond_to

CONNPASS_ENDPOINT = 'https://connpass.com/api/v1/event/'


@respond_to('勉強会教えて')
def mention_func(message):
    text = message.body['text']
    responce = request_util.do_get(CONNPASS_ENDPOINT, {'keyword': 'python'})
    event_titles = [event_detail['title'] for event_detail in responce['events']]
    reply_message = ', '.join(event_titles)
    message.reply(reply_message)