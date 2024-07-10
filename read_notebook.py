import json

def read_notebook(file_path):
    """Reads a Jupyter Notebook file and returns its content as a JSON object."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_conversations(notebook):
    """Extracts conversation cells from the notebook."""
    cells = notebook.get('cells', [])
    conversations = []
    for cell in cells:
        if cell['cell_type'] in ['markdown', 'code']:
            conversations.append({
                'cell_type': cell['cell_type'],
                'source': ''.join(cell['source']),
                'metadata': cell.get('metadata', {}),
                'id': cell.get('id', '')
            })
    return conversations
