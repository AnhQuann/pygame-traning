game_objects = []

def add(obj):
    game_objects.append(obj)

def update():
    print(len(game_objects))
    for obj in game_objects:
        obj.update()

def collide_with(box_collider, obj_type):
    for obj in game_objects:
        if obj.box_collider is not None:
            if obj.box_collider.collide_with(box_collider) and type(obj) == obj_type:
                return obj
    
    return None

def recycle(obj_type, x, y):
    for obj in game_objects:
        if type(obj) == obj_type and not obj.is_active:
            obj.is_active = True
            obj.x = x
            obj.y = y
            return obj

    new_obj = obj_type(x, y)
    add(new_obj)
    return new_obj


def render(canvas):
    for obj in game_objects:
        obj.render(canvas)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.is_active = True
        self.box_collider = None

    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        if self.image is not None and self.is_active:
            width = self.image.get_width()
            height = self.image.get_height()

            render_pos = (self.x - width / 2, self.y - height / 2)

            canvas.blit(self.image, render_pos)

        if self.box_collider is not None:
            self.box_collider.render(canvas)

    def deactivate(self):
        self.is_active = False
