class Omnibus:
    def __init__(self, chapa, km_recorridos, km_maximos, disponible, estado, capacidad):
        self._chapa = chapa
        self._km_recorridos = km_recorridos
        self._km_maximos = km_maximos
        self._disponible = disponible
        self._estado = estado
        self._capacidad = capacidad

    @property
    def chapa(self):
        return self._chapa

    @chapa.setter
    def chapa(self, value):
        self._chapa = value

    @property
    def km_recorridos(self):
        return self._km_recorridos

    @km_recorridos.setter
    def km_recorridos(self, value):
        self._km_recorridos = value

    @property
    def km_maximos(self):
        return self._km_maximos

    @km_maximos.setter
    def km_maximos(self, value):
        self._km_maximos = value

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        self._disponible = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value):
        self._capacidad = value

class Chofer:
    def __init__(self, calificacion, identificacion, anos_experiencia):
        self._calificacion = calificacion
        self._identificacion = identificacion
        self._anos_experiencia = anos_experiencia

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def calificacion(self, value):
        self._calificacion = value

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, value):
        self._identificacion = value

    @property
    def anos_experiencia(self):
        return self._anos_experiencia

    @anos_experiencia.setter
    def anos_experiencia(self, value):
        self._anos_experiencia = value

class Viaje:
    def __init__(self, codigo, km_recorrer, costo_estimado, chofer_id, tipo, provincia_destino=None, regular_especial=None, paradas_intermedias=None):
        self._codigo = codigo
        self._km_recorrer = km_recorrer
        self._costo_estimado = costo_estimado
        self._chofer_id = chofer_id
        self._tipo = tipo
        self._provincia_destino = provincia_destino
        self._regular_especial = regular_especial
        self._paradas_intermedias = paradas_intermedias

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def km_recorrer(self):
        return self._km_recorrer

    @km_recorrer.setter
    def km_recorrer(self, value):
        self._km_recorrer = value

    @property
    def costo_estimado(self):
        return self._costo_estimado

    @costo_estimado.setter
    def costo_estimado(self, value):
        self._costo_estimado = value

    @property
    def chofer_id(self):
        return self._chofer_id

    @chofer_id.setter
    def chofer_id(self, value):
        self._chofer_id = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def provincia_destino(self):
        return self._provincia_destino

    @provincia_destino.setter
    def provincia_destino(self, value):
        self._provincia_destino = value

    @property
    def regular_especial(self):
        return self._regular_especial

    @regular_especial.setter
    def regular_especial(self, value):
        self._regular_especial = value

    @property
    def paradas_intermedias(self):
        return self._paradas_intermedias

    @paradas_intermedias.setter
    def paradas_intermedias(self, value):
        self._paradas_intermedias = value

class Terminal:
    def __init__(self):
        self.omnibuses = []
        self.choferes = []
        self.viajes = []

    def insertar_omnibus(self, omnibus):
        self.omnibuses.append(omnibus)

    def actualizar_omnibus(self, chapa, nuevos_datos):
        for omnibus in self.omnibuses:
            if omnibus.chapa == chapa:
                omnibus.km_recorridos = nuevos_datos.get('km_recorridos', omnibus.km_recorridos)
                omnibus.km_maximos = nuevos_datos.get('km_maximos', omnibus.km_maximos)
                omnibus.disponible = nuevos_datos.get('disponible', omnibus.disponible)
                omnibus.estado = nuevos_datos.get('estado', omnibus.estado)
                omnibus.capacidad = nuevos_datos.get('capacidad', omnibus.capacidad)
                return True
        return False

    def eliminar_omnibus(self, chapa):
        self.omnibuses = [omnibus for omnibus in self.omnibuses if omnibus.chapa != chapa]

    def insertar_chofer(self, chofer):
        self.choferes.append(chofer)

    def actualizar_chofer(self, identificacion, nuevos_datos):
        for chofer in self.choferes:
            if chofer.identificacion == identificacion:
                chofer.calificacion = nuevos_datos.get('calificacion', chofer.calificacion)
                chofer.anos_experiencia = nuevos_datos.get('anos_experiencia', chofer.anos_experiencia)
                return True
        return False

    def eliminar_chofer(self, identificacion):
        self.choferes = [chofer for chofer in self.choferes if chofer.identificacion != identificacion]

    def insertar_viaje(self, viaje):
        self.viajes.append(viaje)

    def actualizar_viaje(self, codigo, nuevos_datos):
        for viaje in self.viajes:
            if viaje.codigo == codigo:
                viaje.km_recorrer = nuevos_datos.get('km_recorrer', viaje.km_recorrer)
                viaje.costo_estimado = nuevos_datos.get('costo_estimado', viaje.costo_estimado)
                viaje.chofer_id = nuevos_datos.get('chofer_id', viaje.chofer_id)
                viaje.tipo = nuevos_datos.get('tipo', viaje.tipo)
                viaje.provincia_destino = nuevos_datos.get('provincia_destino', viaje.provincia_destino)
                viaje.regular_especial = nuevos_datos.get('regular_especial', viaje.regular_especial)
                viaje.paradas_intermedias = nuevos_datos.get('paradas_intermedias', viaje.paradas_intermedias)
                return True
        return False

    def eliminar_viaje(self, codigo):
        self.viajes = [viaje for viaje in self.viajes if viaje.codigo != codigo]

    def listar_omnibus_por_capacidad(self):
        return sorted(self.omnibuses, key=lambda x: x.capacidad, reverse=True)

    def listar_viajes_interprovinciales_especiales(self, provincia_destino):
        return [(viaje.codigo, viaje.chofer_id) for viaje in self.viajes if viaje.tipo == "interprovincial" and viaje.regular_especial == "especial" and viaje.provincia_destino == provincia_destino]

    def contar_omnibus_no_disponibles_malos(self):
        return len([omnibus for omnibus in self.omnibuses if not omnibus.disponible and omnibus.estado == "Malo"])

    def listar_choferes_por_experiencia(self):
        return sorted(self.choferes, key=lambda x: x.anos_experiencia, reverse=True)

    def listar_omnibus_por_km_y_calificacion(self, calificacion):
        return [omnibus for omnibus in self.omnibuses if omnibus.km_recorridos <= omnibus.km_maximos / 2 and any(chofer.calificacion == calificacion for chofer in self.choferes if chofer.identificacion == omnibus.chapa)]

    def calcular_recaudacion_viaje(self, viaje):
        recaudacion = viaje.costo_estimado * next((omnibus.capacidad for omnibus in self.omnibuses if omnibus.chapa == viaje.codigo), 0) - viaje.km_recorrer * 1.5
        if viaje.tipo == "interprovincial" and viaje.regular_especial == "especial":
            recaudacion -= 100
        return recaudacion

# Función para interactuar con el usuario
def menu_interactivo():
    terminal = Terminal()
    while True:
        print("\n--- Menú Interactivo ---")
        print("1. Insertar ómnibus")
        print("2. Actualizar ómnibus")
        print("3. Eliminar ómnibus")
        print("4. Insertar chofer")
        print("5. Actualizar chofer")
        print("6. Eliminar chofer")
        print("7. Insertar viaje")
        print("8. Actualizar viaje")
        print("9. Eliminar viaje")
        print("10. Listar ómnibus por capacidad")
        print("11. Listar viajes interprovinciales especiales a Camagüey")
        print("12. Contar ómnibus no disponibles y en estado malo")
        print("13. Listar choferes por experiencia")
        print("14. Listar ómnibus por km recorridos y calificación del chofer")
        print("15. Calcular recaudación de un viaje")
        print("16. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            chapa = input("Ingrese la chapa del ómnibus: ")
            km_recorridos = int(input("Ingrese los km recorridos: "))
            km_maximos = int(input("Ingrese los km máximos: "))
            disponible = input("¿Está disponible? (True/False): ") == "True"
            estado = input("Ingrese el estado (Bueno/Regular/Malo): ")
            capacidad = int(input("Ingrese la capacidad: "))
            omnibus = Omnibus(chapa, km_recorridos, km_maximos, disponible, estado, capacidad)
            terminal.insertar_omnibus(omnibus)
            print("Ómnibus insertado correctamente.")

        elif opcion == "2":
            chapa = input("Ingrese la chapa del ómnibus a actualizar: ")
            nuevos_datos = {}
            km_recorridos = input("Ingrese los nuevos km recorridos (deje en blanco para no cambiar): ")
            if km_recorridos:
                nuevos_datos['km_recorridos'] = int(km_recorridos)
            km_maximos = input("Ingrese los nuevos km máximos (deje en blanco para no cambiar): ")
            if km_maximos:
                nuevos_datos['km_maximos'] = int(km_maximos)
            disponible = input("¿Está disponible? (True/False, deje en blanco para no cambiar): ")
            if disponible:
                nuevos_datos['disponible'] = disponible == "True"
            estado = input("Ingrese el nuevo estado (Bueno/Regular/Malo, deje en blanco para no cambiar): ")
            if estado:
                nuevos_datos['estado'] = estado
            capacidad = input("Ingrese la nueva capacidad (deje en blanco para no cambiar): ")
            if capacidad:
                nuevos_datos['capacidad'] = int(capacidad)
            if terminal.actualizar_omnibus(chapa, nuevos_datos):
                print("Ómnibus actualizado correctamente.")
            else:
                print("Ómnibus no encontrado.")

        elif opcion == "3":
            chapa = input("Ingrese la chapa del ómnibus a eliminar: ")
            terminal.eliminar_omnibus(chapa)
            print("Ómnibus eliminado correctamente.")

        elif opcion == "4":
            calificacion = input("Ingrese la calificación del chofer (A/B/C): ")
            identificacion = input("Ingrese la identificación del chofer: ")
            anos_experiencia = int(input("Ingrese los años de experiencia: "))
            chofer = Chofer(calificacion, identificacion, anos_experiencia)
            terminal.insertar_chofer(chofer)
            print("Chofer insertado correctamente.")

        elif opcion == "5":
            identificacion = input("Ingrese la identificación del chofer a actualizar: ")
            nuevos_datos = {}
            calificacion = input("Ingrese la nueva calificación (A/B/C, deje en blanco para no cambiar): ")
            if calificacion:
                nuevos_datos['calificacion'] = calificacion
            anos_experiencia = input("Ingrese los nuevos años de experiencia (deje en blanco para no cambiar): ")
            if anos_experiencia:
                nuevos_datos['anos_experiencia'] = int(anos_experiencia)
            if terminal.actualizar_chofer(identificacion, nuevos_datos):
                print("Chofer actualizado correctamente.")
            else:
                print("Chofer no encontrado.")

        elif opcion == "6":
            identificacion = input("Ingrese la identificación del chofer a eliminar: ")
            terminal.eliminar_chofer(identificacion)
            print("Chofer eliminado correctamente.")

        elif opcion == "7":
            codigo = input("Ingrese el código del viaje: ")
            km_recorrer = int(input("Ingrese los km a recorrer: "))
            costo_estimado = float(input("Ingrese el costo estimado para un pasajero: "))
            chofer_id = input("Ingrese la identificación del chofer: ")
            tipo = input("Ingrese el tipo de viaje (interprovincial/intermunicipal): ")
            provincia_destino = None
            regular_especial = None
            paradas_intermedias = None
            if tipo == "interprovincial":
                provincia_destino = input("Ingrese la provincia de destino: ")
                regular_especial = input("Ingrese si es regular o especial: ")
            elif tipo == "intermunicipal":
                paradas_intermedias = int(input("Ingrese la cantidad de paradas intermedias: "))
            viaje = Viaje(codigo, km_recorrer, costo_estimado, chofer_id, tipo, provincia_destino, regular_especial, paradas_intermedias)
            terminal.insertar_viaje(viaje)
            print("Viaje insertado correctamente.")

        elif opcion == "8":
            codigo = input("Ingrese el código del viaje a actualizar: ")
            nuevos_datos = {}
            km_recorrer = input("Ingrese los nuevos km a recorrer (deje en blanco para no cambiar): ")
            if km_recorrer:
                nuevos_datos['km_recorrer'] = int(km_recorrer)
            costo_estimado = input("Ingrese el nuevo costo estimado para un pasajero (deje en blanco para no cambiar): ")
            if costo_estimado:
                nuevos_datos['costo_estimado'] = float(costo_estimado)
            chofer_id = input("Ingrese la nueva identificación del chofer (deje en blanco para no cambiar): ")
            if chofer_id:
                nuevos_datos['chofer_id'] = chofer_id
            tipo = input("Ingrese el nuevo tipo de viaje (interprovincial/intermunicipal, deje en blanco para no cambiar): ")
            if tipo:
                nuevos_datos['tipo'] = tipo
            provincia_destino = input("Ingrese la nueva provincia de destino (deje en blanco para no cambiar): ")
            if provincia_destino:
                nuevos_datos['provincia_destino'] = provincia_destino
            regular_especial = input("Ingrese si es regular o especial (deje en blanco para no cambiar): ")
            if regular_especial:
                nuevos_datos['regular_especial'] = regular_especial
            paradas_intermedias = input("Ingrese la nueva cantidad de paradas intermedias (deje en blanco para no cambiar): ")
            if paradas_intermedias:
                nuevos_datos['paradas_intermedias'] = int(paradas_intermedias)
            if terminal.actualizar_viaje(codigo, nuevos_datos):
                print("Viaje actualizado correctamente.")
            else:
                print("Viaje no encontrado.")

        elif opcion == "9":
            codigo = input("Ingrese el código del viaje a eliminar: ")
            terminal.eliminar_viaje(codigo)
            print("Viaje eliminado correctamente.")

        elif opcion == "10":
            print("\nÓmnibus ordenados por capacidad:")
            for omnibus in terminal.listar_omnibus_por_capacidad():
                print(f"Chapa: {omnibus.chapa}, Capacidad: {omnibus.capacidad}")

        elif opcion == "11":
            print("\nViajes interprovinciales especiales a Camagüey:")
            for viaje in terminal.listar_viajes_interprovinciales_especiales_camagüey():
                print(f"Código: {viaje.codigo}, Chofer: {viaje.chofer_id}, Km a recorrer: {viaje.km_recorrer}")

        elif opcion == "12":
            print("\nCantidad de ómnibus no disponibles y en estado malo:")
            print(terminal.contar_omnibus_no_disponibles_malos())

        elif opcion == "13":
            print("\nChoferes ordenados por años de experiencia:")
            for chofer in terminal.listar_choferes_por_experiencia():
                print(f"Identificación: {chofer.identificacion}, Años de experiencia: {chofer.anos_experiencia}")

        elif opcion == "14":
            calificacion = input("Ingrese la calificación del chofer (A/B/C): ")
            print(f"\nÓmnibus cuyos km recorridos no pasan la mitad de su cantidad máxima de km a recorrer y cuyos choferes tienen calificación {calificacion}:")
            for omnibus in terminal.listar_omnibus_por_km_y_calificacion(calificacion):
                print(f"Chapa: {omnibus.chapa}, Km recorridos: {omnibus.km_recorridos}, Km máximos: {omnibus.km_maximos}")

        elif opcion == "15":
            codigo = input("Ingrese el código del viaje: ")
            viaje = next((viaje for viaje in terminal.viajes if viaje.codigo == codigo), None)
            if viaje:
                print(f"\nRecaudación del viaje {codigo}:")
                print(terminal.calcular_recaudacion_viaje(viaje))
            else:
                print("Viaje no encontrado.")

        elif opcion == "16":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 16.")

# Ejecutar el menú interactivo
menu_interactivo()
