from unittest.mock import patch, Mock
from app.utils import obter_frase_do_dia

@patch('app.utils.requests.get')
def test_obter_frase_do_dia_com_sucesso(mock_get):
    """Testa o caminho feliz: as duas APIs respondem perfeitamente."""
    
    mock_resposta_conselho = Mock()
    mock_resposta_conselho.json.return_value = {'slip': {'advice': 'Drink water.'}}
    mock_resposta_traducao = Mock()
    mock_resposta_traducao.json.return_value = {'responseData': {'translatedText': 'Beba água.'}}
    mock_get.side_effect = [mock_resposta_conselho, mock_resposta_traducao]
    resultado = obter_frase_do_dia()
    
    assert resultado == 'Beba água.'
    assert mock_get.call_count == 2 


@patch('app.utils.requests.get')
def test_obter_frase_do_dia_com_falha(mock_get):
    mock_get.side_effect = Exception("Erro de conexão com a internet!")
    resultado = obter_frase_do_dia()
    assert resultado == "Lembre-se: beber água e descansar também são parte do tratamento!"