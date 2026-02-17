# deployment-fifa

## Colaboración 

Para colaborar al proyecto primero deberemos realizar los siguientes pasos. 


### 1. Clonar repositorio 

```bash
# Clona un repositorio remoto en tu máquina local
git clone <url_del_repositorio>

# Ingresa a la carpeta del proyecto
cd <nombre_del_repositorio>

# Inicializa un nuevo repositorio Git en el proyecto actual
git init
```

---

## 2. Crear y activa El entorno virtual 

Ubicarse en la carpeta raíz del proyecto `FIFA-web` y ejecutar:

```bash
python -m venv myenv

```

### Windows (PowerShell)

```powershell
.\myenv\Scripts\Activate
```

### Windows (CMD)

```cmd
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

### En caso de bloqueo por Execution Policy (PowerShell)

Si se presenta un error relacionado con la política de ejecución, ejecutar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

---

## 3. Instalar dependencias 

Dentro y con el entorno virtual activado, ejecutar:

```bash
    pip install -r requirements.txt
    
    # Archivo que contiene todos las librerias y dependencias del proyecto.
    
```

### 4. Instalación de Tailwind CSS

Instalar Tailwind ejecutando:

```bash
npm install # Ingresa este codigo dentro del archivo fifaproyecto en donde se ubican los archivos relacionados con Tailwind. 

# Este codigo generara las dependecias node_modules y otros.

```

## Migración y inicio del proyecto 

Acceder a la carpeta cd fifaproyecto

makemigrations: sirve para crear archivos de migración que reflejen los cambios que ha hecho en los modelos (models.py) de su aplicación.

```bash
python manage.py makemigrations

python manage.py migrate 

python manage.py runserver
```