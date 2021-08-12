import csv
from typing import List

import yaml

from options import VesselDetectorOptions
from results import VesselDetectorResult


def write_results(results: List[VesselDetectorResult], options: VesselDetectorOptions, stem: str):
    # YAML
    yaml_path = f"{stem}.results.yml"
    print(f"Writing YAML file: {yaml_path}")
    with open(yaml_path, 'w') as file:
        yaml.dump(results, file, default_flow_style=False)

    # CSV
    csv_path = f"{stem}.results.csv"
    print(f"Writing CSV file: {csv_path}")
    with open(csv_path, 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name', 'Area', 'Center of Mass', 'Convex Hull Area', 'Convex Hull Vertices', 'Ellipse Angle', 'Ellipse Center', 'Ellipse Eccentricity', 'Ellipse Major Axis', 'Ellipse Minor Axis', 'Width', 'Height', 'Max Width', 'Max Height', 'In Bounds', 'Longest Path', 'Perimeter', 'Solidity'])
        for result in results:
            writer.writerow([result.name, result.area, result.center_of_mass, result.convex_hull_area, result.convex_hull_vertices, result.ellipse_angle, result.ellipse_center, result.ellipse_eccentricity, result.ellipse_major_axis, result.ellipse_minor_axis, result.width, result.height, result.max_width, result.max_height, result.in_bounds, result.longest_path, result.perimeter, result.solidity,])
