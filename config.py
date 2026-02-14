"""
FILENAME: config.py

Hot-reloadable sampling parameters for the VLM.
main.py reloads this file every turn, so you can edit it
while the loop is running to adjust temperature, etc.
"""

TEMPERATURE: float = 0.7
TOP_P: float = 0.9
MAX_TOKENS: int = 2048
