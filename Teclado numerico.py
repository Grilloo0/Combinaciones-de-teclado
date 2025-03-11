def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapeo de como queda el teclado
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    result = []

    def backtrack(index, current_combination):
        if index == len(digits):
            result.append("".join(current_combination))
            return

        for letter in phone_map[digits[index]]:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()  

    backtrack(0, [])
    return result


while True:
    user_input = input("Ingresa los números del 2 al 9 (o 'N' para salir): ")
    
    if user_input.upper() == "N":
        print("Nos vemos c:")
        break  
    
    if not user_input.isdigit() or any(d not in "23456789" for d in user_input):
        print("No se admite, porfa solo ingresa números del 2 al 9.")
        continue  

    combinations = letterCombinations(user_input)
    print("Posibles combinaciones:", combinations)
