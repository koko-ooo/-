import random


def random_summer_greeting() -> str:
    greetings = [
        "暑中お見舞い申し上げます。",
        "盛夏の候、いかがお過ごしでしょうか。",
        "炎暑の折、どうぞご自愛ください。",
        "猛暑が続いておりますが、元気にお過ごしください。",
        "残暑お見舞い申し上げます。",
        "蝉時雨の中、変わらずお元気でしょうか。",
        "夏の盛りとなりました。くれぐれもお身体を大切に。",
        "うだるような暑さが続きますが、お変わりありませんか。",
    ]
    return random.choice(greetings)


if __name__ == "__main__":
    print(random_summer_greeting())
