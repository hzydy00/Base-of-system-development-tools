import sys

from greetlab.cli import main


def test_normal_name_prints_greeting(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"
