from typing import Union


class Sensor:
    def __init__(self):
        self._channels = list()
        self.text = "OK"

        self._POSSIBLE_SIZES = (
            "one",
            "kilo",
            "mega",
            "giga",
            "tera",
            "byte",
            "kilobyte",
            "megabyte",
            "gigabyte",
            "terabyte",
            "bit",
            "kilobit",
            "megabit",
            "gigabit",
            "terabit",
        )

        self._CONTENT = {
            "unit": {
                "name": "Unit",
                "values": (
                    "custom",
                    "count",
                    "cpu",
                    "bytesfile",
                    "speeddisk",
                    "speednet",
                    "timehours",
                    "timeseconds",
                    "timeresponse",
                    "percent",
                    "temperature",
                    "bytesdisk",
                    "bytesbandwidth",
                ),
            },
            "speed_size": {"name": "SpeedSize", "values": self._POSSIBLE_SIZES},
            "volume_size": {"name": "VolumeSize", "values": self._POSSIBLE_SIZES},
            "speed_time": {"name": "SpeedTime", "values": ("second", "minute", "hour", "day")},
            "mode": {"name": "Mode", "values": ("absolute", "difference")},
            "float": {"name": "Float", "values": (0, 1)},
            "decimal_mode": {"name": "DecimalMode", "values": ("auto", "all")},
            "warning": {"name": "Warning", "values": (0, 1)},
            "show_chart": {"name": "ShowChart", "values": (0, 1)},
            "show_table": {"name": "ShowTable", "values": (0, 1)},
            "limit_mode": {"name": "LimitMode", "values": (0, 1)},
            "custom_unit": "CustomUnit",
            "limit_max_error": "LimitMaxError",
            "limit_min_error": "LimitMinError",
            "limit_max_warning": "LimitMaxWarning",
            "limit_min_warning": "LimitMinWarning",
            "limit_error_msg": "LimitErrorMsg",
            "limit_warning_msg": "LimitWarningMsg",
            "value_lookup": "ValueLookup",
        }

    def add_channel(self, name: str, value: Union[int, float, str], **kwargs) -> None:
        """
        This adds a channel to the sensor object

            Parameters:
            ----------
            ``name : str``
                Name of the channel as displayed in user interfaces
            ``value : int | float | str``
                The value as integer or float
            ``unit : str``
                The unit of the value. This is useful for PRTG to convert volumes and times
            ``custom_unit : str``
                If Custom is used as unit, this is the text displayed behind the value
            ``speed_size : str, volume_size : str``
                Size used for the display value
            ``speed_time : str``
                Used when displaying the speed
            ``mode : str``
                Select if the value is an absolute value or counter
            ``float : int``
                Define if the value is a float. The default is 0 (no)
            ``decimal_mode : str``
                Init value for the Decimal Places option. Use with float
            ``warning : int``
                If enabled for at least one channel, the entire sensor is set to the Warning status. The default is 0 (no)
            ``show_chart : int``
                Init value for the Show in graphs option. The default is 1 (yes)
            ``show_table : int``
                Init value for the Show in tables option. The default is 1 (yes)
            ``limit_max_error : int | float``
                Define an upper error limit for the channel
            ``limit_min_error : int | float``
                Define an upper warning limit for the channel
            ``limit_max_warning : int | float``
                Define a lower warning limit for the channel
            ``limit_min_warning : int | float``
                Define a lower error limit for the channel
            ``limit_error_msg : str``
                Define an additional error message
            ``limit_warning_msg : str``
                Define an additional warning message
            ``limit_mode : int``
                Define if the limit settings defined above are active. The default is 0
            ``value_lookup : str``
                Define if you want to use a lookup file. Enter the ID of the lookup file that you want to use
        """
        if len(self._channels) > 49:
            raise IndexError("You can define only 50 channels per each sensor")

        channel = {"Channel": name}
        for k, v in kwargs.items():
            content = self._CONTENT[k]
            if isinstance(content, dict):
                if (v.lower() if isinstance(v, str) else v) in content["values"]:
                    channel[content["name"]] = v
                else:
                    raise ValueError("The %s value can not be used" % k)
            else:
                channel[content] = v

        if channel.get("Unit") == "Custom" and not channel.get("CustomUnit"):
            raise ValueError("You must to set short custom_unit")

        channel["Value"] = "%f" % float(value) if channel.get("Float") else "%d" % int(float(value))

        self._channels.append(channel)

    def get_result(self, text: str = None) -> dict:
        """
        Return result with channels and text.

        Returns
        ----------
            ``result``
                Dict of result data for prtg
        """
        if not text:
            text = self.text
        return {"prtg": {"result": self._channels, "text": text}}

    def get_ok(self, text: str = None) -> dict:
        """
        Return fast ok result with text.

        Parameters:
        ----------
            ``text : str``
                Text message. The default is text of sensor (OK)

        Returns
        ----------
            ``result``
                Dict of result data for prtg

        """
        if not text:
            text = self.text
        if not self._channels:
            self.add_channel("ok", 1)
        return {"prtg": {"result": self._channels, "error": 0, "text": text}}

    def get_error_result(self, text: str = None) -> dict:
        """
        Return error result with text.

        Parameters:
        ----------
            ``text : str``
                Error message. The default is text of sensor (OK)

        Returns
        ----------
            ``result``
                Dict of result data for prtg

        """
        if not text:
            text = self.text
        return {"prtg": {"error": 1, "text": text}}
