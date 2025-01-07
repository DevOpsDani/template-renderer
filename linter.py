import typer
from jinja2 import Environment, FileSystemLoader, meta
import yaml
from cfnlint.api import lint_all

app = typer.Typer()

@app.command()
def extract_values(template: str):
    """
    Return Values from Jijna template.
    Example: linter.py myjinja.yaml.j2
    """
    with open(template, 'r') as file:
        template_content = file.read()

    # Create a Jinja2 environment
    env = Environment()

    # Parse the template
    parsed_content = env.parse(template_content)

    # Extract all placeholders (undeclared variables)
    placeholders = meta.find_undeclared_variables(parsed_content)

    print("\nPlaceholders found in the template:")
    print("===================================")
    for placeholder in placeholders:
        print(f"- {placeholder}")
    print("===================================\n")

@app.command()
def cfn_lint(mock_data: str, template: str):
    """
    Render template and lint. Example - linter.py data.yaml myjinja.yaml.j2
    """
    with open(mock_data, 'r') as f:
        values = yaml.safe_load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)
    rendered_content = template.render(values)

    for error in lint_all(rendered_content):
        print(error)
        print("\n")
        
@app.command()
def generate_template(mock_data: str, template: str, output_name: str):
    """
    Render template and create a file from it. Example - linter.py data.yaml myjinja.yaml.j2
    """
    with open(mock_data, 'r') as f:
        values = yaml.safe_load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)
    rendered_content = template.render(values)

    with open(f'{output_name}.yaml', 'w') as f:
        f.write(rendered_content)

    print(f"Template rendered and saved to {output_name}.yaml")


if __name__ == "__main__":
    app()
