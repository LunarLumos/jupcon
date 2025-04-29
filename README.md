
---

```md
# ⚡ Jupcon — Jupyter Notebook ⇄ Python Script Converter

> 🧠 A powerful, stylish CLI tool to convert `.ipynb` notebooks into clean `.py` scripts (and back) without cell prompts or clutter.

---

## ✨ Why Jupcon?

`Jupcon` (short for *Jupyter Converter*) is a minimalist yet powerful Python3 utility that makes it effortless to switch between `.ipynb` and `.py` formats. Perfect for:

- ⚙️ Devs who want **clean Python scripts** from notebooks.
- 🧪 Researchers who need to **rebuild notebooks from scripts**.
- 💻 Students and tinkerers working across formats.

No more noisy cell comments. Just clean, readable code.

---

## 🚀 Features

- 🔁 **Two-way Conversion**  
  Convert `.ipynb` ↔ `.py` smoothly with one command.

- ✂️ **Clutter-Free Output**  
  Strips away `# In[1]`, `# %%`, and unnecessary cell prompts.

- 🎨 **Stylish Terminal Interface**  
  Colorful CLI using `colorama` & `termcolor`.

- 🧼 **Tab Customization**  
  Replace tabs with your preferred number of spaces.

- 🐍 **Python 3 Compatible**

---

## ⚙️ Installation

Make sure you have Python 3. Then install the required dependencies:

```bash
pip install nbformat nbconvert colorama termcolor
```

---

## 💡 Usage Guide

```bash
python3 jupcon.py -j my_notebook.ipynb           # Convert .ipynb to clean .py
python3 jupcon.py -p script.py                   # Convert .py back to .ipynb
python3 jupcon.py -j input.ipynb -o output.py    # Custom output filename
python3 jupcon.py -j input.ipynb --tabsize 2     # Custom tab spacing
```

### 🔧 CLI Options

| Argument        | Description                                      |
|-----------------|--------------------------------------------------|
| `-j`, `--ipynb` | Convert from `.ipynb` to `.py`                   |
| `-p`, `--py`    | Convert from `.py` to `.ipynb`                   |
| `-o`, `--output`| Optional output file path                        |
| `--tabsize`     | Number of spaces to replace each tab (default: 4)|

---

## 📸 Terminal Preview

```text
         _ _  _ ___  ____ ____ _  _ 
         | |  | |__] |    |  | |\ | 
        _| |__| |    |___ |__| | \| 

        Created by: Lunar Lumos

A versatile tool for converting Jupyter Notebooks (.ipynb)
to Python scripts (.py) and vice versa without clutter.

✅ Converted to clean .py: notebook_clean.py
```

---

## 📂 Output Example

### Input: `notebook.ipynb`

```python
# In[1]:
import numpy as np

# In[2]:
print("Hello from notebook!")
```

### Output: `notebook.py`

```python
import numpy as np

print("Hello from notebook!")
```

> 🧽 Clean and simple, without any cell prompts or markers!

---

## 👤 Author

**Lunar Lumos**  
🧪 Developer | 🌒 Tinkerer | 🛠️ Toolsmith  
Crafting tools for smart development.

---

## 💫 Show Your Support

If you found this project useful:

⭐ Star this repo  
🍴 Fork it  
🐦 Share it  

Let’s keep the dev tools clean and powerful.

---

## 🧪 License

MIT — feel free to use and improve.
```

---

Would you like me to save this into a `README.md` file for your project or generate a version with emoji-free terminal output style?
