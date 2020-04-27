
// Initialize and add the map
function initMap() {
    // Activation of the services
    var directionService = new google.maps.DirectionsService;
    var directionDisplay = new google.maps.DirectionsRenderer;

    //Build up of the map
    var map = new google.maps.Map(
        document.getElementById('map'),{
            zoom:5,
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
        origin :"Paris,France",
        destination:"Marseille, France",
        travelMode:'DRIVING'
    }, function(response, status){
        if (status ==='OK'){
            directionDisplay.setDirections(response);
        } else {
        windows.alert("Directions requested failed due to " + status)
        }
    });
}

//
////
//function processingUserRequest(){
//// Actions following User's message sending to the website
//
//	// Gather the User's sentence
//	var userRequest = document.getElementById("User_destination");
//
//	// Display a loading picture
//	var pic = loadingPicture("on","Input_bar");
//	displayElement("GrandPy",pic);
//
//	// Call to views.py
//	$.ajax({
//		// Route to /result/ page in views.py
//        url: '/result/',
//        // Data to send with
//        data: {query : userRequest.value},
//        // Return accepted format
//        dataType: 'json',
//
//        // In case of succes - json_data will be returned from AJAX GET call
//        success: function(json_data) {
//			// Message
//            console.log(json_data);
//
//			// Display User's request
//			var request = generateTexte(userRequest.value);
//			displayElement("User", request);
//
//			// Display GrandPy's address
//			var answerAddress = generateTexte("Voici l'adresse: " + json_data.address);
//			displayElement("GrandPy",answerAddress);
//
//			// Display GrandPy's map
//			var answerMap = generateMap (json_data.lat,json_data.lng);
//			displayElement("GrandPy",answerMap);
//
//			// Display GrandPy's about
//			var answerAbout = generateTexte(json_data.sentence + " " + json_data.about);
//			displayElement("GrandPy",answerAbout);
//
//			// Retry?
//			var answerEnough = generateTexte("Autre part?");
//			displayElement("GrandPy",answerEnough);
//
//			// Initialise the user field
//			cleanInputForm();
//
//			// Unloading picture
//			loadingPicture("off","Input_bar");
//		},
//
//		// In case of error
//        error: function(result, status, error_type){
//			// Message
//			console.log("AJAX (Get) function turn crazy " + error_type);
//
//			// Display User's request
//			var request = generateTexte(userRequest.value);
//			displayElement("User", request);
//
//			// Display GrandPy's address
//			var answerAddress = generateTexte("Je ne suis pas sur d'avoir compris. Peux-tu détailler?");
//			displayElement("GrandPy",answerAddress);
//
//			// Initialise the user field
//			cleanInputForm();
//
//			// Unloading picture
//			loadingPicture("off","Input_bar");
//		}
//	});
//};
//
////
//function generateMap(latitude, longitude) {
//// Generate a Google map from :latitude & :longitude
//// Element will be pinned to the :IdHTML
//
//	// Create an element as container
//	var mapElement = document.createElement("div");
//	mapElement.setAttribute("id","googleMap");
//
//	// Creation of the map element
//	var map_ref = new google.maps.Map(mapElement, {
//		center: {lat: latitude, lng: longitude},
//		zoom: 14
//		});
//
//	// Specify the marker
//	var marker_ref = new google.maps.Marker({
//        position: {lat: latitude, lng: longitude},
//        map: map_ref,
//        title: 'It is fucking here, boy!'
//	});
//
//	return mapElement;
//}
//
////
//function generateTexte (text){
//// Return a <p> element
//
//	// Generate a <p> element
//	var textElt = document.createElement("p");
//	textElt.textContent = text;
//
//	return textElt;
//};
//
////
//function generateImage(source){
//// Return a <img> element
//		// Generate a <p> element
//		var picture = document.createElement("img");
//		picture.setAttribute("src",source);
//		picture.setAttribute("class","generateImg");
//
//		return picture;
//};
//
////
//function displayElement (fromWho, elt){
//// Display an :element on interface with :fromWho 's design
//
//	// Container creation
//	var containerElt = document.createElement("div");
//	var containerPicture = document.createElement("div");
//	var picture;
//
//	// Depending on who is talking
//	switch (fromWho){
//		case "GrandPy":
//			// Set the specific attributs
//			containerElt.setAttribute("class","row bubble_right bubble right align-items-center");
//			picture = generateImage("/static/img/GrandPy_Logo.png");
//
//			// Fill the container with elt and picture
//			containerElt.appendChild(elt);
//			containerPicture.appendChild(picture);
//			containerElt.appendChild(containerPicture);
//
//			break;
//
//		case "User":
//			// Set the specific attributs
//			containerElt.setAttribute("class","row bubble_left bubble left align-items-center");
//			picture = generateImage("/static/img/Bebe_Logo.png");
//
//			// Fill the container with elt and picture
//			containerPicture.appendChild(picture);
//			containerElt.appendChild(containerPicture);
//			containerElt.appendChild(elt);
//
//			break;
//
//		default:
//			// Alert message
//			console.log("displayElement : containerElt not defined");
//	}
//
//	// Picture & element position
//	containerPicture.setAttribute("class","col-md-4");
//	elt.setAttribute("class","col-md-8");
//
//	// Add a bubble in the tchat area
//	var textArea = document.getElementById("Tchat");
//	textArea.insertAdjacentElement("beforeend",containerElt);
//};
//
//// Init user's field
//function cleanInputForm(){
//
//	// Replace the filed by a blank area
//	var user = document.getElementById("User_destination");
//
//	user.value = "";
//};
//
////
//function loadingPicture (status){
//// Manage the loading picture
//
//	// Switch On / Off the picture
//	switch (status) {
//		case "on":
//			// Message
//			console.log("loading pic on");
//
//			// Add a bubble
//			var pic = document.createElement("img");
//
//			// Modify attributs
//			pic.setAttribute("id","loading");
//			pic.setAttribute("src","/static/img/loading.gif");
//
//			break;
//
//		case "off":
//			// Message
//			console.log("loading pic off");
//
//			// Remove the bubble
//			var elt = document.getElementById("loading");
//			elt.parentNode.remove();
//
//			break;
//	};
//
//	return pic;
//};
//
////
//function grandPyIntroduction(){
//// Initialisation of the GrandPy
//
//	// Creation of the GrandPy's first sentence
//	var init = generateTexte("Bonjour mon pitchoune! Je suis GrandPy Bot, le papi robot! Où veux tu aller?");
//	displayElement("GrandPy", init);
//};
//
//// At the website launching
//grandPyIntroduction();