
// Initialize and add the map
function initMap() {
    // Activation of the services
    var directionService = new google.maps.DirectionsService;
    var directionDisplay = new google.maps.DirectionsRenderer;

    //Build up of the map
    var map = new google.maps.Map(
        document.getElementById('map'),{
            zoom:6,
            center:{
                lat:46.00,
                lng: 2.00
            }
        }
    );

    directionDisplay.setMap(map);
    calculateAndDisplayRoute(directionService,directionDisplay);
}

function calculateAndDisplayRoute(directionService,directionDisplay){

    // Provide road map indications
    directionService.route({
        // Variables are picked up from the HTML page js script
        origin : departureCity + ", France",
        destination: groceryBrandName + departureCity + ", France",
        travelMode:'DRIVING'
    }, function(response, status){
        if (status ==='OK'){
            directionDisplay.setDirections(response);
        } else {
        console.log("Directions requested failed due to " + status)
        }
    });
}
