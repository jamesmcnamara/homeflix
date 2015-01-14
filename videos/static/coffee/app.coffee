app = angular.module "homeflix", ['ngRoute', 'restangular']

app.config ["$routeProvider", ($routeProvider) ->
    $routeProvider
    .when '/movies',
        templateUrl: "/static/views/movies.html"
        controller: "movieController"
    .when '/music',
        templateUrl: "/static/views/music.html"
        controller: "movieController"
    .when '/tv',
        templateUrl: "/static/views/tv.html"
        controller: "movieController"
    .otherwise
        templateUrl: "/static/views/home.html"
]