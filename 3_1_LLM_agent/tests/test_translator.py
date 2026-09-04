import pytest

from llm_agent.tool_translator import TranslatorTool

@pytest.fixture
def translator():
    return TranslatorTool()

@pytest.mark.parametrize('case', [
	('Hello, World!', 'Привет, Мир!'),
	('How are you?', 'Как дела?'),
	('When I was young...', 'Когда я был молод...'),
	('28 stab wounds', '28 ножевых ранений'),
])
def test_translate_text_input_in_english_to_russian(translator, case):
	source_text, target_text = case
	assert translator.use(source_text, 'en', 'ru') == target_text

@pytest.mark.parametrize('case', [
	('Ни слова по-русски', 'Not a word in Russian'),
	('Физическая боль причиняет вред, но духовная больнее', 'Physical pain hurts, but spiritual pain hurts more'),
	('Пей воду каждый день и будешь здоровым!', 'Drink water every day and you will be healthy!'),
])
def test_translate_text_input_in_russian_to_english(translator, case):
	source_text, target_text = case
	assert translator.use(source_text, 'ru', 'en') == target_text

@pytest.mark.parametrize('empty_input', ['', '   ', '\n'])
def test_translate_empty_input(translator, empty_input):
	assert translator.use(empty_input, 'en', 'ru') == ''

def test_translate_same_language(translator):
    text = 'Homodrill 2.0'
    assert translator.use(text, 'en', 'en') == text

@pytest.mark.parametrize('non_translatable', ['12345', '!!!@#$', 'https://google.com'])
def test_translate_non_translatable_content(translator, non_translatable):
    assert translator.use(non_translatable, 'en', 'ru') == non_translatable

def test_translate_invalid_language_codes_raises_error(translator):
    assert translator.use("Hello", "en", "xyz")