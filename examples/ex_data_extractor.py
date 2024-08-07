from llm_axe.core import read_pdf, safe_read_json
from llm_axe.models import OllamaChat
from llm_axe.agents import DataExtractor


#llm=OllamaChat(model="llama3:8b-instruct-q8_0")
llm=OllamaChat(model="llama3.1:8b-instruct-q8_0")

info = read_pdf("C:/Ia/docs/0/biele05.pdf")

# It will reply in proper json since we set reply_as_json to True
de = DataExtractor(llm, reply_as_json=True,temperature=0)

#resp = de.ask(info, ["name", "email", "phone", "address","items"])
resp = de.ask(info, ["name", "email", "phone", "address","items","all data"])

print(resp)

# We can then convert to a proper python object if we wish
resp_json = safe_read_json(resp)
print(resp_json)