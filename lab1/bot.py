from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    countEmo = emo.detect_emotion_in_raw(str(trigger))
    print(countEmo)
