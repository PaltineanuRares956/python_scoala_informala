import tkinter
from .content import ContentFrame
from handlers.employees import fire, hire


class GUI:
    """This class is responsible for drawing the GUI."""
    def __init__(self):
        self.width = 800
        self.height = 650

        self.window = tkinter.Tk()
        self.window.title("GAD 06 Desktop Apps")
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.configure(background="#fff", padx=10, pady=10)
        self.content_frame = None
        self.loading_label = None
        self.is_content_loading = True
        self.employers = []
        self.users = []

    def set_data(self, users=None, employers=None):
        self.is_content_loading = False

        if not users:
            users = []

        if not employers:
            employers = []

        self.employers = employers
        self.users = users

        brand_name = employers[0].name if len(employers) > 0 else None
        self.draw(brand_name=brand_name, users=users)

    def fire(self, user):
        fire(user, self.employers[0])

    def hire(self, user):
        hire(user, self.employers[0])

    def draw(self, brand_name=None, users=None):
        if self.is_content_loading:
            self.loading_label = tkinter.Label(
                master=self.window,
                bg="#fff",
                fg="#424242",
                text="Loading ...",
                font=("Arial", 24, "bold")
            )
            self.loading_label.pack(side=tkinter.TOP)
        else:
            self.loading_label.pack_forget()
            self.content_frame = ContentFrame(
                self.fire,
                self.hire,
                self.window,
                bg="#fff",
                width=self.width,
                height=self.height,
            )
            self.content_frame.pack(side=tkinter.TOP)
            self.content_frame.pack_propagate(False)
            self.content_frame.draw(brand_name=brand_name, users=users)

    def show(self):
        self.draw()
        self.window.mainloop()
