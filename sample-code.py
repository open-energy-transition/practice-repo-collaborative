# a script that writes a random poem
import random
lines = [
    "Roses are red,",
    "Violets are blue,",
    "Sugar is sweet,",
    "And so are you."
]

print("\n".join(random.sample(lines, len(lines))))

    