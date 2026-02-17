# README - Configuración Django + Tailwind CSS

## 1. Instalación de Tailwind en Django

### Pasos principales

1. Crear un entorno virtual (si no lo tienes):

```
python -m venv myenv
```

2. Activar el entorno virtual:

```
# Windows PowerShell
myenv\Scripts\Activate.ps1

# Windows cmd
myenv\Scripts\activate.bat
```

3. Inicializar npm e instalar Tailwind CSS:

```
npm init -y
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

4. Configurar Tailwind para que observe los archivos del proyecto:

```js
// tailwind.config.js
module.exports = {
  content: [
    "./web/templates/**/*.html",   // todas las plantillas HTML
    "./web/static/js/**/*.js"      // archivos JS locales
  ],
  theme: { extend: {} },
  plugins: [],
}
```

---

## 2. Archivos CSS

1. Crear archivo de entrada `input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

2. Generar el CSS final de Tailwind en `output.css`:

```
npx tailwindcss -i ./web/static/css/input.css -o ./web/static/css/output.css --watch
```

> Nota: `--watch` recompila automáticamente cuando haces cambios en `input.css` o en tus plantillas.

---

## 3. Configuración en Django

1. En `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "web" / "static"]
```

2. En tus templates HTML, cargar los archivos estáticos de Django y enlazar `output.css`:

```html
{% load static %}
<link href="{% static 'css/output.css' %}?v=2" rel="stylesheet">
```

> Nota: `?v=2` se utiliza para forzar el refresco del caché del navegador cuando Tailwind recompila `output.css`.

3. Asegúrate de usar las clases de Tailwind en tu HTML para probar los estilos, por ejemplo:

```html
<h1 class="text-5xl text-red-500 font-bold">¡Hola, mundo!</h1>
```

---

## 4. Problemas comunes y soluciones

* **Cambios de color o estilos no aparecen:**

  * Asegúrate de que el `output.css` esté correctamente enlazado en tu HTML.
  * Usa un query string como `?v=2` para evitar el caché del navegador.

* **Tailwind no detecta tus archivos:**

  * Revisa que la configuración de `content` en `tailwind.config.js` apunte correctamente a tus templates y JS locales.

* **Errores de instalación o mezcla de versiones:**

  * Elimina `node_modules` y `package-lock.json` y reinstala:

```
npm install
```

* Verifica que `tailwindcss`, `postcss` y `autoprefixer` estén instalados como dependencias de desarrollo (`-D`).
