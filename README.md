Taller_10 — Instrucciones de ejecución
=====================================

Resumen
------
Proyecto de ejemplo que genera un backlog técnico a partir de una historia de usuario utilizando Ollama.

Dependencias
------------
Listado de dependencias Python en `requirements.txt`:

- `ollama` 
- `python-dotenv`
- `requests` 
- `fastapi`, `uvicorn` 
- `pytest` 

Preparación del entorno (PowerShell)
-----------------------------------
```powershell
# activar el entorno virtual
.\venv\Scripts\Activate.ps1

# actualizar pip e instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Instalar modelos en Ollama
--------------------------
Los modelos deben descargarse localmente con la CLI de Ollama. Ejemplos:

```powershell
ollama list
ollama pull qwen2.5-coder:1.5b
```

Configuración de entorno
------------------------
Crear un archivo `.env` o usar variables de entorno. Ejemplo mínimo (`.env.example` incluido):

```
OLLAMA_MODEL=qwen2.5-coder:1.5b
```

El código lee `OLLAMA_MODEL` en `app/pm_agent.py` y usará ese identificador para conectar con Ollama.

OpenCode
--------
`OpenCode` es una herramienta externa independiente que puede integrarse con Ollama para ejecutar tareas definidas en prompts. No es una dependencia Python directa de este proyecto —instálala y configúrala siguiendo sus propias instrucciones—, luego conecta su salida/entrada con el flujo de Ollama según necesites.

Para lanzar `OpenCode` con Ollama en PowerShell del equipo, ejecuta:

```powershell
ollama launch opencode
```

Notas adicionales
----------------
- Para cambiar el modelo por defecto exporta `OLLAMA_MODEL` o edita `.env`.
- Si usas Windows y hay problemas creando `venv`, cierra procesos que puedan bloquear archivos y prueba de nuevo.

# AI Task Planner

Sistema basado en IA para generación automática de backlog técnico a partir de historias de usuario.

Tecnologías:
- Python
- Ollama
- OpenCode
- qwen2.5-coder

Flujo:
Historia de Usuario → PM Agent → Backlog Técnico → OpenCode → Boilerplate

Comandos en PowerShell para perparar entorno:

# Activar venv
.\venv\Scripts\Activate.ps1

# Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Verifica modelos disponibles
ollama list

# Bajar los modelos requeridos (descarga local)
ollama pull qwen2.5-coder:1.5b
ollama pull deepseek-coder:1.3b
