import numpy as np

def interpolate_points(points):
    interpolated_points = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        interpolated_points.append((x1, y1))
        interpolated_points.append(((x1 + x2) / 2, (y1 + y2) / 2))
    interpolated_points.append(points[-1])  # Include the last point as well
    return interpolated_points

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        tab = [float( line.strip() )for line in file]

        for i in range(0, len(tab),2):
            x = tab[i]
            y = tab[i+1]
            
            points.append((x, y))
    return points

def write_points_to_file(filename, points):
    with open(filename, 'w') as file:
        for point in points:
            file.write(f'{point[0]} {point[1]}\n')

def interpolate_points_in_file(input_file, output_file):
    points = read_points_from_file(input_file)
    interpolated_points = interpolate_points(points)
    write_points_to_file(output_file, interpolated_points)

# Example usage
input_filename = 'GPS.txt'
output_filename = 'output.txt'
interpolate_points_in_file(input_filename, output_filename)
