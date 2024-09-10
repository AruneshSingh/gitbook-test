import os

def build_tree(startpath):
    tree = {}
    for dirpath, dirnames, filenames in os.walk(startpath):
        relative_path = os.path.relpath(dirpath, startpath)
        
        sub_tree = {dirname: {} for dirname in dirnames}
        tree[relative_path] = {'dirs': sub_tree, 'files': filenames}
    
    tree[''] = tree['.']
    del tree['.']    
    return tree

def convert_text_to_title_case(text):
    return text.replace("_", " ").title()

def get_file_header(file_path):
    first_line = ''
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    
    first_line = list(first_line.split('.'))[-1]
    return convert_text_to_title_case(first_line)


def replace_content_between_headers(file_path, start_header, end_header, new_content_arr):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if start_header in line:
            start_idx = i
        elif end_header in line:
            end_idx = i

    if start_idx is not None and end_idx is not None and start_idx < end_idx:
        updated_lines  = lines[:start_idx + 1]
        updated_lines += new_content_arr
        updated_lines += lines[end_idx:]

        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
    else:
        print("Headers not found or are in the wrong order.")
        exit(1)

new_references_to_write = []

def save_tree(directory_tree, cur_path, indent=0):
    global new_references_to_write
    if cur_path in directory_tree:
        for file in directory_tree[cur_path]['files']:
            if file == 'index.md':
                spaces = ' ' * indent
                dir_name = cur_path.split('/')[-1]
                file_path = f'reference/{cur_path}/{file}'
                line_to_print = f"* [{convert_text_to_title_case(dir_name)}]({file_path})"
                new_references_to_write.append(f"{spaces}{line_to_print}\n")
            else:
                spaces = ' ' * (indent + 2)
                file_path = f'reference/{cur_path}/{file}'
                line_to_print = f"* [{get_file_header(file_path)}]({file_path})"
                new_references_to_write.append(f"{spaces}{line_to_print}\n")

        for dir in directory_tree[cur_path]['dirs']:
            new_path = f"{cur_path}/{dir}".strip('/')
            save_tree(directory_tree, new_path, indent + 2)
        
directory_tree = build_tree('reference')

new_references_to_write.append("* [Overview](reference/overview.md)\n")
new_references_to_write.append("* [Changelog](reference/changelog.md)\n")

save_tree(directory_tree, '', 0)

replace_content_between_headers('SUMMARY.md', '## Concepts', '## Use Cases', new_references_to_write)