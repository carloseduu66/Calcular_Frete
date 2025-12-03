# Main application entry point
# Orchestrates the GUI and business logic

import tkinter as tk
from src.gui import FreteCalculatorUI


def main():
    """Initialize and run the application."""
    root = tk.Tk()
    app = FreteCalculatorUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
