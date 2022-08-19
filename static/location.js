let result = document.getElementById("location-result");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(findLocation, showError);
  } else { 
    result.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function findLocation(position) {
    result.innerHTML = "Thank you! We have received your location!"

    let user_location = {
      'latitude': position.coords.latitude,
      'longitude': position.coords.longitude
    }

    let s = JSON.stringify(user_location);

    $.ajax({
      url:"/grab_location",
      type:"POST",
      contentType: "application/json",
      data: JSON.stringify(s)
    });

    document.getElementById("search-button").style.removeProperty('display');
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      result.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      result.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      result.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      result.innerHTML = "An unknown error occurred."
      break;
  }
}