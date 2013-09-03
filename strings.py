# -*- coding: utf-8 -*-

generic_no = [
    "Nein",
    "Negativ!",
    "Heut gibts kein Regen."
]

texts = {
    "clear-day": generic_no + ["Nein. Die Sonne scheint!"],
    "clear-night": ["Nein"],
    "rain": ["Scheiße, es regnet!"], 
    "snow": [],
    "sleet": generic_no + [],
    "wind": generic_no + [],
    "fog": generic_no + [],
    "cloudy": generic_no + [],
    "partly-cloudy-day": generic_no + [],
    "partly-cloudy-night": generic_no + ["Heut Nacht ist es nur wolkig", "Nope. Aber Wolken gibts."]
}

colors = {
    "clear-day": ("", ""),
    "clear-night": ("", ""),
    "rain": ("", ""), 
    "snow": ("", ""),
    "sleet": ("", ""),
    "wind": ("", ""),
    "fog": ("", ""),
    "cloudy": ("", ""),
    "partly-cloudy-day": ("#84ACBF", "#fff"),
    "partly-cloudy-night": ("#37444A", "#fff")
}

