import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser on Canvas")

        # Canvas setup
        self.canvas = tk.Canvas(root, width=700, height=700, bg="pink")
        self.canvas.pack()

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_canvas)
        self.reset_button.pack(pady=10)

        # Grid settings
        self.cell_size = 10  # Size of each grid cell
        self.rows = self.canvas.winfo_reqheight() // self.cell_size
        self.cols = self.canvas.winfo_reqwidth() // self.cell_size

        # Draw grid of blue cells
        self.cells = {}  # Dictionary to store cell references
        self.create_grid()

        # Create an eraser
        self.eraser_size = 10  # Eraser size
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, outline="white", width=2)

        # Bind mouse movement
        self.canvas.bind("<B1-Motion>", self.erase)  # Left mouse drag

    def create_grid(self):
        """Create a grid of blue squares."""
        self.cells.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white")
                self.cells[(row, col)] = cell  # Store reference

    def erase(self, event):
        """Move the eraser and erase any blue cells it touches."""
        x1, y1 = event.x - self.eraser_size // 2, event.y - self.eraser_size // 2
        x2, y2 = x1 + self.eraser_size, y1 + self.eraser_size

        # Move the eraser
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase cells in contact
        for (row, col), cell in self.cells.items():
            cell_coords = self.canvas.coords(cell)
            if self.overlaps(x1, y1, x2, y2, cell_coords):
                self.canvas.itemconfig(cell, fill="white")  # Change color to white

    def reset_canvas(self):
        """Reset the grid to its original state."""
        self.canvas.delete("all")  # Clear everything
        self.create_grid()  # Recreate the grid
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, outline="black", width=2)

    def overlaps(self, x1, y1, x2, y2, rect_coords):
        """Check if two rectangles overlap."""
        rx1, ry1, rx2, ry2 = rect_coords
        return not (x2 < rx1 or x1 > rx2 or y2 < ry1 or y1 > ry2)

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
