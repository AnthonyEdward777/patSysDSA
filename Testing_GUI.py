import customtkinter as ctk
from linkedList import LinkedList
from tkinter import messagebox


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class HospitalApp(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("Smart Hospital System")
        self.geometry("1100x700")
        

        self.hospital = LinkedList()
        



        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)



        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1) 



        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="🏥 Patient Admission", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))


        self.entry_name = self.create_input("Patient Name", 1)
        self.entry_age = self.create_input("Age", 2)
        self.entry_contact = self.create_input("Contact Info (Email/Phone)", 3)
        self.entry_history = self.create_input("Medical History", 4)
        self.entry_room = self.create_input("Room Number", 5)
        self.entry_severity = self.create_input("Severity Score (1-10)", 6)


        self.btn_add = ctk.CTkButton(
            self.sidebar, 
            text="Admit Patient", 
            command=self.admit_patient_event,
            fg_color="#2CC985", 
            hover_color="#229A66",
            height=40,
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_add.grid(row=7, column=0, padx=20, pady=(30, 10), sticky="ew")

        self.btn_sort = ctk.CTkButton(
            self.sidebar, 
            text="Sort by Severity", 
            command=self.sort_patients_event,
            fg_color="#E04F5F", 
            hover_color="#B03E4A",
            height=40,
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_sort.grid(row=8, column=0, padx=20, pady=10, sticky="ew")




        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_area.grid_rowconfigure(1, weight=1)
        self.main_area.grid_columnconfigure(0, weight=1)

        
        self.header_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        self.lbl_dashboard = ctk.CTkLabel(
            self.header_frame, 
            text="Current Patients List", 
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.lbl_dashboard.pack(side="left")

        self.lbl_count = ctk.CTkLabel(
            self.header_frame, 
            text="Total: 0", 
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        self.lbl_count.pack(side="right", padx=10)

        
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.main_area, 
            label_text="Patient Cards",
            label_font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=15
        )
        self.scroll_frame.grid(row=1, column=0, sticky="nsew")
        self.scroll_frame.grid_columnconfigure(0, weight=1) 

        
        self.populate_demo_data()



    def create_input(self, placeholder, row):
        entry = ctk.CTkEntry(self.sidebar, placeholder_text=placeholder, height=35)
        entry.grid(row=row, column=0, padx=20, pady=8, sticky="ew")
        return entry

    def populate_demo_data(self):

        self.hospital.admitPatient("Mahmoud Eldeeb", 35, "Mahmoud@gmail.com", "Flu", 3, 101)
        self.hospital.admitPatient("Fathy Ahmed", 42, "Fathy@yahoo.com", "Multiple Trauma", 9, 102)
        self.hospital.admitPatient("Hamdy Elrefay", 30, "Elrefay@outlook.com", "Back Pain", 5, 103)
        self.update_ui()


    def admit_patient_event(self):
        try:
            
            name = self.entry_name.get()
            age_str = self.entry_age.get()
            contact = self.entry_contact.get()
            history = self.entry_history.get()
            room_str = self.entry_room.get()
            severity_str = self.entry_severity.get()

            
            if not name or not age_str or not severity_str:
                messagebox.showerror("Error", "Please fill in basic data (Name, Age, Severity)")
                return

            if not age_str.isdigit() or not room_str.isdigit() or not severity_str.isdigit():
                messagebox.showerror("Error", "Age, Room Number, and Severity must be numbers")
                return

            severity = int(severity_str)
            if severity < 1 or severity > 10:
                messagebox.showerror("Error", "Severity score must be between 1 and 10")
                return

            
            self.hospital.admitPatient(name, int(age_str), contact, history, severity, int(room_str))
            

            self.clear_inputs()
            self.update_ui()
            
            print(f"Patient {name} admitted successfully.")

        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def sort_patients_event(self):
        self.hospital.sortPatients()
        self.update_ui()
        messagebox.showinfo("Success", "Patients sorted by severity successfully")

    def clear_inputs(self):
        self.entry_name.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.entry_contact.delete(0, 'end')
        self.entry_history.delete(0, 'end')
        self.entry_room.delete(0, 'end')
        self.entry_severity.delete(0, 'end')

    def update_ui(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()


        records = self.hospital.displayRecords()
        

        self.lbl_count.configure(text=f"Total: {len(records)}")


        for idx, patient in enumerate(records):
            self.create_patient_card(patient, idx)

    def create_patient_card(self, patient, idx):


        severity = patient['Severity Score']
        border_color = "#2CC985"
        if severity >= 8:
            border_color = "#E04F5F"
        elif severity >= 5:
            border_color = "#F4A261"


        card = ctk.CTkFrame(
            self.scroll_frame, 
            fg_color=("gray85", "gray20"),
            border_width=2,
            border_color=border_color,
            corner_radius=10
        )
        card.grid(row=idx, column=0, padx=10, pady=8, sticky="ew")
        

        card.grid_columnconfigure(0, weight=1)


        top_text = f"{patient['Name']}  |  Age: {patient['Age']}"
        lbl_top = ctk.CTkLabel(card, text=top_text, font=ctk.CTkFont(size=16, weight="bold"))
        lbl_top.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 0))


        lbl_sev = ctk.CTkLabel(
            card, 
            text=f"Severity: {severity}/10", 
            text_color=border_color, 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        lbl_sev.grid(row=0, column=1, sticky="e", padx=15, pady=(10, 0))

        
        details = f"Room: {patient['Room Number']}  |  History: {patient['Medical History']}"
        lbl_details = ctk.CTkLabel(card, text=details, font=ctk.CTkFont(size=12))
        lbl_details.grid(row=1, column=0, columnspan=2, sticky="w", padx=15, pady=(5, 10))

if __name__ == "__main__":
    app = HospitalApp()
    app.mainloop()