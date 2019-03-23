from django.db import models

class UsuarioNormal:
    def __init__(self, edad, genero, altura, peso, presion_alta,
                    presion_baja, colesterol, glucosa, fumador,
                    alcohol, actividad):
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.presion_alta = presion_alta
        self.presion_baja = presion_baja

        colesterol = float(colesterol)
        self.colesterol = colesterol
        if (self.colesterol <= 200):
            self.colesterol = 1
        elif (200 < self.colesterol and self.colesterol <= 239):
            self.colesterol = 2
        elif (240 <= self.colesterol):
            self.colesterol = 3

        glucosa = float(glucosa)
        self.glucosa = glucosa
        if (4 <= self.glucosa and self.glucosa <= 6):
            self.glucosa = 1
        elif (7 <= self.glucosa and self.glucosa <= 8):
            self.glucosa = 2
        elif (9 <= self.glucosa and self.glucosa <= 14):
            self.glucosa = 3

        self.fumador = fumador
        self.alcohol = alcohol
        self.actividad = actividad
        self.imc = peso/(altura*altura)

    def getProbabilidad():
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'model_save_medical.h5')
        model = load_model(file_path)
        model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        valores = numpy.array([self.edad,self.genero,self.altura,
                self.peso, self.presion_alta, self.presion_baja,
                self.colesterol,self.glucosa,self.fumador,
                self.alcohol,self.actividad,self.imc])

        valores = valores.reshape(1,12,1)
        valor = model.predict(valores)
        valor = valor[0][0]
        print(valor)
        return valor

    def getInfoColesterol():
        if (self.colesterol == 1):
            info = 'Colesterol 1'
        elif (self.colesterol == 2):
            info = 'Colesterol 2'
        elif (self.colesterol == 3):
            info = 'Colesterol 3'
        return info


class usuarioMedico:
    def __init__(self, dolor,presion,colesterol,
                glucemia,electro,ritmo,angina,depresion):

        self.eddolorad = dolor
        self.presion = presion
        self.colesterol = colesterol
        self.glucemia = glucemia
        self.electro = electro
        self.ritmo = ritmo
        self.angina = angina
        self.depresion = depresion


    def getProbabilidad():
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'hfg_model.h5')
        model = load_model(file_path)
        model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        valores = numpy.array(self, self.dolor,self.presion,
                    self.colesterol, self.glucemia,self.electro,
                    self.ritmo,self.angina,self.depresion)

        valores = valores.reshape(1,8,1)
        valor = model.predict(valores)
        valor = valor[0][0]

        return valor

    def getInfoColesterol():
        if (self.colesterol == 1):
            info = 'Colesterol 1'
        elif (self.colesterol == 2):
            info = 'Colesterol 2'
        elif (self.colesterol == 3):
            info = 'Colesterol 3'
        return info
