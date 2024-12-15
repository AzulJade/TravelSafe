var map = L.map('map').setView([10.633635,-61.379551],12);       
L.tileLayer('https://api.maptiler.com/maps/streets-v2/{z}/{x}/{y}.png?key=dnrfwqtX0yOSV0p2EOPL',{attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'}).addTo(map);
// above is map stuff don't touch it


var short_dis = 0;
var cord_id = 0;
var temp_distance = 0;
var x = 0;
var y = 0;
// declaring variables

var taxi_coord_x = [10.641,10.649,10.650,10.652]; // Arima , Curepe , San Juan, Port of Spain
var taxi_coord_y = [-61.283,-61.409,-61.452,-61.509];
// this is the x and w coordinates of the taxi stand locations in an array. At the side is the order the stands are in


var Arima = L.marker([10.641,-61.283]).addTo(map);
var Curepe =  L.marker([10.649,-61.409]).addTo(map);
var San_Juan =  L.marker([10.650,-61.452]).addTo(map);
var Port_of_Spain =  L.marker([10.652,-61.509]).addTo(map);
// this is the code that handles the map marks that are placed on the map 


// exact distance coords from my house for testing 0.13819562704514,0.03695596480137,0.052257938482111,0.10098393206051

var usericon = L.icon ({
    iconUrl: 'marker.png',
    iconSize: [32,48],
    iconAnchor: [16,47],
})


// handle the new map marker's sprite 

const successCallback = (position) => {
    x = position.coords.latitude; // sets the users current latitude coords as x 
    y = position.coords.longitude;// sets the users current longitude coords as y 
    var Current_Pos =  L.marker([x,y],{icon:usericon}).addTo(map); // adds the user's coords to the map with the special map marker
    for (let i = 0; i < 4; i++)// for loop to iterate through the different taxi stand coordinates
        {
            // distance between two points on a line equation
            var x_to_2 = Math.pow((x-taxi_coord_x[i]),2);
            var y_to_2 = Math.pow((y-taxi_coord_y[i]), 2);
            var sum = x_to_2 + y_to_2;
            temp_distance = Math.sqrt(sum);
            // distance between two points on a line equation 


            if (temp_distance < short_dis || short_dis == 0) //compares the distance 
            {
                short_dis = temp_distance; // set new shortest distance 
                cord_id = i;
            }
        }
    var short_taxi = L.marker([taxi_coord_x[cord_id],taxi_coord_y[cord_id]],{icon:usericon}).addTo(map); // display shorest distance with special marker  
    //console.log(cord_id);
    //console.log(position);
}



// returns an error message
const errorCallback = (error) => {
    console.error(error);
};

navigator.geolocation.getCurrentPosition(successCallback, errorCallback);