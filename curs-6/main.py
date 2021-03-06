from threading import Thread
from app.gui import GUI
from app.gui import Alter_User
from handlers.data_loaders import load

if __name__ == "__main__":
    gui = Alter_User()

    # get data
    Thread(
        target=load,
        kwargs={
            "callback_setter": gui.set_data
        }
    ).start()

    gui.show()
