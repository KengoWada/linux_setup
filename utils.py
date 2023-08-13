import subprocess

class BaseInstaller:

    def __init__(self, options):
        self.__validate_options(options)
        self.options = options

    @property
    def display_options(self):
        if not self.options:
            return []
        
        options = []
        options_length = len(self.options)
        for index in range(0, options_length, 2):
            op1 = self.options[index]
            if index + 1 < options_length:
                op2 = self.options[index + 1]
                options.append(
                    [
                        f"[{op1['id']}] {op1['name']}",
                        f"[{op2['id']}] {op2['name']}",
                    ]
                )
            else:
                options.append([f"[{op1['id']}] {op1['name']}"])
        
        return options

    @property
    def install_options(self):
        return {
            f"{option['id']}": option['install_steps']
            for option in self.options
        } if self.options else dict()

    def install(self, selected_options):
        self.__validate_selected_options(selected_options)

        for i in selected_options:
            install_steps = self.install_options[i]
            for step in install_steps:
                subprocess.call(step, shell=True)

    def __validate_selected_options(self, selected_options):
        if not isinstance(selected_options, list):
            raise ValueError("Selected options must be a list.")
        
        if not all(option.isnumeric() for option in selected_options):
            raise ValueError("Selected options must be numbers.")
        
        if not set(selected_options).issubset(set(self.install_options.keys())):
            raise ValueError("Invalid option selected for install.")
        
        if len(set(selected_options)) != len(selected_options):
            raise ValueError("No duplicates allowed in selected options")

    def __validate_options(self, options):
        if not isinstance(options, list):
            raise ValueError("Invalid options type. Options should be a list.")
        
        option_ids = []
        for option in options:
            if not isinstance(option, dict):
                raise KeyError("Invalid option type. Option should be a dictionary.")

            valid_keys = set(["name", "id", "install_steps"])
            if set(option.keys()) != valid_keys:
                raise ValueError(
                    "Invalid keys provided. "
                    "Valid keys are 'name', 'id' and 'install_steps'."
                )

            if not isinstance(option["id"], int):
                raise ValueError("Option id field must be an integer.")
            if option["id"] in option_ids:
                raise ValueError("Option id must be unqiue.")
            option_ids.append(option["id"])

            if not isinstance(option["name"], str):
                raise ValueError("Option name must be a string.")
            if not len(option["name"]):
                raise ValueError("Options name can not be empty")
            
            if not isinstance(option["install_steps"], list):
                raise ValueError("Install steps must be a list.")
            if not all(isinstance(install_step, str) for install_step in option["install_steps"]):
                raise ValueError("All install steps must be a string.")


def show_options(install_optioins):
    col_width = max(len(word) for row in install_optioins for word in row) + 2
    for row in install_optioins:
        print(''.join(word.ljust(col_width) for word in row))

def select_options(name, installer):
    print("=========================================")
    print(f"Select {name} To Install")
    print("=========================================")
    show_options(installer.display_options)
    print("\n")
    user_input = input("Select numerical value(s) separated by commas. Leave empty if none needed:")
    return user_input if user_input else None

# if __name__ == "__main__":
#     options = [
#         {
#             "id": 4,
#             "name": "Postgres",
#             "install_steps": [
#                 "sudo apt install postgresql postgresql-contrib"
#             ]
#         },
#         {
#             "id": 7,
#             "name": "Redis",
#             "install_steps": [
#                 "sudo apt install postgresql postgresql-contrib"
#             ]
#         }
#     ]

#     installer = BaseInstaller(options)
#     show_options(installer.display_options)
