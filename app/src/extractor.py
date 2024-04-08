from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate.from_template(
   [
       (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
       ()
   ]
)