import openai
import os
from talon import Module, settings, actions

#https://github.com/openai/openai-python
#https://github.com/openai/openai-cookbook/

openai.api_key = os.environ["OPENAI_API_KEY"]
mod = Module()

DEFAULT_PROMPT = """The following text was dictated without correcting misrecognitions stemming from impaired enunciation. Fix any typos and grammatical errors, leaving meaning and structure intact."""

#DEFAULT_PROMPT = """The following text was dictated without correcting misrecognitions stemming from impaired enunciation. Fix any typos and grammatical errors, leaving meaning and structure intact. These technical terms are often misrecognized: Zutobi, Zutobi Instructor, Zutobi Drivers Ed. And these are the names of my colleagues: Joel, Pia, Sachino, Artem, Roman, Taras, Davor, Olha (often misrecognized as all her or all our), Dima. And these are common services that we are using: Figma, Adobe, Imgix, WebPageTest, Cloudflare, GCS, Bitwarden, Jira, Mautic, Cursorless, VS code, Talon, Tiktok, Linkedin, Grammarly, Calendly, Kochava, Trustpilot, Ahrefs, Github, Rango, Gopro."""

#These technical terms are often misrecognized: Zutobi, Zutobi Instructor, Zutobi Drivers Ed.
#And these are the names of my colleagues: Joel, Pia, Sachino, Artem, Roman, Taras, Davor, Olha, Dima.
#And these are common services that we are using: Figma, Adobe, Imgix, WebPageTest, Cloudflare, GCS, Bitwarden, Jira, Mautic, Cursorless, VS code, Talon, Tiktok, Linkedin, Grammarly, Calendly, Kochava, Trustpilot, Ahrefs, Github, Rango, Gopro.

#There are a few technical terms which are often misrecognized, I've listed them below in the format "Correct spelling of the term, Common misrecognition"
#Zutobi,satobe
#Zutobi Drivers Ed,satobe driver's ed
#Zutobi Instructor,satobe instructor

mod.setting(
    "open_ai_fixup_prompt",
    type=str,
    default=DEFAULT_PROMPT,
    desc="Prompt when using GPT to fix misrecognitions.",
)

@mod.action_class
class Actions:
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
        #https://blog.finxter.com/python-print-without-quotes/