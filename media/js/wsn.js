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
$("#service").on("click", function(){
	window.location.href = "/onlineTool";
});
//index js
var nextTime = 15;
console.log(nextTime);
var font = 0;
var time;

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
	day = day;
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


//data real-image
var real_image_time = 15;
var real_image_font = 0;
var real_time;

//RPIC
var RPICTip = 0;
$(function(){
    try{
        var real_image_update = setInterval('realSatelliteCloudImageUpdate()', 1000);
        var RPIC = setInterval("updateRPTC('/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_ACHN_L88_PI_2016', '0000001.PNG')");
        clearInterval(RPIC);
        $(".satellite-cloud-image").on("click", function(){
            clearInterval(RPIC);
            real_image_update = setInterval('realSatelliteCloudImageUpdate()', 1000);
        });
        $(".radar").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_ACHN_L88_PI_2016', '3000001.PNG')", 1000);
            console.log("clear The Time");
        });
        $(".precipitation").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_ER1_ACHN_L88_PB_2016', '0000000.jpg')", 1000);
        });
        $(".temperature").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_2016', '0000000.jpg')", 1000);
        });
        $(".cloudy").on("click", function(){
            //var nextURL = "http://image.nmc.cn/product/2016/05/24/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_20160524010000000.jpg";
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_2016', '0000000.jpg')", 1000);
        });
        $(".soil-humidity").on("click", function(){
            var today = new Date();
            var month = today.getMonth() + 1;
            var day = today.getDate();
            if(month <10){
                month = "0" + String(month);
            }
            if(day < 10){
                day = "0" + String(day);
            }
            var monthDay = String(month) + String(day);
            var nextURL = "http://image.nmc.cn/product/2016/" + month + "/" + day + "/AMSM/medium/SEVP_NMC_AMSM_CAGMSS_ESRH_ACHN_L10CM_PS_2016" + monthDay + "000000000.jpg";
            clearInterval(real_image_update);
            clearInterval(RPIC);
            $("#real-image").attr("src", nextURL);
        });
    }catch(exception){

    }
});
function realSatelliteCloudImageUpdate(){
    console.log("zzzz");
    real_image_time = real_image_time + 30;
    if(real_image_time > 60){
        real_image_font = real_image_font + 1;
        real_image_time = 15;
    }
    var nextNum = "";
    if(real_image_font < 10){
        nextNum = "0" + real_image_font;
    }else{
        nextNum = "" + real_image_font;
    }
    nextNum +=  real_image_time.toString();
    if(parseInt(nextNum) > 2345){
        nextNum = "0015";
        real_image_time = 15;
        real_image_font = 0;
    }
	var today = new Date();
	var month = today.getMonth() + 1;
	var day = today.getDate();
	day = day;
	if(month <10){
		month = "0" + String(month);
	}
	if(day < 10){
		day = "0" + String(day);
	}
	var monthDay = String(month) + String(day);

    var nextURL = "http://image.nmc.cn/product/2016/"+month + "/" + day + "/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_2016" + monthDay + nextNum + "00000.JPG";
    $("#real-image").attr("src", nextURL);
}
function updateRPTC(type, lastP){
    var today = new Date();
    var month = today.getMonth() + 1;
    var day = today.getDate();
    var hour = today.getHours();
    RPICTip = RPICTip + 1;
    if(RPICTip > (hour - 8)){
        RPICTip = 0;
    }
    var timeParameter = RPICTip;
    if(timeParameter < 10){
        timeParameter = "0" + timeParameter;
    }

    if(month <10){
		month = "0" + String(month);
	}
	if(day < 10){
		day = "0" + String(day);
	}
    var monthDay = String(month) + String(day);
    var nextURL = "http://image.nmc.cn/product/2016/" + month + "/" + day + type + monthDay + timeParameter + lastP;
    $("#real-image").attr("src", nextURL);
}