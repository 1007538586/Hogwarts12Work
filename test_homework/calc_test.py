import pytest
import yaml

from python.Calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    # 参数化,加法
    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load(open("./add_data.yaml")))
    def test_add_all(self, a, b, expect):
        # print(a + b)
        result = self.calc.add(a, b)
        print(result)
        assert expect == result

    # 除法
    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load(open("./div_data.yaml")))
    def test_div_all(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            print(result)
        except ZeroDivisionError:
            result = 'None'
        assert expect == result

    if __name__ == '__main__':
        pytest.main(['-vs', 'calc_test.py::TestCalc'])
