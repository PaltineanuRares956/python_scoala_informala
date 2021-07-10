import tkinter
from .employees import EmployeesFrame


class ContentFrame(tkinter.Frame):
    def __init__(self, fire, hire, master, **kwargs):
        super().__init__(master, kwargs)

        self.master = master
        self.brand_label = None
        self.employees_frame = None
        self.fire = fire
        self.hire = hire

    def draw(self, brand_name="N/A", users=None):
        if not users:
            users = []

        self.brand_label = tkinter.Label(
            master=self,
            text=brand_name,
            bg="#fff",
            fg="#000",
            font=("Arial", 24, "bold"),
        )
        self.brand_label.pack(side=tkinter.TOP)

        self.employees_frame = EmployeesFrame(users, self.fire, self.hire, self, bg="#fff", pady=10)
        self.employees_frame.pack(side=tkinter.TOP)
        self.employees_frame.draw()
