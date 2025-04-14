import os
import json
import torchaudio

from fireredtts.models.fireredtts import FireRedTTS


texts = [
    "你好，这里是中囯电信，有什么可以帮助您的嘛？",
    "你好，这里是中囯、电信，有什么可以帮助您的嘛！",
    "你好，这里是中、美、俄交界处，有什么可以帮助您的嘛?",
    "你好，这里是中囯电信，有什么可以帮助您的嘛!",
    "他还欠我30块钱呢，一直没有还给我，这利率快5%了吧。",
    "会议指出，今年我国气候年景偏差，强降雨过程多、历时长，江河洪水发生早、发展快，一些地方反复遭受强降雨冲击，防汛抗洪形势严峻复杂。在以习近平同志为核心的党中央坚强领导下，各级党委和政府迅速行动、全力应对，国家防总、各有关部门和单位履职尽责、通力协作，解放军和武警部队、国家综合性消防救援队伍和各类专业救援力量闻令而动、冲锋在前，广大干部群众风雨同舟、众志成城，共同构筑起了守护家园的坚固防线，防汛抗洪救灾取得重要阶段性成果。",
    "这家“汉丽轩自助烤肉”在济阳，2016年我在机场上班，下午5点下班，太阳还在半空中，就无所事事了，闲的蛋疼，就去附近的济阳转悠着玩。在中心广场上看到这家自助烤肉店。当时是39元一位，儿童半价，现在不知道多少钱了。菜品那是相当丰富，菜品得有上百个吧，还有各类肉片、海鲜等，各类饮料、甜点也很多。有烤炉、火锅。",
    "以前我们加班做手术，做到夜里，主任都会叫我给大家订点吃的喝的，订多少他给我发红包，还嘱咐我别忘了护士妹妹和麻醉老师，于是我订了30杯喜茶，30*30=900",
    "新鲜出炉的。这几天不是开学了吗？一朋友是做养殖场的，养的鸡是供当地烧烤店的。这几天订单呈断崖式下沉，百思不得其解，后来跟其他行业的朋友聊起来，大家发现这几天整个消费市场突然间就一片死寂了，连警察朋友都说这几天大街上都突然冷清了一大截。最后一寻思：开学了，交了各种费用后大家都没钱了。",
    "wflioixh&*%$#^,好吧好吧",
    "呜呜...",
    "我...我也不知道呢",
    "我我也不知道呢",
    "我我我我我我我也不知道呢。",
    "The James Webb Space Telescope (JWST) is a space telescope specifically designed to conduct infrared astronomy. The U.S. National Aeronautics and Space Administration (NASA) led Webb's design and development",
    "We make a good team, you and I. Did you see Albert I. Jones yesterday?",
]


if __name__ == "__main__":
    os.makedirs("./fireredtts_example_out", exist_ok=True)
    tts = FireRedTTS(
        config_path="configs/config_24k.json",
        pretrained_path="/mnt/public/usr/weisi/github/fireredtts-s/pretrained_models",
    )
    for i in range(len(texts)):
        # out_wav = tts.synthesize(
        #     prompt_wav="/mnt/public/usr/weisi/github/fireredtts-s/examples/prompt_1.wav",
        #     prompt_text="这还是香菱儿第一次听丁兰唱曲儿她觉得很奇妙。",
        #     text=texts[i],
        # )

        out_wav = tts.synthesize(
            prompt_wav="/mnt/public/usr/weisi/github/fireredtts-s/examples/prompt_2.wav",
            prompt_text="对，所以说你现在的话，这个账单的话，你既然说能处理，那你就想办法处理掉。",
            text=texts[i],
        )

        if out_wav is not None:
            out_wav_path_codec = os.path.join(
                "./fireredtts_example_out", str(i) + ".wav"
            )
            torchaudio.save(out_wav_path_codec, out_wav, 24000)
            print("\n")
