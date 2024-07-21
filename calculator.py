import math

def convert_number_system(expression):
    conversion_map = {
        "bin": lambda x: bin(int(x)),
        "hex": lambda x: hex(int(x)),
        "dec": lambda x: int(x, 0)
    }
    prefix, number = expression.split(":", 1)
    return conversion_map.get(prefix, lambda x: x)(number)

class CustomCalculator:
    def __init__(self):
        self.last_result = 0
        self.mode = "degrees"
        self.update_math_functions()

    def update_math_functions(self):
        self.math_functions = {
            "sin": math.sin if self.mode == "radians" else lambda x: math.sin(math.radians(x)),
            "cos": math.cos if self.mode == "radians" else lambda x: math.cos(math.radians(x)),
            "tan": math.tan if self.mode == "radians" else lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log,
            "pi": math.pi,
            "fact": math.factorial,
            "e": math.e
        }

    def set_mode(self, new_mode):
        if new_mode in ["degrees", "radians"]:
            self.mode = new_mode
            self.update_math_functions()
            return f"Mode set to {new_mode}"
        else:
            return "Invalid mode. Please choose 'degrees' or 'radians'."

    def calculate(self, expression):
        try:
            if expression.startswith("mode:"):
                return self.set_mode(expression.split(":")[1])

            conversion_result = convert_number_system(expression)
            if conversion_result is not None:
                self.last_result = conversion_result
                return conversion_result

            local_namespace = self.math_functions.copy()
            local_namespace["_last"] = self.last_result

            result = eval(expression, {"math": math}, local_namespace)
            self.last_result = result
            return result
        except SyntaxError:
            return "Error: Invalid syntax. Please check your expression."
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"Error: {str(e)}"
