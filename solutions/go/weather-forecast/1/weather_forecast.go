// Package weather provides tools to predict the weather.
package weather

// CurrentCondition: variable for the current condition.
var CurrentCondition string

// CurrentLocation: variable for the current location.
var CurrentLocation string

// Forecast: uses the variables to print a forecast for the current location and conditions.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
