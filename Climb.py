from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, TransitionBase
from  kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
import random
import zipfile
from kivy.animation import Animation

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics import Rotate
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.uix.slider import Slider




Window.size = (360, 640)

x = Window.width / 6
y = Window.height / 8

x_level = Window.width / 4
y_level = Window.height / 11.5


screens=ScreenManager()

jump = 0


class TestPY(Image):
    def __init__(self, **kwargs):
        super(TestPY, self).__init__(**kwargs)
        with self.canvas.before:
            PushMatrix()
            self.size = (x*6, y*6)
            self.rot = Rotate()
            self.rot.angle = 0
            self.rot.origin = self.center
            self.rot.axis = (0, 0, 1)
        with self.canvas.after:
            PopMatrix()

    def animation_light(self, *args):
        self.rot.origin = self.center
        self.rot.angle += 5

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.p = TestPY(source="Design Screen/light.png", x=0, y =y*3)
        self.add_widget(self.p)




class Climbing(App, Screen):
    # Функция нажатия на кнопку Домой в меню
    def press_HOME(self, args):
        self.sm.current = 'first'
        self.sm.transition.duration = 0.5
        self.menu_image.y = y*8
        self.count = 0
        self.power = 10
        self.press_menu_continue(args)
        self.power_image_box.remove_widget(self.power_image)
        self.power_image = Label(text='x' + str(self.power), font_size='30sp', color=(0,0,0,1), bold=(12))
        self.power_image_box.add_widget(self.power_image)

        for i in self.count_screen[:]:
            i.remove_widget(self.menu_box)
            i.remove_widget(self.menu_image)

    # Функция нажатия на кнопку Play
    def press_ME(self, args):
        self.sm.current = 'character'
        self.sm.transition.direction = 'left'
        self.sm.transition.duration = 0.5

    # Функция возврата к первому экрану
    def press_RETURN(self, args):
        self.sm.current = 'first'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    def press_RETURN_TO_CHARACTER(self,args):
        self.sm.current = 'character'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    def press_RETURN_TO_ITEMS(self,args):
        self.sm.current = 'items'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    # Функция вызова меню Options
    def press_OPTIONS(self, args):
        self.sm.current = 'options'
        self.sm.transition.direction = 'left'
        self.sm.transition.duration = 0.5


    def press_TAP_TO_START(self, args):
        self.sm.current = 'Menu_select_level'
        self.sm.transition.duration = 0.5


    def press_SHOP_BUTTON(self, args):
        self.sm.current = 'items'
        self.sm.transition.duration = 0.5
        for i in self.count_screen[:]:
            i.remove_widget(self.menu_box)
            i.remove_widget(self.menu_image)

    def press_SHUES(self, args):
        self.sm.current = 'shues'
        self.sm.transition.duration = 0.5

    def press_CLOTHES(self, args):
        self.sm.current = 'clothes'
        self.sm.transition.duration = 0.5

    def press_UPGRADES(self, args):
        self.sm.current = 'upgrades'
        self.sm.transition.duration = 0.5

    def press_STORE(self, args):
        self.sm.current = 'store'
        self.sm.transition.duration = 0.5


    def press_change_skin(self, args):
        if self.screen_for_skins.current == 'four_skin':
            self.screen_for_skins.current = 'first_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 0

        elif self.screen_for_skins.current == 'first_skin':
            self.screen_for_skins.current = 'second_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 1

        elif self.screen_for_skins.current == 'second_skin':
            self.screen_for_skins.current = 'three_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 2

        elif self.screen_for_skins.current == 'three_skin':
            self.screen_for_skins.current = 'four_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 3

    def press_change_skin_for_game(self, args):
        for i in self.skins[:]:

            for a in range(3):
                if self.count_skin == a:
                    i = True
                else:
                    i = False

    def press_skin_button(self, args):
        self.sm.current = 'skin'
        self.sm.transition.duration = 0.5



    # фунции вызова анимации падающего меню
    def press_menu(self, args):
        self.animation_menu_down = Clock.schedule_interval(self.menu_animation_down, .01)

    def menu_animation_down(self, args):
        self.menu_image.y -= 10
        if self.menu_image.y <= Window.height/4:
            self.animation_menu_down.cancel()

    # функция вызова поднимающегося меню
    def press_menu_continue(self, args):
        self.animation_menu_up = Clock.schedule_interval(self.menu_animation_up, .01)

    def menu_animation_up(self, args):
        self.menu_image.y += 10
        if self.menu_image.y >= Window.height:
            self.animation_menu_up.cancel()


    def count_plus(self, args):
        self.count += 1
        self.power_image_box.remove_widget(self.power_image)
        self.power -= 1
        self.power_image =Label(text='x' + str(self.power), font_size='30sp', color=(0,0,0,1), bold=(12))
        self.power_image_box.add_widget(self.power_image)

    def restart_level(self, args):
        self.sm.current = 'First_level'
        self.sm.transition.duration = 0.5
        self.press_menu_continue(args)
        self.power_image_box.remove_widget(self.power_image)
        self.power_image = Label(text='x' + str(self.power), font_size='30sp', color=(0,0,0,1), bold=(12))

    def start_level(self, args):
        if self.level_count == 0:
            self.sm.current = 'First_level'
            for i in self.count_screen[:]:
                i.remove_widget(self.menu_box)
                i.remove_widget(self.menu_image)
            self.levels[self.level_count].add_widget(self.menu_box)
            self.levels[self.level_count].add_widget(self.menu_image)
        if self.level_count == 1:
            self.sm.current = 'Second_level'
            for i in self.count_screen[:]:
                i.remove_widget(self.menu_box)
                i.remove_widget(self.menu_image)
            self.levels[self.level_count].add_widget(self.menu_box)
            self.levels[self.level_count].add_widget(self.menu_image)

    def start(self, *args):
        self.level_screen[self.level_count].remove_widget(self.start_boxes[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_start[self.level_count])
        self.knight_image_start[self.level_count].anim_delay = 0.1
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_start[self.level_count])
        self.touch_down_button = Clock.schedule_once(self.touch_down, 2.5)
        self.frages_down()


    def touch_down(self, *args):
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_start[self.level_count])
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])
        self.up_image = Clock.schedule_interval(self.up_up, .01)
        self.start_levels = True
        self.touch_down_button.cancel()

    def frages_down(self, *args):
        self.frages_move = Clock.schedule_interval(self.down_down, 2.5)

    def down_down(self, *args):
        self.random_down = Clock.schedule_interval(self.down_items, .01)

    def down_items(self, *args):

        self.frages_collide_screen()
        if self.random_number != 3:
            self.frags_level_two[self.random_number].y -= 3
            self.frags_image_level_two[self.random_number].y -= 3
        else:
            self.random_number = 0

    def frages_collide_screen(self, *args):
        if self.frages_box_image_level_two.top <= self.knight_image_boxes[self.level_count].y:
            self.random_number += 1
            self.frages_box_image_level_two.y = self.knight_image_boxes[self.level_count].y + y*28
            self.frages_box_level_two.y = self.knight_image_boxes[self.level_count].y + y * 28
            self.random_down.cancel()

        if self.frages_box_image_1_level_two.top <= self.knight_image_boxes[self.level_count].y:
            self.frages_box_image_1_level_two.y = self.knight_image_boxes[self.level_count].y + y*28
            self.random_number += 1
            self.frages_box_1_level_two.y = self.knight_image_boxes[self.level_count].y + y * 28
            self.random_down.cancel()

        if self.frages_box_image_2_level_two.top <= self.knight_image_boxes[self.level_count].y:
            self.frages_box_image_2_level_two.y = self.knight_image_boxes[self.level_count].y + y * 28
            self.random_number += 1
            self.frages_box_2_level_two.y = self.knight_image_boxes[self.level_count].y + y * 28
            self.random_down.cancel()



    def up_up(self, *args):
        self.climb_screen[self.level_count].y -= 2
        self.knight_image_boxes[self.level_count].y += 2
        self.knight_box[self.level_count].y += 2
        self.sky_box[self.level_count].x -= 0.2
        self.defeat()
        self.check_coin()
        self.win_level()


    def on_touch_down(self, touch, *args):
        if self.swipe[self.level_count].value != 0:
            self.swipe[self.level_count].value = 0


    def on_touch_up(self, touch, *args):
        if self.swipe[self.level_count].value == 0:
            self.left_count = False
        if self.swipe[self.level_count].value < 0 and self.left == False:
            self.left = True
            self.start_left = True
            self.knight_left = Clock.schedule_interval(self.knight_move, .01)
            self.jumping()
            self.swipe[self.level_count].value = 0
        if self.right_count == False:
            self.sit_up()
            self.swipe[self.level_count].value = 0

    def on_touch_move(self, touch, *args):
        if self.swipe[self.level_count].value == 1:
            self.sit_down()
            self.up_image.cancel()
            self.swipe[self.level_count].value = 0

    def check_coin(self, *args):
        for i in self.coins[self.level_count][:]:
            if self.knight_box_button[self.level_count].collide_widget(i):
                for a in self.coin_boxes[self.level_count][:]:
                    a.remove_widget(i)
                self.coins[self.level_count].remove(i)
                self.coin_image_boxes[self.level_count].remove_widget(self.coin_image_count[self.level_count])
                self.coin_image_count[self.level_count] = Label(text=str(-(len(self.coins[self.level_count]) - len(self.coin_boxes[self.level_count]))), font_size='30sp', color=(0, 0, 0, 1),
                                              bold=(12))
                self.coin_image_boxes[self.level_count].add_widget(self.coin_image_count[self.level_count])

    def win_level(self, *args):
        if self.climb_screen[self.level_count].y == -y*20:
            self.level_screen[self.level_count].remove_widget(self.swipe[self.level_count])
            self.up_image.cancel()
            self.frages_move.cancel()
            self.random_down.cancel()
            self.win_images = Clock.schedule_interval(self.win, .01)

    def win(self, *args):
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_end[self.level_count])
        self.knight_image_end[self.level_count].anim_delay = 0.1
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_end[self.level_count])
        self.knight_box[self.level_count].y += 2
        self.sky_box[self.level_count].x -= 0.2
        self.frages_move.cancel()
        self.random_down.cancel()
        if self.knight_box[self.level_count].y > self.wall_box[self.level_count].top*2.8:
            self.climb_screen[self.level_count].y -= 2
            self.frages_move.cancel()
            self.random_down.cancel()
            if self.climb_screen[self.level_count].y <= -2100:
                self.win_images.cancel()
                self.climb_screen[self.level_count].add_widget(self.maps_button_box[self.level_count])
                self.first_level_complete = True
                self.level_count += 1

    def hero_hide(self, *args):
        self.level_screen[self.level_count].remove_widget(self.swipe[self.level_count])
        self.hit_count += 1
        if self.hit_count == 1:
            self.climb_screen[self.level_count].remove_widget(self.knight_image_boxes[self.level_count])
        if self.hit_count == 2:
            self.climb_screen[self.level_count].add_widget(self.knight_image_boxes[self.level_count])
        if self.hit_count == 3:
            self.climb_screen[self.level_count].remove_widget(self.knight_image_boxes[self.level_count])
        if self.hit_count == 4:
            self.climb_screen[self.level_count].add_widget(self.knight_image_boxes[self.level_count])
        if self.hit_count == 5:
            self.climb_screen[self.level_count].remove_widget(self.knight_image_boxes[self.level_count])
        if self.hit_count == 6:
            self.level_screen[self.level_count].add_widget(self.swipe[self.level_count])
            self.climb_screen[self.level_count].add_widget(self.knight_image_boxes[self.level_count])
            self.hit_count = 0
            self.hit_tic_tac.cancel()

    def defeat(self, *args):

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[0]):
            self.frags[self.level_count][0].x += x*20
            self.frags_image[self.level_count][0].x += x * 20
            self.one_hit = True
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[1]) and self.one_hit == False:
            self.frags[self.level_count][1].x += x*20
            self.frags_image[self.level_count][1].x += x * 20
            self.one_hit = True
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        elif self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[1]) and self.one_hit == True:
            self.frags[self.level_count][1].x += x * 20
            self.frags_image[self.level_count][1].x += x * 20
            self.two_hit = True
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[2]) and self.one_hit == False and self.two_hit == False:
            self.frags[self.level_count][2].x += x * 20
            self.frags_image[self.level_count][2].x += x * 20
            self.one_hit = True
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[2]) and self.one_hit == True and self.two_hit == False:
            self.frags[self.level_count][2].x += x * 20

            self.frags_image[self.level_count][2].x += x * 20
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[2]) and self.one_hit == False and self.two_hit == True:
            self.frags[self.level_count][2].x += x * 20
            self.frags_image[self.level_count][2].x += x * 20
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Image(source=('Design Screen/сердце.zip')))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

        if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count])[2]) and self.one_hit == True and self.two_hit == True:
            self.frags[self.level_count][2].x += x * 20

            self.frags_image[self.level_count][2].x += x * 20
            self.level_screen_child[self.level_count].remove_widget(self.heart_boxes[self.level_count])
            self.heart_boxes[self.level_count] = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.heart_boxes[self.level_count].add_widget(Widget())
            self.level_screen_child[self.level_count].add_widget(self.heart_boxes[self.level_count])
            self.hit_tic_tac = Clock.schedule_interval(self.hero_hide, .1)
            self.random_down.cancel()

    def jumping(self, *args):
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
        self.knight_image_jump[self.level_count].anim_delay = 0.05
        self.knight_image_jump[self.level_count].anim_loop = 1
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_jump[self.level_count])

    def walking(self, *args):
        if self.start_left == False and self.start_right == False:
            self.knight_image_jump[self.level_count].anim_delay = -1
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])

    def sit_down(self, *args):
        if self.right_count == True:
            self.knight_box[self.level_count].x = self.knight_box[self.level_count].x + x
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_sit[self.level_count])
            self.right_count = False

    def sit_up(self, *args):
        self.up_image()
        self.knight_box[self.level_count].x = self.knight_box[self.level_count].x - x
        self.right_count = True
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit[self.level_count])
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])

    def knight_move(self, args):
        if self.start_left == True:
            self.knight_box[self.level_count].x -= 2**1.2
            self.knight_box[self.level_count].y += 0.8**1.2
            self.knight_image_boxes[self.level_count].x -= 1 ** 1.1

        if self.knight_box[self.level_count].x <= self.first_level_screen_child.x - x*2:
            self.start_left = False
            self.start_right = True

        if self.start_right == True:
            self.knight_box[self.level_count].x += 2**1.2
            self.knight_box[self.level_count].y -= 0.8**1.2
            self.knight_image_boxes[self.level_count].x += 1 ** 1.1

        if self.knight_box[self.level_count].x >= 0:
            self.knight_left.cancel()
            self.start_right = False
            self.left = False
            self.walking()

    def return_maps(self, *args):
        self.sm.current = 'Map'
        self.sm.transition.duration = 0.5
        self.maps_image.anim_delay = 0.8
        self.maps_image_screen.add_widget(self.maps_image)
        self.maps_image_screen.add_widget(self.map_screen_button_box)











































    def build(self):
        self.frag_one = False
        self.frag_two = False
        self.frag_three = False


        self.left = False
        self.left_count = False

        self.right_count = True
        self.start_levels = False
        self.hit_count = 0
        #экран с картой

        self.maps_button_box_level_one =  BoxLayout(padding=(x*2, -y*24, x*2, y*31))
        self.maps_button_box_level_one.add_widget(Button(on_press=self.return_maps, background_color = (0,0,255, .5), text = 'Next'))

        self.maps_button_box_level_two = BoxLayout(padding=(x * 2, -y * 24, x * 2, y * 31))
        self.maps_button_box_level_two.add_widget(
            Button(on_press=self.return_maps, background_color=(0, 0, 255, .5), text='Next'))

        self.maps_image_screen = Screen(name='Map')
        self.maps_image = Image(source=('Design Screen/karta.zip'),anim_delay = -1, allow_stretch=True,
                                keep_ratio=False,
                                keep_data=True, anim_loop = 1)
        self.map_screen_button_box = BoxLayout(padding=(x*2, y, x*2, y * 6))
        self.map_screen_button_box.add_widget(Button(background_color = (0,0,0,.5), text = 'Next Level', on_press = self.start_level))


        # флаги нанесение повреждений
        self.one_hit = False
        self.two_hit = False
        self.three_hit = False
        # флаг с началом фазы полета
        self.start_left = False
        self.start_right = False
        # флаг с прохождением уровня
        self.first_level_complete = False
        self.second_level_complete = False











        self.random_number = 0





        # ..............................................................................добавляем экран с первым уровнем
        self.first_level = Screen(name=('First_level'))
        self.first_level_screen = RelativeLayout()
        self.first_level_screen_child = RelativeLayout()
        self.heart_boxes_level_one = GridLayout(cols = 3, padding = (x, 0, x*3, y*7))
        self.heart_boxes_level_one.add_widget(Image(source=('Design Screen/сердце.zip')))
        self.heart_boxes_level_one.add_widget(Image(source=('Design Screen/сердце.zip')))
        self.heart_boxes_level_one.add_widget(Image(source=('Design Screen/сердце.zip')))
        self.climb_screen_level_one = RelativeLayout()
        self.sky_box_level_one = BoxLayout(padding=(0, 0, -x*12, 0))
        self.sky_image_level_one = Image(source=('Design Screen/небо-1.png'), allow_stretch=True,
                                keep_ratio=False,
                                keep_data=True)
        self.sky_box_level_one.add_widget(self.sky_image_level_one)
        self.wall_box_level_one = BoxLayout(padding = (0, -y*24, 0, 0))
        self.climb_wall_level_one = Image(source=('Design Screen/фон_стена_дерево.png'), allow_stretch = True,
                                                    keep_ratio = False,
                                                    keep_data = True)
        self.wall_box_level_one.add_widget(self.climb_wall_level_one)
        self.green_box_level_one = BoxLayout(padding = (0, -y*24, 0, 0))
        self.green_image_level_one = Image(source=('Design Screen/трава_фон.png'), allow_stretch = True,
                                                    keep_ratio = False,
                                                    keep_data = True)
        self.green_box_level_one.add_widget(self.green_image_level_one)
        self.frages_box_level_one =  BoxLayout(padding=(x*3, -y, x * 2.5, y * 8.6))
        self.frages_box_image_level_one = BoxLayout(padding=(x*2.8, -y*1.7, x * 1.4, y *8.4))
        self.frages_box_image_level_one.add_widget(Image(source=('Design Screen/диск.zip'), anim_delay = .01,  allow_stretch=True,keep_ratio=False,keep_data=True))
        self.frag_level_one = Widget()
        self.frages_box_1_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x*3, -y * 6.5, x * 2.5, y * 14.5))
        self.frages_box_image_1_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x*2.5, -y*6.9, x * 1.7, y *14))
        self.frages_box_image_1_level_one.add_widget(
            Image(source=('Design Screen/шипы.zip'), anim_delay = .2, allow_stretch=True, keep_ratio=False, keep_data=True))
        self.frag_1_level_one = Widget()
        self.frages_box_2_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x_level*2, -y_level*19.5, x_level, y_level *31))
        self.frages_box_image_2_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x_level*1.5, -y_level*21.0, x_level, y_level*29))
        self.frages_box_image_2_level_one.add_widget(
            Image(source=('Design Screen/капкан.zip'),anim_delay = .08, allow_stretch=True, keep_ratio=False, keep_data=True))
        self.frag_2_level_one = Widget()
        self.frages_box_level_one.add_widget(self.frag_level_one)
        self.frages_box_1_level_one.add_widget(self.frag_1_level_one)
        self.frages_box_2_level_one.add_widget(self.frag_2_level_one)
        self.coin_1 = Image(source=('Design Screen/монетка.zip'), anim_delay = .08, keep_ratio=False,keep_data=True)
        self.coin_box_1_level_one = AnchorLayout(padding=(x_level*1.5, 0, x_level * 2, y*7))
        self.coin_box_1_level_one.add_widget(self.coin_1)
        self.coin_2 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_2_level_one = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_2_level_one.add_widget(self.coin_2)
        self.coin_3 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_3_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 2, x_level * 3, y * 9))
        self.coin_box_3_level_one.add_widget(self.coin_3)
        self.coin_4 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_4_level_one = AnchorLayout(padding=(x_level * 1.5, -y *3, x_level * 2, y * 10))
        self.coin_box_4_level_one.add_widget(self.coin_4)
        self.coin_5 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_5_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_5_level_one.add_widget(self.coin_5)
        self.coin_6 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_6_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_6_level_one.add_widget(self.coin_6)
        self.coin_7 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_7_level_one= AnchorLayout(padding=(x_level * 0.5, -y * 7, x_level * 3, y * 14))
        self.coin_box_7_level_one.add_widget(self.coin_7)
        self.coin_8 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_8_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 8, x_level * 3, y * 15))
        self.coin_box_8_level_one.add_widget(self.coin_8)
        self.coin_9 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_9_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_9_level_one.add_widget(self.coin_9)
        self.coin_10 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_10_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 11, x_level * 2, y * 18))
        self.coin_box_10_level_one.add_widget(self.coin_10)
        self.coin_11 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_11_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.coin_box_11_level_one.add_widget(self.coin_11)
        self.coin_12 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_12_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 14, x_level * 3, y * 21))
        self.coin_box_12_level_one.add_widget(self.coin_12)
        self.coin_13 = Image(source=('Design Screen/монетка.zip'), anim_delay=.1, keep_ratio=False, keep_data=True)
        self.coin_box_13_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_13_level_one.add_widget(self.coin_13)
        self.coin_14 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_14_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))
        self.coin_box_14_level_one.add_widget(self.coin_14)
        self.coin_boxes_level_one = [self.coin_box_1_level_one, self.coin_box_2_level_one, self.coin_box_3_level_one, self.coin_box_4_level_one, self.coin_box_5_level_one,
                           self.coin_box_6_level_one, self.coin_box_7_level_one, self.coin_box_8_level_one, self.coin_box_9_level_one, self.coin_box_10_level_one,
                           self.coin_box_11_level_one, self.coin_box_12_level_one, self.coin_box_13_level_one, self.coin_box_14_level_one ]
        self.coins_level_one = [self.coin_1, self.coin_2, self.coin_3, self.coin_4, self.coin_5, self.coin_6, self.coin_7,
                      self.coin_8, self.coin_9, self.coin_10, self.coin_11, self.coin_12, self.coin_13, self.coin_14]
        self.coins_check_level_one = []
        self.coin_count_level_one = 0
        self.knight_image_box_level_one = AnchorLayout()
        self.knight_image_jump_level_one = Image(source=('Design Screen/polet.zip'), anim_delay = -1,
                                  keep_ratio=False, keep_data=True, anim_loop = 1)
        self.knight_image_end_level_one = Image(source=('Design Screen/end.zip'), anim_delay=-1,
                                       keep_ratio=False, keep_data=True, anim_loop=1)
        self.knight_image_start_level_one = Image(source=('Design Screen/начало.zip'), anim_delay= -1, allow_stretch=True,
                                       keep_ratio=False, keep_data=True, anim_loop = 1)
        self.knight_image_walk_level_one = Image(source=('Design Screen/anim.zip'),anim_delay=0.1, allow_stretch=True,keep_ratio=False,keep_data=True)
        self.knight_image_sit_level_one = Image(source=('Design Screen/sit.png'))
        # self.knight_image_jump_level_one = Widget()
        # self.knight_image_end_level_one = Widget()
        # self.knight_image_start_level_one = Widget()
        # self.knight_image_walk_level_one = Widget()
        self.knight_box_level_one = BoxLayout(padding=(x*2.2, y*4, x*2.8, y*3))
        self.knight_box_button_level_one = Widget()
        self.knight_box_level_one.add_widget(self.knight_box_button_level_one)
        self.knight_image_box_level_one.add_widget(self.knight_image_start_level_one)
        self.climb_screen_level_one.add_widget(self.wall_box_level_one)
        self.climb_screen_level_one.add_widget(self.green_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_level_one)
        self.climb_screen_level_one.add_widget(self.knight_box_level_one)
        self.climb_screen_level_one.add_widget(self.knight_image_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_1_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_1_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_2_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_2_level_one)
        for i in self.coin_boxes_level_one[:]:
            self.climb_screen_level_one.add_widget(i)
        self.screen_box_touch = BoxLayout()
        self.first_level_screen_child.add_widget(self.sky_box_level_one)
        self.first_level_screen_child.add_widget(self.climb_screen_level_one)
        self.first_level_screen_child.add_widget(self.heart_boxes_level_one)
        self.first_level_screen.add_widget(self.first_level_screen_child)
        image_buttons_level_one = BoxLayout(padding=(0, y * 6, 0, 0))
        # image_buttons.add_widget(Image(source=('Design Screen/menu.png')))
        self.start_box_level_one = BoxLayout(padding=(x * 2, y * 3, x * 2, y * 3))
        self.start_box_1_level_one = RelativeLayout(size=(x * 2, y * 2))
        self.start_box_1_level_one.add_widget(Image(source=('Design Screen/play_but.png')))
        self.start_box_1_level_one.add_widget(Button(on_press=(self.start), background_color=(0, 0, 0, 0)))
        item_coin_box_level_one = BoxLayout(padding=(x * 4, y / 5, x, y * 7))
        item_coin_box_level_one.add_widget(Image(source=('Design Screen/монетка.zip'), anim_delay=.1,
                                        allow_stretch=False,
                                        keep_ratio=False,
                                        keep_data=True))
        self.start_box_level_one.add_widget(self.start_box_1_level_one)
        self.coin_image_box_level_one = BoxLayout(padding=(x * 5, 0, 0, y * 7))
        self.coin_image_count_level_one = Label(text=str(self.coin_count_level_one), font_size='30sp', color=(0, 0, 0, 1), bold=(12))
        self.coin_image_box_level_one.add_widget(self.coin_image_count_level_one)
        self.first_level_screen.add_widget(self.coin_image_box_level_one)
        self.first_level_screen.add_widget(image_buttons_level_one)
        self.first_level_screen.add_widget(item_coin_box_level_one)
        self.man_poses_image_level_one = BoxLayout(padding=(x, y, x, y * 2))
        self.first_level_screen.add_widget(self.man_poses_image_level_one)
        self.swipe_level_one = Slider(min=-1, max=1, value=0, step = .5,background_width=(0), cursor_size = (0,0),
                        on_touch_up = self.on_touch_up, on_touch_move = self.on_touch_move, on_touch_down = self.on_touch_down)
        self.first_level_screen.add_widget(self.swipe_level_one)
        self.first_level_screen.add_widget(self.start_box_level_one)
        self.first_level.add_widget(self.first_level_screen)



















        # ......................................................................................добавляем второй уровень
        self.second_level = Screen(name=('Second_level'))
        self.second_level_screen = RelativeLayout()
        self.second_level_screen_child = RelativeLayout()
        self.heart_boxes_level_two = GridLayout(cols=3, padding=(x, 0, x * 3, y * 7))

        self.heart_boxes_level_two.add_widget(Image(source=('Design Screen/сердце.zip')))
        self.heart_boxes_level_two.add_widget(Image(source=('Design Screen/сердце.zip')))
        self.heart_boxes_level_two.add_widget(Image(source=('Design Screen/сердце.zip')))

        self.climb_screen_level_two = RelativeLayout()
        self.sky_box_level_two = BoxLayout(padding=(0, 0, -x * 12, 0))
        self.sky_image_level_two = Image(source=('Design Screen/небо-1.png'), allow_stretch=True,
                               keep_ratio=False,
                               keep_data=True)
        self.sky_box_level_two.add_widget(self.sky_image_level_two)
        self.ran_image_level_two = Image(source=('Design Screen/дождь.zip'), anim_delay=.1, allow_stretch=True,
                               keep_ratio=False,
                               keep_data=True)

        self.wall_box_level_two = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_two = Image(source=('Design Screen/фон_стена_дерево.png'), allow_stretch=True,
                                keep_ratio=False,
                                keep_data=True)

        self.wall_box_level_two.add_widget(self.climb_wall_level_two)

        self.green_box_level_two = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.green_image_level_two = Image(source=('Design Screen/трава_фон.png'), allow_stretch=True,
                                 keep_ratio=False,
                                 keep_data=True)
        self.green_box_level_two.add_widget(self.green_image_level_two)


        self.coin_level_two_1 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False, keep_data=True)
        self.coin_box_level_two_1 = AnchorLayout(padding=(x_level * 0.5, 0, x_level * 3, y * 7))
        self.coin_box_level_two_1.add_widget(self.coin_level_two_1)

        self.coin_level_two_2 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False,
                                      keep_data=True)
        self.coin_box_level_two_2 = AnchorLayout(padding=(x_level * 1.5, -y, x_level * 2, y * 8))
        self.coin_box_level_two_2.add_widget(self.coin_level_two_2)

        self.coin_level_two_3 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False,
                                      keep_data=True)
        self.coin_box_level_two_3 = AnchorLayout(padding=(x_level * 1.5, -y *2, x_level * 2, y * 9))
        self.coin_box_level_two_3.add_widget(self.coin_level_two_3)

        self.coin_level_two_4 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False,
                                      keep_data=True)
        self.coin_box_level_two_4 = AnchorLayout(padding=(x_level * 0.5, -y * 3, x_level * 3, y * 10))
        self.coin_box_level_two_4.add_widget(self.coin_level_two_4)

        self.coin_level_two_5 = Image(source=('Design Screen/монетка.zip'), anim_delay=.08, keep_ratio=False,
                                      keep_data=True)
        self.coin_box_level_two_5 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_two_5.add_widget(self.coin_level_two_5)



        self.coin_boxes_level_two = [self.coin_box_level_two_1, self.coin_box_level_two_2, self.coin_box_level_two_3, self.coin_box_level_two_4]

        self.coins_level_two = [self.coin_level_two_1, self.coin_level_two_2, self.coin_level_two_3, self.coin_level_two_4]
        self.coins_check_level_two = []

        self.coin_count_level_two = 0

        self.knight_image_box_level_two = AnchorLayout()

        self.knight_image_jump_level_two = Image(source=('Design Screen/polet.zip'), anim_delay=-1,
                                       keep_ratio=False, keep_data=True, anim_loop=1)
        self.knight_image_end_level_two = Image(source=('Design Screen/end.zip'), anim_delay=-1,
                                      keep_ratio=False, keep_data=True, anim_loop=1)
        self.knight_image_start_level_two = Image(source=('Design Screen/начало.zip'), anim_delay=-1, allow_stretch=True,
                                        keep_ratio=False, keep_data=True, anim_loop=1)
        self.knight_image_walk_level_two = Image(source=('Design Screen/anim.zip'), anim_delay=0.1, allow_stretch=True,
                                       keep_ratio=False, keep_data=True)
        self.knight_image_sit_level_two = Image(source = ('Design Screen/sit.png'))

        self.frages_box_level_two = BoxLayout(padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_level_two = BoxLayout(padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_level_two.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False,allow_stretch=True,
                  keep_data=True))
        self.frag_level_two = Button()

        self.frages_box_1_level_two = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 0.5, 0, x * 3.5, y*6))
        self.frages_box_image_1_level_two = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 0.5, 0, x * 3.5, y*6))
        self.frages_box_image_1_level_two.add_widget(
            Image(source=('Design Screen/рояль.png'), anim_delay=.2, allow_stretch=True, keep_ratio=False,
                  keep_data=True))
        self.frag_1_level_two = Widget()

        self.frages_box_2_level_two = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x, 0, x * 3.5, y*6))
        self.frages_box_image_2_level_two = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x, 0, x * 3.5, y*6))
        self.frages_box_image_2_level_two.add_widget(
            Image(source=('Design Screen/якорь.png'), anim_delay=.08, allow_stretch=True, keep_ratio=False,
                  keep_data=True))
        self.frag_2_level_two = Widget()

        self.frages_box_level_two.add_widget(self.frag_level_two)
        self.frages_box_1_level_two.add_widget(self.frag_1_level_two)
        self.frages_box_2_level_two.add_widget(self.frag_2_level_two)

        self.knight_box_level_two = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_image_level_two.y = self.knight_box_level_two.y + y*28
        self.frages_box_level_two.y = self.knight_box_level_two.y + y*28
        self.frages_box_image_1_level_two.y = self.knight_box_level_two.y + y*28
        self.frages_box_1_level_two.y = self.knight_box_level_two.y + y*28
        self.frages_box_image_2_level_two.y = self.knight_box_level_two.y + y*28
        self.frages_box_2_level_two.y = self.knight_box_level_two.y + y*28

        self.knight_box_button_level_two = Widget()
        self.knight_box_level_two.add_widget(self.knight_box_button_level_two)
        self.knight_image_box_level_two.add_widget(self.knight_image_start_level_two)

        self.climb_screen_level_two.add_widget(self.wall_box_level_two)
        self.climb_screen_level_two.add_widget(self.green_box_level_two)

        self.climb_screen_level_two.add_widget(self.frages_box_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_image_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_1_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_image_1_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_2_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_image_2_level_two)

        self.climb_screen_level_two.add_widget(self.knight_box_level_two)
        self.climb_screen_level_two.add_widget(self.knight_image_box_level_two)
        for i in self.coin_boxes_level_two[:]:
            self.climb_screen_level_two.add_widget(i)
        self.second_level_screen_child.add_widget(self.sky_box_level_two)
        self.second_level_screen_child.add_widget(self.climb_screen_level_two)
        self.second_level_screen_child.add_widget(self.heart_boxes_level_two)
        self.second_level_screen.add_widget(self.second_level_screen_child)

        self.start_box_level_two = BoxLayout(padding=(x * 2, y * 3, x * 2, y * 3))
        self.start_box_1_level_two = RelativeLayout(size=(x * 2, y * 2))
        self.start_box_1_level_two.add_widget(Image(source=('Design Screen/play_but.png')))
        self.start_box_1_level_two.add_widget(Button(on_press=(self.start), background_color=(0, 0, 0, 0)))
        self.start_box_level_two.add_widget(self.start_box_1_level_two)

        item_coin_box_level_two = BoxLayout(padding=(x * 4, y / 5, x, y * 7))
        item_coin_box_level_two.add_widget(Image(source=('Design Screen/монетка.zip'), anim_delay=.1,
                                        allow_stretch=False,
                                        keep_ratio=False,
                                        keep_data=True))

        self.coin_image_box_level_two = BoxLayout(padding=(x * 5, 0, 0, y * 7))
        self.coin_image_count_level_two = Label(text=str(self.coin_count_level_two), font_size='30sp', color=(0, 0, 0, 1), bold=(12))
        self.coin_image_box_level_two.add_widget(self.coin_image_count_level_two)
        self.second_level_screen.add_widget(self.coin_image_box_level_two)
        self.second_level_screen.add_widget(item_coin_box_level_two)

        self.man_poses_image_level_two = BoxLayout(padding=(x, y, x, y * 2))
        self.second_level_screen.add_widget(self.man_poses_image_level_two)

        self.swipe_level_two = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                      on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                      on_touch_down=self.on_touch_down)

        self.second_level_screen.add_widget(self.swipe_level_two)
        self.second_level_screen.add_widget(self.start_box_level_two)
        self.second_level.add_widget(self.second_level_screen)













































        #Создаем экран с поражением
        self.game_over_menu = Screen(name = 'Defeat')
        self.game_over_menu_box = BoxLayout(padding=(150, 300, 150, 250))
        self.game_over_image = Image(source=('Design Screen/Game_over.png'))
        self.game_over_menu_box.add_widget(Button(background_color=(0, 0, 0, 0), on_press=self.restart_level))
        self.game_over_menu_box.add_widget(Button(background_color=(0, 0, 0, 0), on_press=self.press_HOME))
        self.game_over_menu.add_widget(self.game_over_image)
        self.game_over_menu.add_widget(self.game_over_menu_box)

        # Создаем экран с победой
        self.win_menu = Screen(name='Win')
        self.win_menu_box = BoxLayout(padding=(x*2, y*4.5, x*2, y*2.5))
        self.win_image = Image(source=('Design Screen/Win_screen.png'))
        self.win_menu_box.add_widget(Button(background_color=(255, 255, 255, 0), on_press=self.press_HOME))
        light_test = MainWidget()
        self.win_menu.add_widget(light_test)
        self.win_menu.add_widget(self.win_image)
        self.win_menu.add_widget(self.win_menu_box)


        self.sm = ScreenManager(transition=FadeTransition())

        #Первый экран
        self.main_screen = Screen(name='first')
        first_screen = RelativeLayout()

        #кнопка персонажа
        character_box = BoxLayout(padding=(0, y*7, x*4, 0))
        character_button = Button(on_press = self.press_ME, background_color=(0, 0, 0, 0))
        character_box.add_widget(character_button)

        # Кнопка Options
        options_box =  BoxLayout(padding=(0, 0, x*5, y*7))
        options_button = Button(on_press=self.press_OPTIONS, background_color=(0, 0, 0, 0))
        options_box.add_widget(options_button)

        #Кнопка выбора уровня
        play_box = BoxLayout(padding=(0, y, 0, y))
        play_button = Button(on_press=self.press_TAP_TO_START, background_color=(0, 0, 0, 0))

        play_box.add_widget(play_button)

        #Кнопка открытия магазина
        shop_box = BoxLayout(padding=(x*4, y*7, 0, 0))
        shop_button = Button(on_press=self.press_SHOP_BUTTON, background_color=(0, 0, 0, 0))
        shop_box.add_widget(shop_button)


        # Добавить кнопки и картинку на первый экран
        first_screen.add_widget(options_box)
        first_screen.add_widget(play_box)
        first_screen.add_widget(character_box)
        first_screen.add_widget(shop_box)
        self.main_screen.add_widget(Image(source=('Design Screen/первый фон.zip'),anim_delay = .1,  allow_stretch=True,
                                          keep_ratio=False,
                                          keep_data=True))
        self.main_screen.add_widget(Image(source=('Design Screen/First_screen.png'),  allow_stretch = True,
                                                    keep_ratio = False,
                                                    keep_data = True))
        self.main_screen.add_widget(first_screen)

        # Экран персонажа
        self.character_screen = Screen(name='character')
        # Конпка Menu
        choose_character_buttons = RelativeLayout()
        self.menu_box = BoxLayout(padding=(0, 0, x*5, y*7))
        menu_ralative = RelativeLayout()

        menu_button = Button(on_press=self.press_menu, background_color=(0, 0, 0, 0))
        menu_ralative.add_widget(Image(source=("Design Screen/menu button.png")))
        menu_ralative.add_widget(menu_button)

        self.menu_box.add_widget(menu_ralative)


        # Виджет Menu падающий с экрана
        self.menu_image = RelativeLayout(pos =(0, y*8))
        self.menu_image.add_widget(Image(source=("Images/menu_pause.png")))
        self.menu_screen_box = BoxLayout(padding = (x, y*4, x, y*3), spacing = x/2)
        # Кнопка поднимающая меню вверх
        self.menu_screen_box.add_widget(Button(on_press=self.restart_level, background_color=(0, 0, 0, 0)))
        # Кнопка возвращающая к первому экрану
        self.menu_screen_box.add_widget(Button(on_press=self.press_HOME, background_color=(0, 0, 0, 0)))
        self.menu_screen_box.add_widget(Button(on_press=self.press_menu_continue, background_color=(0, 0, 0, 0)))

        # Добавить кнопки и картинку на второй экран
        self.menu_image.add_widget(self.menu_screen_box)
        self.character_screen.add_widget(Image(source=('Design Screen/выбор скина 1.png')))
        self.skin_button_box = BoxLayout(padding = (x*4.5, y*3.3, x*0.8, y*3.8))
        self.skin_button_box.add_widget(Button(on_press=self.press_change_skin, background_color=(0, 0, 0, 0)))
        return_back_character = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_character.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .3)))
        self.character_screen.add_widget(return_back_character)
        self.character_screen.add_widget(self.skin_button_box)

        # Экран Options
        options = Screen(name='options')
        # Кнопка возврата на первый экран
        return_first_screen = BoxLayout(padding=(x*0.5, y*0.5, x*4.5, y*6.5))
        return_first_screen.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .5)))

        # Добавить кнопки и картинку на экран опций
        options.add_widget(Image(source=('Design Screen/Options_screen.png')))
        options.add_widget(return_first_screen)

        """Изоражение 1 скина"""
        self.first_skin = Screen(name='first_skin')
        self.first_skin.add_widget(Image(source=('Design Screen/1 скин.png')))

        """Изоражение 2 скина"""
        self.second_skin = Screen(name='second_skin')
        self.second_skin.add_widget(Image(source=('Design Screen/2 скин.png')))

        """Изоражение 3 скина"""
        self.third_skin = Screen(name='three_skin')
        self.third_skin.add_widget(Image(source=('Design Screen/1 скин.png')))

        """Изоражение 4 скина"""
        self.fourth_skin = Screen(name='four_skin')
        self.fourth_skin.add_widget(Image(source=('Design Screen/2 скин.png')))


        #экран c меню персонажа
        self.skin_screen = Screen(name='skin')
        self.skin_screen.add_widget(Image(source=('Design Screen/выбор скина 1.png')))
        self.screen_box = BoxLayout(padding = (x*0.5, y*1.5, x, y*2))

        self.screen_for_skins = ScreenManager()

        self.screen_for_skins.add_widget(self.first_skin)
        self.screen_for_skins.add_widget(self.second_skin)
        self.screen_for_skins.add_widget(self.third_skin)
        self.screen_for_skins.add_widget(self.fourth_skin)

        self.count_skin = 0
        self.one_skin = True
        self.two_skin = False
        self.three_skin = False
        self.four_skin = False

        self.skins = [self.one_skin, self.two_skin, self.three_skin, self.four_skin]

        self.skin_screen_boxes = BoxLayout(padding = (x*3.2, y*6.5, x*0.8, y))
        self.skin_screen_boxes.add_widget(Button(on_press=self.press_change_skin_for_game,  background_color=(0, 0, 0, 0)))

        self.screen_box.add_widget(self.screen_for_skins)
        self.character_screen.add_widget(self.screen_box)
        self.character_screen.add_widget(self.skin_screen_boxes)

        # Экран с выбором уровня
        self.menu_select_level_screen = Screen(name='Menu_select_level')
        self.menu_select_level_screen.add_widget(Image(source=('Design Screen/первый фон.zip'), anim_delay=.1, allow_stretch=True,
                                          keep_ratio=False,
                                          keep_data=True))
        self.menu_select_level_screen.add_widget(Image(source=('Design Screen/Select_screen.png')))
        self.play_game = BoxLayout(padding=(x, y*2, x, y*4))
        self.play_game.add_widget(Button(background_color=(0, 0, 0, 0), on_press=(self.start_level)))
        self.play_game.add_widget(Button(background_color=(0,0,0, 0)))
        return_back_map = BoxLayout(padding=(0, 0, x*5, y*7))
        return_back_map.add_widget(Button(on_press=self.press_RETURN, background_color=(66, 66, 66, .5)))
        self.menu_select_level_screen.add_widget(self.play_game)
        self.menu_select_level_screen.add_widget(return_back_map)

        # Присваивание значений для анимации кнопок
        #Экран магазина
        self.items_screen = Screen(name=('items'))
        self.items_screen.add_widget(Image(source=('Design Screen/Items_screen.png')))
        return_back_shop = BoxLayout(padding=(0, 0, x*5, y*7))
        return_back_shop.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .5)))
        items_select_shop_box = BoxLayout(padding = (x, y*7, x, 0))
        items_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.items_screen.add_widget(return_back_shop)
        self.items_screen.add_widget(items_select_shop_box)

        #экран обуви
        self.shues_screen = Screen(name=('shues'))
        self.shues_screen.add_widget(Image(source=('Design Screen/Shues_screen.png')))
        return_back_shues = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_shues.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        shues_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        shues_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.shues_screen.add_widget(return_back_shues)
        self.shues_screen.add_widget(shues_select_shop_box)

        #экран одежды
        self.clothes_screen = Screen(name=('clothes'))
        self.clothes_screen.add_widget(Image(source=('Design Screen/Clothes_screen.png')))
        return_back_clothes = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_clothes.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.clothes_screen.add_widget(return_back_clothes)
        self.clothes_screen.add_widget(clothes_select_shop_box)

        #экран улучшений
        self.upgrades_screen = Screen(name=('upgrades'))
        self.upgrades_screen.add_widget(Image(source=('Design Screen/Upgrade_screen.png')))
        return_back_upgrades = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_upgrades.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.upgrades_screen.add_widget(return_back_upgrades)
        self.upgrades_screen.add_widget(upgrades_select_shop_box)

        #магазин
        self.store_screen = Screen(name=('store'))
        self.store_screen.add_widget(Image(source=('Design Screen/Store_screen.png')))
        store_back_upgrades = BoxLayout(padding=(0, 0, x * 5, y * 7))
        store_back_upgrades.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        store_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        store_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.store_screen.add_widget(store_back_upgrades)
        self.store_screen.add_widget(store_select_shop_box)

        #Добавляем экраны к ScreenManager
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.character_screen)
        self.sm.add_widget(self.skin_screen)
        self.sm.add_widget(self.items_screen)

        self.sm.add_widget(self.shues_screen)
        self.sm.add_widget(self.clothes_screen)
        self.sm.add_widget(self.upgrades_screen)
        self.sm.add_widget(self.store_screen)

        self.sm.add_widget(options)
        self.sm.add_widget(self.menu_select_level_screen)
        """self.sm.add_widget(self.america_screen)"""
        self.sm.add_widget(self.first_level)
        self.sm.add_widget(self.second_level)
        self.sm.add_widget(self.game_over_menu)
        self.sm.add_widget(self.win_menu)
        self.sm.add_widget(self.maps_image_screen)

        self.count_screen = [ self.main_screen, self.game_over_menu,
                             self.win_menu,  self.character_screen, self.skin_screen,
                             self.items_screen, self.first_level]

        self.level_count = 1
        self.levels = [self.first_level, self.second_level]
        self.level_screen = [self.first_level_screen, self.second_level_screen]
        self.level_screen_child = [self.first_level_screen_child, self.second_level_screen_child]

        self.start_boxes = [self.start_box_level_one, self.start_box_level_two]
        self.knight_image_boxes = [self.knight_image_box_level_one, self.knight_image_box_level_two]
        self.knight_box = [self.knight_box_level_one, self.knight_box_level_two]
        self.knight_image_start = [self.knight_image_start_level_one, self.knight_image_start_level_two]
        self.knight_image_walk = [self.knight_image_walk_level_one, self.knight_image_walk_level_two]
        self.knight_image_jump = [self.knight_image_jump_level_one, self.knight_image_jump_level_two]
        self.knight_image_end = [self.knight_image_end_level_one, self.knight_image_end_level_two]
        self.knight_image_sit = [self.knight_image_sit_level_one, self.knight_image_sit_level_two]

        self.knight_box_button = [self.knight_box_button_level_one, self.knight_box_button_level_two]
        self.climb_screen = [self.climb_screen_level_one, self.climb_screen_level_two]


        self.sky_box = [self.sky_box_level_one, self.sky_box_level_two]

        self.coins = [self.coins_level_one, self.coins_level_two]
        self.coin_boxes = [self.coin_boxes_level_one, self.coin_boxes_level_two ]
        self.coin_image_boxes = [self.coin_image_box_level_one, self.coin_image_box_level_two]

        self.coin_image_count = [self.coin_image_count_level_one, self.coin_image_count_level_two]
        self.wall_box = [self.wall_box_level_one, self.wall_box_level_two]
        self.maps_button_box = [self.maps_button_box_level_one, self.maps_button_box_level_two]

        self.frags_level_one = [self.frag_level_one, self.frag_1_level_one, self.frag_2_level_one]
        self.frags_image_level_one = [self.frages_box_image_level_one, self.frages_box_image_1_level_one, self.frages_box_image_2_level_one]

        self.frags_level_two = [self.frag_level_two, self.frag_1_level_two, self.frag_2_level_two]
        self.frags_image_level_two = [self.frages_box_image_level_two, self.frages_box_image_1_level_two, self.frages_box_image_2_level_two]

        self.frags = [self.frags_level_one, self.frags_level_two]
        self.frags_image = [self.frags_image_level_one,self.frags_image_level_two]

        self.heart_boxes = [self.heart_boxes_level_one, self.heart_boxes_level_two]

        self.swipe = [self.swipe_level_one,self.swipe_level_two]

        self.frag_flags = [self.frag_one, self.frag_two, self.frag_three]

        return self.sm



if __name__ == '__main__':
    Climbing().run()