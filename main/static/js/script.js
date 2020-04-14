class Site {
    constructor(siteName, address, latitude, longitude) {
        this.siteName = siteName;
        this.address = address;
        this.latitude = latitude;
        this.longitude = longitude;
    }
}
let newJobsites = [];
let data = 'AIzaSyDoVTW1-BZU-gfpY86X4FRKoc6hy8Oa67I'

$(document).ready(function(){
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton();
});


function showSearchResults(results) {
    for(let i = 0; i < results.length; i++) {
        searchedSite = new Site(results[i].name, results[i].formatted_address, results[i].geometry.location.lat, results[i].geometry.location.lng);
        newJobsites.push(searchedSite);
    }
    for(let i = 0; i < newJobsites.length; i++) {
        $('#search-results').append(`<li class="sites" value="${i}">
                                        <div class="collapsible-header"><strong>${newJobsites[i].siteName}</strong></div>
                                            <div class="collapsible-body"><span><strong>${newJobsites[i].address}</strong>
                                                <br><br>
                                                <form action="/restaurants/" method="POST">
                                                    <button class="btn waves-effect waves-light green" type="submit">Add Jobsite
                                                        <i class="material-icons right">add</i>
                                                    </button>
                                                    <input type="hidden" name="name" value="${newJobsites[i].siteName}">
                                                    <input type="hidden" name="address" value="${newJobsites[i].address}">
                                                    <input type="hidden" name="latitude" value="${newJobsites[i].latitude}">
                                                    <input type="hidden" name="longitude" value="${newJobsites[i].longitude}">
                                                </form>
                                            </span>
                                        </div>
                                    </li>`
                                    );
    }
}


$('#site-search-click').on('click', (event)=> {
    event.preventDefault();
    $('li.sites').remove();
    newJobsites = [];
    const regex = / /gi;
    userInput = $('#site-search-data').val().replace(regex, '+');
    let placesURL = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=${userInput}&key=${data}`
    $.ajax({
        url: `https://cors-anywhere.herokuapp.com/${placesURL}`,
        type: "GET",
    }).then(function(data){
        console.log(data.results);
        showSearchResults(data.results);
        });
});