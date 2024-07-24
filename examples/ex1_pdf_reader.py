from llm_axe.agents import PdfReader
from llm_axe.models import OllamaChat

#llm = OllamaChat(model="llama3:instruct")
llm=OllamaChat(model="llama3.1:8b-instruct-q8_0")

# We specify the files that we want the llm to be able to read.
# Note: The files should fit within your LLM's context window.
info = "C:/Ia/docs/0/biele05.pdf"


files = [info]
agent = PdfReader(llm)
#resp = agent.ask("Extract all phone numbers found in any of these documents.", files)
resp = agent.ask("Extract all the information and output as json format.", files)

print(resp)

