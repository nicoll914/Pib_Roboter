import numpy as np
import pib_ik
from pib_ik import ImageConfig, Sketch, Stroke, PaperConfig, TrajectoryConfig, IKConfig


trajectoryConfig = TrajectoryConfig(
    paper=PaperConfig(
        size=0.02, # sehr kleines Papier verschiedene Werte getestet -> out of reach
        drawing_scale=0.7, # Skalierungsfaktor 0.7 innerhalb Papiergrenzen
        lift_height=0.015, # Hebehöhe Stift bei absetzen
        height_z=0.6, # 60 cm über ??? werte 0.2 - 1 getestet -> out of reach
        start_x=0.15 # 15cm vor RobotBase
    ),
    ik=IKConfig(
        #max_iterations=150, # stürzt leider trotzdem ab
        tolerance=0.005,
    ),
    point_density=0.01,
)

def translate_sketch(sketch, dx, dy):
    """Move all strokes in a sketch."""
    new_strokes = []
    for stroke in sketch:
        translated = stroke.points + np.array([dx, dy])
        new_strokes.append(Stroke(points=translated, closed=stroke.closed))
    return Sketch(strokes=new_strokes, source_size=sketch.source_size)


def scale_sketch(sketch, scale_x, scale_y):
    """Scale all strokes in a sketch."""
    new_strokes = []
    for stroke in sketch:
        scaled_points = stroke.points.copy()
        scaled_points[:, 0] *= scale_x
        scaled_points[:, 1] *= scale_y
        new_strokes.append(Stroke(points=scaled_points, closed=stroke.closed))
    return Sketch(strokes=new_strokes, source_size=sketch.source_size)

# Sketch erstellen -> Debugging hat Fehler bei ursprünglichen Bildern ergeben -> neue Bilder verwendet welche einen Sketch ergaben
sketch = pib_ik.image_to_sketch("/home/user/Desktop/pib robot/my_project/controllers/my_controller/123.jpg")

# Sketch Debugausgabe
print(f"Number of strokes: {len(sketch)}")
print(f"Total points: {sketch.total_points()}")
print(f"Total length: {sketch.total_length():.2f}")
print(f"Bounding box: {sketch.bounds()}")

#centered = translate_sketch(sketch, 0.1, 0.1)
#scaled = scale_sketch(centered, 0.12, 0.12)

# Trajectory aus Sketch erstellen 
trajectory = pib_ik.sketch_to_trajectory(sketch, trajectoryConfig)

# Trajectory ausgeben zur verwendung in Webots
trajectory.to_json("/home/user/Desktop/pib robot/my_project/controllers/my_controller/output_testkkreis.json")
