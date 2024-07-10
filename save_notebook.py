import json

def save_notebook(variations, original_notebook, output_path):
    """Saves the varied conversations to a new notebook file."""
    new_cells = []
    for variation in variations:
        new_cells.append({
            'cell_type': variation['cell_type'],
            'source': [variation['source']],
            'metadata': variation['metadata'],
            'id': variation['id']
        })
    
    # Create a new notebook structure
    new_notebook = {
        'cells': new_cells,
        'metadata': original_notebook.get('metadata', {}),
        'nbformat': original_notebook.get('nbformat', 4),
        'nbformat_minor': original_notebook.get('nbformat_minor', 2)
    }
    
    # Save the new notebook to the output path
    with open(output_path, 'w') as file:
        json.dump(new_notebook, file, indent=2)
