def iniciar_festival(lista_artistas):
    print("\n========== ¡BIENVENIDOS AL FESTIVAL MUSICAL! ==========")

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("\n🎆 Fin de la actuación 🎆\n")

    print("========== FIN DEL FESTIVAL ==========")
