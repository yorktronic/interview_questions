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

MY_RECTANGLE3 = {'left_x': 0,
                 'bottom_y': 0,
                 'width': 2,
                 'height': 3}

MY_RECTANGLE4 = {'left_x': 3,
                 'bottom_y': 4,
                 'width': 3,
                 'height': 9}

# My solution, faster and simple than IC

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

# IC's solution, slower than mine

def find_range_overlap(point1, length1, point2, length2):

    # find the highest start point and lowest end point.
    # the highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # the lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return (None, None)

    # compute the overlap length
    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)

def find_rectangular_overlap(rect1, rect2):

    # get the x and y overlap points and lengths
    x_overlap_point, overlap_width  = find_range_overlap(\
        rect1['left_x'], rect1['width'],  rect2['left_x'], rect2['width'])
    y_overlap_point, overlap_height = find_range_overlap(\
        rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])

    # return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    return {
        'left_x': x_overlap_point,
        'bottom_y': y_overlap_point,
        'width': overlap_width,
        'height': overlap_height,
    }