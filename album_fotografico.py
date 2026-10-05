def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    "puoi usare qualsiasi struttura dati"
    album=[]
    try:
        with open(file_path) as infile:
            infile.readline() #letta prima riga,a vuoto per skippare intestazione
            for riga in infile:
                #essendo un csv dividiamo le parole usando la virgola
                lista_valori=riga.strip().split(",")
            #controlliamo che riga non sia vuota e abbia tutti i campi
                if len(lista_valori)==5:
                    codice=lista_valori[0]
                    titolo=lista_valori[1]
                    autore=lista_valori[2]
                    mese=int(lista_valori[3])
                    anno=int(lista_valori[4])
                    foto=[codice,titolo,autore,mese,anno]
                # Ora check se anno già presente in album
                    anno_trovato=False
                    for blocco_anno in album:
                        if blocco_anno[0]==anno:  #blocco_anno[0] indica che prendiamo il primo elemento non dell'album,ma della sottolista avente come primo mebro album e secondo la foto
                            #se la risposta e sì infatti non aggiungo la foto a blocco_anno[0] che è l'anno ma
                            # a secondo elemento che è la lista delle foto
                            blocco_anno[1].append(foto)
                            anno_trovato=True
                            break
                    if not anno_trovato:
                        album.append([anno,[foto]]) #La struttura che ho scelto è infatti
                        #Lista 1 album contenitore esterno
                        #con elementi liste da 2 elementi anno e una terza lista contenitore ancora più piccolo contenente info di tutte le foto
    except FileNotFoundError:
        return None
    return album







def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO


def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO


def main():

    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
