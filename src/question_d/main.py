# main.py
from question_d import get_fahrenheit

def main():
    print("Celsius\tFahrenheit")
    print("------------------")
    for celsius in range(21):
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius}\t{fahrenheit}")

if __name__ == "__main__":
    main()
