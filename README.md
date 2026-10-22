# Flight-planner
Flight planner to calculate time and show the path taken

## Roadmap

### 1. Taxi, takeoff and landing time
- [ ] Add fixed extra time on top of cruise time (e.g. ~15 min taxi out, ~10 min climb/descent, ~7 min taxi in)
- [ ] Print a breakdown of each phase as well as the total

### 2. Map of the flight path
- [ ] Use `folium` to make an HTML map with markers for both airports
- [ ] Draw the real great-circle route (many points along the curve, not a straight line)
- [ ] Handle routes that cross the Pacific (longitude jumps from +180 to -180)
- [ ] Show airport names and cities on the markers

### 3. Weather
- [ ] Show the current weather (METAR) at both airports using the free aviationweather.gov API
- [ ] Use winds at cruise altitude (e.g. Open-Meteo) to adjust speed for headwinds and tailwinds

### Extras
- [ ] Show airport names in the output (e.g. "London Heathrow → John F. Kennedy")
- [ ] Keep a fuel reserve in the range check (e.g. only count ~90% of max range as usable)
- [ ] Suggest a fuel stop when no plane has enough range
- [ ] Add `pytest` tests for `haversine` and `flight_t`
