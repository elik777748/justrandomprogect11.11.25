import time
import main


class TestTimerDecorator:

    def test_delay_is_callable(self):
        assert callable(main.delay)

    def test_delay_returns_none(self):
        result = main.delay()
        assert result is None

    def test_delay_execution_time(self):
        start = time.time()
        main.delay()
        end = time.time()
        assert end - start >= 5
        assert end - start <= 6

    def test_output_contains_function_name(self, capsys):
        main.delay()
        output = capsys.readouterr().out
        assert "delay" in output

    def test_output_contains_execution_time(self, capsys):
        main.delay()
        output = capsys.readouterr().out
        assert "took" in output
        assert "seconds" in output
