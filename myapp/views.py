from django.shortcuts import render
from django.http import HttpResponseRedirect
from keras.models import load_model
import os
import numpy

def view_index(request):
    return render(request, 'index.html', {})

def view_personal(request):
    return render(request, 'personal.html', {})

def form_personal(request):
    data = request.GET.copy()

    edad = float(data.get('edad'))/356
    genero = float(data.get('genero'))

    altura = float(data.get('altura'))
    if (altura < 10):
        altura = altura*100

    peso = float(data.get('peso'))
    presion_alta = float(data.get('presion_alta'))
    presion_baja = float(data.get('presion_baja'))

    colesterol = float(data.get('colesterol'))
    if (colesterol <= 200):
        colesterol = 1
    elif (200 < colesterol and colesterol <= 239):
        colesterol = 2
    elif (240 <= colesterol):
        colesterol = 3

    glucosa = float(data.get('glucosa'))
    fumador = float(data.get('fumador'))
    alcohol = float(data.get('alcohol'))
    actividad = float(data.get('actividad'))
    imc = peso/((altura/100)*(altura/100))


    valorNormal = calcularValorNormal(edad,genero,altura,peso,presion_alta,presion_baja,colesterol,glucosa,fumador,alcohol,actividad,imc)

    enunciadoIndice = 'Su índice de masa corporal es: ' + str(round(imc,2))

    if (imc < 18):
        resultadoIndice = 'Bajo peso.'
    elif (18 <=imc and imc <25):
        resultadoIndice = 'Peso adecuado'
    elif (imc >= 25 and imc < 30):
        resultadoIndice = 'Sobrepeso'
    else:
        resultadoIndice = 'Obesidad'

    enunciadoIndice = enunciadoIndice + '. '  + resultadoIndice

    resultado = str(round(valorNormal*100,0)) + '% de riesgo de evento cardiovascular en 10 años.'

    return render(request, 'personalMostrar.html', {'enunciadoIndice':enunciadoIndice, 'resultado': resultado})

def calcularValorNormal(edad,genero,altura,peso,presion_alta,presion_baja,colesterol,glucosa,fumador,alcohol,actividad,imc):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model_personal.h5')
    model = load_model(file_path)
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    genero1 =0
    genero2 = 0
    if genero == 0:
        genero1 = 1
    elif genero == 1:
        genero2 = 1

    colesterol1 =0
    colesterol2 = 0
    colesterol3 = 0
    if colesterol == 1:
        colesterol1 = 1
    elif colesterol == 2:
        colesterol2 = 1
    elif colesterol == 3:
        colesterol2 = 1

    glucosa1 =0
    glucosa2 = 0
    glucosa3 = 0
    if glucosa == 1:
        glucosa1 = 1
    elif glucosa == 2:
        glucosa2 = 1
    elif glucosa == 3:
        glucosa2 = 1

    fumador1 =0
    fumador2 = 0
    if fumador == 0:
        fumador1 = 1
    elif fumador == 1:
        fumador2 = 1

    actividad1 =0
    actividad2 = 0
    if actividad == 0:
        actividad1 = 1
    elif actividad == 1:
        actividad2 = 1

    alcohol1 =0
    alcohol2 = 0
    if alcohol == 0:
        alcohol1 = 1
    elif alcohol == 1:
        alcohol2 = 1

    valores = numpy.array([edad,
            altura,
            peso,
            presion_alta,
            presion_baja,
            genero1, genero2,
            colesterol1, colesterol2, colesterol3,
            glucosa1, glucosa2, glucosa3,
            fumador1, fumador2,
            alcohol1, alcohol2,
            actividad1, actividad2])


    valores = valores.reshape(1,19,1)
    valor = model.predict(valores)
    valor = valor[0][0]
    return valor


def form_medico(request):
    data = request.GET.copy()

    edad = float(data.get('edad'))/356
    genero = float(data.get('genero'))

    dolor = float(data.get('dolor'))
    dolor1 =0
    dolor2 = 0
    dolor3 = 0
    dolor4 = 0
    if dolor == 1:
        dolor1 = 1
    elif dolor == 2:
        dolor2 = 1
    elif dolor == 3:
        dolor2 = 1
    elif dolor == 4:
        dolor2 = 1
    presion = float(data.get('presion'))
    colesterol = float(data.get('colesterol'))

    azucar = float(data.get('azucar'))
    if azucar < 125:
        azucar = 0
    else:
        azucar = 1

    azucar1 =0
    azucar2 = 0
    if azucar == 0:
        azucar1 = 1
    elif azucar == 1:
        azucar2 = 1


    electro = float(data.get('electro'))
    electro1 =0
    electro2 = 0
    electro3 = 0
    if electro == 1:
        electro1 = 1
    elif electro == 2:
        electro2 = 1
    elif electro == 3:
        electro2 = 1
    ritmo = float(data.get('ritmo'))
    angina = float(data.get('angina'))
    angina1 =0
    angina2 = 0
    if angina == 1:
        angina1 = 1
    elif angina == 2:
        angina2 = 1
    depresion = float(data.get('depresion'))


    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model_save_medical.h5')
    model = load_model(file_path)
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    valores = numpy.array([edad,
            genero,
            dolor1, dolor2, dolor3, dolor4,
            presion,
            colesterol,
            azucar1, azucar2,
            electro1, electro2, electro3,
            ritmo,
            angina1, angina2,
            depresion])


    valores = valores.reshape(1,17)
    valor = model.predict(valores)
    valorMedico = valor[0][0]


    if valorMedico < 0.5:
        resultado = 'No pacede estenosis significativa. (más de 50%)'
    else:
        resultado = 'Posiblemente padece estenosis significativa. (más de 50%)'

    return render(request, 'medicoMostrar.html', {'resultado':resultado})

def calcularValorMedico():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model_personal.h5')
    model = load_model(file_path)
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    valores = numpy.array([edad,
            altura,
            peso,
            presion_alta,
            presion_baja,
            genero,
            colesterol,
            glucosa,
            fumador,
            alcohol,
            actividad,])


    valores = valores.reshape(1,11,1)
    valor = model.predict(valores)
    valor = valor[0][0]
    return valor


def view_nosotros(request):
    return render(request, 'nosotros.html', {})

def view_medico(request):
    return render(request, 'medico.html', {})

def view_resultados(request):
    return render(request, 'personal.html', {})

def view_habitos(request):
    return render(request, 'habitos.html', {})






        # colesterol1 =0
        # colesterol2 = 0
        # colesterol3 = 0
        # if colesterol == 1:
        #     colesterol1 = 1
        # elif colesterol == 2:
        #     colesterol2 = 1
        # elif colesterol == 3:
        #     colesterol2 = 1
        #
        # glucosa1 = 0
        # glucosa2 = 0
        # glucosa3 = 0
        # if glucosa == 1:
        #     glucosa1 = 1
        # elif glucosa == 2:
        #     glucosa2 = 1
        # elif glucosa == 3:
        #     glucosa3 = 1
        #
        # genero1 = 0
        # genero2 = 0
        # if genero == 1:
        #     genero1 = 1
        # elif genero == 2:
        #     genero2 = 1
        #
        # fumador1 = 0
        # fumador2 = 0
        # if fumador == 1:
        #     fumador1 = 1
        # elif fumador == 2:
        #     fumador2 = 1
        #
        # actividad1 = 0
        # actividad2 = 0
        # if actividad  == 1:
        #     actividad1 = 1
        # elif actividad  == 2:
        #     actividad2 = 1
        #
        # alcohol1 = 0
        # alcohol2 = 0
        # if alcohol  == 1:
        #     alcohol1 = 1
        # elif alcohol  == 2:
        #     alcohol2 = 1
