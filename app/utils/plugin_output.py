import re

def extract_plugin_output_info(plugin_output: str):
    main_points = ['Check Name', 'Audit File', 'Information', 'Rationale', 'Result', 'Actual Value', 
                   'Policy Value', 'Solution', 'See Also', 'Reference Information', 'Additional Information',
                   'Note', 'Default Value', 'Impact']

    output_dict = {key: '-' for key in main_points}
    pattern = r'({}):\s*(.*?)\s*(?={}:|$)'.format('|'.join(re.escape(mp) for mp in main_points), '|'.join(re.escape(mp) for mp in main_points))
    matches = re.findall(pattern, plugin_output, re.DOTALL)

    for key, value in matches:
        output_dict[key.strip()] = value.strip()

    return output_dict
