import console_fun as cf


def console():
    while True:
        cf.print_menu()

        mode = input('Выберите режим работы справочника: ')
        if mode == '1':
            cf.load_notes()
        elif mode == '2':
            cf.new_note()
        elif mode == '3':
            cf.edit_note()
        elif mode == '4':
            cf.del_note()
        elif mode == '0':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
