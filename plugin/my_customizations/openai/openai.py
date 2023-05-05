import openai
import os
from talon import Module, settings, actions

#https://github.com/openai/openai-python
#https://github.com/openai/openai-cookbook/

openai.api_key = os.environ["OPENAI_API_KEY"]
mod = Module()

DEFAULT_PROMPT = """The following text was dictated without correcting misrecognitions stemming from impaired enunciation. Fix any typos and grammatical errors, leaving meaning and structure intact."""

mod.setting(
    "open_ai_fixup_prompt",
    type=str,
    default=DEFAULT_PROMPT,
    desc="Prompt when using GPT to fix misrecognitions.",
)

@mod.action_class
class Actions:
    def open_ai_fixup_text_gpt(text: str) -> str:
        """Uses the OpenAI GPT API to correct misrecognitions in dictated text."""
        prompt = settings.get("user.open_ai_fixup_prompt")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": text},
        ],
        temperature=0, 
        max_tokens=3500, 
        request_timeout=10)
        print(response)
        return response["choices"][0]["message"]["content"].strip('"\'')
    
    def open_ai_fixup_text_davinci(text: str) -> str:
        """Uses the OpenAI GPT API to correct misrecognitions in dictated text."""
        prompt = settings.get("user.open_ai_fixup_prompt")
        model_input = prompt+"\n\n"+text 
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=model_input, 
        temperature=0, 
        max_tokens=3500, 
        request_timeout=10)
        print(response)
        return response["choices"][0]["text"].strip()

    def open_ai_fixup_text_davinci_edit(text: str) -> str:
        """Uses the OpenAI GPT API to correct misrecognitions in dictated text."""
        prompt = settings.get("user.open_ai_fixup_prompt")
        response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=text, 
        instruction=prompt,
        temperature=0,
        #max_tokens=3500, 
        request_timeout=10)
        print(response)
        return response["choices"][0]["text"].strip()