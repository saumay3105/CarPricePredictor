import tkinter as tk
from tkinter import ttk

class CustomThemedTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = ttk.Style(self)
        self.configure(bg="black")  # Set the background color to black
        self.style.configure("TButton", padding=10, relief="flat")  # Modern button style

# Part 1: Import Libraries and Load Data
import pandas as pd
from sklearn import linear_model

data = pd.read_csv("cars.csv")
X = data[['Mileage', 'Doors', 'Cylinder']]
Y = data["Price"]
regr = linear_model.LinearRegression()
regr.fit(X, Y)

# Part 2: Define Prediction Function
def predict(x, y, z):
    predictedPrice = regr.predict([[x, y, z]])
    return int(predictedPrice[0])
def calculate_price():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    result = predict(num1, num2, num3)
    result_label.config(text=f"Predicted Price in $: {result}")
# Part 3: Create GUI with Custom Themed Tkinter
root = CustomThemedTk()
root.geometry("400x300")  # Adjust the size to your preference
root.title("Car Price Predictor")

frame = ttk.Frame(root)  # No need to set background here
frame.pack(pady=20)
frame.configure(style="Black.TFrame")  # Set the frame style to "Black.TFrame"

root.style = ttk.Style()
root.style.configure(
    "Black.TFrame",
    background="black",  # Set the background color of the frame to black
)

label1 = ttk.Label(frame, text="Enter Distance Travelled(in miles):", foreground="white", background="black")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = ttk.Entry(frame)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = ttk.Label(frame, text="Enter No. of Doors:", foreground="white", background="black")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = ttk.Entry(frame)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = ttk.Label(frame, text="Enter No. of Cylinders:", foreground="white", background="black")
label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry3 = ttk.Entry(frame)
entry3.grid(row=2, column=1, padx=10, pady=5)

calculate_button = ttk.Button(frame, text="Predict Price", command=calculate_price)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = ttk.Label(root, text="Predicted Price in $: ", foreground="white", background="black")
result_label.pack()



root.mainloop()
