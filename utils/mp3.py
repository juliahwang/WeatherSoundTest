import os

import eyed3

current = os.getcwd()


def find_mp3(current):  # 추후에 media root로 고정(mp3저장되는 위치로)
    # TODO DB에 넣도록, model에 필요한 필드 정보 추가, img 저장위치에 대한 고찰
    # chdir를 이용하여 glob을 이용해볼까? -> 차선책
    """
    current 폴더 안에 있는 모든 mp3의 정보 앨범이미지 가져온다.

    :param current: 작업 폴더
    :return: None
    """
    for path, dirs, files in os.walk(current):
        if files:
            for f in files:
                name = os.path.splitext(f)
                if name[1] == ".mp3":  # 추후에 mp3정보는 뺴와야하니까. mp3판단 부터
                    audio = eyed3.load(os.path.join(path, f))
                    album = audio.tag.album
                    if not os.path.isfile(album + ".jpg"):
                        img = audio.tag.images[0].image_data
                        address = path + "/images/"
                        if not os.path.isdir(address):  # 폴더 x시 생성, 나중에 mp3한폴더에?
                            os.mkdir(address)
                        with open(address + "/{}.jpg".format(album), "wb") as f:  # 추후 image저장위치 지정 다시
                            f.write(img)
