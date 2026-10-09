from tkinter import messagebox, simpledialog
import customtkinter as ctk


class  Menu(ctk.CTk):
    """The menu for formulas to be linked to the calculator"""
    
    LIST_STYLE = {
            "fg_color": "azure",
            "corner_radius": 15,
            "border_width": 0,
            "border_color": "#B8B8B8",
        }
    LIST_STYLE2 = {
        **LIST_STYLE,
        "font": ("Garamond", 13),
        "text_color": "brown"
    }
    
    def __init__(self):
        super().__init__()
        self.title("Menu for formulas")
        self.wm_attributes("-alpha", 0.925)
        self.geometry("400x650")
        self.resizable(True, True)
    
    def create_display(self):
        layout = (
            (.05, .025, .02, .125), 
            (.05, .35, .02, .125), 
            (.05, .675, .02, .125)
        )
        position = (.05, .4, .9, .6), (.65, .1, .3, .2)
        
        motion_frame = ctk.CTkFrame(self, **self.LIST_STYLE)
        motion_frame.place(
            relx=layout[0][0],
            rely=layout[0][1],
            relwidth=.9,
        )
        
        power_frame = ctk.CTkFrame(self, **self.LIST_STYLE)
        power_frame.place(
            relx=layout[1][0],
            rely=layout[1][1],
            relwidth=.9,
        )
        
        force_frame = ctk.CTkFrame(self, **self.LIST_STYLE)
        force_frame.place(
            relx=layout[2][0],
            rely=layout[2][1],
            relwidth=.9,
        )
        
        motion_choice = ctk.CTkOptionMenu(motion_frame, values=["None", "1st equation of motion", "2nd equation of motion", "3rd equation of motion"], command=self._calculate)
        motion_choice.place(relx=layout[0][2], rely=layout[0][3], relwidth=.6)
        
        power_choice = ctk.CTkOptionMenu(power_frame, values=["None", "Power, work and time", "Power, energy and time", "Electrical power"], command=self._calculate)
        power_choice.place(relx=layout[1][2], rely=layout[1][3], relwidth=.6)
        
        force_choice = ctk.CTkOptionMenu(force_frame, values=["None", "Newton's 2nd law of motion", "Weight", "Hooke's law (Spring force)"], command=self._calculate)
        force_choice.place(relx=layout[2][2], rely=layout[2][3], relwidth=.6)
        
        motion_text = ctk.CTkTextbox(motion_frame, **self.LIST_STYLE2)
        motion_text.place(relx= position[0][0], rely=position[0][1], relwidth= position[0][2], relheight=position[0][3])
        #motion_text.tag_config("center",justify="center")
        motion_text.insert(f"1.0", "1st equation of motion: \nv = u + at \n2nd equation of motion: \ns = ut + 1/2at**2 \n3rd equation of motion: \nv**2 = u**2 + 2as", "center")
        motion_text.configure(state="disabled")

        power_text = ctk.CTkTextbox(power_frame, **self.LIST_STYLE2)
        power_text.place(relx= position[0][0], rely=position[0][1], relwidth= position[0][2], relheight=position[0][3])
        #power_text.tag_config("center",justify="center")
        power_text.insert("1.0", "Power, work and time: \nP = W/t \nPower, energy and time: \nP = E/t \nElectrical Power: \nP = VI", "center")
        power_text.configure(state="disabled")
        
        force_text = ctk.CTkTextbox(force_frame, **self.LIST_STYLE2)
        force_text.place(relx= position[0][0], rely=position[0][1], relwidth= position[0][2], relheight=position[0][3])
        #force_text.tag_config("center",justify="center")
        force_text.insert("1.0", "Newton's 2nd law of motion: \nF = ma \nWeight: \nF = mg; g = 9.8ms**-2 \nHooke's law (Spring force): \nF = -kx; where k = spring constant", "center")
        force_text.configure(state="disabled")
        
    def _calculate(self, choice=None):
        print(f"Selected choice: {choice!r}")
        
        if choice == "None":
            return
        
        formulas = {
            "motion": {
                "v = u + at": ("v", "u", "a", "t"),
                "s = ut + ½at²": ("s", "u", "a", "t"),
                "v² = u² + 2as": ("v", "u", "a", "s")
            },
            "power": {
                "P = W / t": ("P", "W", "t"),
                "P = E / t": ("P", "E", "t"),
                "P = VI": ("P", "V", "I")
            },
            "Force": {
                "F = ma": ("F", "m", "a"),
                "W = mg": ("W", "m", "g"),
                "F = kx": ("F", "k", "x")
            }
        }
        print(f"Selected choice: {choice!r}")
        match choice:
            case "1st equation of motion":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['motion'].keys())[0]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['motion']["v = u + at"]}",
                    parent=self
                )
                if missing == list(formulas["motion"].values())[0][0]:
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = u + (a*t)
                    messagebox.showinfo(
                        title= "Answer",
                        message= f"Final velocity: {answer}",
                        default= "ok"
                    )
                elif missing == list(formulas["motion"].values())[0][1]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = v - (a*t)
                    messagebox.showinfo(
                        title= "Answer",
                        message= f"Initial velocity: {answer}",
                        default= "ok"
                    )
                elif missing == list(formulas["motion"].values())[0][2]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = (v - u)/t
                    messagebox.showinfo(
                        title= "Answer",
                        message= f"Acceleration: {answer}",
                        default= "ok"
                    )
                elif missing == list(formulas["motion"].values())[0][3]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    answer = (v - u)/a
                    messagebox.showinfo(
                        title= "Answer",
                        message= f"Time: {answer}s",
                        default= "ok"
                    )
            
            case "2nd equation of motion":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['motion'].keys())[1]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['motion']['s = ut + ½at²']}",
                    parent=self
                )
                if missing == list(formulas["motion"].values())[1][0]:
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = (u*t) + (0.5*a*t**2)
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Displacement: {answer}m",
                        default="ok"
                    )
                elif missing == list(formulas["motion"].values())[1][1]:
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    if t == 0:
                        messagebox.showerror(
                            title="Math Error",
                            message="Time cannot be zero when calculating initial velocity.",
                            default="ok"
                        )
                    else:
                        answer = (s - (0.5*a*t**2))/t
                        messagebox.showinfo(
                            title="Answer",
                            message=f"Initial velocity: {answer}m/s",
                            default="ok"
                        )
                elif missing == list(formulas["motion"].values())[1][2]:
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    if t == 0:
                        messagebox.showerror(
                            title="Math Error",
                            message="Time cannot be zero when calculating acceleration.",
                            default="ok"
                        )
                    else:
                        answer = 2*(s - (u*t))/t**2
                        messagebox.showinfo(
                            title="Answer",
                            message=f"Acceleration: {answer}m/s²",
                            default="ok"
                        )
                elif missing == list(formulas["motion"].values())[1][3]:
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    if a == 0:
                        if u == 0:
                            messagebox.showerror(
                                title="Math Error",
                                message="Time cannot be uniquely determined when both initial velocity and acceleration are zero.",
                                default="ok"
                            )
                        else:
                            answer = s/u
                            messagebox.showinfo(
                                title="Answer",
                                message=f"Time: {answer}s",
                                default="ok"
                            )
                    else:
                        discriminant = u**2 + 2*a*s
                        if discriminant < 0:
                            messagebox.showerror(
                                title="Math Error",
                                message="No real value for time exists.",
                                default="ok"
                            )
                        else:
                            answer = (-u + discriminant**0.5)/a
                            messagebox.showinfo(
                                title="Answer",
                                message=f"Time: {answer}s",
                                default="ok"
                            )

            case "3rd equation of motion":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['motion'].keys())[2]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['motion']['v² = u² + 2as']}",
                    parent=self
                )
                if missing == list(formulas["motion"].values())[2][0]:
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    answer = (u**2 + 2*a*s)**0.5
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Final velocity: {answer}m/s",
                        default="ok"
                    )
                elif missing == list(formulas["motion"].values())[2][1]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    answer = (v**2 - 2*a*s)**0.5
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Initial velocity: {answer}m/s",
                        default="ok"
                    )
                elif missing == list(formulas["motion"].values())[2][2]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    s = simpledialog.askfloat(
                        "s; displacement",
                        "Enter the value of s:"
                    )
                    answer = (v**2 - u**2)/(2*s)
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Acceleration: {answer}m/s²",
                        default="ok"
                    )
                elif missing == list(formulas["motion"].values())[2][3]:
                    v = simpledialog.askfloat(
                        "v; final velocity",
                        "Enter the value of v:"
                    )
                    u = simpledialog.askfloat(
                        "u; initial velocity",
                        "Enter the value of u:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    answer = (v**2 - u**2)/(2*a)
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Displacement: {answer}m",
                        default="ok"
                    )

            case "Power, work and time":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['power'].keys())[0]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['power']['P = W / t']}",
                    parent=self
                ); print("passed")
                if missing == list(formulas["power"].values())[0][0]:
                    W = simpledialog.askfloat(
                        "W; work done",
                        "Enter the value of W:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = W/t
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Power: {answer}W",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[0][1]:
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = P*t
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Work done: {answer}J",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[0][2]:
                    W = simpledialog.askfloat(
                        "W; work done",
                        "Enter the value of W:"
                    )
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    answer = W/P
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Time: {answer}s",
                        default="ok"
                    )

            case "Power, energy and time":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['power'].keys())[1]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['power']['P = E / t']}",
                    parent=self
                )
                if missing == list(formulas["power"].values())[1][0]:
                    E = simpledialog.askfloat(
                        "E; energy",
                        "Enter the value of E:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = E/t
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Power: {answer}W",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[1][1]:
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    t = simpledialog.askfloat(
                        "t; time taken",
                        "Enter the value of t:"
                    )
                    answer = P*t
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Energy: {answer}J",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[1][2]:
                    E = simpledialog.askfloat(
                        "E; energy",
                        "Enter the value of E:"
                    )
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    answer = E/P
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Time: {answer}s",
                        default="ok"
                    )

            case "Electrical power":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['power'].keys())[2]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['power']['P = VI']}",
                    parent=self
                )
                if missing == list(formulas["power"].values())[2][0]:
                    V = simpledialog.askfloat(
                        "V; voltage",
                        "Enter the value of V:"
                    )
                    I = simpledialog.askfloat(
                        "I; current",
                        "Enter the value of I:"
                    )
                    answer = V*I
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Electrical power: {answer}W",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[2][1]:
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    I = simpledialog.askfloat(
                        "I; current",
                        "Enter the value of I:"
                    )
                    answer = P/I
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Voltage: {answer}V",
                        default="ok"
                    )
                elif missing == list(formulas["power"].values())[2][2]:
                    P = simpledialog.askfloat(
                        "P; power",
                        "Enter the value of P:"
                    )
                    V = simpledialog.askfloat(
                        "V; voltage",
                        "Enter the value of V:"
                    )
                    answer = P/V
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Current: {answer}A",
                        default="ok"
                    )

            case "Newton's 2nd law of motion":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['Force'].keys())[0]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['Force']['F = ma']}",
                    parent=self
                )
                if missing == list(formulas["Force"].values())[0][0]:
                    m = simpledialog.askfloat(
                        "m; mass",
                        "Enter the value of m:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    answer = m*a
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Force: {answer}N",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[0][1]:
                    F = simpledialog.askfloat(
                        "F; force",
                        "Enter the value of F:"
                    )
                    a = simpledialog.askfloat(
                        "a; acceleration",
                        "Enter the value of a:"
                    )
                    answer = F/a
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Mass: {answer}kg",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[0][2]:
                    F = simpledialog.askfloat(
                        "F; force",
                        "Enter the value of F:"
                    )
                    m = simpledialog.askfloat(
                        "m; mass",
                        "Enter the value of m:"
                    )
                    answer = F/m
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Acceleration: {answer}m/s²",
                        default="ok"
                    )

            case "Weight":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['Force'].keys())[1]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['Force']['W = mg']}",
                    parent=self
                )
                if missing == list(formulas["Force"].values())[1][0]:
                    m = simpledialog.askfloat(
                        "m; mass",
                        "Enter the value of m:"
                    )
                    g = simpledialog.askfloat(
                        "g; acceleration due to gravity",
                        "Enter the value of g:"
                    )
                    answer = m*g
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Weight: {answer}N",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[1][1]:
                    W = simpledialog.askfloat(
                        "W; weight",
                        "Enter the value of W:"
                    )
                    g = simpledialog.askfloat(
                        "g; acceleration due to gravity",
                        "Enter the value of g:"
                    )
                    answer = W/g
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Mass: {answer}kg",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[1][2]:
                    W = simpledialog.askfloat(
                        "W; weight",
                        "Enter the value of W:"
                    )
                    m = simpledialog.askfloat(
                        "m; mass",
                        "Enter the value of m:"
                    )
                    answer = W/m
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Acceleration due to gravity: {answer}m/s²",
                        default="ok"
                    )

            case "Hooke's law (Spring force)":
                print("Power, work and time case reached")
                missing = simpledialog.askstring(
                    "Missing variable",
                    f"Selected formula:\n{list(formulas['Force'].keys())[2]}\n\n"
                    f"Which variable do you want to calculate?\n"
                    f"Enter one of: {formulas['Force']['F = kx']}",
                    parent=self
                )
                if missing == list(formulas["Force"].values())[2][0]:
                    k = simpledialog.askfloat(
                        "k; spring constant",
                        "Enter the value of k:"
                    )
                    x = simpledialog.askfloat(
                        "x; extension",
                        "Enter the value of x:"
                    )
                    answer = k*x
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Spring force: {answer}N",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[2][1]:
                    F = simpledialog.askfloat(
                        "F; spring force",
                        "Enter the value of F:"
                    )
                    x = simpledialog.askfloat(
                        "x; extension",
                        "Enter the value of x:"
                    )
                    answer = F/x
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Spring constant: {answer}N/m",
                        default="ok"
                    )
                elif missing == list(formulas["Force"].values())[2][2]:
                    F = simpledialog.askfloat(
                        "F; spring force",
                        "Enter the value of F:"
                    )
                    k = simpledialog.askfloat(
                        "k; spring constant",
                        "Enter the value of k:"
                    )
                    answer = F/k
                    messagebox.showinfo(
                        title="Answer",
                        message=f"Extension: {answer}m",
                        default="ok"
                    )


if __name__ == "__main__":
    app = Menu()
    app.create_display()
    app.mainloop()