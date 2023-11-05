var slides = document.getElementsByClassName("mySlides");
var currentSlide = 0;
var slideInterval = setInterval(nextSlide, 2000);

function nextSlide(){
	slides[currentSlide].className = 'mySlides';
	currentSlide = (currentSlide+1)%slides.length;
	slides[currentSlide].className = 'mySlides showing';
}

function prevSlide() {
	slides[currentSlide].className = 'mySlides';
	if (currentSlide == 0)
		currentSlide = slides.length - 1;
	else
		currentSlide -= 1;
	slides[currentSlide].className = 'mySlides showing';
}

var playing = true;
var pauseButton = document.getElementById('pause');

function pauseSlideshow(){
	pauseButton.innerHTML = 'Play';
	playing = false;
	clearInterval(slideInterval);
}

pauseButton.onclick = function(){
	if(playing){ pauseSlideshow(); }
	else{ playSlideshow(); }
};

function playSlideshow(){
	pauseButton.innerHTML = 'Pause';
	playing = true;
	slideInterval = setInterval(nextSlide,2000);
}

// let slideIndex = 0;
// timeout = setTimeout(showSlides, 2000);

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides() {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   for (i = 0; i < slides.length; i++) {
// 	slides[i].style.display = "none";
//   }
//   slideIndex++;
//   if (slideIndex > slides.length) {slideIndex = 1}
//   slides[slideIndex-1].style.display = "block";
//   timeout = setTimeout(showSlides, 2000); // Change image every 2 seconds
// }

// function stop() {
// 	clearTimeout(timeout);
// }


// var slides = document.querySelectorAll('#slides .slide');
// var currentSlide = 0;
// var slideInterval = setInterval(nextSlide,2000);

// function nextSlide(){
// 	slides[currentSlide].className = 'slide';
// 	currentSlide = (currentSlide+1)%slides.length;
// 	slides[currentSlide].className = 'slide showing';
// }

// var playing = true;
// var pauseButton = document.getElementById('pause');

// function pauseSlideshow(){
// 	pauseButton.innerHTML = 'Play';
// 	playing = false;
// 	clearInterval(slideInterval);
// }

// function playSlideshow(){
// 	pauseButton.innerHTML = 'Pause';
// 	playing = true;
// 	slideInterval = setInterval(nextSlide,2000);
// }

// pauseButton.onclick = function(){
// 	if(playing){ pauseSlideshow(); }
// 	else{ playSlideshow(); }
// };