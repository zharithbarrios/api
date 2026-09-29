# Eventos Escolares - Frontend

## 1. Descripción del proyecto

Este proyecto corresponde al frontend del sistema de gestión de eventos y actividades extracurriculares del Colegio San Miguel.

El frontend está desarrollado con:

* SvelteKit
* Svelte
* Vite
* JavaScript
* HTML y CSS

El sistema permite visualizar e interactuar con las funcionalidades del proyecto, como actividades, inscripciones y autorizaciones, mediante comunicación con una API desarrollada en FastAPI.

---

## 2. Arquitectura del proyecto

El sistema está dividido en dos proyectos independientes:

### Frontend

* Tecnología: SvelteKit
* Dirección local: `http://localhost:5173`

### Backend

* Tecnología: FastAPI
* Dirección local: `http://127.0.0.1:8000`

El frontend se comunica con el backend mediante solicitudes HTTP y respuestas en formato JSON.

**Importante:** El frontend necesita que la API esté ejecutándose para consultar o modificar los datos.

---

## 3. Requisitos para ejecutar el frontend

Antes de comenzar, es necesario instalar:

1. Node.js
2. Visual Studio Code
3. Git, si se utiliza el repositorio del proyecto
4. El proyecto del backend, cuando se requiera ejecutar la API localmente

Se recomienda utilizar una versión LTS de Node.js.

---

## 4. Cómo abrir el proyecto

1. Descargar y descomprimir el archivo ZIP.

2. Abrir Visual Studio Code.

3. Seleccionar:

   `File > Open Folder`

4. Abrir la carpeta:

   `EventosEscolaresFrontend\my-app`

La carpeta que se abre debe contener el archivo `package.json`.

---

## 5. Instalar las dependencias

Abrir una terminal dentro de Visual Studio Code y ejecutar:

```powershell
npm install
```

Este comando instala las dependencias definidas en `package.json`.

No es necesario enviar la carpeta `node_modules` en el ZIP, porque se genera automáticamente mediante `npm install`.

---

## 6. Ejecutar el frontend

Después de instalar las dependencias, ejecutar:

```powershell
npm run dev
```

La aplicación estará disponible normalmente en:

```text
http://localhost:5173
```

Para detener el servidor:

```text
Ctrl + C
```

---

## 7. Conexión con el backend

El frontend realiza solicitudes al backend de FastAPI.

Cuando se trabaja localmente, la API normalmente se ejecuta en:

```text
http://127.0.0.1:8000
```

El backend debe estar iniciado antes de probar las funcionalidades que consultan información de la base de datos.

Si el backend utiliza una dirección diferente, se debe revisar la configuración de la URL de la API dentro del proyecto.

No se deben publicar contraseñas, claves privadas ni archivos `.env` que contengan información sensible.

---

## 8. Estructura principal del frontend

```text
my-app/
├── src/
│   ├── lib/
│   └── routes/
├── static/
├── package.json
├── package-lock.json
├── jsconfig.json
├── vite.config.js
└── README.md
```

### src/routes

Contiene las páginas y rutas de la aplicación SvelteKit.

### src/lib

Contiene componentes reutilizables, recursos y funcionalidades compartidas.

### static

Contiene archivos estáticos utilizados por la aplicación.

### package.json

Contiene la información del proyecto y sus dependencias.

### package-lock.json

Permite instalar versiones consistentes de las dependencias.

---

## 9. Comandos principales

Instalar dependencias:

```powershell
npm install
```

Ejecutar en modo desarrollo:

```powershell
npm run dev
```

Crear una versión de producción:

```powershell
npm run build
```

Previsualizar la versión de producción, si está configurado:

```powershell
npm run preview
```

---

## 10. Solución de problemas comunes

### Error: npm no se reconoce

Verificar que Node.js esté instalado y reiniciar Visual Studio Code.

Comprobar la instalación:

```powershell
node --version
npm --version
```

### Error: Cannot find package

Ejecutar:

```powershell
npm install
```

### No aparecen las actividades

Comprobar que:

1. El backend esté ejecutándose.
2. La URL de la API sea correcta.
3. La ruta del endpoint esté disponible.
4. No exista un error de CORS.
5. La base de datos esté conectada correctamente al backend.

### El puerto 5173 está ocupado

Cerrar el proceso que utiliza el puerto o ejecutar SvelteKit en otro puerto.

---

## 11. Recomendaciones de trabajo

* No modificar el archivo `package-lock.json` manualmente.
* No subir contraseñas ni credenciales al repositorio.
* Ejecutar `npm install` después de descargar el proyecto.
* Mantener el frontend y el backend en carpetas independientes.
* Consultar al equipo antes de realizar cambios importantes en las rutas o componentes.

---

## 12. Flujo de ejecución

```text
1. Abrir el backend.
2. Iniciar FastAPI.
3. Abrir el frontend.
4. Ejecutar npm install si es necesario.
5. Ejecutar npm run dev.
6. Abrir http://localhost:5173.
7. Comprobar la comunicación con la API.
```

**Proyecto:** Gestión de Eventos y Actividades Extracurriculares - Colegio San Miguel.
