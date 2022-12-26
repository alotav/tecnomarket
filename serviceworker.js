// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/app/css/estilos.css',
    '/static/app/footer/apple.png',
    '/static/app/footer/lenovo.png',
    '/static/app/footer/microsoft.png',
    '/static/app/footer/samsung.png',
    '/static/app/footer/xiaomi.png',
    '/static/app/tecnomarketpngicono.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
// self.addEventListener("fetch", event => {
//     event.respondWith(
//         caches.match(event.request)
//             .then(response => {
//                 return response || fetch(event.request);
//             })
//             .catch(() => {
//                 return caches.match('/offline/');
//             })
//     )
// });


// Guardar TODO en cache: 

self.addEventListener("fetch", function(event){
    event.respondWidth(
        fetch(event.request)
        .then(function(result){
            return cache.open(staticCacheName)
            .then(function(c){
                c.put(event.request.url,result.clone())
                return result;
            })
        })
        .catch(function(e){
            return cache.match(event.request);
        })
    )
});