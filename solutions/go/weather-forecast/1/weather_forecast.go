// Package weather provides tools for forecasting and reporting the current weather conditions.
// It allows setting the current location and condition, and generating a formatted weather forecast.
package weather


var (
    // CurrentCondition stores the latest weather condition for the specified location.
    // It is updated whenever Forecast is called.
	CurrentCondition string
    // CurrentLocation stores the name of the location for which the weather forecast applies.
    // It is updated whenever Forecast is called.
	CurrentLocation  string
)
// Forecast returns a weather report for the given city and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
