# GameSpot - Sistema de Gestión de Catálogo de Videojuegos

## Descripción del Proyecto

**GameSpot** es una aplicación web desarrollada con Django que permite gestionar un catálogo completo de videojuegos. El sistema facilita la administración de juegos, plataformas, géneros y desarrolladores mediante una interfaz web con operaciones CRUD (Create, Read, Update, Delete) completas usando ModelForm.

---

## Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Pasos de Instalación

#### 1. **Clonar el Repositorio**
```bash
git clone https://github.com/KevinJp21/GameSpot_django.git
cd GameSpot
```

#### 2. **Crear Entorno Virtual**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

#### 4. **Aplicar Migraciones**
```bash
python manage.py migrate
```

#### 5. **Crear Superusuario (Opcional)**
```bash
python manage.py createsuperuser
```

#### 6. **Ejecutar el Servidor de Desarrollo**
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

### Acceso a Funcionalidades

- **Página Principal**: `http://127.0.0.1:8000/`
- **Admin Django**: `http://127.0.0.1:8000/admin/`
- **Lista de Juegos**: `http://127.0.0.1:8000/game_list/`
- **Lista de Plataformas**: `http://127.0.0.1:8000/platform_list/`
- **Lista de Géneros**: `http://127.0.0.1:8000/genre_list/`
- **Lista de Desarrolladores**: `http://127.0.0.1:8000/developer_list/`

---

## Estructura del Proyecto Django

El proyecto sigue la estructura estándar de Django con una organización clara y modular:

```
GameSpot/
├── GameSpot/              # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py        # Configuración de Django
│   ├── urls.py            # URLs principales
│   ├── wsgi.py
│   └── asgi.py
├── catalog/               # Aplicación principal
│   ├── __init__.py
│   ├── admin.py           # Registro de modelos en admin
│   ├── apps.py
│   ├── forms.py           # ModelForms
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas (lógica de negocio)
│   ├── urls.py            # URLs de la aplicación
│   ├── migrations/        # Migraciones de base de datos
│   └── templates/         # Templates HTML
│       ├── base.html      # Template base
│       ├── index.html     # Página principal
│       ├── games/         # Templates de juegos
│       ├── platforms/     # Templates de plataformas
│       ├── genres/        # Templates de géneros
│       └── developers/    # Templates de desarrolladores
├── db.sqlite3             # Base de datos SQLite
├── manage.py              # Script de administración
└── requirements.txt       # Dependencias del proyecto
```

### Características de la Estructura

- **Separación de responsabilidades**: Cada componente tiene su función específica
- **Organización modular**: Templates organizados por entidad
- **Rutas organizadas**: URLs agrupadas por funcionalidad en `catalog/urls.py`
- **Modelos registrados en admin**: Todos los modelos están disponibles en el panel de administración

---

## Modelos y Relaciones

El sistema utiliza **4 modelos principales** con relaciones bien definidas:

### Diagrama Modelo Entidad Relación

![Modelo Entidad Relacion](https://github.com/KevinJp21/GameSpot_django/blob/294a1b44ab4c3b8445287b2df2bfbae47f028503/MER%20GameSpot.png?raw=true)

### Descripción de Modelos

#### 1. **Plataforma**
Almacena información sobre las plataformas de videojuegos (consolas, PC, móviles, etc.).

```python
class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
```

**Campos:**
- `nombre`: Nombre de la plataforma (ej: PlayStation 5, Xbox Series X, PC)
- `fabricante`: Empresa fabricante (ej: Sony, Microsoft, Nintendo)
- `img_url`: URL de la imagen representativa

**Relaciones:**
- ManyToMany con `Juego` (un juego puede estar en múltiples plataformas)

---

#### 2. **Genero**
Categorías o géneros de videojuegos.

```python
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
```

**Campos:**
- `nombre`: Nombre del género (ej: Acción, RPG, Estrategia, Deportes)

**Relaciones:**
- ManyToMany con `Juego` (un juego puede tener múltiples géneros)

---

#### 3. **Desarrollador**
Información sobre las empresas o estudios que desarrollan videojuegos.

```python
class Desarrollador(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=100, null=True, blank=True)
```

**Campos:**
- `nombre`: Nombre del desarrollador (ej: Naughty Dog, CD Projekt Red)
- `pais`: País de origen del desarrollador

**Relaciones:**
- OneToMany con `Juego` (un desarrollador puede tener múltiples juegos)

---

#### 4. **Juego**
Modelo principal que representa un videojuego en el catálogo.

```python
class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    plataforma = models.ManyToManyField(Plataforma)
    genero = models.ManyToManyField(Genero)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    img_url = models.TextField(null=True, blank=True)
```

**Campos:**
- `titulo`: Título del juego
- `descripcion`: Descripción detallada del juego
- `fecha_lanzamiento`: Fecha de lanzamiento
- `img_url`: URL de la imagen del juego
- `plataforma`: Relación ManyToMany con Plataforma
- `genero`: Relación ManyToMany con Genero
- `desarrollador`: Relación ForeignKey con Desarrollador

**Relaciones:**
- **ForeignKey** con `Desarrollador` (cada juego tiene un desarrollador)
- **ManyToMany** con `Plataforma` (un juego puede estar en múltiples plataformas)
- **ManyToMany** con `Genero` (un juego puede tener múltiples géneros)

---

## CRUD con ModelForms

El proyecto implementa **CRUD completo** para las 4 entidades utilizando Django ModelForms.

### ModelForms Implementados

#### 1. **PlataformaForm**
```python
class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'
```

#### 2. **GeneroForm**
```python
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
```

#### 3. **DesarrolladorForm**
```python
class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = '__all__'
```

#### 4. **GameForm**
```python
class GameForm(forms.ModelForm):
    plataforma = forms.ModelMultipleChoiceField(
        queryset=Plataforma.objects.all(), 
        widget=forms.CheckboxSelectMultiple
    )
    genero = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(), 
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Juego
        fields = '__all__'
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }
```

**Características especiales:**
- Uso de `CheckboxSelectMultiple` para selección múltiple de plataformas y géneros
- Widget personalizado para fecha de lanzamiento (date picker)

### Operaciones CRUD por Entidad

#### **Plataformas**
- **Create**: `new_platform()` - Crear nueva plataforma
- **Read**: `platform_list()` - Listar todas las plataformas
- **Update**: `update_platform(id)` - Actualizar plataforma existente
- **Delete**: `delete_platform(id)` - Eliminar plataforma

#### **Géneros**
- **Create**: `new_genre()` - Crear nuevo género
- **Read**: `genre_list()` - Listar todos los géneros
- **Update**: `update_genre(id)` - Actualizar género existente
- **Delete**: `delete_genre(id)` - Eliminar género

#### **Desarrolladores**
- **Create**: `new_developer()` - Crear nuevo desarrollador
- **Read**: `developer_list()` - Listar todos los desarrolladores
- **Update**: `update_developer(id)` - Actualizar desarrollador existente
- **Delete**: `delete_developer(id)` - Eliminar desarrollador

#### **Juegos**
- **Create**: `new_game()` - Crear nuevo juego
- **Read**: `game_list()` y `index()` - Listar juegos (tabla y catálogo visual)
- **Update**: `update_game(id)` - Actualizar juego existente
- **Delete**: `delete_game(id)` - Eliminar juego

### Flujo de Operaciones CRUD

Todas las operaciones siguen el mismo patrón:

1. **GET**: Mostrar formulario vacío o con datos existentes
2. **POST**: Validar formulario con `is_valid()`
3. **Guardar/Eliminar**: Ejecutar operación en la base de datos
4. **Redirect**: Redirigir a la lista correspondiente

**Ejemplo de implementación:**
```python
def new_platform(request):
    if request.method == 'POST':
        platform_form = PlataformaForm(request.POST)
        if platform_form.is_valid():
            platform_form.save()
            return redirect('platform_list')
    else:
        platform_form = PlataformaForm()
    return render(request, 'platforms/new_platform.html', {'platform_form': platform_form})
```

---

## Templates y base.html

### Arquitectura de Templates

El proyecto utiliza **herencia de templates** con un `base.html` centralizado que contiene todos los estilos CSS compartidos.

### Estructura de Templates

```
templates/
├── base.html                 # Template base con estilos compartidos
├── index.html               # Página principal (catálogo visual)
├── games/
│   ├── game_list.html       # Lista de juegos (tabla)
│   ├── new_game.html        # Formulario crear juego
│   ├── update_game.html     # Formulario actualizar juego
│   └── delete_game.html     # Confirmación eliminar juego
├── platforms/
│   ├── platform_list.html
│   ├── new_platform.html
│   ├── update_platform.html
│   └── delete_platform.html
├── genres/
│   ├── genre_list.html
│   ├── new_genre.html
│   ├── update_genre.html
│   └── delete_genre.html
└── developers/
    ├── developer_list.html
    ├── new_developer.html
    ├── update_developer.html
    └── delete_developer.html
```

### Template Base (base.html)

El `base.html` incluye:

1. **Estilos CSS compartidos**:
   - Reset CSS y estilos base
   - Estilos para formularios (inputs, labels, botones)
   - Estilos para tablas/listas
   - Estilos para el catálogo visual de juegos
   - Diseño responsive con tema oscuro

2. **Bloques Django**:
   - `{% block title %}`: Título de la página
   - `{% block extra_css %}`: CSS adicional específico por página
   - `{% block content %}`: Contenido principal

### Ejemplo de Template que Extiende Base

```django
{% extends 'base.html' %}

{% block title %}Agregar Juego{% endblock %}

{% block content %}
<section class="form_section">
    <h1>Agregar Juego</h1>
    <form method="post">
        {% csrf_token %}
        {{ game_form.as_div }}
        <button type="submit">Guardar</button>
    </form>
</section>
{% endblock %}
```

### Uso de Estructuras de Control en Templates

#### **If/Else**
```django
{% if juegos %}
    <div class="game_grid">
        {% for juego in juegos %}
            <!-- contenido -->
        {% endfor %}
    </div>
{% else %}
    <p>No hay juegos disponibles</p>
{% endif %}
```

#### **For Loops**
```django
{% for juego in juegos %}
    <div class="game_card">
        <h3>{{ juego.titulo }}</h3>
        {% for plataforma in juego.plataforma.all %}
            <img src="{{ plataforma.img_url }}" alt="{{ plataforma.nombre }}">
        {% endfor %}
    </div>
{% endfor %}
```

---

## URLs y Vistas

### Organización de URLs

Las URLs están organizadas en dos niveles:

#### **1. URLs Principales (GameSpot/urls.py)**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
]
```

#### **2. URLs de la Aplicación (catalog/urls.py)**
```python
urlpatterns = [
    path('', views.index),  # Página principal
    
    # CRUD de Plataformas
    path('new_platform/', views.new_platform, name='new_platform'),
    path('platform_list/', views.platform_list, name='platform_list'),
    path('update_platform/<int:id>/', views.update_platform, name='update_platform'),
    path('delete_platform/<int:id>/', views.delete_platform, name='delete_platform'),
    
    # CRUD de Géneros
    path('new_genre/', views.new_genre, name='new_genre'),
    path('genre_list/', views.genre_list, name='genre_list'),
    path('update_genre/<int:id>/', views.update_genre, name='update_genre'),
    path('delete_genre/<int:id>/', views.delete_genre, name='delete_genre'),
    
    # CRUD de Desarrolladores
    path('new_developer/', views.new_developer, name='new_developer'),
    path('developer_list/', views.developer_list, name='developer_list'),
    path('update_developer/<int:id>/', views.update_developer, name='update_developer'),
    path('delete_developer/<int:id>/', views.delete_developer, name='delete_developer'),
    
    # CRUD de Juegos
    path('new_game/', views.new_game, name='new_game'),
    path('game_list/', views.game_list, name='game_list'),
    path('update_game/<int:id>/', views.update_game, name='update_game'),
    path('delete_game/<int:id>/', views.delete_game, name='delete_game'),
]
```

### Características de las URLs

- **Nombres descriptivos**: Cada URL tiene un nombre único usando `name=`
- **Parámetros dinámicos**: Uso de `<int:id>` para operaciones de actualización y eliminación
- **Organización lógica**: URLs agrupadas por entidad
- **Inclusión modular**: Uso de `include()` para separar URLs de la app

### Vistas Implementadas

Todas las vistas siguen el patrón de **Function-Based Views**:

1. **Vista de Listado** (Read):
   ```python
   def platform_list(request):
       platforms = Plataforma.objects.all()
       return render(request, 'platforms/platform_list.html', {'platforms': platforms})
   ```

2. **Vista de Creación** (Create):
   ```python
   def new_platform(request):
       if request.method == 'POST':
           platform_form = PlataformaForm(request.POST)
           if platform_form.is_valid():
               platform_form.save()
               return redirect('platform_list')
       else:
           platform_form = PlataformaForm()
       return render(request, 'platforms/new_platform.html', {'platform_form': platform_form})
   ```

3. **Vista de Actualización** (Update):
   ```python
   def update_platform(request, id):
       platform = Plataforma.objects.get(id=id)
       if request.method == 'POST':
           platform_form = PlataformaForm(request.POST, instance=platform)
           if platform_form.is_valid():
               platform_form.save()
               return redirect('platform_list')
       else:
           platform_form = PlataformaForm(instance=platform)
       return render(request, 'platforms/update_platform.html', {'platform_form': platform_form})
   ```

4. **Vista de Eliminación** (Delete):
   ```python
   def delete_platform(request, id):
       platform_form = Plataforma.objects.get(id=id)
       if request.method == 'POST':
           platform_form.delete()
           return redirect('platform_list')
       return render(request, 'platforms/delete_platform.html', {'platform_form': platform_form})
   ```

---

## Funcionalidades de la Aplicación

### 1. **Página Principal (Catálogo Visual)**
- Muestra todos los juegos en formato de tarjetas (cards)
- Información completa: título, descripción, desarrollador, plataformas, géneros, fecha de lanzamiento
- Enlaces a todas las secciones de administración

### 2. **Gestión de Plataformas**
- Crear nuevas plataformas con nombre, fabricante e imagen
- Listar todas las plataformas en formato tabla
- Actualizar información de plataformas existentes
- Eliminar plataformas

### 3. **Gestión de Géneros**
- Crear nuevos géneros
- Listar todos los géneros
- Actualizar géneros existentes
- Eliminar géneros

### 4. **Gestión de Desarrolladores**
- Crear nuevos desarrolladores con nombre y país
- Listar todos los desarrolladores
- Actualizar información de desarrolladores
- Eliminar desarrolladores

### 5. **Gestión de Juegos**
- Crear nuevos juegos con:
  - Título y descripción
  - Fecha de lanzamiento (date picker)
  - Selección múltiple de plataformas (checkboxes)
  - Selección múltiple de géneros (checkboxes)
  - Selección de desarrollador (dropdown)
  - URL de imagen
- Listar juegos en formato tabla con todas las relaciones
- Actualizar juegos existentes
- Eliminar juegos (con confirmación y vista previa)

### 6. **Panel de Administración Django**
- Acceso a todos los modelos desde el admin
- Gestión avanzada de datos
- Interfaz administrativa estándar de Django