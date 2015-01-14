app = angular.module "homeflix"

app.controller "movieController", ["$scope", "Restangular", ($scope, Restangular) ->
    class Row
        constructor: (data) ->
            [@first, @second, @third] = data

    $scope.rows = []

    Restangular.all("videos").getList().then (movies) ->
        for i in [0...movies.length / 3]
            [start, end] = [i*3, i*3+3]
            $scope.rows.push new Row movies[start...end]
]
