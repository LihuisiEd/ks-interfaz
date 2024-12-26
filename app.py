from pywinauto import application
app = application.Application()
#app.start('C:\Users\eddii\Desktop\HolaMundo.txt')

app.connect(title='HolaMundo.txt: Bloc de notas', timeout=100)
BlocDeNotas = app.window(title="HolaMundo.txt: Bloc de notas", class_name="Notepad")

SinBlocDeNotas = app.window(title="*HolaMundo.txt: Bloc de notas", class_name="Notepad")
'''
BlocDeNotas.print_control_identifiers()
textEditor = BlocDeNotas.child_window(class_name="RichEditD2DPT").wrapper_object()
textEditor.type_keys("Escribiendo - Procedemos a Guardar")
print("Escribiendo - Procedemos a Guardar")
'''

'''
BlocDeNotas.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                        with_spaces=True,
                        with_newlines=True,
#                        pause=0.5,
                        with_tabs=True)
                        '''
BlocDeNotas.print_control_identifiers()
#BlocDeNotas.Archivo.click_input()
#BlocDeNotas.PopupHost.Font.click_input(double=True)
#fileMenu = SinBlocDeNotas.child_window(title='File',control_type='MenuItem').wrapper_object()
#fileMenu.click_input()