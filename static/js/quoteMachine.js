	function randomize(words, element) {
		var frameCount = 0;
		var wordIndex = 0;
		var randomWord = "";

		for (var i = 0; i < words.length; i++){
			var randomNum = Math.floor(Math.random() * (126 - 33) + 33);
			randomWord += String.fromCharCode(randomNum);
		}
		var stringArray = randomWord.split("");
		element.text(randomWord);
		var animate = setInterval(frame, 30);

	  function frame() {
	    if (frameCount === (words.length)) {
	    	frameCount = 0;
	      	clearInterval(animate);
	      
	    }

	    var difference = randomWord.charCodeAt(wordIndex) - words.charCodeAt(wordIndex);

	    var changeTo = String.fromCharCode(randomWord.charCodeAt(wordIndex) - difference);
	    stringArray[wordIndex] = changeTo;
	    var newWord = stringArray.join('');
	    element.text(newWord);
	    wordIndex += 1;
	    frameCount += 1;
	  }
	}


	// quote api**********************************
	var quoteUrl = "http://api.forismatic.com/api/1.0/?method=getQuote&format=jsonp&lang=en&jsonp=?";

	var twitterUrl = "https://twitter.com/intent/tweet?text="

	var getQuote = function(data) {
	  var result = twitterUrl + data.quoteText + "&hashtags=" + data.quoteAuthor;
	  $("a").attr("href", result);

	  if (data.quoteAuthor !== "") {
	    $("#quote-author").text("- " + data.quoteAuthor);
	  } else {
	    $("#quote-author").text("- unknown");
	  }
	  var quoteElement = $("#quote-content")
	  randomize(data.quoteText, quoteElement);
	  var titleElement = $("#title");
	  randomize("Random Quote Machine", titleElement);
	};

	// color changing******************************

	var colors = [];

	function setRGB() {
	  for (var i = 0; i < 3; i++) {
	    colors[i] = Math.floor(Math.random() * 255);
	  }
	}

	function startLoop() {
	  setRGB();
	  var r = colors[0];
	  var g = colors[1];
	  var b = colors[2];
	  $("#main").animate({
	    backgroundColor: "rgb(" + r + "," + g + "," + b + ")",
	    color: "rgb(" + r + "," + g + "," + b + ")"
	  }, 4000, function() {
	    startLoop();
	  });

	}

	

	// start everything*************************

	$(document).ready(function() {

	  $.getJSON(quoteUrl, getQuote, 'jsonp');

	  $("#new-quote").click(function() {
	    $.getJSON(quoteUrl, getQuote, 'jsonp');
	  });

	  startLoop();

	});