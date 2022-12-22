import ephem
import datetime

constellations = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                  'Libra', 'Scorpio', 'Sagittarius', 'Capricornus', 'Aquarius', 'Pisces')

ephem.

def celestialinfo(celestial,place,date):
    place.date = date
    celestial.compute(place)
    # 天体の角度の誤差が大きいので原因を探る必要がある
    # へびつかい座が出る。１２星座にできないか探る
    if (ephem.constellation(celestial)[1] == 'Ophiuchus'):
        index = 9
    else:
        index = constellations.index(ephem.constellation(celestial)[1])

    return celestial.az * (180/3.1415) - index * 30 , ephem.constellation(celestial)

sapporo = ephem.Observer()
sapporo.lat = '43.062087'
sapporo.lon = '141.354404'

print(sapporo.date)

sun = ephem.Sun()
mercury = ephem.Mercury()
venus = ephem.Venus()
moon = ephem.Moon()
mars = ephem.Mars()
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()
uranus = ephem.Uranus()
neptune = ephem.Neptune()
pluto = ephem.Pluto()

print("Sun",celestialinfo(sun, sapporo, datetime.datetime.utcnow()))
print("Mercury",celestialinfo(mercury, sapporo, datetime.datetime.utcnow()))
print("Venus",celestialinfo(venus, sapporo, datetime.datetime.utcnow()))
print("Moon",celestialinfo(moon, sapporo, datetime.datetime.utcnow()))
print("Mars", celestialinfo(mars, sapporo, datetime.datetime.utcnow()))
print("Jupiter", celestialinfo(jupiter, sapporo, datetime.datetime.utcnow()))
print("Satuen", celestialinfo(saturn, sapporo, datetime.datetime.utcnow()))
print("Uranus", celestialinfo(uranus, sapporo, datetime.datetime.utcnow()))
print("Neptune", celestialinfo(neptune, sapporo, datetime.datetime.utcnow()))
print("Pluto", celestialinfo(pluto, sapporo, datetime.datetime.utcnow()))
