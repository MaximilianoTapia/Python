from ninja import Ninja
from mascota import Mascota

mascota = Mascota("Max", "Perro", 3)
ninja = Ninja("John", "Doe", "Trofeo", "Croquetas", mascota)

ninja.alimentar()
ninja.caminar()
ninja.bañar()
