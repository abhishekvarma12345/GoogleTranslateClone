from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)

from langchain.chains import LLMChain

# loading the environment variables
load_dotenv()

class LanguageTranslator:
    def __init__(self):
        self._system_prompt = "Your job is to translate {input_language} to {output_language}."
        self.system_prompt_template = SystemMessagePromptTemplate.from_template(self._system_prompt)

        self._human_prompt = "{text}"
        self.human_prompt_template = HumanMessagePromptTemplate.from_template(self._human_prompt)

        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_prompt_template, self.human_prompt_template])


    def translate(self, source_lang: str, dst_lang:str, text:str):
        # loading LLM chat model
        chat = ChatOpenAI(temperature=0)

        # initialize LLM chain
        translate = LLMChain(llm=chat, prompt=self.chat_prompt)

        return translate.run(input_language=source_lang, output_language=dst_lang, text=text)