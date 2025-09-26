Dans votre application, le backend (Django) et le frontend (Svelte) sont liés principalement par des requêtes HTTP, où le frontend interagit avec le backend via des API REST. Voici comment cela fonctionne et où les fichiers et contenus sont échangés :

### 1. **Endpoints API dans le Backend**
Le backend expose des endpoints API que le frontend peut appeler pour récupérer ou envoyer des données. Dans votre code, cela se trouve dans le fichier `films/urls.py` :

```python:backend/films_backend/films/urls.py
from django.urls import path 
from films.views import FilmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')
urlpatterns = router.urls
```

### 2. **Vue du Backend**
Le `FilmViewSet` dans `views.py` gère les requêtes pour les films. Voici un extrait de ce fichier :

```python:backend/films_backend/films/views.py
from rest_framework import viewsets
from films.models import Film
from films.serializers import FilmSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer    
```

### 3. **Requêtes du Frontend**
Le frontend utilise `fetch` pour faire des requêtes vers ces endpoints. Par exemple, dans `+page.svelte`, vous avez :

```javascript:frontend/src/routes/films/+page.svelte
const endpoint = 'http://localhost:8000/api/films/';
const response = await fetch(endpoint);
const data = await response.json();
FilmStore.set(data);
```

### 4. **Gestion des Données**
Le frontend utilise un store Svelte (`FilmStore`) pour gérer l'état des films. Les données récupérées du backend sont stockées dans ce store, ce qui permet à l'application de réagir aux changements d'état.

### 5. **Ajout et Suppression de Films**
Pour ajouter un film, le frontend envoie une requête POST à l'API :

```javascript:frontend/src/routes/films/add/+page.svelte
fetch(endpoint, {method: 'POST', body: data}).then(response => response.json()).then(data => {
    FilmStore.update(prev => [...prev, data]);
});
```

Pour supprimer un film, une requête DELETE est envoyée :

```javascript:frontend/src/routes/films/+page.svelte
const endpoint = `http://localhost:8000/api/films/${id}`;
fetch(endpoint, {method: 'DELETE'}).then(response => {
    if (response.status == 204) {
        FilmStore.update(prev => prev.filter(film => film.id != id));
    }
});
```

### 6. **Conclusion**
En résumé, le frontend et le backend échangent des données via des requêtes HTTP. Le frontend envoie des requêtes pour récupérer, ajouter ou supprimer des films, et le backend répond avec les données appropriées. Les fichiers et contenus sont échangés principalement par le biais des endpoints API définis dans le backend, et le frontend utilise ces endpoints pour interagir avec les données.