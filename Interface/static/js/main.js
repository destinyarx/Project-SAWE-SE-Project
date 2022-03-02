$(document).ready(function(){
  $("#sentimentArea").emojioneArea(
    {
      pickerPosition : "bottom"
    }
  );
})

$('.interactive-menu-button a').click(function() {
  $(this).toggleClass('active');
});

var scroll = new SmoothScroll('a[href*="#"]');




$('.more-btn').click(function() {
  $('#hiden-gallery').toggleClass('hide');
  $('#hiden-gallery').toggleClass('open');
  if ( $('#hiden-gallery').is( ".open" ) ) {
    $(".more-btn-inside").text("Show Less.");
  }else {
    $(".more-btn-inside").text("Show More.");
  }
});



function slickify(){
  $('.blog-slider').slick({
      autoplay: true,
      slidesToShow: 3,
      slidesToScroll: 3,
      responsive: [
        {
            breakpoint: 991,
            settings: "unslick"
        }
      ] 
  });
  $(".slick-next").text("");
  $(".slick-next").addClass("icofont-long-arrow-right");
  $(".slick-prev").text("");
  $(".slick-prev").addClass("icofont-long-arrow-left");
}

slickify();
$(window).resize(function(){
  var $windowWidth = $(window).width();
  if ($windowWidth > 991) {
      slickify(); 
      $('#blog-btn').addClass('hide-me');  
  }else if($windowWidth < 991) {
    $('#blog-btn').removeClass('hide-me');
  }
});

$('#blog-btn').click(function() {
  $('.hiden-blog').toggleClass('hide-blog');
  $('.hiden-blog').toggleClass('open-blog');
  if ( $('.hiden-blog').is( ".open-blog" ) ) {
    $("#blog-btn").text("Show Less Stories.");
  }else {
    $("#blog-btn").text("Show More Stories.");
  }
});




// SCRIPT FIRST FOR LOADING BUTTONS 

// SCRIPT FIRST FOR LOADING BUTTONS 

let showDownload = window.localStorage.getItem('show');


//document.getElementById("loading").style.display = "none";

// get the eshow value to flag if downoad button will show up
let show = document.getElementById('show-value').innerHTML




//showDownload !='1'  &&  
if(show == "False"){
    
    alert("Invalid File Input")

    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";
    
    


//showDownload !='1'
}else if(show == "Empty"){
    alert("Empty File Input")
    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";
    
   

}else if(show == "True"){
    document.getElementById("download").style.display = "block";
    

}else{
    document.getElementById("download").style.display = "none";
    
    
}



// to show and hide download button
  function removeDisable(){

    window.localStorage.setItem("show", "1");

}


function removeDisable(){

    window.localStorage.setItem("show", "1");

}

