import logging
import os
import openai
from dotenv import load_dotenv
import os

class SummarizeService():
	def __init__(self):
		load_dotenv()
		openai.api_key = os.getenv("OPENAI_API_KEY")

	def summarize_text(self, text_to_summarize):
		if not text_to_summarize:
			raise ValueError("The text to summarize cannot be empty")
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=text_to_summarize + "\n\nTl;dr",
			temperature=0.7,
			max_tokens=200,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=1
			)

		summarized = response["choices"][0]["text"]
		print(f"Text to summarize:{text_to_summarize} summarized : {summarized}")
		return summarized