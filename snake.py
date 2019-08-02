class Snake:
    def __init__(self, SCREEN_LENGTH, MIDDLE_SCREEN):
        self.screen = SCREEN_LENGTH
        self.middle_screen = MIDDLE_SCREEN
        self.position = [self.middle_screen, self.middle_screen]
        self.body = [[self.middle_screen, self.middle_screen], [self.middle_screen - 10 , self.middle_screen], [self.middle_screen - 20, self.middle_screen]]
        self.direction = "RIGHT"

    def change_direction_to(self, direction):
        if direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"

        if direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"

        if direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"

        if direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self):
        if self.direction == "RIGHT":
            self.position[0] += 20

        if self.direction == "LEFT":
            self.position[0] -= 20

        if self.direction == "UP":
            self.position[1] -= 20

        if self.direction == "DOWN":
            self.position[1] += 20
        self.body.insert(0, list(self.position))


    def eat(self, food_pos):
        if self.position == food_pos:
            return 1
        else:
            self.body.pop()
            return 0

    def check_collision(self):
        if self.position[0] > self.screen - 10 or self.position[0] < 0:
            return 1
        elif self.position[1] > self.screen - 10 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

    def get_head(self):
        return self.position

    def get_body(self):
        return self.body
