from .challenge import *

base_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_can_find_corrupted():
    assert first_corrupted("(]") == "]"
    assert first_corrupted("{()()()>") == ">"
    assert first_corrupted("(((()))}") == "}"
    assert first_corrupted("<([]){()}[{}])") == ")"
    assert first_corrupted("{([(<{}[<>[]}>{[]{[(<()>") == "}"


def test_can_sum_corrupted():
    assert sum_corrupted(base_input) == 26397


def test_can_generate_completion():
    assert "".join(generate_completion_chars("[({(<(())[]>[[{[]{<()<>>")) == "}}]])})]"
    assert "".join(generate_completion_chars("[(()[<>])]({[<{<<[]>>(")) == ")}>]})"
    assert "".join(generate_completion_chars("(((({<>}<{<{<>}{[]{[]{}")) == "}}>}>))))"
    assert "".join(generate_completion_chars("{<[[]]>}<{[{[{[]{()[[[]")) == "]]}}]}]}>"
    assert "".join(generate_completion_chars("<{([{{}}[<[[[<>{}]]]>[]]")) == "])}>"
