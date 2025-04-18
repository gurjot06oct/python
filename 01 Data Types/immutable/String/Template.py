from string import Template

# Step 1: Creating a template string
template_string = "Hello, $name! Today is ${day}."


# Step 2: Creating a Template object
template = Template(template_string)


# Step 3: Substituting placeholders with values using substitute()
result_substitute = template.substitute(name="Alice", day="Monday")


# Step 4: Substituting placeholders with values using safe_substitute()
# If "day" is not provided in the dictionary passed to substitute(), safe_substitute() will still successfully substitute other placeholders and leave the ${day} placeholder unchanged in the resulting string.
result_safe_substitute = template.safe_substitute(name="Alice")


# Step 5: Substituting placeholders with values using substitute() with a dictionary
values = {"name": "Bob", "day": "Tuesday"}
result_dict_substitute = template.substitute(values)


# Step 6: Output
print("Result using substitute():", result_substitute)
print("Result using safe_substitute():", result_safe_substitute)
print("Result using substitute() with a dictionary:", result_dict_substitute)
