import json
import pandas as pd
import datetime


def flatten_json(json_data, parent_key='', flattened_dict=None):
    if flattened_dict is None:
        flattened_dict = {}

    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            flatten_json(value, new_key, flattened_dict)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            new_key = f"{parent_key}[{i}]"
            flatten_json(item, new_key, flattened_dict)
    else:
        flattened_dict[parent_key] = json_data

    return flattened_dict


# Read the run_results.json file
with open('gcp_automation/target/run_results.json') as file:
    data = json.load(file)
# Extract the test results from the data
test_results = data.get('results', [])
print('Test_Results:', test_results)

# Flatten the test results
flattened_data = []
for result in test_results:
    flattened_result = flatten_json(result)
    flattened_data.append(flattened_result)

print('Flatten \n', flattened_data)
# Convert the flattened data to a DataFrame
df = pd.DataFrame(flattened_data)

# Rename the columns
new_column_names = {'status': 'status', 'timing[0].name': '1st Level','timing[0].started_at':'C_started_at',
                    'timing[0].completed_at':'C_completed_at','timing[1].name': 'Excute Level',
                    'timing[1].started_at':'C_started_at','timing[1].completed_at':'C_completed_at',
                    'thread_id':'thread_id','execution_time':'execution_time','error_message':'error_message',
                    'failures':'failures','unique_id':'test_name'}
df.rename(columns=new_column_names, inplace=True)

# Print the flattened DataFrame
print(df)

# Generate a timestamp string
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%p")
df.to_csv(f'reporting/dbt_test/run_results_{timestamp}.csv',index=False)

# Apply styling to the DataFrame
# styled_df = df.style.set_table_styles([
#     {'selector': 'thead',
#      'props': [('background-color', 'lightblue'),
#                ('font-weight', 'bold')]}
# ])

# Export the styled DataFrame to an HTML file
# styled_df.to_html(f'reporting/dbt_test/html/run_results_{timestamp}.html', index=False)
# df.to_html('reporting/run_results.html',justify='center',index=False)