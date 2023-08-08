# JSFusion

JSFusion is a simple Python tool that converts JavaScript files into beautified text files, with one text file per JavaScript file. It traverses through the provided directory, recursively searches for JavaScript files, and saves the beautified code in corresponding text files.

## Installation

1. Clone this repository or download the `jsfusion.py` script.
2. Install the required Python packages by running:

   ```bash
   pip3 install jsbeautifier
   ```

## Usage

```bash
python3.10 jsfusion.py --path /path/to/your/js/folder --out /path/to/output/folder
```

## Result

```
output/
│
├── script1_beautified.txt
├── script2_beautified.txt
├── subfolder/
│   ├── script3_beautified.txt
│   └── script4_beautified.txt
└── ...
``````
