def generate_readme():
    # Prompting user for project details
    project_name = input("Enter project name: ")
    description = input("Enter project description: ")
    installation = input("Enter installation instructions: ")
    usage = input("Enter usage examples: ")
    contributors = input("Enter contributors (separated by commas): ")
    license = input("Enter license type: ")
    github_username = input("Enter your GitHub username: ")

    # Generating README content
    readme_content = f"""# {project_name}

{description}

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Installation
{installation}

## Usage
{usage}

## Contributors
{contributors}

## License
This project is licensed under the {license} License.

---

Liked the project? Give it a star on [GitHub](https://github.com/{github_username}/{project_name})

---

Feel free to contribute to the project by forking it and creating a pull request.
    """

    # Writing README content to a file
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    print("README.md file generated successfully!")


if __name__ == "__main__":
    generate_readme()
