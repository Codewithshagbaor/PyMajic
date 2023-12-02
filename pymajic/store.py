import json
import os
import sys
import subprocess
import datetime
import requests 
import webbrowser


command_aliases = {}

def verify_project_path(project_path):
    # Verify if the specified project directory is valid
    if not os.path.exists(os.path.join(project_path, 'manage.py')):
        print("Error: Invalid project directory.")
        sys.exit(1)

def store_data():
    # Store environment and project directory information
    env_path = input("Enter the virtual environment: ")
    project_path = input("Enter the path to the Django project directory: ")

    verify_project_path(project_path)

    data = {
        'env_path': env_path,
        'project_path': project_path
    }

    with open(os.path.join(project_path, 'pymajic_config.json'), 'w') as config_file:
        json.dump(data, config_file)


    # Create run.bat file in the project directory
    run_bat_path = os.path.join(project_path, 'run.bat')
    with open(run_bat_path, 'w') as run_file:
        run_file.write(f'@echo off\n'
                        f'start cmd /k "workon {env_path} && cd {project_path} && python manage.py runserver"')

# def run_custom_command(command):
#     # Run custom Django management command
#     subprocess.run(["python", "manage.py"] + command.split())

def django_shell():
    # Open Django shell session
    subprocess.run(["python", "manage.py", "shell"])
def backup_database():
    # Create a timestamped backup of the database
    backup_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"db_backup_{backup_timestamp}.json"
    
    # Use subprocess.run without '>'
    subprocess.run(["python", "manage.py", "dumpdata", "--indent", "2", ">", backup_filename], shell=True)
    
    print(f"Database backup created: {backup_filename}")

import shlex

def restore_database(backup_filename):
    # Restore the database from a backup file
    subprocess.run(["python", "manage.py", "flush", "--noinput"])  # Clear existing data
    subprocess.run(["python", "manage.py", "loaddata", backup_filename], shell=True)
    print("Database restored from backup.")

def project_info():
    # Display information about the Django project
    subprocess.run(["python", "manage.py", "showmigrations"])
    subprocess.run(["python", "manage.py", "inspectdb"])
    subprocess.run(["python", "manage.py", "check"])

def check_update():
    # Check for updates to the PyMajic package
    current_version = "0.1"  # Update with your current version
    response = requests.get("https://pypi.org/pypi/pymajic/json")
    latest_version = response.json()["info"]["version"]

    if current_version < latest_version:
        print(f"A new version ({latest_version}) of PyMajic is available. Please update.")
    else:
        print("You are using the latest version of PyMajic.")
def edit_config():
    # Edit the configuration file using the default text editor
    config_path = "pymajic_config.json"
    subprocess.run(["notepad.exe", config_path])  # Use notepad as an example, adjust for your system's default editor
command_aliases = {}

def save_command_aliases():
    # Load existing data from the configuration file
    config_file_path = 'pymajic_config.json'
    data = {'command_aliases': {}}

    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as config_file:
            data = json.load(config_file)

    # Update command_aliases in the data
    data['command_aliases'] = command_aliases

    # Save the updated data to the configuration file
    with open(config_file_path, 'w') as config_file:
        json.dump(data, config_file)

def interactive_mode():
    print("Welcome to PyMajic Interactive Mode!")
    print("Enter commands one by one. Type 'exit' to quit.")
    
    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower().startswith('set alias '):
            _, _, alias, *command_parts = user_input.split(' ', 3)
            command = ' '.join(command_parts)
            command_aliases[alias] = command
            print(f"Alias '{alias}' set for command '{command}'.")
            save_command_aliases()
        elif user_input in command_aliases:
            # If the user enters an alias, substitute the alias with the corresponding command
            alias_command = command_aliases[user_input]
            subprocess.run(["python", "manage.py"] + alias_command.split(), shell=True)
        else:
            # Run the user input as-is
            subprocess.run(["python", "manage.py"] + user_input.split(), shell=True)



def documentation_command():
    # Open the Django project documentation in the default web browser
    webbrowser.open("https://docs.djangoproject.com/en/stable/")

def main():
    sys.argv = [arg.lower() for arg in sys.argv]

    if len(sys.argv) == 2 and sys.argv[1] == "shell":
        django_shell()
        sys.exit(0)

    if len(sys.argv) == 3 and sys.argv[1] == "backup" and sys.argv[2] == "database":
        backup_database()
        sys.exit(0)

    if len(sys.argv) == 4 and sys.argv[1] == "restore" and sys.argv[2] == "database":
        restore_database(sys.argv[3])
        sys.exit(0)


    if len(sys.argv) == 3 and sys.argv[1] == "project" and sys.argv[2] == "info":
        project_info()
        sys.exit(0)

    if len(sys.argv) == 3 and sys.argv[1] == "check" and sys.argv[2] == "update":
        check_update()
        sys.exit(0)

    if len(sys.argv) == 3 and sys.argv[1] == "edit" and sys.argv[2] == "config":
        edit_config()
        sys.exit(0)

    if len(sys.argv) == 3 and sys.argv[1] == "interactive" and sys.argv[2] == "mode":
        interactive_mode()
        sys.exit(0)


    if len(sys.argv) == 2 and sys.argv[1] == "documentation":
        documentation_command()
        sys.exit(0)

    if len(sys.argv) == 3 and sys.argv[1] == "store" and sys.argv[2] == "data":
            store_data()
            sys.exit(0)

    # If no matching command is found, show the help message
    print("Usage: pymajic <command>")
    sys.exit(1)

if __name__ == "__main__":
    main()
