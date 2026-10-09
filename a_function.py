def _calculate(self, choice=None):
        import math

        
        if not choice or choice == "None":
            return

        formulas = {
            "1st equation of motion": {
                "equation": "v = u + at",
                "variables": {
                    "v": ("Final velocity, v (m/s)", lambda x: x["u"] + x["a"] * x["t"]),
                    "u": ("Initial velocity, u (m/s)", lambda x: x["v"] - x["a"] * x["t"]),
                    "a": ("Acceleration, a (m/s²)", lambda x: (x["v"] - x["u"]) / x["t"]),
                    "t": ("Time, t (s)", lambda x: (x["v"] - x["u"]) / x["a"])
                }
            },
            "2nd equation of motion": {
                "equation": "s = ut + ½at²",
                "variables": {
                    "s": ("Displacement, s (m)", lambda x: x["u"] * x["t"] + 0.5 * x["a"] * x["t"]**2),
                    "u": ("Initial velocity, u (m/s)", lambda x: (x["s"] - 0.5 * x["a"] * x["t"]**2) / x["t"]),
                    "a": ("Acceleration, a (m/s²)", lambda x: 2 * (x["s"] - x["u"] * x["t"]) / x["t"]**2),
                    "t": ("Time, t (s)", lambda x: (-x["u"] + math.sqrt(x["u"]**2 + 2 * x["a"] * x["s"])) / x["a"])
                }
            },
            "3rd equation of motion": {
                "equation": "v² = u² + 2as",
                "variables": {
                    "v": ("Final velocity, v (m/s)", lambda x: math.sqrt(x["u"]**2 + 2 * x["a"] * x["s"])),
                    "u": ("Initial velocity, u (m/s)", lambda x: math.sqrt(x["v"]**2 - 2 * x["a"] * x["s"])),
                    "a": ("Acceleration, a (m/s²)", lambda x: (x["v"]**2 - x["u"]**2) / (2 * x["s"])),
                    "s": ("Displacement, s (m)", lambda x: (x["v"]**2 - x["u"]**2) / (2 * x["a"]))
                }
            },
            "Power, work, and time": {
                "equation": "P = W / t",
                "variables": {
                    "P": ("Power, P (W)", lambda x: x["W"] / x["t"]),
                    "W": ("Work, W (J)", lambda x: x["P"] * x["t"]),
                    "t": ("Time, t (s)", lambda x: x["W"] / x["P"])
                }
            },
            "Power, energy and time": {
                "equation": "P = E / t",
                "variables": {
                    "P": ("Power, P (W)", lambda x: x["E"] / x["t"]),
                    "E": ("Energy, E (J)", lambda x: x["P"] * x["t"]),
                    "t": ("Time, t (s)", lambda x: x["E"] / x["P"])
                }
            },
            "Electrical power": {
                "equation": "P = VI",
                "variables": {
                    "P": ("Power, P (W)", lambda x: x["V"] * x["I"]),
                    "V": ("Voltage, V (volts)", lambda x: x["P"] / x["I"]),
                    "I": ("Current, I (amperes)", lambda x: x["P"] / x["V"])
                }
            },
            "Newton's 2nd law of motion": {
                "equation": "F = ma",
                "variables": {
                    "F": ("Force, F (N)", lambda x: x["m"] * x["a"]),
                    "m": ("Mass, m (kg)", lambda x: x["F"] / x["a"]),
                    "a": ("Acceleration, a (m/s²)", lambda x: x["F"] / x["m"])
                }
            },
            "Weight": {
                "equation": "W = mg",
                "variables": {
                    "W": ("Weight, W (N)", lambda x: x["m"] * x["g"]),
                    "m": ("Mass, m (kg)", lambda x: x["W"] / x["g"]),
                    "g": ("Gravitational acceleration, g (m/s²)", lambda x: x["W"] / x["m"])
                }
            },
            "Hooke's law (Spring force)": {
                "equation": "F = kx",
                "variables": {
                    "F": ("Spring force magnitude, F (N)", lambda x: x["k"] * x["x"]),
                    "k": ("Spring constant, k (N/m)", lambda x: x["F"] / x["x"]),
                    "x": ("Extension, x (m)", lambda x: x["F"] / x["k"])
                }
            }
        }

        # Match the selected option to a supported formula.
        formula = formulas.get(choice)

        # Allow for the missing space in your existing menu text.
        if formula is None:
            choice = choice.replace("equationof", "equation of")
            formula = formulas.get(choice)

        if formula is None:
            messagebox.showerror(
                "Invalid selection",
                f"The formula '{choice}' is not supported."
            )
            return

        # Ask which variable the user wants to calculate.
        variables = formula["variables"]
        variable_list = ", ".join(variables)

        missing = simpledialog.askstring(
            "Missing variable",
            f"Selected formula:\n{formula['equation']}\n\n"
            f"Which variable do you want to calculate?\n"
            f"Enter one of: {variable_list}",
            parent=None
        )

        if missing is None:
            return

        missing = missing.strip()

        if missing not in variables:
            messagebox.showerror(
                "Invalid variable",
                f"Enter one of these variables: {variable_list}"
            )
            return

        # Collect every other variable as a known value.
        values = {}

        for variable, (prompt, _) in variables.items():
            if variable == missing:
                continue

            while True:
                answer = ctk.CTkInputDialog(
                    title="Enter known value",
                    text=f"{prompt}\nEnter its known value:"
                ).get_input()

                if answer is None:
                    return

                try:
                    number = float(answer.strip())

                    if not math.isfinite(number):
                        raise ValueError

                    values[variable] = number
                    break

                except ValueError:
                    messagebox.showerror(
                        "Invalid input",
                        "Enter a valid, finite number."
                    )

        # Calculate the missing variable.
        try:
            result = variables[missing][1](values)

            if not math.isfinite(result):
                raise ValueError("The result is not a finite number.")

            messagebox.showinfo(
                "Calculation result",
                f"Formula: {formula['equation']}\n\n"
                f"Missing variable: {missing}\n"
                f"Answer: {result:.6g}"
            )

        except (ZeroDivisionError, ValueError, OverflowError) as error:
            messagebox.showerror(
                "Calculation error",
                f"Unable to calculate {missing}.\n\n"
                f"Check your known values.\n{error}"
            )