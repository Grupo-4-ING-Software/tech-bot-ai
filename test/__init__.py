import os
import sys
from pathlib import Path

# Añade el directorio src al PYTHONPATH
project_root = Path(__file__).parent.parent
src_path = str(project_root / 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Configuración de variables de entorno para testing
os.environ.setdefault('ENVIRONMENT', 'test')
os.environ.setdefault('OPENAI_API_KEY', 'test-key')