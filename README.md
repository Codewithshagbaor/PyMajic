# PyMajic: Crafting Django Projects, One Command at a Time!
![PyMajic Logo](https://github.com/Codewithshagbaor/PyMajic/assets/67190277/9a12d4a9-07c5-446e-a392-55e1457f3292)
PyMajic is a Python package that simplifies working with Django projects by providing convenient commands for environment management, custom commands, and more.

## Installation

```bash
pip install pymajic
```

## Usage

### Store Data

To store environment and project directory information:

```bash
pymajic store data
```

### Run Custom Command(In Dev Mode)

To run a custom Django management command:

```bash
pymajic run command <your_custom_command>
```

### Django Shell Access

To open a Django shell session:

```bash
pymajic shell
```

### Environment Verification(Dev Mode)

Ensure the correctness of your project environment:

```bash
pymajic verify environment
```

### Project Sharing(Dev Mode)

Share your Django project easily with PyMajic:

```bash
pymajic share project
```

This command creates a new virtual environment, installs the project dependencies, and runs the project.

### Database Backup and Restore

Backup your Django project database:

```bash
pymajic backup database
```

Restore your Django project database:

```bash
pymajic restore database <backup_filename>
```

### Project Configuration Viewer

View the configuration of your Django project:

```bash
pymajic project info
```

### Update Check

Check for updates to the PyMajic package:

```bash
pymajic check update
```

### Config File Editor

Edit the PyMajic configuration file:

```bash
pymajic edit config
```

### Interactive Mode

Enter interactive mode to execute commands dynamically:

```bash
pymajic interactive mode
```

### Set Command Alias

Set aliases for your custom commands:

```bash
set alias <alias_name> <your_custom_command>
```

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
