import subprocess
import sys

PYTHON_EXECUTABLE = sys.executable


def run_script(args):
    cmd = [PYTHON_EXECUTABLE, "checker.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def test_even_number():
    result = run_script(["10"])
    assert result.returncode == 0
    assert result.stdout.strip() == "I'm Even."


def test_odd_number():
    result = run_script(["7"])
    assert result.returncode == 0
    assert result.stdout.strip() == "I'm Odd."


def test_multiple_args():
    result = run_script(["5", "10"])
    assert result.returncode != 0
    assert "AssertionError: more than one or no argument is provided" in result.stderr


def test_very_long_number_string():
    """Expected: ValueError: Exceeds the limit (4300 digits) for integer string conversion -> arg isn't an int."""
    long_number_str = "9" * 5000
    result = run_script([long_number_str])
    assert result.returncode != 0
    assert "AssertionError: argument is not an integer" in result.stderr


def test_zero():
    result = run_script(["0"])
    assert result.returncode == 0
    assert result.stdout.strip() == "I'm Zero."


def test_no_arguments():
    result = run_script([])
    assert result.returncode != 0
    assert "AssertionError: more than one or no argument is provided" in result.stderr


def test_string_argument():
    result = run_script(["hello"])
    assert result.returncode != 0
    assert "AssertionError: argument is not an integer" in result.stderr
