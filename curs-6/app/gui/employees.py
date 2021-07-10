import tkinter
from .generic_frames import RowFrame


class EmployeeFrame(tkinter.Frame):
    def __init__(self, user, fire, hire, bg_color, master, **kwargs):
        super().__init__(master, kwargs)

        self.user = user
        self.bg_color = bg_color
        self.fire = fire
        self.hire = hire
        self.row_frame = None

    @property
    def is_hired(self):
        print(self.user.employees)
        if len(self.user.employees) == 0:
            return False

        return True

    def toggle_employee(self):
        if self.is_hired:
            self.fire(self.user)
        else:
            self.hire(self.user)

        self.draw()

    def get_btn_data(self):
        if self.is_hired:
            bg = "#800000"
            active_background = "#990000"
            text = "Fire"
        else:
            bg = "#008000"
            active_background = "#009900"
            text = "Hire"

        return {
            "fg": "#fff",
            "bg": bg,
            "activebackground": active_background,
            "activeforeground": "#fff",
            "text": text,
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.toggle_employee,
        }

    def draw(self):
        if self.row_frame is not None:
            self.row_frame.pack_forget()

        col_values = [
            self.user.first_name,
            self.user.last_name,
            self.user.email,
            'ACTION'
        ]
        col_props = list(map(lambda col_value: {
            "text": col_value,
            "bg": self.bg_color,
            "font": ("Arial", 12, "normal"),
            "padx": 10,
            "width": 15 if "@" not in col_value else 30,
        } if col_value != "ACTION" else self.get_btn_data(), col_values))

        self.row_frame = RowFrame(col_props, self, bg=self.bg_color)
        self.row_frame.pack(side=tkinter.TOP)
        self.row_frame.draw()


class EmployeesFrame(tkinter.Frame):
    def __init__(self, users, fire, hire, master, **kwargs):
        super().__init__(master, kwargs)

        self.users = users
        self.fire = fire
        self.hire = hire

    def draw_header(self):
        header_cols = list(map(lambda header_value: {
            "text": header_value,
            "bg": "#eee",
            "font": ("Arial", 12, "bold"),
            "padx": 10,
            "width": 15 if header_value != "EMAIL" else 30,
        }, ["FIRST NAME", "LAST NAME", "EMAIL", "ACTION"]))

        header_frame = RowFrame(header_cols, self, bg="#eee")
        header_frame.pack(side=tkinter.TOP)
        header_frame.draw()

    def draw(self):
        self.draw_header()

        for index, user in enumerate(self.users):
            row_color = "#fff" if index % 2 == 0 else "#eee",
            user_frame = EmployeeFrame(
                user,
                self.fire,
                self.hire,
                row_color,
                self,
                bg=row_color,
                padx=10,
                pady=10,
            )
            user_frame.pack(side=tkinter.TOP)
            user_frame.draw()
