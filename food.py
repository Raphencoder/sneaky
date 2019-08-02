import random

class FoodSpawer:
    def __init__(self, SCREEN_LENGTH, MIDDLE_SCREEN):
        self.screen = SCREEN_LENGTH
        self.middle_screen = MIDDLE_SCREEN
        self.position = [random.randrange(1, self.screen / 20) * 20, random.randrange(1, self.screen / 20) * 20]
        self.isFoodOnScreen = True

    def spawn_food(self, snake_body):
        if self.isFoodOnScreen is False:
            self.position = [random.randrange(1, self.screen / 20) * 20, random.randrange(1, self.screen / 20) * 20]
            if self.position in snake_body:
                self.spawn_food(snake_body)
            self.isFoodOnScreen = True
        return self.position