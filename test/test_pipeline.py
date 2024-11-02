import sys
from pathlib import Path

# Añadir el directorio src al path de Python
src_path = str(Path(__file__).parent.parent / 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from pipeline import generate_learning_path, is_relevant_input
from unittest.mock import Mock, patch
import pytest
import json
from openai import APIError

# Test data
MOCK_RESPONSE = """1. HTML - Lenguaje de marcado para estructurar contenido web
2. CSS - Hojas de estilo en cascada para diseño web
3. JavaScript - Lenguaje de programación para interactividad web"""

@pytest.fixture
def mock_llm_response():
    mock_response = Mock()
    mock_response.content = MOCK_RESPONSE
    return mock_response

def test_is_relevant_input():
    """Test the is_relevant_input function with various inputs"""
    assert is_relevant_input("desarrollador frontend") == True
    assert is_relevant_input("científico de datos") == True
    assert is_relevant_input("cocinero") == False
    assert is_relevant_input("abogado") == False

def test_generate_learning_path_non_relevant():
    """Test generate_learning_path with non-relevant career"""
    result = generate_learning_path("cocinero")
    assert "message" in result
    assert "TechBot" in result["message"]

@patch('src.learning_path.llm')
def test_generate_learning_path_success(mock_llm, mock_llm_response):
    """Test successful generation of learning path"""
    mock_llm.invoke.return_value = mock_llm_response
    
    result = generate_learning_path("desarrollador frontend")
    
    assert "roadmap" in result
    assert "nodes" in result["roadmap"]
    assert len(result["roadmap"]["nodes"]) == 3
    assert result["roadmap"]["nodes"][0]["name"] == "HTML"

@patch('src.learning_path.llm')
def test_generate_learning_path_api_error(mock_llm):
    """Test error handling for API errors"""
    mock_llm.invoke.side_effect = APIError("API Error")
    
    result = generate_learning_path("desarrollador frontend")
    assert "error" in result
    assert "Error en la solicitud a OpenAI" in result["error"]

def test_empty_input():
    """Test handling of empty input"""
    result = generate_learning_path("")
    assert "message" in result
    assert "TechBot" in result["message"]

# Añadimos algunos tests adicionales para mayor cobertura
def test_generate_learning_path_with_spaces():
    """Test handling of input with extra spaces"""
    result = generate_learning_path("   desarrollador frontend   ")
    assert "roadmap" in result or "message" in result

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    [],
    {},
])
def test_generate_learning_path_invalid_input(invalid_input):
    """Test handling of invalid input types"""
    result = generate_learning_path(invalid_input)
    assert "message" in result
    assert "TechBot" in result["message"]