import tkinter as tk
from tkinter import Canvas
import math

class CompassApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compass")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a1a")

        self.canvas = Canvas(root, width=400, height=400, bg="#1a1a1a", highlightthickness=0)
        self.canvas.pack()

        # Draw the compass background
        self.draw_compass()

    def draw_compass(self):
        center_x, center_y = 200, 200
        radius = 150

        # Outer circle
        self.canvas.create_oval(center_x - radius, center_y - radius,
                                center_x + radius, center_y + radius,
                                outline="#f0f0f0", width=3)

        # Cardinal points
        self.canvas.create_text(center_x, center_y - radius - 20, text="N", fill="red", font=("Arial", 16, "bold"))
        self.canvas.create_text(center_x, center_y + radius + 20, text="S", fill="white", font=("Arial", 16, "bold"))
        self.canvas.create_text(center_x - radius - 20, center_y, text="W", fill="white", font=("Arial", 16, "bold"))
        self.canvas.create_text(center_x + radius + 20, center_y, text="E", fill="white", font=("Arial", 16, "bold"))

        # Draw compass ticks
        for angle in range(0, 360, 15):
            x1 = center_x + radius * math.cos(math.radians(angle))
            y1 = center_y - radius * math.sin(math.radians(angle))
            x2 = center_x + (radius - 10) * math.cos(math.radians(angle))
            y2 = center_y - (radius - 10) * math.sin(math.radians(angle))
            color = "white" if angle % 45 != 0 else "red"
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

        # Draw pointer (initially pointing north)
        self.pointer = self.canvas.create_line(center_x, center_y,
                                               center_x, center_y - radius + 20,
                                               fill="red", width=4)

    def update_pointer(self, direction_angle):
        center_x, center_y = 200, 200
        radius = 150

        # Calculate new pointer position
        x = center_x + (radius - 20) * math.sin(math.radians(direction_angle))
        y = center_y - (radius - 20) * math.cos(math.radians(direction_angle))

        # Update pointer
        self.canvas.coords(self.pointer, center_x, center_y, x, y)

if __name__ == "__main__":
    root = tk.Tk()
    app = CompassApp(root)

    # Simulate pointer update (for demonstration)
    import time
    import threading

    def simulate_rotation():
        angle = 0
        while True:
            app.update_pointer(angle)
            angle = (angle + 1) % 360
            time.sleep(0.05)

    threading.Thread(target=simulate_rotation, daemon=True).start()

    root.mainloop()
