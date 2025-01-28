import time

class User :
    def __init__(self, nickname, password, age) :
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self) :
        return self.nickname

class Video :
    def __init__(self, title, duration, time_now = 0, adult_mode = False) :
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube :
    def __init__(self) :
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users :
            if nickname == user.nickname and hash(password) == user.password :
                self.current_user = user
                return
        print("Пользователь не найден")

    def register(self, nickname, password, age) :
        for user in self.users :
            if user.nickname == nickname :
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self) :
        self.current_user = None

    def add(self, *videos: Video) :
        for video in videos :
            if all(vid.title != video.title for vid in self.videos) :
                self.videos.append(video)

    def get_videos(self, title) :
        for vid in self.videos :
            if title.casefold() in vid.title.casefold() :
                print(vid.title)

    def watch_video(self, title) :
        if self.current_user :
            video = next((vid for vid in self.videos if vid.title == title), None)
            if video :
                if video.adult_mode and self.current_user.age < 18 :
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(1, video.duration + 1) :
                        time.sleep(1)
                        print(i)
                    print("Конец видео")
        else :
            print("Войдите в аккаунт, чтобы смотреть видео")


    def __contains__(self, video) :
        return video.title in [vid.title for vid in self.videos]




ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


# Добавление видео
ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')