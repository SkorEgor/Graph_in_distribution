import numpy as np


class ObjectsAntennasField:
    def __init__(self, pixmap, painter):
        # Массив 256 * 256
        size_distribution = 256
        mass = np.zeros(size_distribution, dtype="uint16")

        # Параметры поля
        self.cells_width = 15
        self.cells_height = 15
        self.maximum_radius_value_x = size_distribution -1
        self.maximum_radius_value_y = size_distribution - 1

        # Объекты для рисования
        self.pixmap = pixmap
        self.painter = painter
