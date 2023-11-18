import tkinter as tk
from tkinter import ttk

class AppleProductGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Product Selector")

        # Creating variables to store user input
        self.selected_category = tk.StringVar()
        self.selected_model = tk.StringVar()

        # Dictionary to store models for each category
        self.product_models = {
            "iPhone": ["iPhone SE","iPhone 7","iPhone 8","iPhone X","iPhone 11","iPhone 12", "iPhone 13", "iPhone 14","iPhone 15",],
            "MacBook": ["MacBook Air", "MacBook Pro 13", "MacBook Pro 16"],
            "iPad": ["iPad", "iPad Air", "iPad Pro", "iPad Mini", "Apple Pencil "],
            "Apple Watch": ["Series 3", "SE", "Series 7"]
        }

        # Creating GUI components
        self.create_widgets()

        #sets initial model based on the default catagory
        self.update_models(None)

    def create_widgets(self):
        # Label for category selection
        category_label = ttk.Label(self.root, text="Select Apple Product Category:")
        category_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Combobox for category selection
        categories = list(self.product_models.keys())
        category_combobox = ttk.Combobox(self.root, values=categories, textvariable=self.selected_category)
        category_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        category_combobox.set(categories[0])  # Set default value

        # Event binding to update models when the category changes
        category_combobox.bind("<<ComboboxSelected>>", self.update_models)

        # Label for model selection
        model_label = ttk.Label(self.root, text="Select Apple Product Model:")
        model_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Combobox for model selection
        self.model_combobox = ttk.Combobox(self.root, textvariable=self.selected_model)
        self.model_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Button to submit user input
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_input)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_models(self, event):
        # Update the model Combobox based on the selected category
        selected_category = self.selected_category.get()
        models = self.product_models.get(selected_category, [])
        self.model_combobox['values'] = models
        self.selected_model.set(models[0] if models else "")  # Set default value

    def submit_input(self):
        # Retrieve and print the user's selected category and model
        selected_category = self.selected_category.get()
        selected_model = self.selected_model.get()

        if selected_category and selected_model:
            print(f"Selected Category: {selected_category}")
            print(f"Selected Model: {selected_model}")
        else:
            print("Please select a category and enter a model.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppleProductGUI(root)
    root.mainloop()
