from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum, unique

import numpy as np


@unique
class DeleteMeshOption(IntEnum):
    """Option to delete the mesh inside a polygon """

    """Delete all nodes inside the polygon. """
    ALL_NODES = 0

    """ Delete all faces of which the circum center is inside the polygon """
    ALL_FACE_CIRCUMCENTERS = 1

    """ Delete all faces of which the complete face is inside the polygon. """
    ALL_COMPLETE_FACES = 2


@unique
class ProjectToLandBoundaryOption(IntEnum):
    """Option how to project to the land boundary."""

    DO_NOT_PROJECT_TO_LANDBOUNDARY = 0
    TO_ORIGINAL_NETBOUNDARY = 1
    OUTER_MESH_BOUNDARY_TO_LANDBOUNDARY = 2
    INNER_AND_OUTER_MESH_BOUNDARY_TO_LANDBOUNDARY = 3
    WHOLE_MESH = 4


@dataclass
class Mesh2d:
    """This class is used for getting and setting two-dimensional mesh data

    Attributes:
        node_x (np.ndarray(double)): The x-coordinates of the nodes.
        node_y (np.ndarray(double)): The y-coordinates of the nodes.
        edge_nodes (np.ndarray(int)): The nodes composing each mesh 2d edge.

        face_nodes (np.ndarray(int), optional): The nodes composing each mesh 2d face.
        nodes_per_face (np.ndarray(int), optional): The nodes composing each mesh 2d face.
        edge_x (np.ndarray(double), optional): The x-coordinates of the mesh edges' middle points.
        edge_y (np.ndarray(double), optional): The x-coordinates of the mesh edges' middle points.
        face_x (np.ndarray(double), optional): The x-coordinates of the mesh faces' mass centers.
        face_y (np.ndarray(double), optional): The y-coordinates of the mesh faces' mass centers.

    """

    node_x: np.ndarray
    node_y: np.ndarray
    edge_nodes: np.ndarray
    face_nodes: np.ndarray = np.empty(0, dtype=np.int32)
    nodes_per_face: np.ndarray = np.empty(0, dtype=np.int32)
    edge_x: np.ndarray = np.empty(0, dtype=np.double)
    edge_y: np.ndarray = np.empty(0, dtype=np.double)
    face_x: np.ndarray = np.empty(0, dtype=np.double)
    face_y: np.ndarray = np.empty(0, dtype=np.double)


@dataclass
class GeometryList:
    """A class to describe a list of geometries.

    Attributes:
        x_coordinates (np.ndarray(np.double)): The x coordinates.
        y_coordinates (np.ndarray(np.double)): The y coordinates.
        geometry_separator (float, optional): The value used as a separator in the coordinates. Default is `-999.0`
        inner_outer_separator (float, optional): The value used to separate the inner part of a polygon from its outer
                                                 part. Default is `-998.0`
    """

    x_coordinates: np.ndarray
    y_coordinates: np.ndarray
    geometry_separator: float = -999.0
    inner_outer_separator: float = -998.0


@dataclass
class OrthogonalizationParameters:
    """A class holding the parameters for orthogonalization.

    Attributes:
        outer_iterations (int): Number of outer iterations in orthogonalization. Increase this parameter for complex
                                grids..
        boundary_iterations (int): Number of boundary iterations in grid/net orthogonalization within itatp.
        inner_iterations (int): Number of inner iterations in grid/net orthogonalization within itbnd.
        orthogonalization_to_smoothing_factor (float): Factor from 0 to 1. between grid smoothing and grid
                                                       orthogonality.
        orthogonalization_to_smoothing_factor_at_boundary (float): Minimum ATPF on the boundary.
        areal_to_angle_smoothing_factor (float): Factor between smoother 1d0 and area-homogenizer 0d0.
    """

    outer_iterations: int
    boundary_iterations: int
    inner_iterations: int
    orthogonalization_to_smoothing_factor: float
    orthogonalization_to_smoothing_factor_at_boundary: float
    areal_to_angle_smoothing_factor: float
