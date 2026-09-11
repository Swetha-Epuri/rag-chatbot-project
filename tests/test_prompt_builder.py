from backend.prompts.promt_builder import PromptBuilder

def test_prompt_contains_context():

    prompt = PromptBuilder.build("AI is the simulation of human intelligence.", "What is AI?")

    assert "AI is the simulation" in prompt

def test_prompt_contains_question():

    prompt = PromptBuilder.build("Context","Explain AI")

    assert "Explain AI" in prompt