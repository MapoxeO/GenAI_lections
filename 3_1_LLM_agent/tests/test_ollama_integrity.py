import pytest

from llm_agent.core_v2 import LLMAgent

OLLAMA_MODEL = 'qwen3.5:latest'

agent = LLMAgent(local = True, ollama_model = OLLAMA_MODEL)

def test_ollama_connection_is_available():
	assert agent.test_ollama_connection()

def test_process_query_returns_non_empty_answer():
	query = 'What is 2 + 2? Answer only with one number.'
	response = agent.process_query(query)
	assert int(response) == 2 + 2

@pytest.mark.parametrize('case', [
	('What is 1 + 4 + 9? Answer only with one number.', '14', True),
	('Translate pharse "How are you?" into Russian. Answer only with translated phrase.', 'Как дела?', True),
	('Hello!', 'Hello', False),
	#('28 stab wounds', '28 ножевых ранений'),
])
def test_usage_of_actions(case):
	test_query, awaited, used_tool = case
	base_query = 'Solve given task. If you have used tools then append to the answer string "<USED TOOL>" else append "<NOT USED TOOL>". '
	query = base_query + test_query
	response = agent.process_query(query)

	assert (awaited in query) and (('<USED TOOL>' in response) == used_tool)