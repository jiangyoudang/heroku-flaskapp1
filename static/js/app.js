/**
 * Created by congliu on 2/10/15.
 */

var app = angular.module("app", []);

app.controller('AppCtrl', function($scope,$http){

    $http.get('api/users').success(function(data){
        $scope.users = data.objects;
    });

    $scope.dropli = {
        'fruit':['apple','peach'],
        'animal':['dog','cat']
    }
    $scope.curr_d = 'fruit';

    $scope.addUser = function(){
        $http.post('api/users',{'name':'cong'+$scope.users.length, 'email':'cong'+Math.random()+'@scu.edu'} )
            .success(function(data){
                $scope.users.push(data)
            })
    };

    $scope.deleteUser = function(user){
        $http.delete('api/users/'+user.id).success(function(data){
            $scope.users.splice($scope.users.indexOf(user),1)
        })
    }

    $scope.updateUser = function(user){
        $http.put('api/users/' + user.id, user)
    }


})