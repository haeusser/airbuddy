
<!--[if lt IE 9]>
document.createElement('header');
document.createElement('nav');
document.createElement('section');
document.createElement('article');
document.createElement('aside');
document.createElement('footer');
document.createElement('hgroup');
<!--[endif]-->



/* --- Toggle function --- */
jQuery(document).ready(function(){

	// Equalize Div heights
	/*
	var highestCol = Math.max($('#logo_icon').height(),$('#logo_typo').height());
	$('#logo_icon').height(highestCol);
	$('#logo_typo').height(highestCol);
	$('#logo_typo').css({"line-height": highestCol + "px"});
	$('#logo_typo').css({"vertical-align": "middle"});
	*/
	
	// hide divs onload
	if (document.documentElement.clientWidth < 768) {
		$('nav#nav_main').hide();
		$('div#mobile_search').hide();
	}
	// slideToggle button 1
	$('a#toggle_nav').click(function(){
		$('nav#nav_main').slideToggle('250', function(){
			// show as enbaled
			if ($('nav#nav_main').is(":visible")) {
				$('a#toggle_nav').css("background-color", "#53AD43");
				$('a#toggle_nav').css("color", "#FFF");
			}
			// show as disabled
			if ($('nav#nav_main').is(":hidden")) {
				$('a#toggle_nav').css("background-color", "#FFF");
				$('a#toggle_nav').css("color", "#2C2C2C");
			}
			// disabled other button
			$('a#toggle_search').css("background-color", "#FFF");
			$('a#toggle_search').css("background-image", "url(/wp-content/themes/dgspj/images/search-mobile.png)");
		});
		if ($('div#mobile_search').is(":visible")) {
			$('div#mobile_search').slideToggle('250');
		}
	});
	// slideToggle button 2
	$('a#toggle_search').click(function(){
		$('div#mobile_search').slideToggle('250', function(){
			if ($('div#mobile_search').is(":visible")) {
				$('a#toggle_search').css("background-color", "#53AD43");
				$('a#toggle_search').css("background-image", "url(/wp-content/themes/dgspj/images/search-mobile_hover.png)");
			}
			if ($('div#mobile_search').is(":hidden")) {
				$('a#toggle_search').css("background-color", "#FFF");
				$('a#toggle_search').css("background-image", "url(/wp-content/themes/dgspj/images/search-mobile.png)");
			}
			$('a#toggle_nav').css("background-color", "#FFF");
			$('a#toggle_nav').css("color", "#2C2C2C");
		});
		if ($('nav#nav_main').is(":visible")) {
			$('nav#nav_main').slideToggle('250');
		}
	});
});



function toggle() {
}


