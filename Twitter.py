# -*- coding: cp1252 -*-
""" Realizado por: Laura Arango, Tania Obando, Verónica Tofiño """
#coding=utf-8
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.repository import Repository
from franz.openrdf.connect import ag_connect
from franz.openrdf.vocabulary import RDF
from franz.miniclient import repository
import os, urllib, datetime, time

#Cada repositorio es una coleccion de tripletas para el mismo grafo

def obtenerRepositorio(repositorio):
    serverAG = AllegroGraphServer('localhost', port=10035, user='superu', password='1234')
    catalogo = serverAG.openCatalog('')
    Repositorio = catalogo.getRepository(repositorio, Repository.ACCESS)
    Repositorio.initialize()
    return Repositorio

def agregar(repository):
    ##CONEXIÃ<93>N Y DEFINICIÃ<93>N DE NAMESPACE
    repositorio = obtenerRepositorio (repository)
    conn = repositorio.getConnection ()
    namespace_ = "http://example.org/people/"

    null = conn.createURI(namespace=namespace_,localname="Null")

    ##DEFINICIÃ<93>N DE URIS DE USUARIOS
    user = conn.createURI(namespace=namespace_,localname="User")
    maria = conn.createURI(namespace=namespace_, localname="Maria")
    vivian = conn.createURI(namespace=namespace_,localname="Vivian")
    pablo = conn.createURI(namespace=namespace_,localname="Pablo")
    david = conn.createURI(namespace=namespace_,localname="David")
    marta = conn.createURI(namespace=namespace_,localname="Marta")
    carlos = conn.createURI(namespace=namespace_,localname="Carlos")

    ##DEFINICIÃ<93>N DE URIS DE DISPONIBILIDAD
    dispo = conn.createURI(namespace=namespace_,localname="Dispo")
    noDipo = conn.createURI(namespace=namespace_,localname="noDispo")

    ##DEFINCIÃ<93>N DE URIS DE CIUDAD
    ciCali = conn.createURI(namespace=namespace_,localname="Cali")
    ciBogota = conn.createURI(namespace=namespace_,localname="Bogota")
    ciMedellin = conn.createURI(namespace=namespace_,localname="Medellin")

    ##DEFICIÃ<93>N DE URIS CÃ<93>DIGO DE  MENSAJES
    codM1 = conn.createURI(namespace=namespace_,localname="01")
    codM2 = conn.createURI(namespace=namespace_,localname="02")
    codM3 = conn.createURI(namespace=namespace_,localname="03")
    codM4 = conn.createURI(namespace=namespace_,localname="04")
    codM5 = conn.createURI(namespace=namespace_,localname="05")
    codM6 = conn.createURI(namespace=namespace_,localname="06")
    codM7 = conn.createURI(namespace=namespace_,localname="07")
    codM8 = conn.createURI(namespace=namespace_,localname="08")
    codM9 = conn.createURI(namespace=namespace_,localname="09")
    codM10 = conn.createURI(namespace=namespace_,localname="10")

    ##DEFINICIÃ<93>N DE URIS TEXTO
    txt1 = conn.createURI(namespace=namespace_,localname="txt1")
    txt2 = conn.createURI(namespace=namespace_,localname="txt2")
    txt3 = conn.createURI(namespace=namespace_,localname="txt3")
    txt4 = conn.createURI(namespace=namespace_,localname="txt4")
    txt5 = conn.createURI(namespace=namespace_,localname="txt5")
    txt6 = conn.createURI(namespace=namespace_,localname="txt6")
    txt7 = conn.createURI(namespace=namespace_,localname="txt7")
    txt8 = conn.createURI(namespace=namespace_,localname="txt8")
    txt9 = conn.createURI(namespace=namespace_,localname="txt9")
    txt10 = conn.createURI(namespace=namespace_,localname="txt10")

    ##DEFINICIÃ<93>N DE URIS DE FECHA
    date1 = conn.createURI(namespace=namespace_,localname="date1")
    date2 = conn.createURI(namespace=namespace_,localname="date2")
    date3 = conn.createURI(namespace=namespace_,localname="date3")
    date4 = conn.createURI(namespace=namespace_,localname="date4")
    date5 = conn.createURI(namespace=namespace_,localname="date5")
    date6 = conn.createURI(namespace=namespace_,localname="date6")
    date7 = conn.createURI(namespace=namespace_,localname="date7")
    date8 = conn.createURI(namespace=namespace_,localname="date8")
    date9 = conn.createURI(namespace=namespace_,localname="date9")
    date10 = conn.createURI(namespace=namespace_,localname="date10")

    ##DEFINICIÃ<93>N DE URIS DE TIPO
    tipo_pv = conn.createURI(namespace=namespace_,localname="privado")
    tipo_pb = conn.createURI(namespace=namespace_,localname="publico")

    ##DEFINICIÃ<93>N DE URIS DE RELACIÃ<93>N
    seguir = conn.createURI(namespace=namespace_, localname="sigue-a")
    ciudad = conn.createURI(namespace=namespace_,localname="ciudad")
    grafo = conn.createURI(namespace=namespace_,localname="Usuarios")
    enviar = conn.createURI(namespace=namespace_,localname="envia")
    contiene = conn.createURI(namespace=namespace_,localname="contiene")
    fecha = conn.createURI(namespace=namespace_,localname="fecha")
    destinatario = conn.createURI(namespace=namespace_,localname="destinatario")
    tipo = conn.createURI(namespace=namespace_,localname="tipo")
    disponible = conn.createURI(namespace=namespace_,localname="disponible")

    nullnode = conn.createLiteral("Null")

    ##CREACIÃ<93>N DE NODOS USUARIOS
    marianode = conn.createLiteral("Maria")
    viviannode = conn.createLiteral("Vivian")
    pablonode = conn.createLiteral("Pablo")
    usernode = conn.createLiteral("User")
    davidnode = conn.createLiteral("David")
    martanode = conn.createLiteral("Marta")
    carlosnode = conn.createLiteral("Carlos")

    ##DEFINICIÃ<93>N DE NODOS CIUDAD
    calinode = conn.createLiteral("Cali")
    bogotanode = conn.createLiteral("Bogota")
    medellinnode = conn.createLiteral("Medellin")

    ##DEFINICIÃ<93>N DE NODOS CODIGOS MENSAJE
    M1node = conn.createLiteral("01")
    M2node = conn.createLiteral("02")
    M3node = conn.createLiteral("03")
    M4node = conn.createLiteral("04")
    M5node = conn.createLiteral("05")
    M6node = conn.createLiteral("06")
    M7node = conn.createLiteral("07")
    M8node = conn.createLiteral("08")
    M9node = conn.createLiteral("09")
    M10node = conn.createLiteral("10")

    ##DEFINCIÃ<93>N DE NODOS DE TEXTO
    txt1node = conn.createLiteral("Prueba de mensaje 1")
    txt2node = conn.createLiteral("Buenos dias Mundo")
    txt3node = conn.createLiteral("print: Hola mundo")
    txt4node = conn.createLiteral("Mensaje privado")
    txt5node = conn.createLiteral("Mensaje publico")
    txt6node = conn.createLiteral("Buenas noches Mundo")
    txt7node = conn.createLiteral("Otro mensaje publico")
    txt8node = conn.createLiteral("Mensaje Nro 8")
    txt9node = conn.createLiteral("Mensaje intermedio")
    txt10node = conn.createLiteral("Mensaje final")

    ##DEFINCIÃ<93>N DE NODOS DE FECHA
    date1node = conn.createLiteral("2017-02-19")
    date2node = conn.createLiteral("2017-05-25")
    date3node = conn.createLiteral("2018-02-15")
    date4node = conn.createLiteral("2018-09-01")
    date5node = conn.createLiteral("2018-10-02")
    date6node = conn.createLiteral("2018-11-15")
    date7node = conn.createLiteral("2018-11-18")
    date8node = conn.createLiteral("2018-11-20")
    date9node = conn.createLiteral("2018-12-02")
    date10node = conn.createLiteral("2018-12-23")

    ##DEFINCIÃ<93>N DE NODOS DE TIPO
    pvnode = conn.createLiteral("Privado")
    pbnode = conn.createLiteral("Publico")

    ##DEFINICIÃ<93>N DE NODOS DE DISPONIBILIDAD
    disponode = conn.createLiteral("True")
    ndisponode = conn.createLiteral("False")

    ##AGREGAR RELACIONES USUARIO
    conn.add(marianode,RDF.TYPE,usernode,grafo)
    conn.add(viviannode,RDF.TYPE,usernode,grafo)
    conn.add(pablonode,RDF.TYPE,usernode,grafo)
    conn.add(davidnode,RDF.TYPE,usernode,grafo)
    conn.add(martanode,RDF.TYPE,usernode,grafo)
    conn.add(carlosnode,RDF.TYPE,usernode,grafo)

    ##AGREGAR RELACIONES SEGUIR
    conn.add(viviannode,seguir,marianode,grafo)
    conn.add(pablonode,seguir,viviannode,grafo)
    conn.add(carlosnode,seguir,pablonode,grafo)

    conn.add(pablonode,seguir,marianode,grafo)
    conn.add(martanode,seguir,pablonode,grafo)
    conn.add(viviannode,seguir,martanode,grafo)
    conn.add(davidnode,seguir,carlosnode,grafo)

    conn.add(carlosnode,seguir,marianode,grafo)
    conn.add(viviannode,seguir,carlosnode,grafo)
    conn.add(pablonode,seguir,carlosnode,grafo)
    conn.add(davidnode,seguir,pablonode,grafo)
    conn.add(martanode,seguir,davidnode,grafo)

    ##AGREGAR RELACIONES CIUDAD
    conn.add(pablonode,ciudad,calinode,grafo)
    conn.add(marianode,ciudad,bogotanode,grafo)
    conn.add(viviannode,ciudad,medellinnode,grafo)
    conn.add(davidnode,ciudad,calinode,grafo)
     conn.add(martanode,ciudad,bogotanode,grafo)
    conn.add(carlosnode,ciudad,medellinnode,grafo)

    ##AGREGAR RELACIONES ENVIAR
    conn.add(marianode,enviar,M1node,grafo)
    conn.add(pablonode,enviar,M2node,grafo)
    conn.add(carlosnode,enviar,M3node,grafo)
    conn.add(marianode,enviar,M4node,grafo)
    conn.add(viviannode,enviar,M5node,grafo)
    conn.add(carlosnode,enviar,M6node,grafo)
    conn.add(carlosnode,enviar,M7node,grafo)
    conn.add(carlosnode,enviar,M8node,grafo)
    conn.add(carlosnode,enviar,M9node,grafo)
    conn.add(carlosnode,enviar,M10node,grafo)

    ##AGREGAR RELACIONES CONTENIDO
    conn.add(M1node,contiene,txt1node,grafo)
    conn.add(M2node,contiene,txt2node,grafo)
    conn.add(M3node,contiene,txt3node,grafo)
    conn.add(M4node,contiene,txt4node,grafo)
    conn.add(M5node,contiene,txt5node,grafo)
    conn.add(M6node,contiene,txt6node,grafo)
    conn.add(M7node,contiene,txt7node,grafo)
    conn.add(M8node,contiene,txt8node,grafo)
    conn.add(M9node,contiene,txt9node,grafo)
    conn.add(M10node,contiene,txt10node,grafo)

    ##AGREGAR RELACIONES FECHA
    conn.add(M1node,fecha,date1node,grafo)
    conn.add(M2node,fecha,date2node,grafo)
    conn.add(M3node,fecha,date3node,grafo)
    conn.add(M4node,fecha,date4node,grafo)
    conn.add(M5node,fecha,date5node,grafo)
    conn.add(M6node,fecha,date6node,grafo)
    conn.add(M7node,fecha,date7node,grafo)
    conn.add(M8node,fecha,date8node,grafo)
    conn.add(M9node,fecha,date9node,grafo)
    conn.add(M10node,fecha,date10node,grafo)

    ##AGREGAR RELACIONES DESTINATARIO
    conn.add(M1node,destinatario,viviannode,grafo)
    conn.add(M2node,destinatario,marianode,grafo)
    conn.add(M3node,destinatario,pablonode,grafo)
    conn.add(M4node,destinatario,pablonode,grafo)
    conn.add(M5node,destinatario,nullnode,grafo)
    conn.add(M6node,destinatario,nullnode,grafo)
    conn.add(M7node,destinatario,nullnode,grafo)
    conn.add(M8node,destinatario,nullnode,grafo)
    conn.add(M9node,destinatario,nullnode,grafo)
    conn.add(M10node,destinatario,nullnode,grafo)


    ##AGREGAR RELACIONES TIPO
    conn.add(M1node,tipo,pvnode,grafo)
    conn.add(M2node,tipo,pvnode,grafo)
    conn.add(M3node,tipo,pvnode,grafo)
    conn.add(M4node,tipo,pvnode,grafo)
    conn.add(M5node,tipo,pbnode,grafo)
    conn.add(M6node,tipo,pbnode,grafo)
    conn.add(M7node,tipo,pbnode,grafo)
    conn.add(M8node,tipo,pbnode,grafo)
    conn.add(M9node,tipo,pbnode,grafo)
    conn.add(M10node,tipo,pbnode,grafo)


    ##AGREGAR RELACIONES DE DISPONIBILIDAD
    conn.add(marianode,disponible,disponode,grafo)
    conn.add(viviannode,disponible,ndisponode,grafo)
    conn.add(pablonode,disponible,disponode,grafo)
    conn.add(davidnode,disponible,disponode,grafo)
    conn.add(martanode,disponible,ndisponode,grafo)
    conn.add(carlosnode,disponible,ndisponode,grafo)

def consultarDatos(rep,query_string,tipo):
    repositorio = obtenerRepositorio(rep)
    conn = repositorio.getConnection()
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL,query_string)
    result = tuple_query.evaluate()
    lista = []
    with result:
        for binding_set in result:
            s = binding_set.getValue("s")
            p = binding_set.getValue("p")
            o = binding_set.getValue("o")
            #print("%s" %(s))

            if tipo=="s":
                #print("%s" %(s))
                lista.append(s)
            if tipo=="o":
                #print("%s" %(o))
                lista.append(o)
                #print("%s %s %s " %(s,p,o))
    return lista


def getFollowings(nombre):
    #nombre=str(raw_input("Porfavor ingrese nombre de usuario: "))
    #print(nombre)
    j=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE{'+'"'+nombre+'"'+' <http://example.org/people/sigue-a> ?o .}',"o")
    return j

def getFollowers(nombre):
    #nombre=str(raw_input("Porfavor ingrese nombre de usuario: "))
    i=consultarDatos("Prueba",'SELECT ?s ?p ?o  WHERE{?s <http://example.org/people/sigue-a> '+'"'+nombre+'"'+' .}',"s")
    return i

def sent(nombre):
    #nombre=str(raw_input("Porfavor ingrese nombre de usuario: "))
    cod=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE{'+'"'+nombre+'"'+' <http://example.org/people/envia> ?o .}',"o")
    #·print(cod)
    List=[]

    for dato in cod:
        subList=[]
        resultTipo=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/tipo> ?o .}',"o")
        print("Codigo: ")
        print(str(dato))
        print("Tipo: ")
        print(resultTipo[0])
        resultDestinatario=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/destinatario> ?o .}',"o")
        resultTexto=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+'<http://example.org/people/contiene> ?o .}',"o")
        resultFecha=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/fecha> ?o .}',"o")
        print ("Destinatario: ")
        print(resultDestinatario[0])
        print("Texto: ")
        print(resultTexto[0])
        print("Fecha: ")
        print(resultFecha[0])
        subList.append(resultTipo[0])
        subList.append(resultDestinatario[0])
        subList.append(resultTexto[0])
        subList.append(resultFecha[0])
        print("--------------------------------------------------------------")
        List.append(subList)
    print(List)

def inbox(nombre):
    #nombre=str(raw_input("Porfavor ingrese nombre de usuario: "))
    #sent()
    cod=consultarDatos("Prueba",'SELECT ?s ?p ?o  WHERE{?s <http://example.org/people/destinatario> '+'"'+nombre+'"'+' .}',"s")
    # print(cod)
    List=[]
    for dato in cod:
        subList=[]
        resultTexto=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/contiene> ?o .}',"o")
        resultFecha=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/fecha> ?o .}',"o")
        resultRemitente=consultarDatos("Prueba",'SELECT ?s ?p ?o  WHERE{?s <http://example.org/people/envia> '+str(dato)+' .}',"s")
        resultDispo=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(resultRemitente[0])+' <http://example.org/people/disponible> ?o .}',"o")
        print("Codigo: ")
        print(str(dato))
        print("Remitente: ")
        print(resultRemitente[0])
        print("Texto: ")
        print(resultTexto[0])
        print("fecha: ")
        print(resultFecha[0])
        print("Disponibilidad: ")
        print(str(resultDispo[0]))
        resultCiudad=[[]]
        if(str(resultDispo[0]) =='"True"'):
                resultCiudad=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(resultRemitente[0])+' <http://example.org/people/ciudad> ?o .}',"o")
                print("Ciudad del remitente: ")
                print(resultCiudad)
        subList.append(resultRemitente[0])
        subList.append(resultDispo[0])
        subList.append(resultCiudad[0])
        subList.append(resultTexto[0])
        subList.append(resultFecha[0])
        print("------------------------------------------------------------")
        List.append(subList)
    print(List)

def get5msg(nombre):
    lista=getFollowings(nombre)
    for usuario in lista:
        cod=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE{'+str(usuario)+' <http://example.org/people/envia> ?o .}',"o")
        List=[]
        x=len(cod)
        if (x >5):
                j=0
                cod2=[]
                while(j < 4):
                        cod2.append(cod[j])
                        j=j+1
                cod=cod2
        listaFinal=[]
        for dato in cod:
                subList=[]
                resultTipo=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/tipo> ?o .}',"o")
                if (str(resultTipo[0])=='"Publico"'):
                        resultDestinatario=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/destinatario> ?o .}',"o")
                        resultTexto=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+'<http://example.org/people/contiene> ?o .}',"o")
                        resultFecha=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE {'+str(dato)+' <http://example.org/people/fecha> ?o .}',"o")
                        #print("Codigo: ")
                        #print(dato)
                        print("Remitente: ")
                        print(usuario)
                        print("Texto: ")
                        print(resultTexto[0])
                        print("Fecha: ")
                        print(resultFecha[0])
                        #subList.append(resultTipo[0])
                        #subList.append(resultDestinatario[0])
                        #subList.append(resultTexto[0])
                        #subList.append(resultFecha[0])
                        print("--------------------------------------------------------------")
                        #List.append(subList)
                #listaFinal.append(List)
        #print(listaFinal)

def get5lvl(nombre):
    #nombre=str(raw_input("Porfavor ingrese nombre de usuario: "))
    cod=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE{?s <http://example.org/people/sigue-a> '+'"'+nombre+'"'+'.}',"s")
    contF=1
    while contF <= 5:
        subList=[]
        for dato in cod:
                result=consultarDatos("Prueba",'SELECT ?s ?p ?o WHERE{?s <http://example.org/people/sigue-a> '+str(dato)+' .}',"s")
                subList.append(result)
        Temp=[]
        for i in subList:
                for j in i:
                        Temp.append(j)
        cod=[]
        for i in Temp:
                bol=0
                for j in cod:
                        if (i == j):
                                bol = 1
                if (bol == 0):
                        cod.append(i)
        print("Nivel ",contF)
        print(cod)
        contF=contF+1
    #print(cod)

def main2(usuario):
   while(True):
        print("\n\n~~~~~~~~~~~~~#~~~~~~MENÚ DE OPCIONES~~~~~~~~#~~~~~~~~~~~\n")
        print("1. Conseguir sus seguidores\n2. Los usuarios a los que usted sigue\n3. Sus seguidores hasta el quinto nivel\n4. Salir")
        Opcion=str(raw_input("\nIngrese opción: "))
        if (Opcion == "1"):
                print(getFollowers(usuario))
        elif (Opcion == "2"):
                print(getFollowings(usuario))
        elif (Opcion == "3"):
                get5lvl(usuario)
        elif Opcion == "4":
                break


def main():
   print("\n\n++++++ BIENVENIDO ++++++\n\n")
   usuario=str(raw_input("Ingrese nombre de usuario: "))
   print("#~~~~~~~~Bandeja de Salida~~~~~~~~#")
   sent(usuario)
   print("#~~~~~~~~Bandeja de Entrada~~~~~~~~#")
   inbox(usuario)
   print("#~~~~~~~~FEED~~~~~~~~#")
   get5msg(usuario)
   main2(usuario)

main()


                    























