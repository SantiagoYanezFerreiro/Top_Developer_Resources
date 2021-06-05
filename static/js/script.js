$(document).ready(function () {
     // Hide Resources in the Profile Page
    $('#user_resources').hide();
    $('#hide_resources_btn').hide();
    // Counter
    $('.count-up').counter();
    $('.count1').counter();
    $('.count2').counter();
    // bootstrap tooltip functionality
    $('[data-toggle="tooltip"]').tooltip(); 
});

 // Hide Resources in the Profile Page
 $('#hide_resources_btn').click(function(){
    $('#hide_resources_btn').hide();
    $('#show_resources_btn').show();
    $('#user_resources').hide(); 
});

 // show Resources in the Profile Page
$('#show_resources_btn').click(function(){
    $('#show_resources_btn').hide();
    $('#hide_resources_btn').show();
    $('#user_resources').show(); 
});


