
import statistics


def better_than_averave (class_points, your_points):
    class_points.append(your_points)
    # average = sum(class_points)/len(class_points)
    average = statistics.mean(class_points)
    return True if your_points>average else False
    
    
print(better_than_averave([100, 40, 34, 57, 29, 72, 57, 88], 75))