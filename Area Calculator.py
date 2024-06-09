import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.widgets import PolygonSelector, Button

class AreaCalculator:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Draw your shape')

        self.polygon = Polygon([(0, 0)], closed=True, fill=None, edgecolor='r')
        self.ax.add_patch(self.polygon)

        self.area_label = self.ax.text(0.05, 0.95, 'Area: 0.00', transform=self.ax.transAxes)

        self.selector = PolygonSelector(self.ax, self.onselect)
        self.erase_button_ax = self.fig.add_axes([0.81, 0.05, 0.1, 0.075])
        self.erase_button = Button(self.erase_button_ax, 'Erase')
        self.erase_button.on_clicked(self.erase_polygon)

        plt.show()

    def onselect(self, verts):
        if len(verts) > 2:
            self.polygon.set_xy(verts)
            area = self.calculate_area(verts)
            self.area_label.set_text(f"Area: {area:.2f}")
        else:
            self.area_label.set_text("Area: 0.00")
        self.fig.canvas.draw()

    def calculate_area(self, verts):
        x = np.array([v[0] for v in verts])
        y = np.array([v[1] for v in verts])
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def erase_polygon(self, event):
        self.polygon.set_xy([(0, 0)])
        self.area_label.set_text("Area: 0.00")
        self.fig.canvas.draw_idle()

AreaCalculator()
