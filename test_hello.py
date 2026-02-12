import subprocess

def test_hello_output():
    """Test that hello.py prints 'Hello, World!'"""
    result = subprocess.run(["python", "hello.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!", "Output should be 'Hello, World!'"