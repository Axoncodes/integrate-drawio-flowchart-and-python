# Capabilities
You can visit the demo_flowchart.drawio and commands.py files as an example.
- Identify the "Data, process, Storage, Decision, Display" shapes
- Identify the edges connecting one to another
- Sort from start to end
# How to use
1. setup your .env file
    - SRC_FILE: the path to drawio file that has your flowchart diagram
    - DEST_FILE: the path to python file where you want the codes to be written in
    - DEST_XML_FILE: (optional) the path to the XML file which the drawio is first compiled as
2. run the main.ipynb file which will watch the drawio file and update the python file as the drawio file is changed and saved

# Notes
## Layers
- One, just connects the blocks
- Second, makes sense of the possibilities and resolves the short circuits or implementing any simplification which would end up the same as before but no need to all the useless stuff
- Third, Run the flow