from typing import Tuple


class VesselDetectorResult:
    def __init__(
            self,
            name: str,
            area: float = None,
            center_of_mass: str = None,
            convex_hull_area: float = None,
            convex_hull_vertices: int = None,
            ellipse_angle: float = None,
            ellipse_center: str = None,
            ellipse_eccentricity: float = None,
            ellipse_major_axis: float = None,
            ellipse_minor_axis: float = None,
            width: int = None,
            height: int = None,
            max_width: int = None,
            max_height: int = None,
            in_bounds: bool = None,
            longest_path: int = None,
            perimeter: float = None,
            solidity: float = None):
        self.name = name
        self.area = area
        self.center_of_mass = center_of_mass
        self.convex_hull_area = convex_hull_area
        self.convex_hull_vertices = convex_hull_vertices
        self.ellipse_angle = ellipse_angle
        self.ellipse_center = ellipse_center
        self.ellipse_eccentricity = ellipse_eccentricity
        self.ellipse_major_axis = ellipse_major_axis
        self.ellipse_minor_axis = ellipse_minor_axis
        self.width = width
        self.height = height
        self.max_width = max_width
        self.max_height = max_height
        self.in_bounds = in_bounds
        self.longest_path = longest_path
        self.perimeter = perimeter
        self.solidity = solidity
