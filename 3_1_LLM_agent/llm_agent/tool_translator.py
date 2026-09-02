# llm_agent/tool_tranlator.py

from libretranslatepy import LibreTranslateAPI
import asyncio

class TranslatorTool:
	#"""Инструмент для перевода текста с одного языка на другой через бесплатный API GoogleTrans"""
	name: str = 'translator'
	description: str = 'Переводит текст с одного языка на другой'
	translator = LibreTranslateAPI('http://localhost:5000')

	def use(self, text: str, source_lang: str, target_lang: str) -> str:
		"""
			Переводит текст 'text' с языка 'source_lang' на язык 'target_lang'. Требует язык в двухбуквенном формате
		"""
		try:
			translated = self.translator.translate(text, source_lang, target_lang)
			return translated
		except Exception as e:
			# Это сообщение будет выведено в лог, если ошибка возникнет на самом верхнем уровне
			print(f"> Ошибка при выполнении перевода: {e}")
			return f"Произошла ошибка при попытке перевода текста '{text}' с языка '{source_lang}' на язык '{target_lang}': {e}"

if __name__ == '__main__':
	tt = TranslatorTool()
	res = tt.use('Hello, World!', 'en', 'sv')
	print(res)