// Generated by CoffeeScript 1.8.0
(function() {
  var app;

  app = angular.module("homeflix");

  app.directive("homeFlixVideo", function() {
    return {
      restrict: "E",
      scope: {
        video: "="
      },
      controller: function($scope, $http) {
        var url_safe_title;
        if ($scope.video) {
          url_safe_title = $scope.video.title.replace(" ", "+");
          return $http.get("http://omdbapi.com/?t=" + url_safe_title + "&plot=short&r=json&tomatoes=true").then(function(response) {
            return $scope.data = response.data;
          });
        }
      },
      templateUrl: "static/views/homeFlixVideo.html"
    };
  });

}).call(this);
