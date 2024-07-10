from read_notebook import read_notebook, extract_conversations
from prompts import create_variation_prompt
from gpt_call import generate_variation
from save_notebook import save_notebook
import json
import time

def create_conversation_variations(conversations):
    """Creates variations for each conversation in the list."""
    variations = []
    for convo in conversations:
        prompt = create_variation_prompt(convo['source'])
        if convo['source'] == "# Conversation":
            variation =  convo['source']
        else:
            variation = generate_variation(prompt, model='gpt')
            time.sleep(2)  # Wait for 2 seconds before making the next request, only for groq, this can be commented out when using gpt-4
        variations.append({
            'cell_type': convo['cell_type'],
            'source': variation,
            'metadata': convo['metadata'],
            'id': convo['id']
        })
    return variations

# Example usage with a single notebook file
file_path = 'notebooks/Sample3.ipynb'  # Change this path to test other files
output_path = 'outputs/Varied_Sample3.ipynb'  # Output file path
notebook = read_notebook(file_path)
conversations = extract_conversations(notebook)

# Create variations
variations = create_conversation_variations(conversations)

# Save the varied conversations to a new notebook file
save_notebook(variations, notebook, output_path)
print("done!")