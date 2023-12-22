import os
import re
import subprocess
import pandas as pd
from bs4 import BeautifulSoup, Tag

filedir = os.listdir("wrapped_functions")

# parsing each function with srcml
for file in filedir:
    infile = f"wrapped_functions/{file}"
    outfile = f"{infile[:-5]}.xml"

    subprocess.run(["srcml", infile, "--position", "-o", outfile])