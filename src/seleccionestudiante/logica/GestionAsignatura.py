from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class GestionAsignatura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        if len(nombreAsignatura)==0:
            return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def editar_asignatura(self, nombreAsignatura):
<<<<<<< HEAD
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).filter(asignatura.nombreAsignatura == nombreAsignatura).first()
            asignatura.nombreAsignatura = nombreAsignatura
            session.commit()
            return True
        else:
            return False
=======
        pass
>>>>>>> 8a05cbc57e2c3ab5018c19e8944257196ef14304
