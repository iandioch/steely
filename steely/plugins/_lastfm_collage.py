from plugins._lastfm_helpers import *
import requests


def get_collage(author_id, user, period, size):
    params = {'user': user,
              'type': period,
              'size': size,
              'caption': 'true'}
    image_res = requests.get(COLLAGE_BASE, params=params)
    image = image_res.content
    image_path = f'/tmp/{author_id}.jpg'
    with open(image_path, 'wb') as image_file:
        image_file.write(image)
    return image_path


def main(bot, author_id, message_parts, thread_id, thread_type, **kwargs):
    if not message_parts or message_parts[0] not in PERIODS:
        period_string = '|'.join(PERIODS)
        bot.sendMessage(f'usage: {COMMAND} collage <{period_string}> [username]',
                        thread_id=thread_id, thread_type=thread_type)
        return
    else:
        period = message_parts[0]
    if len(message_parts) >= 2:
        username = message_parts[1]
    else:
        username = USERDB.get(USER.id == author_id)["username"]
    size = '3x3'
    if len(message_parts) >= 3:
        if message_parts[2] in ['3', '4', '5']:
            size = f'{message_parts[2]}x{message_parts[2]}'

    bot.sendLocalImage(get_collage(author_id, username, period, size),
                       message=None, thread_id=thread_id, thread_type=thread_type)
