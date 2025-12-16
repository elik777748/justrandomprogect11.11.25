import pytest
import main


class TestTimer:

    @pytest.fixture
    def run_delay(self, capsys):
        main.delay()
        captured = capsys.readouterr()
        return captured.out

    def test_delay_is_callable(self):
        assert callable(main.delay)

    def test_output_contains_function_name(self, run_delay):
        assert "delay" in run_delay
        assert "took" in run_delay
        assert "seconds" in run_delay


