/**
 * Created by congliu on 2/10/15.
 */

var app = angular.module("app", []);

app.controller('AppCtrl', function($scope,$http){

    $http.get('api/users').success(function(data){
        $scope.users = data.objects;
    })



})