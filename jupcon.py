import os
import argparse
import nbformat
from nbconvert import PythonExporter
from nbformat.v4 import new_notebook, new_code_cell
from colorama import Fore, Back, Style, init
from termcolor import colored

init(autoreset=True)

def print_banner():
    banner = r""" 
         _ _  _ ___  ____ ____ _  _ 
         | |  | |__] |    |  | |\ | 
        _| |__| |    |___ |__| | \| 
    """

    print(Fore.CYAN + banner)

    static_text = "		Created by: "
    creator_name = colored("Lunar Lumos", 'magenta', attrs=['blink'])  # Only name will blink
    print(static_text + creator_name)


    description_text = colored("A versatile tool for converting Jupyter Notebooks (.ipynb) to Python scripts (.py) and vice versa without clutter.", 'green')
    print(description_text)


def convert_ipynb_to_clean_py(input_file, output_file=None, tab_size=4):
    if not os.path.isfile(input_file):
        print(Fore.RED + f"❌ File not found: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    exporter = PythonExporter()
    exporter.exclude_output = True
    exporter.exclude_input_prompt = True

    raw_script, _ = exporter.from_notebook_node(notebook)

    cleaned_lines = []
    previous_blank = False

    for line in raw_script.splitlines():
        stripped = line.strip()

        if (
            stripped.startswith("# In[") or
            stripped.startswith("# %%") or
            stripped.startswith("# ---") or
            (stripped.startswith("#") and not stripped[1:].lstrip().startswith("!"))
        ):
            continue

        line = line.replace('\t', ' ' * tab_size)
        line = line.rstrip()

        if line == "":
            if not previous_blank:
                cleaned_lines.append("")
                previous_blank = True
            continue

        previous_blank = False
        cleaned_lines.append(line)

    final_script = "\n".join(cleaned_lines).strip() + "\n"

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.py'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_script)

    print(Fore.GREEN + f"✅ Converted to clean .py: {output_file}")

def convert_py_to_ipynb(input_file, output_file=None):
    if not os.path.isfile(input_file):
        print(Fore.RED + f"❌ File not found: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()

    blocks = code.split('\n\n')
    cells = [new_code_cell(source=block.strip()) for block in blocks if block.strip()]

    notebook = new_notebook(cells=cells)

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.ipynb'

    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

    print(Fore.GREEN + f"✅ Converted to .ipynb: {output_file}")

if __name__ == "__main__":
    print_banner()

    parser = argparse.ArgumentParser(description="Convert .ipynb <=> .py with formatting")
    parser.add_argument("-j", "--ipynb", help="Convert .ipynb to  .py")
    parser.add_argument("-p", "--py", help="Convert .py to .ipynb")
    parser.add_argument("-o", "--output", help="Optional output file path")
    parser.add_argument("--tabsize", type=int, default=4, help="Tab size to use when cleaning .py (default: 4)")

    args = parser.parse_args()

    if args.ipynb:
        convert_ipynb_to_clean_py(args.ipynb, args.output, args.tabsize)
    elif args.py:
        convert_py_to_ipynb(args.py, args.output)
    else:
        print(Fore.YELLOW + "❗ Please use -j <notebook.ipynb> or -p <script.py> to specify the conversion direction.")
