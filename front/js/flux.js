var fluxApp = angular.module('fluxApp', [
	'ngRoute'
]);

fluxApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/home', {
				templateUrl: 'content/home.html'
			}).
			when('/societeit', {
				templateUrl: 'content/societeit.html'
			}).
			when('/verhuur', {
				templateUrl: 'content/verhuur.html'
			}).
			when('/verhuur2', {
				templateUrl: 'content/verhuur2.html',
				controller: 'RentalCtrl'
			}).
		when('/contact', {
		templateUrl: 'content/contact.html'
		}).
			otherwise({
				redirectTo: '/home'
			});
	}
]);

fluxApp.directive('activeLink', ['$location', function(location) {
		console.log('test');
		return {
				restrict: 'A',
				link: function(scope, element, attrs, controller) {

						var clazz = attrs.activeLink;
						var path = attrs.href;
						path = path.substring(1); //hack because path does bot return including hashbang
						scope.location = location;
						scope.$watch('location.path()', function(newPath) {
								if (path === newPath) {
										element.addClass(clazz);
								} else {
										element.removeClass(clazz);
								}
						});
				}
		};
	}
]);

fluxApp.controller('RentalCtrl',[function($scope,$log){
	$log.log('test');
	$scope.rentalForm = {};
}]);