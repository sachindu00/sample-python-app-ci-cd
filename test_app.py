from app import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, DevOps World!" in captured.out
