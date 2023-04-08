# Formas de importar un módulo y acceder a uno o varios miembros.
# 1)
    # import Modulos.saludar_usuario
    # saludo = Modulos.saludar_usuario.saludar_usuario("Exequiel")

# 2)
    # from Modulos import saludar_usuario
    # saludo = saludar_usuario.saludar_usuario("Exequiel") 

# 3) 
    # from Modulos.saludar_usuario import saludar_usuario
    # saludo = saludar_usuario("Exequiel")

# 4) Importar dos miembros del módulo
    # from Modulos.saludar_usuario import saludar_usuario, despedir_usuario
    # saludo = saludar_usuario("Exequiel")
    # despedida = despedir_usuario("Exequiel")

# 5) Importar todos los miembros del módulo (MALA PRÁCTICA)
    # from Modulos.saludar_usuario import *
    # saludo = saludar_usuario("Exequiel")
    # despedida = despedir_usuario("Exequiel")
    # mensaje = hago_algo()

# 6) Importar un módulo en un enrutamiento diferente.
    # import sys
    # sys.path.append("rutaModulo")
    # import modulo
    # accion = modulo.funcion()


# Formas de referenciar un módulo o miembros almacenados en este.
# 1)
    # import Modulos.saludar_usuario as m_saludar
    # saludo = m_saludar.saludar_usuario("Exequiel")

# 2)
    # from Modulos import saludar_usuario as m_saludo
    # saludo = m_saludo.saludar_usuario("Exequiel")

# 3)
    # from Modulos.saludar_usuario import saludar_usuario as sal_usu
    # saludo = sal_usu("Exequiel")
