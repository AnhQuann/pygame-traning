game_objects = []

def add(obj):
    game_objects.append(obj)

def update():
    print(len(game_objects))
    for obj in game_objects:
        obj.update()

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
        if obj.image is not None and obj.is_active:
            width = obj.image.get_width()
            height = obj.image.get_height()

            render_pos = (obj.x - width / 2, obj.y - height / 2)

            canvas.blit(obj.image, render_pos)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.is_active = True

    def deactivate(self):
        self.is_active = False
