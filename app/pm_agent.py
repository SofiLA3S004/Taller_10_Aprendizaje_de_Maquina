"""Genera un backlog a partir de una historia de usuario usando Ollama."""

import os

import ollama

from prompts import PM_AGENT_PROMPT


DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")


def generate_backlog(user_story):

    full_prompt = PM_AGENT_PROMPT + user_story

    response = ollama.chat(
        model=DEFAULT_MODEL,
        messages=[
            {
                'role': 'user',
                'content': full_prompt
            }
        ]
    )

    return response['message']['content']