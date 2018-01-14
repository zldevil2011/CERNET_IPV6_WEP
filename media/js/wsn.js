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
//console.log(nextTime);
var font = 0;
var time;

$(function(){
    try{
        setInterval('timeUpdate()', 1000);
        setInterval('imageUpdate()', 1000);
        $(".city-choice-item").on("click", updateLocationFunction);
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
	//console.log(nextTime);
    nextTime = nextTime + 30;
    //console.log(nextTime);
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
    //console.log(nextNum);
    //console.log(nextTime);
    nextNum +=  nextTime.toString();
    //console.log(nextNum);
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

	//console.log(monthDay);
    var nextURL = "http://image.nmc.cn/product/2017/"+month + "/" + day + "/WXCL/small/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_2017" + monthDay + nextNum + "00000.JPG";

	//console.log(nextURL);
    $("#nephogram").attr("src", nextURL);
}
function updateLocationFunction(){
    var location = $(this).html();
    console.log(location);
    $(this).addClass("div-text-active").siblings().removeClass("div-text-active");
    var targetUrl = "/city_all_info/";
    var formdata = new FormData();
    formdata.append("location", location);
    $.ajax({
        url:targetUrl,
        data: formdata,
        type: "POST",
        cache: false,
        processData:false,
        contentType:false,
    }).done(function(res){
        if(res != "error"){
            real = res[0];
            forecast = res[1];
            //console.log(real.location);
            $("[name=latest_location]").html(real.location);
            $(".today-degree").html(real.temperature + "℃");
            var today_detail = real.weather + "&nbsp;&nbsp;|&nbsp;&nbsp;" + real.cloud + real.cloud_speed + "级&nbsp;&nbsp;|&nbsp;&nbsp;湿度：" + real.humidity + "%";
            $(".today-detail").html(today_detail);
            $(".warning-value").html(real.pm25);
            var  week_forecast_T = '';
            var date = new Array();
            var high = new Array();
            var low = new Array();
            for(var i = 0; i < 6; ++i){
                week_forecast = '<div class="col-md-2"><div>';
                week_forecast = week_forecast + forecast[i].date + '</div><div>';
                week_forecast = week_forecast + forecast[i].week + '</div><div>';
                week_forecast = week_forecast + forecast[i].weather_day + '/' + forecast[i].weather_night + '</div><div>';
                week_forecast = week_forecast + forecast[i].high_temperature + '℃/' + forecast[i].low_temperature + '</div><div>';
                week_forecast = week_forecast + forecast[i].cloud +  forecast[i].cloud_speed + '</div><div>';
                week_forecast = week_forecast + '</div></div>';//<span class="week-weather-info">72 良</span>
                week_forecast_T += week_forecast;
                date.push(forecast[i].date);
                high.push(forecast[i].high_temperature);
                low.push(forecast[i].low_temperature);
             }
            $(".week-weather").html(week_forecast_T);

            var chart = new CanvasJS.Chart("forecast-chart", {
                backgroundColor: "rgba(0,0,0,0.75)",
                title:{
                },
                data: [{
                    type: "line",

                    dataPoints: [
                        { x: 1, y: low[0]   ,indexLabel:  low[0] + "℃", label: date[0]},
                        { x: 2, y: low[1], indexLabel:  low[1] + "℃", label: date[1] },
                        { x: 3, y: low[2], indexLabel:  low[2] + "℃", label: date[2] },
                        { x: 4, y: low[3] , indexLabel:  low[3] + "℃", label: date[3]},
                        { x: 5, y: low[4] , indexLabel:  low[4] + "℃", label: date[4]},
                        { x: 6, y: low[5], indexLabel:  low[5] + "℃", label: date[5] }
                    ]
                }, {
                    type: "line",
                    dataPoints: [
                    { x: 1, y: high[0] , indexLabel:  high[0] + "℃",label: date[0]},
                    { x: 2, y: high[1], indexLabel:  high[1] + "℃", label: date[1] },
                    { x: 3, y: high[2], indexLabel:  high[2] + "℃", label: date[2] },
                    { x: 4, y: high[3] , indexLabel:  high[3] + "℃", label: date[3]},
                    { x: 5, y: high[4] , indexLabel:  high[4] + "℃", label: date[4]},
                    { x: 6, y: high[5], indexLabel:  high[5] + "℃", label: date[5] }
                    ]
                }
                ]
            });
            chart.render();
            $('#place-choice').modal('hide');
        }else{
           window.location.href="/home/";
        }
    }).fail(function(res){

    })
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
        var RPIC = setInterval("updateRPTC('/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_ACHN_L88_PI_2018', '0000001.PNG')");
        clearInterval(RPIC);
        $(".satellite-cloud-image").on("click", function(){
            clearInterval(RPIC);
            real_image_update = setInterval('realSatelliteCloudImageUpdate()', 1000);
        });
        $(".radar").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_ACHN_L88_PI_2018', '3000001.PNG')", 1000);
            console.log("clear The Time");
        });
        $(".precipitation").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_ER1_ACHN_L88_PB_2018', '0000000.jpg')", 1000);
        });
        $(".temperature").on("click", function(){
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_2018', '0000000.jpg')", 1000);
        });
        $(".cloudy").on("click", function(){
            //var nextURL = "http://image.nmc.cn/product/2018/05/24/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_20180524010000000.jpg";
            RPICTip = 0;
            clearInterval(real_image_update);
            clearInterval(RPIC);
            RPIC = setInterval("updateRPTC('/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_2018', '0000000.jpg')", 1000);
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
            var nextURL = "http://image.nmc.cn/product/2018/" + month + "/" + day + "/AMSM/medium/SEVP_NMC_AMSM_CAGMSS_ESRH_ACHN_L10CM_PS_2018" + monthDay + "000000000.jpg";
            clearInterval(real_image_update);
            clearInterval(RPIC);
            $("#real-image").attr("src", nextURL);
        });
    }catch(exception){

    }
});
function realSatelliteCloudImageUpdate(){
    //console.log("zzzz");
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

    var nextURL = "http://image.nmc.cn/product/2018/"+month + "/" + day + "/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_2018" + monthDay + nextNum + "00000.JPG";
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
    var nextURL = "http://image.nmc.cn/product/2018/" + month + "/" + day + type + monthDay + timeParameter + lastP;
    $("#real-image").attr("src", nextURL);
}

//onlineTool
$(function(){
   $(".LAI").on("click", function(){
      window.location = "/onlineTool/1";
   });
});

//toolWindow
$(function(){
    $("#uploadPath").on("change", selectFile);
    $("#fileinput-upload-button").on("click", uploadFile);
    $("#fileinput-transfer-button").on("click", transferFile);
});
function selectFile(){
    var fileName = $("#uploadPath").val();
    console.log(fileName);
    $("#btn-tip").html(fileName);
    $(".original-image").show();
    $(".progress-upload-bar").css("width", "0%");
    $(".progress").css("display", "none");
}
function sleep(sleepTime) {
    for(var start = Date.now(); Date.now() - start <= sleepTime; ) { }
}
function uploadFile(){
    //alert("上传图片");
    $(".progress").show();
    $(".progress-upload-bar").css("width", "10%").html("10%");
    var file_list = $("#uploadPath").prop('files');
    console.log(file_list[0]);
    var fileNum = file_list.length;
    var formdata = new FormData();
    for(var i = 0; i < fileNum; ++i){
        var keyIndex = "originalImage";
        formdata.append(keyIndex, file_list[i]);
        $(".progress-upload-bar").css("width", "20%").html("20%");
    }
    $.ajax({
        url : "/onlineTool/upload/",
        type : "POST",
        cache : false,
        data : formdata,
        processData : false,
        contentType : false
    }).done(function(res){
        //alert(res);
        $(".original-image").removeClass("glyphicon-file");
        $(".original-image-preview").removeClass("hidden").attr("src", "/web_media/images/originalImage/" + res);
        $("#originalFile").html(res);
        $(".progress-upload-bar").css("width", "100%").html("上传成功");
        $("#btn-tip").html("选择文件");
        return false;
    }).fail(function(res){
        alert(res);
        return false;
    });
}
function transferFile(){
    $(".processing").show();
    $(".final-image").removeClass("glyphicon-file").show();
    $(".processing-image-preview").attr("src", "/web_media/images/loading.gif");
    var originalFile = $("#originalFile").html();
    var formdata = new FormData();
    formdata.append("originalFile", originalFile);
    $.ajax({
        url : "/onlineTool/transfer/",
        type : "POST",
        cache : false,
        data : formdata,
        processData : false,
        contentType : false
    }).done(function(res){
        //alert(res);
        $(".processing-image-preview").attr("src", "/web_media/images/processImage/" + res);
        //$(".final-image").html("").addClass("glyphicon-file");
        return false;
    }).fail(function(res){
        alert(res);
        return false;
    });
}
