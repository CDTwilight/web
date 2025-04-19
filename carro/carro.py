class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro

    def agregar(self, material, cantidad=1):
        return self.actualizar_cantidad(material, cantidad)

    def actualizar_cantidad(self, material, cantidad):
        material_id = str(material.id)
        precio_unitario = float(material.precio_actual)  # Usar precio_actual en lugar de precio
        
        nueva_cantidad = cantidad

        if material.cantidad < nueva_cantidad:
            return False
        
        self.carro[material_id] = {
            'material_id': material.id,
            'nombre': material.nombre,
            'precio_unitario': str(precio_unitario),
            'precio': str(precio_unitario * nueva_cantidad),
            'cantidad': nueva_cantidad,
            'imagen': material.imagen.url,
            'en_oferta': material.en_oferta,  # Guardar si estaba en oferta
            'precio_regular': str(material.precio)  # Guardar precio regular para referencia
        }

        self.guardar_carro()
        return True

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, material):
        material_id = str(material.id)
        if material_id in self.carro:
            del self.carro[material_id]
            self.guardar_carro()

    def restar_material(self, material):
        material_id = str(material.id)
        if material_id in self.carro:
            nueva_cantidad = self.carro[material_id]['cantidad'] - 1
            if nueva_cantidad > 0:
                self.actualizar_cantidad(material, nueva_cantidad)
            else:
                self.eliminar(material)

    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True