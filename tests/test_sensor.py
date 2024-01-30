import pytest

from prtg_sensor import Sensor


class TestSensor:
    def test_error_result(self):
        s = Sensor()
        assert s.get_error_result("Test error text") == {"prtg": {"error": 1, "text": "Test error text"}}
        s = Sensor()
        s.text = "Text wasnt set"
        assert s.get_error_result() == {"prtg": {"error": 1, "text": "Text wasnt set"}}

    def test_result(self):
        s = Sensor()
        s.add_channel(
            "Test1-",
            1.98989,
            unit="Custom",
            custom_unit="pcs",
            float=1,
            decimal_mode="all",
        )
        s.add_channel(
            "Test2",
            98,
            unit="percent",
            float=1,
            limit_max_error=98,
            limit_min_error=1,
            limit_max_warning=90,
            limit_min_warning=10,
            limit_error_msg="test error msg$",
            limit_warning_msg="Test w@rn msg!",
            limit_mode=1,
        )
        s.add_channel(
            "Test3@@",
            -3.2,
            unit="timeseconds",
            show_table=0,
            show_chart=0,
        )
        s.add_channel(
            "Test4",
            "-18",
        )
        s.add_channel(
            "Test5",
            "-11.3",
            float=1,
        )
        pld = {
            "prtg": {
                "result": [
                    {
                        "Channel": "Test1-",
                        "Unit": "Custom",
                        "CustomUnit": "pcs",
                        "Float": 1,
                        "DecimalMode": "all",
                        "Value": "1.989890",
                    },
                    {
                        "Channel": "Test2",
                        "Unit": "percent",
                        "Float": 1,
                        "LimitMaxError": 98,
                        "LimitMinError": 1,
                        "LimitMaxWarning": 90,
                        "LimitMinWarning": 10,
                        "LimitErrorMsg": "test error msg$",
                        "LimitWarningMsg": "Test w@rn msg!",
                        "LimitMode": 1,
                        "Value": "98.000000",
                    },
                    {
                        "Channel": "Test3@@",
                        "Unit": "timeseconds",
                        "ShowTable": 0,
                        "ShowChart": 0,
                        "Value": "-3",
                    },
                    {
                        "Channel": "Test4",
                        "Value": "-18",
                    },
                    {
                        "Channel": "Test5",
                        "Value": "-11.300000",
                        "Float": 1,
                    },
                ],
                "text": "OK",
            }
        }
        assert s.get_result() == pld

    def test_result_exceptions(self):
        s = Sensor()
        with pytest.raises(IndexError):
            for i in range(51):
                s.add_channel("%d" % i, i)
        s = Sensor()

        raise_channels = [
            {"name": "test", "value": 0, "mode": "abs"},
            {"name": "test", "value": 0, "unit": "Custom"},
            {"name": "test", "value": -5.4534, "show_chart": 9999},
        ]

        for channel in raise_channels:
            with pytest.raises(ValueError):
                s.add_channel(**channel)
