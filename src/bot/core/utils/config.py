import os
import json


class Settings:
    def __init__(self, data):
        self.discordToken = "Your Token"
        self.kakaoToken = "Your Token"
        self.commandPrefix = "."
        self.messageColor = "#FAA61A"
        self.disabledPrivateChannel = False
        self.connectOnStart = False
        self.__DEBUG_MODE__ = False
        self.__dict__.update(data)


def invoke():
    with open('../data/config.json', 'rt', encoding='utf-8') as f:
        TOKEN = json.load(f)

    sch_url = 'https://mgylabs.gitlab.io/discord-bot/config.schema'

    if TOKEN.get('$schema', None) != sch_url:
        with open('../data/config.json', 'wt', encoding='utf-8') as f:
            if '$schema' in TOKEN:
                TOKEN['$schema'] = sch_url
                json.dump(TOKEN,
                          f, indent=4, ensure_ascii=False)
            else:
                json.dump({'$schema': sch_url, **TOKEN},
                          f, indent=4, ensure_ascii=False)

    return TOKEN


CONFIG = Settings(invoke())