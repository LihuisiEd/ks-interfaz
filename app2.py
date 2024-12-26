from pywinauto import application
from pywinauto.timings import wait_until

# Inicia la aplicación usando el backend UIA
app = application.Application(backend="uia")
route = r"C:\Program Files\RealVNC\VNC Viewer\vncviewer.exe"
app.start(route)

# Seleccionar "Archivo -> Preferencias" en el menú
dlg = app.window()
dlg.menu_select("Archivo->Nueva conexión")

# Obtener la ventana emergente
try:
    wait_until(20, 1, lambda: app.window(title_re=".*Propiedades.*").exists())
    preferences_window = app.window(title_re=".*Propiedades.*")
    preferences_window.wait("visible", timeout=20) 
    print("Ventana de preferencias encontrada.")
except TimeoutError:
    print("La ventana no se encontró en el tiempo especificado.")

# Obtener el botón y sus propiedades
button = preferences_window["Actualizar automáticamente la vista previa del escritorio"]
button.click()
# Verificar los estados del botón
properties = button.get_properties()
print("Propiedades del botón (UIA):")
for key, value in properties.items():
    print(f"{key}: {value}")

# Usar states() para obtener el estado del botón
try:
    states = button.iface_acc.state
    print(f"Estado actual del botón (UIA): {states}")
except Exception as e:
    print(f"No se pudo obtener el estado: {e}")