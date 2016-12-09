# Rectangle intersection
MY_RECTANGLE1 = {'left_x': 1,
                'bottom_y': 5,
                'width': 10,
                'height': 4,
                }

MY_RECTANGLE2 = {'left_x': 8,
                 'bottom_y': 6,
                 'width': 3,
                 'height': 9}

def get_intersecting_rectangle(rect1, rect2):
    x_min = max(rect1['left_x'], rect2['left_x'])
    y_min = max(rect1['bottom_y'], rect2['bottom_y'])
    x_max = min(rect1['left_x'] + rect1['width'],
                rect2['left_x'] + rect2['width'])
    y_max = min(rect1['bottom_y'] + rect1['height'],
                rect2['bottom_y'] + rect2['height'])

    if (x_max < x_min) or (y_max < y_min):
        return None
    else:
        return {'left_x': x_min,
                'bottom_y': y_min,
                'width': x_max - x_min,
                'height': y_max - y_min}
