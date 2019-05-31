# Example of the pathlib module

from pathlib import Path
# Absolute path
# C:\Program Files\Microsoft etc
# /use/local/bin etc

path = Path("ecommerce")
for file in path.glob('*.py'):
    print(file)