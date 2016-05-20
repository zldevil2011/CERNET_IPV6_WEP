$("#index").on("click", function(){
	window.location.href = "/home";
})
$("#data").on("click", function(){
	window.location.href = "/data";
})
$("#products").on("click", function(){
	window.location.href = "/products";
})
$("#material").on("click", function(){
	window.location.href = "/material";
});
//index js
var nextTime = 15;
console.log(nextTime);
var font = 0;
var time
$(function(){
    try{
        setInterval('timeUpdate()', 1000);
        setInterval('imageUpdate()', 1000);
    }catch(exception){

    }
});
function timeUpdate(){
    var t = new Date();
    var hour = t.getHours();
    var minute = t.getMinutes();
    var second = t.getSeconds();
    var currentTime = String(hour) + ":" + String(minute) + ":" + second;
    $(".today-time").html(currentTime);
}
function imageUpdate(){
	console.log(nextTime);
    nextTime = nextTime + 30;
    console.log(nextTime);
    if(nextTime > 60){
        font = font + 1;
        nextTime = 15;
    }
    var nextNum = "";
    if(font < 10){
        nextNum = "0" + font;
    }else{
        nextNum = "" + font;
    }
    console.log(nextNum);
    console.log(nextTime);
    nextNum +=  nextTime.toString();
    console.log(nextNum);
	try{

	}catch (exception){

	}
    if(parseInt(nextNum) > 2345){
        nextNum = "0015";
        nextTime = 15;
        font = 0;
    }
	var today = new Date();
	var month = today.getMonth() + 1;
	var day = today.getDate();
	day = day - 2;
	if(month <10){
		month = "0" + String(month);
	}
	if(day < 10){
		day = "0" + String(day);
	}
	var monthDay = String(month) + String(day);

	console.log(monthDay);
    var nextURL = "http://image.nmc.cn/product/2016/"+month + "/" + day + "/WXCL/small/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_2016" + monthDay + nextNum + "00000.JPG";

	console.log(nextURL);
    $("#nephogram").attr("src", nextURL);
}