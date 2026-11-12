import random


class SlotMachine:
    def __init__(self, name, credits):
        self.name = name
        self._credits = credits
        self._total_bet = 0
        self._total_won = 0

    def display(self):
        status = f"Créditos: S/ {self._credits}" if self._credits > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.name} — {status}")

    def spin(self):
        symbols = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        result = []
        for _ in range(3):
            index = random.randint(0, len(symbols) - 1)
            result.append(symbols[index])
        print(f"[ {result[0]}  {result[1]}  {result[2]} ]")
        return result

    def play(self, bet):
        if self._credits == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if bet <= 0:
            print("❌ La apuesta debe ser mayor a 0.")
            return False
        if bet > self._credits:
            print(f"❌ No tienes suficiente saldo. Créditos: S/ {self._credits}")
            return False

        self._credits -= bet
        self._total_bet += bet
        result = self.spin()

        if result[0] == result[1] == result[2]:
            prize = bet * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {prize}")
            self._credits += prize
            self._total_won += prize
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            prize = bet * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {prize}")
            self._credits += prize
            self._total_won += prize
        else:
            print(f"😢 Perdiste S/ {bet}")
        return True

    def show_stats(self):
        print(f"   🎰 {self.name}")
        print(f"      Apostado: S/ {self._total_bet} | Ganado: S/ {self._total_won}")
        balance = self._total_won - self._total_bet
        sign = "+" if balance >= 0 else ""
        print(f"      Balance:  S/ {sign}{balance} | Créditos actuales: S/ {self._credits}\n")


class FruitSlotMachine(SlotMachine):
    def __init__(self, name, credits):
        super().__init__(name, credits)

    def spin(self):
        symbols = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        result = []
        for _ in range(3):
            index = random.randint(0, len(symbols) - 1)
            result.append(symbols[index])
        print(f"[ {result[0]}  {result[1]}  {result[2]} ]")
        return result


class ClassicSlotMachine(SlotMachine):
    def __init__(self, name, credits):
        super().__init__(name, credits)

    def spin(self):
        symbols = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        result = []
        for _ in range(3):
            index = random.randint(0, len(symbols) - 1)
            result.append(symbols[index])
        print(f"[ {result[0]}  {result[1]}  {result[2]} ]")
        return result


class WorldCupSlotMachine(SlotMachine):
    def __init__(self, name, credits):
        super().__init__(name, credits)

    def spin(self):
        symbols = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        result = []
        for _ in range(3):
            index = random.randint(0, len(symbols) - 1)
            result.append(symbols[index])
        print(f"[ {result[0]}  {result[1]}  {result[2]} ]")
        return result

    def play(self, bet):
        if self._credits == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if bet <= 0:
            print("❌ La apuesta debe ser mayor a 0.")
            return False
        if bet > self._credits:
            print(f"❌ No tienes suficiente saldo. Créditos: S/ {self._credits}")
            return False

        self._credits -= bet
        self._total_bet += bet
        result = self.spin()
        has_peru = "🇵🇪" in result

        if result[0] == result[1] == result[2]:
            prize = bet * 15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {prize}")
            self._credits += prize
            self._total_won += prize
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            prize = bet * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {prize}")
            self._credits += prize
            self._total_won += prize
        elif has_peru:
            print(f"🇵🇪 ¡Perú apareció! Recuperas S/ {bet}")
            self._credits += bet
            self._total_won += bet
        else:
            print(f"😢 Perdiste S/ {bet}")
        return True


def play_machine(machine):
    while machine._credits > 0:
        print()
        machine.display()
        try:
            bet = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if bet == 0:
            break

        machine.play(bet)
    else:
        print("\n💸 Te quedaste sin créditos en esta máquina.")


def show_general_summary(machines):
    total_bet = 0
    total_won = 0
    remaining_credits = 0

    for machine in machines:
        total_bet += machine._total_bet
        total_won += machine._total_won
        remaining_credits += machine._credits

    balance = total_won - total_bet
    sign = "+" if balance >= 0 else ""

    print("\n" + "=" * 38)
    print("   🧾 RESUMEN GENERAL DEL CASINO")
    print("=" * 38)
    print(f"   Total apostado:    S/ {total_bet}")
    print(f"   Total ganado:      S/ {total_won}")
    print(f"   Balance general:   S/ {sign}{balance}")
    print(f"   Créditos actuales: S/ {remaining_credits}")
    print("=" * 38)
    print("💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")


machines = [
    FruitSlotMachine("La Frutal", 200),
    ClassicSlotMachine("La Clásica", 300),
    WorldCupSlotMachine("Mundial 2026", 150),
]

while True:
    print("\n" + "=" * 35)
    print("     🎰 CASINO ROYALE 🎰")
    print("=" * 35)

    for i, machine in enumerate(machines, 1):
        status = f"S/ {machine._credits}" if machine._credits > 0 else "💀 SIN CRÉDITOS"
        print(f"  {i}. {machine.name} ({status})")

    print(f"  {len(machines) + 1}. Mostrar estadísticas de todas")
    print(f"  {len(machines) + 2}. Salir")

    try:
        option = int(input("\nElige una opción: "))
    except ValueError:
        print("Opción inválida.")
        continue

    if 1 <= option <= len(machines):
        selected_machine = machines[option - 1]
        if selected_machine._credits == 0:
            print("💀 Esta máquina está sin créditos. Elige otra.")
        else:
            play_machine(selected_machine)

    elif option == len(machines) + 1:
        print("\n📊 ESTADÍSTICAS DEL CASINO")
        print("-" * 35)
        for machine in machines:
            machine.show_stats()

    elif option == len(machines) + 2:
        show_general_summary(machines)
        break

    else:
        print("Opción inválida.")