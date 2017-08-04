app = angular.module 'example.app.static', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.posts = [
        author:
            username: 'Quang'
        title: 'Sample Post #1'
        body: 'This is the first sample post'
    ,
        author:
            username: 'Karen'
        title: 'Sample Post #2'
        body: 'This is another sample post'
    ]
]
