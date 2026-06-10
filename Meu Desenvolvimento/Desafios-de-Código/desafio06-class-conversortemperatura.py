class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Exemplo de uso
conversor = ConversorTemperatura()

temperatura_celsius = 25
temperatura_fahrenheit = conversor.celsius_para_fahrenheit(temperatura_celsius)

print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")