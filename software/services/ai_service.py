import ollama


def summarize_text(text):

    prompt = f"""
Você é um assistente jurídico especializado em análise de processos judiciais brasileiros.

Analise o documento abaixo e gere um resumo jurídico estruturado e explicativo.

O resumo deve possuir DUAS PARTES:

1. RESUMO ESTRUTURADO
- Número do processo
- Vara/Comarca
- Partes envolvidas
- Advogados
- Assunto principal
- Valor da causa
- Principais movimentações
- Decisões importantes
- Prazos relevantes
- Situação atual do processo

2. RESUMO CONTEXTUAL
Explique em texto corrido:
- o que aconteceu no processo
- qual o conflito discutido
- quais pedidos foram realizados
- quais decisões foram tomadas
- em que fase o processo está atualmente

Regras:
- Utilize linguagem jurídica clara e profissional
- Organize bem os parágrafos
- Evite repetir informações
- Destaque informações importantes
- Explique os acontecimentos de forma objetiva
- Caso existam muitas movimentações repetidas, resuma apenas as mais relevantes

Documento judicial:

{text}>
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