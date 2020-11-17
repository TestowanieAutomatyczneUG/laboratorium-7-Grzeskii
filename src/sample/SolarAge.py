class SolarAge:

    def game(self, seconds, planet):
        if type(seconds) is not int or type(planet) is not str:
            raise Exception("Wrong arguments!")
        solar_system = {
            "ziemia" : 31557600,
            "merkury" : round(0.2408467 * 31557600),
            "wenus" : round(0.61519726 * 31557600),
            "mars" : round(1.8808158 * 31557600),
            "jowisz" : round(11.862615 * 31557600),
            "saturn" :  round(29.447498 * 31557600),
            "uran" :  round(84.016846 * 3157600),
            "neptun" : round(164.79132 * 3157600)
        }
        age = seconds / solar_system[planet.lower()]
        return round(age, 2)
