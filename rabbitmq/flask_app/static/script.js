$(document).ready(function() {
    $("#temp-humidity-form").on('submit', function(event) {
        event.preventDefault();
        
        let temperature = $("#temperature").val();
        let humidity = $("#humidity").val();
        
        $.ajax({
            url: '/submit',
            type: 'POST',
            data: { temperature: temperature, humidity: humidity },
            dataType: 'json',
            success: function(response) {
                alert("Data sent successfully. Temperature: " + response.temperature + ", Humidity: " + response.humidity);
            },
            error: function(xhr, status, error) {
                alert("An error occurred: " + error);
            }
        });
    });
});