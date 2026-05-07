# Definición del flujo principal para generar un backlog a partir de una historia de usuario utilizando el agente PM.

from pm_agent import generate_backlog

user_story = """
Como usuario quiero iniciar sesión
para acceder a la plataforma.

Criterios:
- email válido
- JWT
- recuperación de password
- bloqueo tras múltiples intentos
"""

result = generate_backlog(user_story)

print("\n=== BACKLOG GENERADO ===\n")
print(result)

with open("../outputs/backlog.json", "w", encoding="utf-8") as file:
    file.write(result)

print("\nBacklog guardado en outputs/backlog.json")