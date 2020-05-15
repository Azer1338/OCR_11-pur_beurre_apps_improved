// Initialise variables
var departure = {};
var arrival = {};
var map;

// Initialize and add the map
function initMap() {

    //Build up of the map
    map = new google.maps.Map(
        document.getElementById('map'),{
            zoom:15,
            center:{
                lat:46.539139,
                lng: 2.430070
                }
            }
        );

    // Looking the closest places requested by the user
    var address = departureCity + "France";
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
        // Departure Address
        departure["position"]= results[0].geometry.location;
        departure["address"]= results[0].formatted_address;

        // Looking for the closest grocery requested by customer
        getNearbyPlaces(departure.position);
    });
}

// Perform a Places Nearby Search Request
function getNearbyPlaces(position) {

    // Generate a request to API
    var request = {
    location: position,
    rankBy: google.maps.places.RankBy.DISTANCE,
    keyword: groceryBrandName,
    type: 'grocery_or_supermarket',
    };
    console.log("Magasin: " + groceryBrandName);

    // Activation of the service
    var service = new google.maps.places.PlacesService(map);
    var closestStore = service.nearbySearch(request, function(results, status){
        // Arrival Address
        arrival["position"] = results[0].geometry.location;
        arrival["address"]= results[0].formatted_address;
        arrival["name"]=results[0].name;
        console.log(results[0]);

        // Reverse geocoding
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode( { 'location': arrival["position"]}, function(results, status) {
            arrival["address"] = results[0].formatted_address;

            // View variables
            console.log("Departure Address: " + departure.address);
            console.log("Departure GPS: " + departure.position);
            console.log("Arrival Address: " + arrival.address);
            console.log("Arrival GPS: " + arrival.position);
            console.log("Arrival name: " + arrival.name);

            // Services activation
            var directionService = new google.maps.DirectionsService;
            var directionDisplay = new google.maps.DirectionsRenderer;

            // Get directions
            directionDisplay.setMap(map);
            calculateAndDisplayRoute(directionService,directionDisplay);
        });
    });
}

function calculateAndDisplayRoute(directionService,directionDisplay){

    // Provide road map indications
    directionService.route({
        // Variables are picked up from the HTML page js script
        origin : departure.address,
        destination: arrival.address,
        travelMode:'DRIVING',
        unitSystem: google.maps.UnitSystem.METRIC,
    }, function(response, status){
        if (status ==='OK'){
            directionDisplay.setDirections(response);
        } else {
        console.log("Directions requested failed due to " + status)
        }
    });
}