import pytest

from llm_agent.core_v2 import LLMAgent

OLLAMA_MODEL = 'qwen3.5:latest'

@pytest.fixture
def agent():
    return LLMAgent(local = True, ollama_model = OLLAMA_MODEL)

def test_ollama_connection_is_available(agent):
	assert agent.test_ollama_connection()

def test_process_query_returns_non_empty_answer(agent):
	query = 'What is 2 + 2? Answer only with one number.'
	response = agent.process_query(query)
	assert int(response) == 2 + 2

@pytest.mark.parametrize('case', [
	('What is 1 + 4 + 9? Use tool \'Calculator\' and answer only with one number.', '14', True),
	('Translate pharse "How are you?" into Russian. Use tool \'Translator\'. Answer only with translated phrase.', 'Как дела?', True),
	('Hello!', 'Hello', False),
])
def test_usage_of_actions(agent, case):
	test_query, awaited, used_tool = case
	base_query = 'Solve given task. If you have used tools then append to the answer string "<USED TOOL>" else append "<NOT USED TOOL>". '
	query = base_query + test_query
	response = agent.process_query(query)

	# debug-only
	print(f'Model\'s response for query: {response}')

	assert (awaited in response) and (('<USED TOOL>' in response) == used_tool)