import ollama


def summarize_text(text):

    prompt = f"""
    Você é um assistente jurídico.

    Gere um resumo claro e objetivo do documento abaixo:

    {text[:5000]}
    """

    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content'] 
