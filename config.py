import os

def update_config():
    token = os.environ['PANDEMICBOT_TOKEN']
    prefix = os.environ['PANDEMICBOT_PREFIX']
    guild_id = int(os.environ['PANDEMICBOT_GUILDID'])
    excluded_channels = os.environ['PANDEMICBOT_EXCLUDEDCHANNELS'].split(",")
    if excluded_channels == ['']:
        excluded_channels = []

    return {
        'token': token,
        'prefix': prefix,
        'guild_id': guild_id,
        'excluded_channels': excluded_channels,
    }

