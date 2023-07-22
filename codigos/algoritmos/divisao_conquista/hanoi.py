def hanoi(n, origin, destiny, aux):
    if n > 0:
        hanoi(n - 1, origin, aux, destiny)
        print(f'Move disk {n} from turret {origin} to turret {destiny}')
        hanoi(n - 1, aux, destiny, origin)

# Example
hanoi(3, 'A', 'C', 'B')