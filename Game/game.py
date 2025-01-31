from math import *


import arcade


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pong Game"

class Ball(arcade.Sprite) :
    def __init__(self) :
        super().__init__("ball.png", 0.5)
        self.change_x = 3
        self.change_y = 3

    def update(self) :
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_y > 0 :
            self.angle = degrees(atan2(self.change_x, self.change_y))
        else :
            self.angle = degrees(atan2(self.change_x, self.change_y))

        if self.right >= SCREEN_WIDTH or self.left <= 0 :
            self.change_x = -self.change_x

        if self.top >= SCREEN_HEIGHT :
            self.change_y = -self.change_y

        if self.bottom <= 0 :
            self.kill()



class Bar(arcade.Sprite) :
    def __init__(self) :
        super().__init__("bar.png", 0.5)


    def update(self) :
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH :
            self.right = SCREEN_WIDTH

        if self.left <= 0 :
            self.left = 0

class Game(arcade.Window) :
    def __init__(self, width, height, title) :
        super().__init__(width, height, title)
        self.sprite_list = arcade.SpriteList()
        self.bar = Bar()
        self.ball = Ball()
        self.sprite_list.append(self.bar)
        self.sprite_list.append(self.ball)
        self.setup()

    def setup(self) :
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 10
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 10 + 20

    def on_draw(self) :
        self.clear((0, 0, 0))
        self.sprite_list.draw()
        self.sprite_list.draw_hit_boxes((255, 255, 255))

    def on_update(self, delta_time) :
        if arcade.check_for_collision(self.ball, self.bar) :
            overlap = self.bar.top - self.ball.bottom
            self.ball.center_y += overlap
            self.ball.change_y *= -1
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers) :
        if key == arcade.key.RIGHT :
            self.bar.change_x = 5
        if key == arcade.key.LEFT :
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers) :
        if key == arcade.key.RIGHT or key == arcade.key.LEFT :
            self.bar.change_x = 0




if __name__ == "__main__" :
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
