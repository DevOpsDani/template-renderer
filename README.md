# template-renderer
Tool to render Jinja templates, lint cloudformation templates that are rendered with Jijna


How to Run the CloudFormation Linter Script
The linter.py script provides three options for validating and processing templates. Below are the available modes and usage examples:

1. Extract Values
This option returns the values referenced in a Jinja template without rendering the template. This will help you build the values template according the output.
Usage: 
```python linter.py extract-values myjinja.yaml.j2```
 

2. CloudFormation Linting
This option renders the template using the provided data file and performs CloudFormation linting.
Usage:
```python linter.py cfn-lint data.yaml myjinja.yaml.j2```
 
3. Generate a Rendered Template
This option renders the Jinja template using the provided data file and generates a rendered output file.
Usage:
```python linter.py generate-template data.yaml myfile```
