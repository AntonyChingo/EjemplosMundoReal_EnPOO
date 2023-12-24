#En este ejemplo, tendremos clases para representar películas, clientes y reservas. Cada reserva estará asociada a un cliente y una película.
class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Película: {self.titulo}, Duración: {self.duracion}, Género: {self.genero}")


class Cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre}, Edad: {self.edad}")


class Reserva:
    def __init__(self, cliente, pelicula, horario):
        self.cliente = cliente
        self.pelicula = pelicula
        self.horario = horario

    def mostrar_informacion(self):
        print("Reserva:")
        self.cliente.mostrar_informacion()
        self.pelicula.mostrar_informacion()
        print(f"Horario de la reserva: {self.horario}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de películas
    pelicula1 = Pelicula("Titanic", "2h 30min", "Romance")
    pelicula2 = Pelicula("Matrix", "2h 15min", "Ciencia Ficción")

    # Crear instancias de clientes
    cliente1 = Cliente("Juan", 25)
    cliente2 = Cliente("Ana", 30)

    # Crear instancias de reservas
    reserva1 = Reserva(cliente1, pelicula1, "Viernes 20:00")
    reserva2 = Reserva(cliente2, pelicula2, "Sábado 15:30")

    # Mostrar información de las reservas
    reserva1.mostrar_informacion()
    print("------------------------")
    reserva2.mostrar_informacion()
#En este ejemplo: Pelicula, Cliente, y Reserva son clases que representan entidades del mundo real.
Cada clase tiene un constructor (__init__) para inicializar sus atributos.
Cada clase tiene un método (mostrar_informacion) que muestra la información de la entidad.
Las reservas están asociadas a clientes y películas.