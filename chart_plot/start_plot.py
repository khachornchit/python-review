import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Create a Tkinter window
root = tk.Tk()
root.title("Sin Function")

# Generate data points
x = np.linspace(0, 20, 100)

# Plot the sine wave
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, np.sin(x))

# Embed the Matplotlib plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Maximize the Tkinter window
root.state('zoomed')

# Run the Tkinter event loop
root.mainloop()
