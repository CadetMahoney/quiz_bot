def get_all_variables(questions):
    all_variables = []
    for variable_list in [question['variables'] for question in questions]:
        for variable in variable_list:
            all_variables.append(variable)
    return all_variables