game_objects = []

def add(obj):
    game_objects.append(obj)

def update():
    for obj in game_objects:
        obj.update()

def render(canvas):
    for obj in game_objects:
        canvas.blit(obj.image, (obj.x, obj.y))