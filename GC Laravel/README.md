# GiftCards API (Laravel) - Ejemplo

Proyecto de ejemplo: API REST para manejo de GiftCards hecha con Laravel (estructura mínima para evaluación).

## Contenido
- Modelo: `app/Models/Giftcard.php`
- Controlador: `app/Http/Controllers/GiftcardController.php`
- Migración: `database/migrations/2025_11_03_000000_create_giftcards_table.php`
- Rutas API: `routes/api.php`
- .env.example: configuración de ejemplo
- composer.json: referencia mínima

## Requisitos
- PHP 8.1+
- Composer
- MySQL (u otra BDD compatible)
- Laravel 10+

## Instalación rápida (local)
1. Clona o descarga el repositorio.
2. Copia `.env.example` a `.env` y ajusta las variables DB.
3. Ejecuta `composer install` (si no tienes composer, puedes revisar las instrucciones de tu entorno o usar Laragon).
4. Ejecuta migraciones:
   ```
   php artisan migrate
   ```
5. Levanta el servidor:
   ```
   php artisan serve
   ```

## Endpoints
- `GET  /api/giftcards` - listar
- `POST /api/giftcards` - crear
- `GET  /api/giftcards/{id}` - ver uno
- `PUT  /api/giftcards/{id}` - actualizar
- `DELETE /api/giftcards/{id}` - eliminar

## Ejemplo JSON para creación
```json
{
  "code": "ABC123",
  "amount": 50,
  "is_active": true
}
```

## Notas para el profesor
Este repo contiene la estructura mínima para evaluación. Para correrlo en un entorno real se requiere instalar dependencias con Composer y configurar la base de datos en `.env`.
