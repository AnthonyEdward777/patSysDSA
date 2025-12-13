import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ScrollableListApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scrollable List Viewer")
        self.geometry("350x520") # Increased height to fit the button

        self.patientList = LinkedList()
        self.patientList.admitPatient("Eyad", 20, "eyad.mahmoud24d@eslsca.edu.eg", "Back Pain", 2, 5)
        self.is_sorted = False # Track the current sort state

        # --- 1. Create the Sort Button ---
        self.sort_button = ctk.CTkButton(
            self,
            text="Sort List (Ascending)",
            command=self.sort_list
        )
        self.sort_button.pack(pady=(20, 10), padx=20) # Top padding (20), Bottom padding (10)

        self.scroll_frame = ctk.CTkScrollableFrame(
            self, 
            label_text="List Contents", 
            width=300, 
            height=400,
            corner_radius=10
        )
        self.scroll_frame.pack(pady=(10, 20), padx=20, fill="both", expand=True)

        self.create_list_widgets()

    def clear_widgets(self):
        """Destroys all child widgets inside the scrollable frame."""
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

    def create_list_widgets(self):
        """Creates a CTkLabel for each item in the data_list."""
        
        self.scroll_frame.columnconfigure(0, weight=1)

        for index, item_value in enumerate(self.patientList):
            
            item_label = ctk.CTkLabel(
                self.scroll_frame, 
                text=str(item_value), # Convert integer to string for display
                font=("Roboto", 14),
                anchor="w"
            )
            
            item_label.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

    def sort_list(self):
        """Sorts the data list and reloads the widgets."""
        
        self.clear_widgets()
        
        if not self.is_sorted:
            self.patientList.sort()
            self.sort_button.configure(text="Sort List (Descending)")
            self.is_sorted = True
        else:
            self.patientList.sort(reverse=True)
            self.sort_button.configure(text="Sort List (Ascending)")
            self.is_sorted = False
            
        self.create_list_widgets()
        print(f"List sorted. New order: {self.patientList}")


if __name__ == "__main__":
    app = ScrollableListApp()
    app.mainloop()