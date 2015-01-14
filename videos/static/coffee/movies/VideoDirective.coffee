app = angular.module "homeflix"

app.directive "homeFlixVideo", ->
    restrict: "E"
    scope:
        video: "="
    controller: ($scope, $http) ->
        if $scope.video
            url_safe_title = $scope.video.title.replace(" ", "+")

            $http.get("http://omdbapi.com/?t=#{url_safe_title}&plot=short&r=json&tomatoes=true").then (response) ->
                $scope.data = response.data



    templateUrl: "static/views/homeFlixVideo.html"