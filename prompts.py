def create_variation_prompt(conversation):
    variation_prompt = f"""You are provided with a part of a long conversation between a "User" and an AI "Assistant".
            The task is to create a variation of the given part of the conversation following the instructions given.
            Instructions:\n
                - The start of the string might have "User" or "Assistant" or any abbreviation of weather the given part is from the user or the AI, use the same abbreviation for the output. 
                - If the conversation contains code then you can create a variation without chanding the main logic. Do not change the function names as well.
                - if the conversation does not contain code: Do not change the original meaning of the content, just rephrase.
                - Strictly refrain from giving any additional information or description like: "Here is the output", "Here is the modified content", etc. Only straight away return the output.
            Below is the given part of the conversation, also strictly adher to the instructions provided for the output.
            
            "{conversation}\n"
            
            Additional information: return the output Without any additional information.
    """
    return variation_prompt
