import requests

def obter_frase_do_dia():
    """
    Busca um conselho aleatório em inglês e traduz para português na mesma hora.
    Usa duas APIs públicas gratuitas.
    """
    try:
        # Busca o conselho em inglês (adviceslip)
        url_conselho = "https://api.adviceslip.com/advice"
        resposta_conselho = requests.get(url_conselho, timeout=3)
        resposta_conselho.raise_for_status()
        
        dados_conselho = resposta_conselho.json()
        frase_em_ingles = dados_conselho['slip']['advice']
        
        # Manda a frase para a API de Tradução (MyMemory)
        url_traducao = "https://api.mymemory.translated.net/get"
        parametros = {
            "q": frase_em_ingles,
            "langpair": "en|pt-br"
        }
        
        resposta_traducao = requests.get(url_traducao, params=parametros, timeout=3)
        resposta_traducao.raise_for_status()
        
        dados_traducao = resposta_traducao.json()
        frase_em_portugues = dados_traducao['responseData']['translatedText']
        
        return frase_em_portugues
        
    except Exception as e:
        print(f"Erro na integração de APIs: {e}")
        
        # Frase padrão caso algum erro ocorra
        return "Lembre-se: beber água e descansar também são parte do tratamento!"