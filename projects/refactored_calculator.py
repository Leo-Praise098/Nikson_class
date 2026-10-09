from tkinter import messagebox
from menu_for_calculator import Menu
import customtkinter as ctk


class CalculatorApp(ctk.CTk):
    """A compact four-function calculator with shared input handling."""

    BUTTON_STYLE = {
        "font": ("Garamond", 20),
        "fg_color": "azure",
        "text_color": "black",
        "hover_color": "#D9FFFF",
        "corner_radius": 15,
        "border_width": 2,
        "border_color": "#B8B8B8",
    }
    CLEAR_BUTTON_STYLE = {
        **BUTTON_STYLE,
        "fg_color": "#FFF8E7",
        "text_color": "#47C322",
        "hover_color": "#F0E5CC",
    }
    OPERATORS = {"+", "-", "*", "/"}
    INPUT_KEYS = set("0123456789.+-*/")

    def __init__(self):
        super().__init__()

        self.title("Calculator and formula menu")
        self.wm_attributes("-alpha", 0.875)
        self.geometry("325x500")
        self.resizable(False, False)

        # State is deliberately separate from the widgets.  The expression is
        # never read back from a display that also contains a prior answer.
        self.expression = ""
        self.result = ""
        self.just_calculated = False

        self._create_display()
        self._create_button_container()
        self._create_buttons()
        self.bind("<Key>", self.handle_keyboard_input)
        self.after_idle(self.focus_set)

    def _create_display(self):
        self.interface = ctk.CTkFrame(self, corner_radius=15)
        self.interface.place(
            relx=0.5,
            rely=0.01,
            relwidth=0.925,
            relheight=0.25,
            anchor="n",
        )

        self.expression_display = ctk.CTkTextbox(
            self.interface,
            wrap="none",
            font=("Garamond", 16),
            corner_radius=15,
            border_width=2,
            border_color="#B8B8B8",
            fg_color="white",
            text_color="black",
        )
        self.expression_display.place(relx=0.05, rely=0.07, relwidth=0.9, relheight=0.43)
        self.expression_display.configure(state="disabled")

        self.result_display = ctk.CTkLabel(
            self.interface,
            text="",
            font=("Garamond", 24),
            text_color="grey",
            anchor="e",
        )
        self.result_display.place(relx=0.08, rely=0.55, relwidth=0.84, relheight=0.33)

    def _create_button_container(self):
        self.container = ctk.CTkFrame(self, border_width=3, corner_radius=15)
        self.container.place(relx=0.0125, rely=0.275, relwidth=0.975, relheight=0.7)

    def _create_buttons(self):
        number_layout = (
            ("7", 0.04, 0.04), ("8", 0.28, 0.04), ("9", 0.52, 0.04),
            ("4", 0.04, 0.28), ("5", 0.28, 0.28), ("6", 0.52, 0.28),
            ("1", 0.04, 0.52), ("2", 0.28, 0.52), ("3", 0.52, 0.52),
            ("0", 0.28, 0.76),
        )
        for value, relx, rely in number_layout:
            self.create_button(
                text=value,
                command=lambda value=value: self.insert_value(value),
                relx=relx,
                rely=rely,
                relwidth=0.2,
                relheight=0.2,
            )

        self.create_button(
            text=".",
            command=lambda: self.insert_value("."),
            relx=0.52,
            rely=0.76,
            relwidth=0.2,
            relheight=0.2,
            style={"font": ("Garamond", 30)},
        )
        self.create_button(
            text="⌫",
            command=self.delete_last_character,
            relx=0.76,
            rely=0.04,
            relwidth=0.2,
            relheight=0.144,
        )

        operator_layout = (
            ("+", 0.2048),
            ("-", 0.3296),
            ("/", 0.4544),
            ("*", 0.5792),
        )
        for value, rely in operator_layout:
            self.create_button(
                text=value,
                command=lambda value=value: self.insert_value(value),
                relx=0.76,
                rely=rely,
                relwidth=0.2,
                relheight=0.104,
            )

        clear_button = self.create_button(
                text="C",
                command=self.clear_calculation,
                relx=0.04,
                rely=0.76,
                relwidth=0.2,
                relheight=0.2,
                style=self.CLEAR_BUTTON_STYLE,
            )
        clear_button.bind("<Double-Button-1>", lambda event: self.instantiateMenu())
        self.create_button(
            text="=",
            command=self.calculate_expression,
            relx=0.76,
            rely=0.76,
            relwidth=0.2,
            relheight=0.2,
        )

    def create_button(self, text, command, relx, rely, relwidth, relheight, style=None):
        button_style = self.BUTTON_STYLE.copy()
        if style:
            button_style.update(style)

        button = ctk.CTkButton(
            self.container,
            text=text,
            command=command,
            **button_style,
        )
        button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return button

    def insert_value(self, value):
        """Add a string value from either a button or the keyboard."""
        if self.just_calculated:
            self.expression = self.result if value in self.OPERATORS else ""
            self.result = ""
            self.just_calculated = False

        self.expression += str(value)
        self.refresh_display()

    def delete_last_character(self):
        if self.just_calculated:
            self.expression = self.result
            self.result = ""
            self.just_calculated = False

        self.expression = self.expression[:-1]
        self.refresh_display()

    def clear_calculation(self):
        self.expression = ""
        self.result = ""
        self.just_calculated = False
        self.refresh_display()

    def calculate_expression(self):
        try:
            answer = eval(self.expression)
        except ZeroDivisionError:
            self.show_error("Division by zero", "Division by zero is not allowed.")
        except (SyntaxError, ValueError, NameError, TypeError):
            self.show_error("Invalid expression", "Please enter a valid calculation.")
        else:
            self.result = str(answer)
            self.just_calculated = True
            self.refresh_display()

    def show_error(self, title, message):
        """Reset the calculator and show a clear, non-technical message."""
        self.clear_calculation()
        messagebox.showerror(title=title, message=message, parent=self)

    def refresh_display(self):
        self.expression_display.configure(state="normal")
        self.expression_display.delete("1.0", "end")
        self.expression_display.insert("1.0", str(self.expression))
        self.expression_display.see("end")
        self.expression_display.configure(state="disabled")
        self.result_display.configure(text=str(self.result))

    def handle_keyboard_input(self, event):
        """Route all supported calculator keys through the same public actions."""
        if event.keysym in {"Return", "KP_Enter"} or event.char == "=":
            self.calculate_expression()
            return "break"
        if event.keysym == "BackSpace":
            self.delete_last_character()
            return "break"
        if event.keysym == "Delete":
            self.clear_calculation()
            return "break"
        if event.char in self.INPUT_KEYS:
            self.insert_value(event.char)
            return "break"
    
    def instantiateMenu(self):
        """Instantiate the Menu class and display it."""
        menu = Menu()
        menu.create_display()
        menu.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
